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
        # path of xml file
        self.xmlFilePath = xmlFilePath
        # path of json file where json file will be created
        self.jsonFilePath = jsonFilePath
        # call getjson function
        self.getjson()

    # convert XML file to list
    def convertXMLFileToList(self):
        # for handle the exception using try and case
        try:
            for root, dirs, files in os.walk(self.xmlFilePath):
                for file in files:
                    if file.endswith('.xml'):
                        self.xmlFile.append(file)
            return self.xmlFile
        # This is skipped if file exists
        except FileNotFoundError:
            print("FileNotFoundError")
            # This is processed instead
        except Exception as e:
            print("An exception occurred: ", e)
            # This is always processed no matter what
        finally:
            pass

    # convert xml file to json file
    def getjson(self):
        # this function is to convert xml file to json file
        try:
            # call function to read xml file
            for filename in self.convertXMLFileToList():
                # read XML file one by one
                with open(self.xmlFilePath + '/' + filename, 'r') as f:
                    xml = f.read()
                    xml = minidom.parseString(xml)
                    xml = xml.toprettyxml()
                    xml = xmltodict.parse(xml, attr_prefix='', encoding='utf-8', expat=expat)
                    baseFileName = filename.split('.xml')[0]
                    with open(self.jsonFilePath + '/' + baseFileName + '.json', 'w') as f:
                        json.dump(xml, f, indent=4)
                    self.clean_clm_file(baseFileName + '.json')
            print(colored(f"Total {len(self.xmlFile)} files Successfully converted XML to JSON", 'green'))
            # This is skipped if file exists
        except FileNotFoundError:
            print("FileNotFoundError")
            # This is processed instead
        except Exception as e:
            print("An exception occurred: ", e)
            # This is always processed no matter what
        finally:
            pass

    # clean json file
    def clean_clm_file(self, file):
        with open(self.jsonFilePath + "/" + file, 'r') as f:
            data = json.load(f)
        # clean data to remove unwanted data from json file
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
    XmlToJson()  # XmlToJson("D:/xmlfile", "D:/jsonfile")
