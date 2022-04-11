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
            if sfile == 'CLM':
                with open(jsonFilePath + "/" + file, 'r') as f:
                    data = json.load(f)
                data = json.dumps(data, indent=4)
                data = data.replace("\\t", "")
                data = data.replace("\\n", "")
                data = data.replace("#", "")
                data = data.replace("ns0:", "")
                data = json.loads(data)
                applicationNumber = \
                    int(data['ClaimsDocument']['DocumentHeaderDetails']['ApplicationHeaderDetails'][
                            'ApplicationNumber'])
                date = data['ClaimsDocument']['MailRoomDate']
                documentType = 'CLM'
                sections = []
                if 'ClaimsDocument' in data:
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
                getjson = {
                    'applicationNumber': applicationNumber,
                    'date': date,
                    'documentType': documentType,
                    'sections': sections
                }
            with open("D:/cleanjson" + "/" + file, 'w') as f:
                json.dump(getjson, f, indent=4)
            print(colored(f"{file} Successfully cleaned", 'green'))
