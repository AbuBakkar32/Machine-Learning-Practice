import json
import os
from xml.dom import minidom

import xmltodict


class xmltojson:
    def __init__(self, path: any = None, savepath: any = None):
        self.xmlFile = []
        self.path = path
        self.savepath = savepath
        self.getjson()

    def convertXMLFileToList(self):
        # for handle the exception using try and case
        try:
            for root, dirs, files in os.walk(self.path):
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
                with open(self.path + '/' + filename, 'r') as f:  # read XML file one by one
                    xml = f.read()
                    xml = minidom.parseString(xml)
                    xml = xml.toprettyxml()
                    xml = xmltodict.parse(xml)
                    baseFileName = filename.split('.xml')[0]
                    with open(self.savepath + '/' + baseFileName + '.json', 'w') as f:
                        json.dump(xml, f, indent=4)
            print(f"Total {len(self.xmlFile)} files Successfully converted XML to JSON")
        except FileNotFoundError:  # This is skipped if file exists
            print("FileNotFoundError")
        except Exception as e:  # This is processed instead
            print("An exception occurred: ", e)
        finally:  # This is always processed no matter what
            pass


if __name__ == '__main__':
    xmltojson("D:/xmlfile", "D:/jsonfile")
