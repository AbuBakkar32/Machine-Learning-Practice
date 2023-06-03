from io import BytesIO

import requests
from lxml import etree


# parsing document metadata
def parse_document_metadata(xml_root):
    application_number = ""
    date = ""

    for element in xml_root.iter("document-id"):
        children = element.getchildren()
        for child in children:
            if child.tag == "doc-number":
                application_number = child.text
            elif child.tag == "date":
                date = child.text

    # Add hypen to date string if length is 8 (i.e. format YYYYMMDD >> YYYY-MM-DD)
    if len(date) == 8:
        date = date[0:4] + "-" + date[4:6] + "-" + date[6:]

    return application_number, date


def parse_xml_claims_v2(xml: bytes):
    """
    Translate and parse the Patent application's XML sections specific to a
    Patent claims set. The final output will return an array with sections
    as dictionary of text and IDs.

    example format:

    {
        "applicationNumber": "1234567890"
        "date": "YYYY-MM-DD",
        "documentType": "CLM",
        "sections": [
            {
                "id": "CLM-00001",
                "text": "example text"
            },
            {
                "id": "CLM-00002",
                "text": "example text"
            },
            {
                "id": "CLM-00003",
                "text": "example text"
            }
        ]
    }
    """

    parser = etree.XMLParser(ns_clean=True)
    root = etree.parse(BytesIO(xml), parser)

    with open("D:/xmlfile/claims-transform.xsl") as f:
        transform = etree.XSLT(etree.parse(f))

    result = transform(root)

    application_number, date = parse_document_metadata(result)

    if application_number == "":
        # print(etree.tostring(root, pretty_print=True))
        for action, elem in etree.iterwalk(root, events=("start", "end")):
            # print("%s: %s" % (action, elem.tag))
            if elem.tag == "{urn:us:gov:doc:uspto:patent}ClaimText":
                print("Claim text:")
                print(elem.text)
            # if action == "start" and elem.tag == "a":
            #     context.skip_subtree()  # ignore <b>

    elements = []

    claim_id_format = "CLM-00000"

    for claim in result.iter("claim"):

        claim_dict = {"text": []}
        claim_id = ""

        if "id" in claim.attrib:
            claim_id = claim.attrib["id"]

        # If the claim ID is not set, do not include it in the final list of
        # claims.
        if claim_id == "":
            continue

        for t in claim.iter("claim-text"):
            claim_text = str(t.text).strip()
            claim_dict["text"].append(claim_text)

        skip_claim = False
        full_claim_text = " ".join(claim_dict["text"])

        if full_claim_text == "":
            skip_claim = True
        else:
            for i, c in enumerate(full_claim_text):
                if i > 1:
                    # Because claims can be placeholders we need to detect if
                    # the claim we are parsing is unknown without a proper digit
                    # identifier. We will skip non-digit combined with unknown
                    # claim IDs.
                    if "unknown" in claim_id.lower():
                        print(
                            "Skipping claim. Digit was not the first character in the claim text..."
                        )
                        skip_claim = True
                    break
                # Detect the first digit in the claim text to replace the claim
                # ID that was unknown.
                if c.isdigit():
                    claim_id = f"{claim_id_format[0: -len(c)]}{c}"
                    break

        # If we must skip the claim continue on.
        if skip_claim:
            continue
        else:
            claim_dict["id"] = claim_id

        elements.append(claim_dict)

    document = {
        "applicationNumber": application_number,
        "date": date,
        "documentType": "CLM",
        "sections": elements,
    }
    print(document)
    return document


def parse_xml_claims_v1(xml: bytes):
    """
    Translate and parse the Patent application's XML sections specific to a
    Patent claims set. The final output will return an array with sections
    as dictionary of text and IDs.
    example format:
    {
        "applicationNumber": "1234567890"
        "date": "YYYY-MM-DD",
        "documentType": "CLM",
        "sections": [
            {
                "id": "CLM-00001",
                "text": "example text"
            },
            {
                "id": "CLM-00002",
                "text": "example text"
            },
            {
                "id": "CLM-00003",
                "text": "example text"
            }
        ]
    }
    """

    parser = etree.XMLParser(ns_clean=True)
    root = etree.parse(BytesIO(xml), parser)

    with open("D:/xmlfile/claims-transform.xsl") as f:
        transform = etree.XSLT(etree.parse(f))

    result = transform(root)

    application_number, date = parse_document_metadata(result)

    elements = []

    claim_id_format = "CLM-00000"

    for claim in result.iter("claim"):

        claim_dict = {"text": []}

        claim_id = ""

        if "id" in claim.attrib:
            claim_id = claim.attrib["id"]

        # If the claim ID is unknown or not set, do not include it in the final
        # list of claims.
        if claim_id == "":
            continue

        for t in claim.iter("claim-text"):
            claim_text = str(t.text).strip()
            claim_dict["text"].append(claim_text)

        skip_claim = False
        full_claim_text = " ".join(claim_dict["text"])

        if full_claim_text == "":
            skip_claim = True
        else:
            digit = ""
            for i, c in enumerate(full_claim_text):
                # Detect the first digit in the claim text to replace the claim
                # ID that was unknown.
                if c.isdigit():
                    digit += c

                if i > 1 and not c.isdigit():
                    # Because claims can be placeholders we need to detect if
                    # the claim we are parsing is unknown without a proper digit
                    # identifier. We will skip non-digit combined with unknown
                    # claim IDs.
                    if "unknown" in claim_id.lower():
                        print(
                            "Skipping claim. Digit was not the first character in the claim text..."
                        )
                        skip_claim = True
                    break

                if digit != "":
                    claim_id = f"{claim_id_format[0: -len(digit)]}{digit}"

        # If we must skip the claim continue on.
        if skip_claim:
            continue
        else:
            claim_dict["id"] = claim_id

        elements.append(claim_dict)

    document = {
        "applicationNumber": application_number,
        "date": date,
        "documentType": "CLM",
        "sections": elements,
    }
    print(document)
    return document


