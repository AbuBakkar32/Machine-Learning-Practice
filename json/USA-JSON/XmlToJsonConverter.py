# Import all necessary module
import json
import os
from xml.dom import minidom
from xml.parsers import expat

import xmltodict
from termcolor import colored


# xml to json coverter class
class XmlToJson:
    def __init__(self, xmlFilePath: any = "D:/xmlfile", jsonFilePath: any = "D:/jsonfile"):
        self.xmlFile = []
        self.xmlFilePath = xmlFilePath  # path of xml file
        self.jsonFilePath = jsonFilePath  # path of json file where json file will be created
        self.getjson()  # call getjson function

    # convert XML file to list
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

    # convert xml file to json file
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
                    self.clean_clm_file(baseFileName + '.json')
            print(colored(f"Total {len(self.xmlFile)} files Successfully converted XML to JSON", 'green'))
        except FileNotFoundError:  # This is skipped if file exists
            print("FileNotFoundError")
        except Exception as e:  # This is processed instead
            print("An exception occurred: ", e)
        finally:  # This is always processed no matter what
            pass

    # clean json file
    def clean_clm_file(self, file):
        with open(self.jsonFilePath + "/" + file, 'r') as f:
            data = json.load(f)
        data = json.dumps(data, indent=4)
        data = data.replace("\\t", "")
        data = data.replace("\\n", "")
        data = data.replace("#", "")
        data = data.replace("ns0:", "")
        data = data.replace("ns2:", "")
        data = data.replace("xsi:", "")
        data = data.replace("pat:", "")
        data = data.replace("com:", "")
        data = json.loads(data)
        with open(self.jsonFilePath + "/" + file, 'w') as f:
            json.dump(data, f, indent=4)


if __name__ == '__main__':
    XmlToJson() # XmlToJson("D:/xmlfile", "D:/jsonfile")
