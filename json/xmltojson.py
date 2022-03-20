import json
import os
from xml.dom import minidom
from xml.parsers import expat

import xmltodict


class xmltojson:
    def __init__(self, xmlfilepath: any = None, jsonfilepath: any = None):
        self.xmlFile = []
        self.xmlfilepath = xmlfilepath
        self.jsonfilepath = jsonfilepath
        self.getjson()

    def convertXMLFileToList(self):
        # for handle the exception using try and case
        try:
            for root, dirs, files in os.walk(self.xmlfilepath):
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
                with open(self.xmlfilepath + '/' + filename, 'r') as f:  # read XML file one by one
                    xml = f.read()
                    xml = minidom.parseString(xml)
                    xml = xml.toprettyxml()
                    xml = xmltodict.parse(xml, attr_prefix='', encoding='utf-8', expat=expat)
                    baseFileName = filename.split('.xml')[0]
                    with open(self.jsonfilepath + '/' + baseFileName + '.json', 'w') as f:
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
