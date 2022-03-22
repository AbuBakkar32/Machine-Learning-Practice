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
            id = data['us-patent-application']['claims']['id']
            applicationNumber = \
                data['us-patent-application']['us-bibliographic-data-application']['application-reference'][
                    'document-id'][
                    'doc-number']
            date = \
                data['us-patent-application']['us-bibliographic-data-application']['application-reference'][
                    'document-id'][
                    'date']
            documentType = id.split("-")[0]
            sections = []

            for i in range(len(data['us-patent-application']['claims']['claim'])):
                if data['us-patent-application']['claims']['claim'][i]['id'].split("-")[0] == 'CLM':
                    try:
                        text = data['us-patent-application']['claims']['claim'][i]['claim-text']['text'].strip()
                        text = " ".join(text.split())
                    except TypeError:
                        text = data['us-patent-application']['claims']['claim'][i]['claim-text'][1]['text'].strip()
                        text = " ".join(text.split())
                    section = {
                        "text": text,
                        "id": data['us-patent-application']['claims']['claim'][i]['id']
                    }
                    sections.append(section)
            getjson = {
                'applicationNumber': applicationNumber,
                'date': date,
                'documentType': documentType,
                'sections': sections
            }
            with open(jsonFilePath + "/" + file, 'w') as f:
                json.dump(getjson, f, indent=4)
