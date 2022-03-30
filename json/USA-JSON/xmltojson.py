import json
import os
import time
from xml.dom import minidom
from xml.parsers import expat

import xmltodict
from termcolor import colored


class XmlToJson:
    def __init__(self, xmlFilePath: any = None, jsonFilePath: any = None):
        self.xmlFile = []
        self.xmlFilePath = xmlFilePath  # path of xml file
        self.jsonFilePath = jsonFilePath  # path of json file where json file will be created
        self.getjson()  # call getjson function

    def convertXMLFileToList(self):
        # for handle the exception using try and case
        try:
            for root, dirs, files in os.walk(self.xmlFilePath):
                for file in files:
                    if file.endswith('.xml'):
                        self.xmlFile.append(file)
            return self.xmlFile
        except FileNotFoundError:  # This is skipped if file exists
            print("FileNotFoundError")
        except Exception as e:  # This is processed instead
            print("An exception occurred: ", e)
        finally:  # This is always processed no matter what
            pass

    def getjson(self):
        # this function is to convert xml file to json file
        try:
            for filename in self.convertXMLFileToList():  # call function to read xml file
                with open(self.xmlFilePath + '/' + filename, 'r') as f:  # read XML file one by one
                    xml = f.read()
                    xml = minidom.parseString(xml)
                    xml = xml.toprettyxml()
                    xml = xmltodict.parse(xml, attr_prefix='', encoding='utf-8', expat=expat)
                    baseFileName = filename.split('.xml')[0]
                    with open(self.jsonFilePath + '/' + baseFileName + '.json', 'w') as f:
                        json.dump(xml, f, indent=4)
                print(colored(f"{filename} files Successfully converted XML to JSON", 'green'))
                time.sleep(1)
        except FileNotFoundError:  # This is skipped if file exists
            print("FileNotFoundError")
        except Exception as e:  # This is processed instead
            print("An exception occurred: ", e)
        finally:  # This is always processed no matter what
            pass

    # this is the end of class where we are calling the function to convert josn to clean json formet
    def cleanjson(self):
        print("\nPlease wait while cleaning json file started\n")
        time.sleep(3)
        for root, dirs, files in os.walk(self.jsonFilePath):
            for file in files:
                if file.endswith('.json'):
                    sfile = file.split('-')[-1]
                    sfile = sfile.split('.')[0]
                    if sfile == 'SPEC':  # if file name is SPEC.json then we are converting it to SPEC.json
                        with open(self.jsonFilePath + "/" + file, 'r') as f:
                            data = json.load(f)
                        data = json.dumps(data, indent=4)
                        data = data.replace("\\t", "")
                        data = data.replace("\\n", "")
                        data = data.replace("#", "")
                        data = json.loads(data)
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
                        for i in range(len(data['us-patent-application']['description']['p'])):
                            if 'boundary-data' in data['us-patent-application']['description']['p'][i]:
                                if type(data['us-patent-application']['description']['p'][i]['boundary-data']) == dict:
                                    text = data['us-patent-application']['description']['p'][i]['text'].strip()
                                    text = " ".join(text.split())
                                    section = {
                                        "text": text,
                                        "type": data['us-patent-application']['description']['p'][i]['boundary-data'][
                                            'type']
                                    }
                                    sections.append(section)
                                elif type(
                                        data['us-patent-application']['description']['p'][i]['boundary-data']) == list:
                                    text = data['us-patent-application']['description']['p'][i]['text'].strip()
                                    text = " ".join(text.split())
                                    section = {
                                        "text": text,
                                        "type":
                                            data['us-patent-application']['description']['p'][i]['boundary-data'][0][
                                                'type']
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
                        time.sleep(1)

                    elif sfile == 'ABST':  # if file name is ABST.json then we are converting it to ABST.json
                        with open(self.jsonFilePath + "/" + file, 'r') as f:
                            data = json.load(f)
                        data = json.dumps(data, indent=4)
                        data = data.replace("\\t", "")
                        data = data.replace("\\n", "")
                        data = data.replace("#", "")
                        data = json.loads(data)
                        applicationNumber = \
                            int(data['us-patent-application']['us-bibliographic-data-application'][
                                    'application-reference'][
                                    'document-id'][
                                    'doc-number'])
                        date = \
                            data['us-patent-application']['us-bibliographic-data-application'][
                                'application-reference'][
                                'document-id'][
                                'date']
                        documentType = 'ABST'
                        sections = []
                        if type(data['us-patent-application']['abstract']['p']) == list:
                            for i in range(len(data['us-patent-application']['abstract']['p'])):
                                if 'boundary-data' in data['us-patent-application']['abstract']['p'][i]:
                                    sections.append(data['us-patent-application']['abstract']['p'][i]['text'])
                                else:
                                    sections.append(
                                        data['us-patent-application']['abstract']['p'][i]['confidence']['text'])
                        else:
                            sections.append(data['us-patent-application']['abstract']['p']['text'])
                        getjson = {
                            'applicationNumber': applicationNumber,
                            'date': date,
                            'documentType': documentType,
                            'sections': sections
                        }
                        with open("D:/cleanjson" + "/" + file, 'w') as f:
                            json.dump(getjson, f, indent=4)
                        print(colored(f"{file} Successfully cleaned", 'green'))
                        time.sleep(1)
                    elif sfile == 'CLM':
                        with open(self.jsonFilePath + "/" + file, 'r') as f:
                            data = json.load(f)
                        data = json.dumps(data, indent=4)
                        data = data.replace("\\t", "")
                        data = data.replace("\\n", "")
                        data = data.replace("#", "")
                        data = json.loads(data)
                        applicationNumber = \
                            int(data['us-patent-application']['us-bibliographic-data-application'][
                                    'application-reference'][
                                    'document-id'][
                                    'doc-number'])
                        date = \
                            data['us-patent-application']['us-bibliographic-data-application']['application-reference'][
                                'document-id'][
                                'date']
                        documentType = 'CLM'
                        sections = []
                        for i in range(len(data['us-patent-application']['claims']['claim'])):
                            if data['us-patent-application']['claims']['claim'][i]['id'].split('-')[0] != 'UNKNOWN':
                                if type(data['us-patent-application']['claims']['claim'][i]['claim-text']) != list:
                                    text = data['us-patent-application']['claims']['claim'][i]['claim-text'][
                                        'text'].strip()
                                    text = " ".join(text.split())
                                    section = {
                                        "text": text,
                                        "id": data['us-patent-application']['claims']['claim'][i]['id']
                                    }
                                    sections.append(section)
                                elif type(data['us-patent-application']['claims']['claim'][i]['claim-text']) == list:
                                    text = data['us-patent-application']['claims']['claim'][i]['claim-text'][0]['text']
                                    text = " ".join(text.split())
                                    section = {
                                        "text": text,
                                        "id": data['us-patent-application']['claims']['claim'][i]['id']
                                    }
                                    sections.append(section)
                                else:
                                    section = {
                                        "text": '',
                                        "id": data['us-patent-application']['claims']['claim'][i]['id']
                                    }

                            getjson = {
                                'applicationNumber': applicationNumber,
                                'date': date,
                                'documentType': documentType,
                                'sections': sections
                            }
                        with open("D:/cleanjson" + "/" + file, 'w') as f:
                            json.dump(getjson, f, indent=4)
                        print(colored(f"{file} Successfully cleaned", 'green'))
                        time.sleep(1)
                    else:
                        print("Someting Went Wrong")


if __name__ == '__main__':
    cnvjson = XmlToJson("D:/xmlfile", "D:/jsonfile")
    cnvjson.cleanjson()
