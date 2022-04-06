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
                if 'us-patent-application' in data:
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
                                        "type":
                                            data['us-patent-application']['description']['p'][i]['boundary-data'][0][
                                                'type']
                                    }
                                    sections.append(section)
                                except:
                                    section = {
                                        "text": " ",
                                        "type":
                                            data['us-patent-application']['description']['p'][i]['boundary-data'][0][
                                                'type']
                                    }
                                    sections.append(section)
                elif 'SpecificationDocument' in data:
                    applicationNumber = \
                        int(data['SpecificationDocument']['DocumentHeaderDetails']['ApplicationHeaderDetails'][
                                'ApplicationNumber'])
                    date = \
                        data['SpecificationDocument']['MailRoomDate']
                    documentType = 'SPEC'
                    sections = []
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

                getjson = {
                    'applicationNumber': applicationNumber,
                    'date': date,
                    'documentType': documentType,
                    'sections': sections
                }

            with open("D:/cleanjson" + "/" + file, 'w') as f:
                json.dump(getjson, f, indent=4)
            print(colored(f"{file} Successfully cleaned", 'green'))
