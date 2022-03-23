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
            # print(data['us-patent-application']['claims']['claim'][0]['claim-text']['text'])
            # print(data['us-patent-application']['claims']['claim'][3]['claim-text'])
            # print(data['us-patent-application']['claims']['claim'][6]['claim-text'][0])
            # print(data['us-patent-application']['claims']['claim'][7]['claim-text'][0]['text'])
            for i in range(len(data['us-patent-application']['claims']['claim'])):
                try:
                    text = data['us-patent-application']['claims']['claim'][i]['claim-text']['text']
                except TypeError:
                    try:
                        text = data['us-patent-application']['claims']['claim'][i]['claim-text']
                    except TypeError:
                        try:
                            text = data['us-patent-application']['claims']['claim'][i]['claim-text'][0]['text']
                        except TypeError:
                            text = data['us-patent-application']['claims']['claim'][i]['claim-text']['boundary-data'][
                                'text']
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
