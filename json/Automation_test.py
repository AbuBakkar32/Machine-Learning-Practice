import json
import os
import time
from pathlib import Path
from xml.dom import minidom
from xml.parsers import expat

import xmltodict
from termcolor import colored


class XmlToJsonConverter:
    def __init__(self, xmlFilePath: any = None):
        self.xmlFilePath = xmlFilePath  # path of xml file

        self.jsonFilePath = 'c:/jsonfile'  # path of json where json file will be created
        self.cleanJsonPath = 'c:/cleanjson'  # path of json where clean json file will be created

        xmlFile = Path(self.xmlFilePath)

        # check txt file exist or not. if not it will create new txt file automatically
        if 'xml_file.txt' in os.listdir(xmlFile):
            pass
        else:
            with open(xmlFile.joinpath('xml_file.txt'), 'w') as f:
                f.write("")

        path = ['c:/jsonfile', 'c:/cleanjson']
        for p in path:
            if not os.path.exists(p):
                os.mkdir(p)
                print(colored("Directory " + p + " Created", 'green'))
            else:
                pass

        # call convert_xml_file_to_json function for processing xml file to json file
        self.convert_xml_file_to_json()

    def convert_xml_file_to_json(self):
        # for handle the exception using try and case
        t1 = time.time()
        for root, dirs, files in os.walk(self.xmlFilePath):
            if len(files) > 0:
                for file in files:
                    if file.endswith('.xml'):
                        with open(self.xmlFilePath + '/' + "xml_file.txt", 'r') as f:
                            if file not in f.read():
                                try:
                                    with open(self.xmlFilePath + '/' + file, 'r') as f:  # read XML file one by one
                                        xml = f.read()
                                        xml = minidom.parseString(xml)
                                        xml = xml.toprettyxml()
                                        xml = xmltodict.parse(xml, attr_prefix='', encoding='utf-8', expat=expat)
                                        baseFileName = file.split('.xml')[0]
                                        with open(self.jsonFilePath + '/' + baseFileName + '.json', 'w') as f:
                                            json.dump(xml, f, indent=4)
                                    json_file = baseFileName + '.json'
                                    self.clean_json(json_file)
                                except:
                                    # self.fail_db_message(file)
                                    print(f"{file} File Not Converted XML to JSON")

                            else:
                                print(f"{file} File already exists")
            else:
                print(f"No XML file found in this {self.xmlFilePath} folder")
        t2 = time.time()
        print(f"Total time taken to convert xml to json file is {t2 - t1}")

    def new_spec_xml_format_clean_to_json(self, data, fileName, file):
        applicationNumber = \
            int(data['us-patent-application']['us-bibliographic-data-application'][
                    'application-reference'][
                    'document-id'][
                    'doc-number'])
        date = \
            data['us-patent-application']['us-bibliographic-data-application'][
                'application-reference'][
                'document-id'][
                'date']
        documentType = 'SPEC'
        sections = []
        for i in range(len(data['us-patent-application']['description']['p'])):
            try:
                if 'boundary-data' in data['us-patent-application']['description']['p'][i]:
                    if type(data['us-patent-application']['description']['p'][i]['boundary-data']) == dict:
                        try:
                            text = data['us-patent-application']['description']['p'][i]['text'].strip()
                            text = " ".join(text.split())
                            section = {
                                "text": text,
                                "type": data['us-patent-application']['description']['p'][i]['boundary-data'][
                                    'type']
                            }
                            sections.append(section)
                        except:
                            section = {
                                "text": " ",
                                "type": data['us-patent-application']['description']['p'][i]['boundary-data'][
                                    'type']
                            }
                            sections.append(section)
                    elif type(data['us-patent-application']['description']['p'][i]['boundary-data']) == list:
                        try:
                            text = data['us-patent-application']['description']['p'][i]['text'].strip()
                            text = " ".join(text.split())
                            section = {
                                "text": text,
                                "type": data['us-patent-application']['description']['p'][i]['boundary-data'][0][
                                    'type']
                            }
                            sections.append(section)
                        except:
                            section = {
                                "text": " ",
                                "type": data['us-patent-application']['description']['p'][i]['boundary-data'][0][
                                    'type']
                            }
                            sections.append(section)
            except Exception as e:
                pass
                # self.fail_db_message(file)

        getjson = {
            'applicationNumber': applicationNumber,
            'date': date,
            'documentType': documentType,
            'sections': sections
        }

        with open(self.cleanJsonPath + "/" + file, 'w') as f:
            json.dump(getjson, f, indent=4)

        # self.success_db_message(fileName)

        with open(self.xmlFilePath + '/' + "xml_file.txt", 'a') as f:
            f.write("\n" + fileName + ".xml")

        print(colored(f"\n{file} Successfully cleaned", 'green'))

    def old_spec_xml_format_clean_to_json(self, data, fileName, file):
        applicationNumber = \
            int(data['SpecificationDocument']['DocumentHeaderDetails']['ApplicationHeaderDetails'][
                    'ApplicationNumber'])
        date = \
            data['SpecificationDocument']['MailRoomDate']
        documentType = 'SPEC'
        sections = []
        try:
            for i in range(len(data['SpecificationDocument']['Specification']['P'])):
                try:
                    text = data['SpecificationDocument']['Specification']['P'][i]['text']
                    text = ' '.join(text.split())
                    section = {
                        "text": text,
                        "type": data['SpecificationDocument']['Specification']['P'][i]['id']
                    }
                    sections.append(section)
                except:
                    section = {
                        "text": " ",
                        "type": data['SpecificationDocument']['Specification']['P'][i]['id']
                    }
                    sections.append(section)

        except Exception as e:
            pass
            # self.fail_db_message(fileName)
        getjson = {
            'applicationNumber': applicationNumber,
            'date': date,
            'documentType': documentType,
            'sections': sections
        }

        with open(self.cleanJsonPath + "/" + file, 'w') as f:
            json.dump(getjson, f, indent=4)

        # self.success_db_message(fileName)

        with open(self.xmlFilePath + '/' + "xml_file.txt", 'a') as f:
            f.write("\n" + fileName + ".xml")

        print(colored(f"\n{file} Successfully cleaned", 'green'))

    def clean_spec_file(self, file):
        fileName = file.split('.json')[0]
        with open(self.jsonFilePath + "/" + file, 'r') as f:
            data = json.load(f)
        data = json.dumps(data, indent=4)
        data = data.replace("\\t", "")
        data = data.replace("\\n", "")
        data = data.replace("#", "")
        data = data.replace("ns0:", "")
        data = data.replace("ns2:", "")
        data = data.replace("xsi:", "")
        data = json.loads(data)
        if 'us-patent-application' in data:
            # this method will be cleaned new SPEC type of xml file into json file
            self.new_spec_xml_format_clean_to_json(data, fileName,
                                                   file)
        elif 'SpecificationDocument' in data:
            # this method will be cleaned old SPEC type of xml file into json file
            self.old_spec_xml_format_clean_to_json(data, fileName,
                                                   file)

    def clean_new_old_abst_file_to_json(self, file):
        fileName = file.split('.json')[0]
        with open(self.jsonFilePath + "/" + file, 'r') as f:
            data = json.load(f)
        data = json.dumps(data, indent=4)
        data = data.replace("\\t", "")
        data = data.replace("\\n", "")
        data = data.replace("#", "")
        data = data.replace("ns0:", "")
        data = json.loads(data)
        applicationNumber = \
            int(data['us-patent-application']['us-bibliographic-data-application'][
                    'application-reference'][
                    'document-id'][
                    'doc-number'])
        date = \
            data['us-patent-application']['us-bibliographic-data-application'][
                'application-reference'][
                'document-id'][
                'date']
        documentType = 'ABST'
        sections = []
        try:
            if type(data['us-patent-application']['abstract']['p']) == list:
                for i in range(len(data['us-patent-application']['abstract']['p'])):
                    try:
                        text = data['us-patent-application']['abstract']['p'][i]['text']
                        text = " ".join(text.split())
                        sections.append(text)
                    except:
                        sections.append(" ")
            elif type(data['us-patent-application']['abstract']['p']) != list:
                try:
                    text = data['us-patent-application']['abstract']['p']['text']
                    text = " ".join(text.split())
                    sections.append(text)
                except:
                    sections.append(" ")
        except Exception as e:
            pass
            # self.fail_db_message(fileName)

        getjson = {
            'applicationNumber': applicationNumber,
            'date': date,
            'documentType': documentType,
            'sections': sections
        }

        with open(self.cleanJsonPath + "/" + file, 'w') as f:
            json.dump(getjson, f, indent=4)

        # self.success_db_message(fileName)

        with open(self.xmlFilePath + '/' + "xml_file.txt", 'a') as f:
            f.write("\n" + fileName + ".xml")

        print(colored(f"\n{file} Successfully cleaned", 'green'))

    def new_clm_xml_format_clean_to_json(self, data, fileName, file):
        applicationNumber = \
            int(data['us-patent-application']['us-bibliographic-data-application'][
                    'application-reference'][
                    'document-id'][
                    'doc-number'])
        date = \
            data['us-patent-application']['us-bibliographic-data-application'][
                'application-reference'][
                'document-id'][
                'date']
        documentType = 'CLM'
        sections = []
        try:
            for i in range(len(data['us-patent-application']['claims']['claim'])):
                if data['us-patent-application']['claims']['claim'][i]['id'].split('-')[0] != 'UNKNOWN':
                    if type(data['us-patent-application']['claims']['claim'][i]['claim-text']) != list:
                        try:
                            text = data['us-patent-application']['claims']['claim'][i]['claim-text']['text']
                            text = " ".join(text.split())
                            section = {
                                "text": text,
                                "id": data['us-patent-application']['claims']['claim'][i]['id']
                            }
                            sections.append(section)
                        except TypeError:
                            text = data['us-patent-application']['claims']['claim'][i]['claim-text']
                            text = " ".join(text.split())
                            section = {
                                "text": text,
                                "id": data['us-patent-application']['claims']['claim'][i]['id']
                            }
                            sections.append(section)
                        except:
                            section = {
                                "text": ' ',
                                "id": data['us-patent-application']['claims']['claim'][i]['id']
                            }
                            sections.append(section)
                    elif type(data['us-patent-application']['claims']['claim'][i]['claim-text']) == list:
                        try:
                            text = data['us-patent-application']['claims']['claim'][i]['claim-text'][0]['text']
                            text = " ".join(text.split())
                            section = {
                                "text": text,
                                "id": data['us-patent-application']['claims']['claim'][i]['id']
                            }
                            sections.append(section)
                        except TypeError:
                            try:
                                text = data['us-patent-application']['claims']['claim'][i]['claim-text'][-1]['text']
                                text = " ".join(text.split())
                                section = {
                                    "text": text,
                                    "id": data['us-patent-application']['claims']['claim'][i]['id']
                                }
                                sections.append(section)
                            except TypeError:
                                text = data['us-patent-application']['claims']['claim'][i]['claim-text']
                                section = {
                                    "text": text,
                                    "id": data['us-patent-application']['claims']['claim'][i]['id']
                                }
                                sections.append(section)
                        except:
                            section = {
                                "text": ' ',
                                "id": data['us-patent-application']['claims']['claim'][i]['id']
                            }
                            sections.append(section)
        except Exception as e:
            pass
            # self.fail_db_message(fileName)
        getjson = {
            'applicationNumber': applicationNumber,
            'date': date,
            'documentType': documentType,
            'sections': sections
        }

        with open(self.cleanJsonPath + "/" + file, 'w') as f:
            json.dump(getjson, f, indent=4)

        # self.success_db_message(fileName)

        with open(self.xmlFilePath + '/' + "xml_file.txt", 'a') as f:
            f.write("\n" + fileName + ".xml")

        print(colored(f"\n{file} Successfully cleaned", 'green'))

    def old_clm_xml_format_clean_to_json(self, data, fileName, file):
        applicationNumber = \
            int(data['ClaimsDocument']['DocumentHeaderDetails']['ApplicationHeaderDetails'][
                    'ApplicationNumber'])
        date = data['ClaimsDocument']['MailRoomDate']
        documentType = 'CLM'
        sections = []
        if 'ClaimsDocument' in data:
            try:
                for i in range(len(data['ClaimsDocument']['ClaimSet']['ClaimList']['Claim'])):
                    if 'ClaimText' in data['ClaimsDocument']['ClaimSet']['ClaimList']['Claim'][i]:
                        if data['ClaimsDocument']['ClaimSet']['ClaimList']['Claim'][i]['id'].split('-')[
                            0] != 'UNKNOWN':
                            if type(data['ClaimsDocument']['ClaimSet']['ClaimList']['Claim'][i][
                                        'ClaimText']) == list:
                                try:
                                    text = \
                                        data['ClaimsDocument']['ClaimSet']['ClaimList']['Claim'][i]['ClaimText'][
                                            -1][
                                            'text']
                                    text = " ".join(text.split())
                                    section = {
                                        "text": text,
                                        "id": data['ClaimsDocument']['ClaimSet']['ClaimList']['Claim'][i]['id']
                                    }
                                    sections.append(section)
                                except:
                                    section = {
                                        "text": ' ',
                                        "id": data['ClaimsDocument']['ClaimSet']['ClaimList']['Claim'][i]['id']
                                    }
                                    sections.append(section)
                            elif type(data['ClaimsDocument']['ClaimSet']['ClaimList']['Claim'][i][
                                          'ClaimText']) != list:
                                try:
                                    text = data['ClaimsDocument']['ClaimSet']['ClaimList']['Claim'][i]['ClaimText'][
                                        'text']
                                    text = " ".join(text.split())
                                    section = {
                                        "text": text,
                                        "id": data['ClaimsDocument']['ClaimSet']['ClaimList']['Claim'][i]['id']
                                    }
                                    sections.append(section)
                                except:
                                    section = {
                                        "text": ' ',
                                        "id": data['ClaimsDocument']['ClaimSet']['ClaimList']['Claim'][i]['id']
                                    }
                                    sections.append(section)
            except Exception as e:
                pass
                # self.fail_db_message(fileName)
            getjson = {
                'applicationNumber': applicationNumber,
                'date': date,
                'documentType': documentType,
                'sections': sections
            }
            with open(self.cleanJsonPath + "/" + file, 'w') as f:
                json.dump(getjson, f, indent=4)

            # self.success_db_message(fileName)
            with open(self.xmlFilePath + '/' + "xml_file.txt", 'a') as f:
                f.write("\n" + fileName + ".xml")

            print(colored(f"\n{file} Successfully cleaned", 'green'))

    def clean_clm_file(self, file):
        fileName = file.split('.json')[0]
        with open(self.jsonFilePath + "/" + file, 'r') as f:
            data = json.load(f)
        data = json.dumps(data, indent=4)
        data = data.replace("\\t", "")
        data = data.replace("\\n", "")
        data = data.replace("#", "")
        data = data.replace("ns0:", "")
        data = json.loads(data)
        if 'ClaimsDocument' in data:
            # this method will be cleaned old CLM type of xml file into json file
            self.old_clm_xml_format_clean_to_json(data, fileName, file)
        else:
            # this method will be cleaned new CLM type of xml file into json file
            self.new_clm_xml_format_clean_to_json(data, fileName, file)

    def clean_json(self, file):
        fileName = file.split('.json')[0]
        if file.endswith('.json'):
            sfile = file.split('-')[-1]
            sfile = sfile.split('.')[0]

            # if file type is SPEC then it will be converting it to SPEC.json
            if sfile == 'SPEC':
                self.clean_spec_file(file)
            # if file type is ABST then it will be converting it to ABST.json
            elif sfile == 'ABST':
                self.clean_new_old_abst_file_to_json(file)
            # if file type is CLM then it will be converting it to CLM.json
            elif sfile == 'CLM':
                self.clean_clm_file(file)
            else:
                print(f"This {fileName}.xml file Suffix should be CLM, ABST & SPEC format")
                # self.fail_db_message(fileName)


def main():
    # this is the main function where we are calling the class to convert json to clean json format
    xml_file = "c:/search-ai-data-landing"
    XmlToJsonConverter(xml_file)


if __name__ == '__main__':
    main()
