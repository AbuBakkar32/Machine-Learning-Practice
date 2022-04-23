import json
import os

from termcolor import colored


def append_all_text(obj):
    text_data = []

    def get_text(obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if key == 'text':
                    txt = " ".join(value.split())
                    if len(txt) > 3:
                        if txt.endswith(':'):
                            txt = txt[:-1]
                            text_data.append(txt)
                        else:
                            text_data.append(txt)
                else:
                    get_text(value)
        elif isinstance(obj, list):
            for item in obj:
                get_text(item)

    get_text(obj)
    return text_data


def specDataClean():
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
                            int(data['us-patent-application']['us-bibliographic-data-application'][
                                    'application-reference'][
                                    'document-id'][
                                    'doc-number'])
                        date = \
                            data['us-patent-application']['us-bibliographic-data-application']['application-reference'][
                                'document-id'][
                                'date']
                        documentType = 'SPEC'
                        sections = []
                        try:
                            for i in range(len(data['us-patent-application']['description']['p'])):
                                if 'boundary-data' in data['us-patent-application']['description']['p'][i]:
                                    text = append_all_text(data['us-patent-application']['description']['p'][i])
                                    section = {
                                        "type":
                                            data['us-patent-application']['description']['p'][i]['boundary-data'][
                                                'type'],
                                        "text": text
                                    }
                                    sections.append(section)
                        except KeyError:
                            text = append_all_text(data['us-patent-application']['description']['p'][i])
                            section = {
                                "type":
                                    data['us-patent-application']['description']['p'][i]['boundary-data'][
                                        'type'],
                                "text": text
                            }
                            sections.append(section)

                    # elif 'SpecificationDocument' in data:
                    #     applicationNumber = \
                    #         int(data['SpecificationDocument']['DocumentHeaderDetails']['ApplicationHeaderDetails'][
                    #                 'ApplicationNumber'])
                    #     date = \
                    #         data['SpecificationDocument']['MailRoomDate']
                    #     documentType = 'SPEC'
                    #     sections = []
                    #     for i in range(len(data['SpecificationDocument']['Specification']['P'])):
                    #         try:
                    #             text = data['SpecificationDocument']['Specification']['P'][i]['text']
                    #             text = ' '.join(text.split())
                    #             section = {
                    #                 "text": text,
                    #                 "type": data['SpecificationDocument']['Specification']['P'][i]['id']
                    #             }
                    #             sections.append(section)
                    #         except:
                    #             section = {
                    #                 "text": " ",
                    #                 "type": data['SpecificationDocument']['Specification']['P'][i]['id']
                    #             }
                    #             sections.append(section)

                    getjson = {
                        'applicationNumber': applicationNumber,
                        'date': date,
                        'documentType': documentType,
                        'sections': sections
                    }

                with open("D:/cleanjson" + "/" + file, 'w') as f:
                    json.dump(getjson, f, indent=4)
                print(colored(f"{file} Successfully cleaned", 'green'))


specDataClean()
