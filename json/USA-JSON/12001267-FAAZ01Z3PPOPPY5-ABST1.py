import json
import os

jsonFilePath = "D:/jsonfile"
jsonfile = []
for root, dirs, files in os.walk(jsonFilePath):
    for file in files:
        if file.endswith('.json'):
            with open(jsonFilePath + "/" + file, 'r') as f:
                data = json.load(f)
            data = json.dumps(data, indent=4)
            data = data.replace("\\t", "")
            data = data.replace("\\n", "")
            data = data.replace("#", "")
            data = json.loads(data)
            applicationNumber = \
                data['us-patent-application']['us-bibliographic-data-application']['application-reference'][
                    'document-id'][
                    'doc-number']
            date = \
                data['us-patent-application']['us-bibliographic-data-application']['application-reference'][
                    'document-id'][
                    'date']
            documentType = "ABST"
            sections = []
            section = {
                "text": data['us-patent-application']['abstract']['p'][0]['text'],
                "id": data['us-patent-application']['abstract']['id']
            }
            sections.append(section)
            getjson = {
                'applicationNumber': applicationNumber,
                'date': date,
                'documentType': documentType,
                'sections': section
            }
            with open(jsonFilePath + "/" + file, 'w') as f:
                json.dump(getjson, f, indent=4)