def parse_xml_abst(xml: bytes):
    """
    Translate and parse the Patent application's XML sections specific to a
    Patent abstract. The final output will return a dictionary with sections
    as a single string.

    example format:

    {
        "applicationNumber": "1234567890"
        "date": "YYYY-MM-DD",
        "documentType": "ABST",
        "sections": "text"
    }
    """

    root = etree.parse(BytesIO(xml))

    with open("D:/xmlfile/claims-transform.xsl") as f:
        transform = etree.XSLT(etree.parse(f))

    result = transform(root)

    application_number, date = parse_document_metadata(result)

    elements = []

    # Even though there are many sections of text, we want to structure
    # everything as a single array of strings.
    for element in result.iter("abstract"):
        for t in element.iter("p"):
            elements.append(str(t.text).strip())

    # Remove the last element of the abstract list, because it tends to be a bad
    # OCR confidence <p> tag.
    del element[-1]

    document = {
        "applicationNumber": application_number,
        "date": date,
        "documentType": "ABST",
        "sections": elements,
    }
    print(document)
    return document


def parse_xml_specification(xml: bytes):
    """
    Translate and parse the Patent application's XML sections specific to a
    Patent specification. The final output will return an array with sections
    as dictionary of text and types.

    example format:

    {
        "applicationNumber": "1234567890"
        "date": "YYYY-MM-DD",
        "documentType": "SPEC",
        "sections": [
            {
                "type": "heading",
                "text": "example text"
            },
            {
                "type": "heading",
                "text": "example text"
            },
            {
                "type": "paragraph",
                "text": "example text"
            }
        ]
    }
    """

    root = etree.parse(BytesIO(xml))

    with open("D:/xmlfile/claims-transform.xsl") as f:
        transform = etree.XSLT(etree.parse(f))

    result = transform(root)

    application_number, date = parse_document_metadata(result)

    elements = []

    for element in result.iter("description"):

        for t in element.iter("p"):

            section = {"text": str(t.text).strip()}

            if "type" in t.attrib:
                if t.attrib["type"] == "heading":
                    section["type"] = "heading"
                else:
                    section["type"] = "paragraph"
            else:
                section["type"] = "paragraph"

            elements.append(section)

    document = {
        "applicationNumber": application_number,
        "date": date,
        "documentType": "SPEC",
        "sections": elements,
    }
    print(document)
    return document


def parse_json_specification(specification):
    """
    Parse the given specification JSON object sections as a single space
    delimited text string.
    """
    section_texts = []
    for section in specification:
        section_texts.append(section["text"])
    return " ".join(section_texts)


def parse_json_abstract(abstract):
    """
    Parse the given abstract JSON object sections as a single space delimited
    text string.
    """
    return " ".join(abstract)


def parse_json_claims(claims):
    """
    Parse the given claims JSON object sections as a single space delimited
    text string.
    """
    section_texts = []
    for section in claims:
        texts = section["text"]
        section_texts.append(" ".join(texts))
    return " ".join(section_texts)


def embed_application(host: str, abstract: str, claims: str, description: str):
    """
    Generate Patent Application similarity embedding vector based on values that
    are given. Request payload structure sent to the machine learning model API
    is documented below.

    {
        "publication_number_docdb": 'US-20080138074-A1',
        "cpc_first": 'H04J14/0227',
        "cpcs": ['H04J14/0227', 'H04J14/0221', 'H04J14/0246', 'H04J14/0279'],
        "title_xml": 'text here',
        "abstract_xml": 'abstract text here',
        "claims_xml": 'claims xml text here'
        "description_xml": 'description xml text'
    }
    """

    payload = {
        # FIXME: Update these to be pulled from docs
        "publication_number_docdb": "",
        "cpc_first": "",
        "cpcs": [],
        "title_xml": "",
        "abstract_xml": abstract,
        "claims_xml": claims,
        "description_xml": description,
    }

    response = requests.post(host, json=payload)
    print(response.json())
    return response.json()


print(parse_xml_claims_v2("D:/xmlfile/claims-transform.xsl"))
