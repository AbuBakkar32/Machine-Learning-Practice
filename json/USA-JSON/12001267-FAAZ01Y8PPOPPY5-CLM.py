# import json
# import os
#
# from termcolor import colored
#
# jsonFilePath = "D:/jsonfile"
# jsonfile = []
# for root, dirs, files in os.walk(jsonFilePath):
#     for file in files:
#         if file.endswith('.json'):
#             sfile = file.split('-')[-1]
#             sfile = sfile.split('.')[0]
#             if sfile == 'CLM':
#                 with open(jsonFilePath + "/" + file, 'r') as f:
#                     data = json.load(f)
#                 data = json.dumps(data, indent=4)
#                 data = data.replace("\\t", "")
#                 data = data.replace("\\n", "")
#                 data = data.replace("#", "")
#                 data = json.loads(data)
#                 applicationNumber = \
#                     int(data['us-patent-application']['us-bibliographic-data-application']['application-reference'][
#                             'document-id'][
#                             'doc-number'])
#                 date = \
#                     data['us-patent-application']['us-bibliographic-data-application']['application-reference'][
#                         'document-id'][
#                         'date']
#                 documentType = 'CLM'
#                 sections = []
#                 for i in range(len(data['us-patent-application']['claims']['claim'])):
#                     if data['us-patent-application']['claims']['claim'][i]['id'].split('-')[0] != 'UNKNOWN':
#                         if type(data['us-patent-application']['claims']['claim'][i]['claim-text']) != list:
#                             text = data['us-patent-application']['claims']['claim'][i]['claim-text']['text'].strip()
#                             text = " ".join(text.split())
#                             section = {
#                                 "text": text,
#                                 "id": data['us-patent-application']['claims']['claim'][i]['id']
#                             }
#                             sections.append(section)
#                         elif type(data['us-patent-application']['claims']['claim'][i]['claim-text']) == list:
#                             text = data['us-patent-application']['claims']['claim'][i]['claim-text'][0]['text']
#                             text = " ".join(text.split())
#                             section = {
#                                 "text": text,
#                                 "id": data['us-patent-application']['claims']['claim'][i]['id']
#                             }
#                             sections.append(section)
#                         else:
#                             section = {
#                                 "text": '',
#                                 "id": data['us-patent-application']['claims']['claim'][i]['id']
#                             }
#
#                     getjson = {
#                         'applicationNumber': applicationNumber,
#                         'date': date,
#                         'documentType': documentType,
#                         'sections': sections
#                     }
#                 with open("D:/cleanjson" + "/" + file, 'w') as f:
#                     json.dump(getjson, f, indent=4)
#                 print(colored(f"{file} Successfully cleaned", 'green'))
import time

from progress.spinner import MoonSpinner

# for i in tqdm(range(100)):
#     time.sleep(0.001)

with MoonSpinner('Processing…') as bar:
    for i in range(100):
        time.sleep(0.02)
