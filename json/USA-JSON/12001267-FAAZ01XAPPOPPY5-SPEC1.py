import json
import os

from termcolor import colored

jsonFilePath = "D:/jsonfile"
for root, dirs, files in os.walk(jsonFilePath):
    for file in files:
        if file.endswith('.json'):
            sfile = file.split('-')[-1]
            sfile = sfile.split('.')[0]
            if sfile == 'SPEC':
                with open(jsonFilePath + "/" + file, 'r') as f:
                    data = json.load(f)
                data = json.dumps(data, indent=4)
                data = data.replace("\\t", "")
                data = data.replace("\\n", "")
                data = data.replace("#", "")
                data = json.loads(data)
                applicationNumber = \
                    int(data['us-patent-application']['us-bibliographic-data-application']['application-reference'][
                            'document-id'][
                            'doc-number'])
                date = \
                    data['us-patent-application']['us-bibliographic-data-application']['application-reference'][
                        'document-id'][
                        'date']
                documentType = 'SPEC'
                sections = []
                for i in range(len(data['us-patent-application']['description']['p'])):
                    if 'boundary-data' in data['us-patent-application']['description']['p'][i]:
                        if type(data['us-patent-application']['description']['p'][i]['boundary-data']) == dict:
                            text = data['us-patent-application']['description']['p'][i]['text'].strip()
                            text = " ".join(text.split())
                            section = {
                                "text": text,
                                "type": data['us-patent-application']['description']['p'][i]['boundary-data']['type']
                            }
                            sections.append(section)
                        elif type(data['us-patent-application']['description']['p'][i]['boundary-data']) == list:
                            text = data['us-patent-application']['description']['p'][i]['text'].strip()
                            text = " ".join(text.split())
                            section = {
                                "text": text,
                                "type": data['us-patent-application']['description']['p'][i]['boundary-data'][0]['type']
                            }
                            sections.append(section)
                getjson = {
                    'applicationNumber': applicationNumber,
                    'date': date,
                    'documentType': documentType,
                    'sections': sections
                }

            with open("D:/cleanjson" + "/" + file, 'w') as f:
                json.dump(getjson, f, indent=4)
            print(colored(f"{file} Successfully cleaned", 'green'))
