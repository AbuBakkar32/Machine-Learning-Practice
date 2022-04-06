import json
import os

from termcolor import colored

jsonFilePath = "D:/jsonfile"
jsonfile = []
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
                getjson = {
                    'applicationNumber': applicationNumber,
                    'date': date,
                    'documentType': documentType,
                    'sections': sections
                }
                with open("D:/cleanjson" + "/" + file, 'w') as f:
                    json.dump(getjson, f, indent=4)
                print(colored(f"{file} Successfully cleaned", 'green'))
