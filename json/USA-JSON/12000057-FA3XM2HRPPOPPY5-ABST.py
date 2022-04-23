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


def abstDataClean():
    jsonFilePath = "D:/jsonfile"
    for root, dirs, files in os.walk(jsonFilePath):
        for file in files:
            if file.endswith('.json'):
                sfile = file.split('-')[-1]
                sfile = sfile.split('.')[0]
                if sfile == 'ABST':
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
                    documentType = 'ABST'
                    sections = []

                    for i in range(len(data['us-patent-application']['abstract']['p'])):
                        try:
                            txt = append_all_text(data['us-patent-application']['abstract']['p'][i])
                            sections.append(txt)
                        except KeyError:
                            txt = append_all_text(data['us-patent-application']['abstract']['p'])
                            sections.append(txt)

                    getjson = {
                        'applicationNumber': applicationNumber,
                        'date': date,
                        'documentType': documentType,
                        'sections': sections
                    }
                    with open("D:/cleanjson" + "/" + file, 'w') as f:
                        json.dump(getjson, f, indent=4)
                    print(colored(f"{file} Successfully cleaned", 'green'))


abstDataClean()
