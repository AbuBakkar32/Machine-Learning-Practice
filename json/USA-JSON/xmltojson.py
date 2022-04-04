import json
import os
import shutil
from datetime import datetime
from xml.dom import minidom
from xml.parsers import expat

import psycopg2
import xmltodict
from termcolor import colored


class XmlToJsonConverter:
    def __init__(self, xmlFilePath: any = None):
        self.xmlFile = []
        self.xmlFilePath = xmlFilePath  # path of xml file

        self.jsonFilePath = 'c:/jsonfile'  # path of json file where json file will be created
        self.cleanJsonPath = 'c:/cleanjson'  # path of json file where clean json file will be created
        self.CopyXmlPath = 'c:/copyxml'  # path of xml file where xml file will be stored after cleaning
        self.con = None

        path = ['c:/jsonfile', 'c:/cleanjson', 'c:/copyxml']
        for p in path:
            if not os.path.exists(p):
                os.mkdir(p)
                print(colored("Directory " + p + " Created", 'green'))
            else:
                print(f"{p} folder already exists")
        self.getjson()  # call getjson function

    def db_con(self):
        try:
            connection = psycopg2.connect(user="postgres", password="asl123", host="localhost", port="5433",
                                          database="automation")
            self.con = connection
            return self.con

        except (Exception, psycopg2.Error) as error:
            print("Database Can't Connected Successfully", error)

    def convertXMLFileToList(self):
        # for handle the exception using try and case
        for root, dirs, files in os.walk(self.xmlFilePath):
            if len(files) > 0:
                for file in files:
                    if file.endswith('.xml'):
                        if not os.path.exists(self.CopyXmlPath + '/' + file):
                            self.xmlFile.append(file)
                        else:
                            print(f"{file} File already exists")
                            os.remove(self.xmlFilePath + '/' + file)
                return self.xmlFile
            else:
                print("No XML file found")
                break

    def getjson(self):
        # this function is to convert xml file to json file
        try:
            for filename in self.convertXMLFileToList():  # call function to read xml file
                try:
                    with open(self.xmlFilePath + '/' + filename, 'r') as f:  # read XML file one by one
                        xml = f.read()
                        xml = minidom.parseString(xml)
                        xml = xml.toprettyxml()
                        xml = xmltodict.parse(xml, attr_prefix='', encoding='utf-8', expat=expat)
                        baseFileName = filename.split('.xml')[0]
                        with open(self.jsonFilePath + '/' + baseFileName + '.json', 'w') as f:
                            json.dump(xml, f, indent=4)
                except:  # This is skipped if file exists
                    print("FileNotFoundError")
                    break
            self.cleanjson()  # call cleanjson function
        except:
            pass

    # this is the end of class where we are calling the function to convert json to clean json format
    def cleanjson(self):
        global getjson
        if len(self.xmlFile) > 0:
            for root, dirs, files in os.walk(self.jsonFilePath):
                for file in files:
                    if file.endswith('.json'):
                        sfile = file.split('-')[-1]
                        sfile = sfile.split('.')[0]
                        fileName = file.split('.json')[0]
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
                                data['us-patent-application']['us-bibliographic-data-application'][
                                    'application-reference'][
                                    'document-id'][
                                    'date']
                            documentType = 'SPEC'
                            sections = []
                            for i in range(len(data['us-patent-application']['description']['p'])):
                                if 'boundary-data' in data['us-patent-application']['description']['p'][i]:
                                    try:
                                        if type(data['us-patent-application']['description']['p'][i][
                                                    'boundary-data']) == dict:
                                            text = data['us-patent-application']['description']['p'][i]['text'].strip()
                                            text = " ".join(text.split())
                                            section = {
                                                "text": text,
                                                "type": data['us-patent-application']['description']['p'][i][
                                                    'boundary-data'][
                                                    'type']
                                            }
                                            sections.append(section)
                                        elif type(
                                                data['us-patent-application']['description']['p'][i][
                                                    'boundary-data']) == list:
                                            text = data['us-patent-application']['description']['p'][i]['text'].strip()
                                            text = " ".join(text.split())
                                            section = {
                                                "text": text,
                                                "type":
                                                    data['us-patent-application']['description']['p'][i][
                                                        'boundary-data'][0][
                                                        'type']
                                            }
                                            sections.append(section)
                                    except Exception as e:
                                        print(e)
                            getjson = {
                                'applicationNumber': applicationNumber,
                                'date': date,
                                'documentType': documentType,
                                'sections': sections
                            }

                            with open(self.cleanJsonPath + "/" + file, 'w') as f:
                                json.dump(getjson, f, indent=4)
                            try:
                                self.db_con()
                                connection = self.con
                                cursor = connection.cursor()
                                fetch_student = """
                                                insert into success (file_name, time_stamp, status) values (%s, %s, %s)
                                            """
                                # Print PostgreSQL version
                                cursor.execute(fetch_student, (file, datetime.now().date(), 'success'))
                                connection.commit()
                                print("Record inserted successfully into the student table")
                                cursor.close()
                            except:
                                print("Data Can not insert")
                            shutil.move(self.xmlFilePath + "/" + fileName + ".xml",
                                        self.CopyXmlPath + "/" + fileName + ".xml")
                            os.remove(self.jsonFilePath + "/" + file)

                            print(colored(f"\n{file} Successfully cleaned", 'green'))

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

                            with open(self.cleanJsonPath + "/" + file, 'w') as f:
                                json.dump(getjson, f, indent=4)
                            try:
                                self.db_con()
                                connection = self.con
                                cursor = connection.cursor()
                                fetch_student = """
                                                insert into success (file_name, time_stamp, status) values (%s, %s, %s)
                                            """
                                # Print PostgreSQL version
                                cursor.execute(fetch_student, (file, datetime.now().date(), 'success'))
                                connection.commit()
                                print("Record inserted successfully into the student table")
                                cursor.close()
                            except:
                                print("Data Can not insert")
                            shutil.move(self.xmlFilePath + "/" + fileName + ".xml",
                                        self.CopyXmlPath + "/" + fileName + ".xml")
                            os.remove(self.jsonFilePath + "/" + file)
                            print(colored(f"\n{file} Successfully cleaned", 'green'))

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
                                data['us-patent-application']['us-bibliographic-data-application'][
                                    'application-reference'][
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
                                    elif type(
                                            data['us-patent-application']['claims']['claim'][i]['claim-text']) == list:
                                        text = data['us-patent-application']['claims']['claim'][i]['claim-text'][0][
                                            'text']
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
                                        sections.append(section)

                            getjson = {
                                'applicationNumber': applicationNumber,
                                'date': date,
                                'documentType': documentType,
                                'sections': sections
                            }

                            with open(self.cleanJsonPath + "/" + file, 'w') as f:
                                json.dump(getjson, f, indent=4)
                            try:
                                self.db_con()
                                connection = self.con
                                cursor = connection.cursor()
                                fetch_student = """
                                                insert into success (file_name, time_stamp, status) values (%s, %s, %s)
                                            """
                                # Print PostgreSQL version
                                cursor.execute(fetch_student, (file, datetime.now().date(), 'success'))
                                connection.commit()
                                print("Record inserted successfully into the student table")
                                cursor.close()
                            except:
                                print("Data Can not insert")
                            shutil.move(self.xmlFilePath + "/" + fileName + ".xml",
                                        self.CopyXmlPath + "/" + fileName + ".xml")
                            os.remove(self.jsonFilePath + "/" + file)
                            print(colored(f"\n{file} Successfully cleaned", 'green'))
                        else:
                            print("File type should be CLM, ABST and SPEC")
        else:
            pass


if __name__ == '__main__':
    xmlfile = "c:/xmlfile"
    XmlToJsonConverter(xmlfile)
