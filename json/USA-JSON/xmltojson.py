import json
import os
import shutil
import time
from datetime import datetime
from xml.dom import minidom
from xml.parsers import expat

import psycopg2
import xmltodict
from termcolor import colored


class XmlToJsonConverter:
    def __init__(self, xmlFilePath: any = None):
        self.xmlFilePath = xmlFilePath  # path of xml file

        self.jsonFilePath = 'c:/jsonfile'  # path of json where json file will be created
        self.cleanJsonPath = 'c:/cleanjson'  # path of json where clean json file will be created
        self.CopyXmlPath = 'c:/copyxml'  # path of xml file where xml file will be stored after cleaning
        self.con = self.db_con()  # Established connection to database (postgres database)

        path = ['c:/jsonfile', 'c:/cleanjson', 'c:/copyxml']
        for p in path:
            if not os.path.exists(p):
                os.mkdir(p)
                print(colored("Directory " + p + " Created", 'green'))
            else:
                print(f"{p} folder already exists")

        # call convertXMLFileToJson function
        self.convertXMLFileToJson()

    # for Established to connect to database
    def db_con(self):
        try:
            connection = psycopg2.connect(user="postgres", password="asl123", host="localhost", port="5433",
                                          database="automation")
            self.con = connection
            return self.con

        except (Exception, psycopg2.Error) as error:
            print("Database Can't Connected Successfully", error)

    def convertXMLFileToJson(self):
        # for handle the exception using try and case
        t1 = time.time()
        for root, dirs, files in os.walk(self.xmlFilePath):
            if len(files) > 0:
                for file in files:
                    if file.endswith('.xml'):
                        if not os.path.exists(self.CopyXmlPath + '/' + file):
                            try:
                                with open(self.xmlFilePath + '/' + file, 'r') as f:  # read XML file one by one
                                    xml = f.read()
                                    xml = minidom.parseString(xml)
                                    xml = xml.toprettyxml()
                                    xml = xmltodict.parse(xml, attr_prefix='', encoding='utf-8', expat=expat)
                                    baseFileName = file.split('.xml')[0]
                                    with open(self.jsonFilePath + '/' + baseFileName + '.json', 'w') as f:
                                        json.dump(xml, f, indent=4)
                                json_file = baseFileName + '.json'
                                self.cleanjson(json_file)
                            except:  # This is skipped if file exists
                                # this block belongs to insert fail data in database
                                try:
                                    connection = self.con
                                    cursor = connection.cursor()
                                    conn = """
                                        insert into fail (file_name, time_stamp, status) values (%s, %s, %s)
                                    """
                                    cursor.execute(conn, (
                                        file + ".xml", datetime.now().date(), 'File Not Converted XML to JSON'))
                                    connection.commit()
                                    print("Record inserted successfully into the fail table")
                                    cursor.close()
                                except:
                                    print("Data Can not insert")

                                print(f"{file} File Not Converted XML to JSON")
                        else:
                            print(f"{file} File already exists")
                            os.remove(self.xmlFilePath + '/' + file)
            else:
                print("No XML file found")
                break
        t2 = time.time()
        print(f"Total time taken to convert XML to JSON is {t2 - t1}")

    # this method will be cleaned SPEC type of xml file into json file
    def clean_spec_file(self, file):
        fileName = file.split('.json')[0]
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

                    # this block belongs to insert fail data in database
                    try:
                        connection = self.con
                        cursor = connection.cursor()
                        conn = """
                                        insert into fail (file_name, time_stamp, status) values (%s, %s, %s)
                                    """
                        cursor.execute(conn, (fileName + ".xml", datetime.now().date(), 'Failed to process'))
                        connection.commit()
                        print("Record inserted successfully into the fail table")
                        cursor.close()
                    except:
                        print("Data Can not insert")

        getjson = {
            'applicationNumber': applicationNumber,
            'date': date,
            'documentType': documentType,
            'sections': sections
        }

        with open(self.cleanJsonPath + "/" + file, 'w') as f:
            json.dump(getjson, f, indent=4)

        # this block belongs to insert success data in database
        try:
            connection = self.con
            cursor = connection.cursor()
            conn = """
                            insert into success (file_name, time_stamp, status) values (%s, %s, %s)
                        """
            cursor.execute(conn, (fileName + ".xml", datetime.now().date(), 'success'))
            connection.commit()
            print("Record inserted successfully into the success table")
            cursor.close()
        except:
            print("Data Can not insert")

        shutil.move(self.xmlFilePath + "/" + fileName + ".xml",
                    self.CopyXmlPath + "/" + fileName + ".xml")
        os.remove(self.jsonFilePath + "/" + file)

        print(colored(f"\n{file} Successfully cleaned", 'green'))

    # this method will be cleaned ABST type of xml file into json file
    def clean_abst_file(self, file):
        fileName = file.split('.json')[0]
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
        try:
            if type(data['us-patent-application']['abstract']['p']) == list:
                for i in range(len(data['us-patent-application']['abstract']['p'])):
                    if 'boundary-data' in data['us-patent-application']['abstract']['p'][i]:
                        sections.append(data['us-patent-application']['abstract']['p'][i]['text'])
                    else:
                        sections.append(
                            data['us-patent-application']['abstract']['p'][i]['confidence']['text'])
            else:
                sections.append(data['us-patent-application']['abstract']['p']['text'])
        except Exception as e:

            # this block belongs to insert fail data in database
            try:
                connection = self.con
                cursor = connection.cursor()
                conn = """
                                insert into fail (file_name, time_stamp, status) values (%s, %s, %s)
                            """
                cursor.execute(conn, (fileName + ".xml", datetime.now().date(), 'Failed to process'))
                connection.commit()
                print("Record inserted successfully into the fail table")
                cursor.close()
            except:
                print("Data Can not insert")

        getjson = {
            'applicationNumber': applicationNumber,
            'date': date,
            'documentType': documentType,
            'sections': sections
        }

        with open(self.cleanJsonPath + "/" + file, 'w') as f:
            json.dump(getjson, f, indent=4)

        # this block belongs to insert success data in database
        try:
            connection = self.con
            cursor = connection.cursor()
            conn = """
                            insert into success (file_name, time_stamp, status) values (%s, %s, %s)
                        """
            cursor.execute(conn, (fileName + ".xml", datetime.now().date(), 'success'))
            connection.commit()
            print("Record inserted successfully into the success table")
            cursor.close()
        except:
            print("Data Can not insert")

        shutil.move(self.xmlFilePath + "/" + fileName + ".xml",
                    self.CopyXmlPath + "/" + fileName + ".xml")
        os.remove(self.jsonFilePath + "/" + file)
        print(colored(f"\n{file} Successfully cleaned", 'green'))

    # this method will be cleaned CLM type of xml file into json file
    def clean_clm_file(self, file):
        fileName = file.split('.json')[0]
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
        try:
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
        except Exception as e:

            # this block belongs to insert fail data in database
            try:
                connection = self.con
                cursor = connection.cursor()
                conn = """
                                insert into fail (file_name, time_stamp, status) values (%s, %s, %s)
                            """
                cursor.execute(conn, (fileName + ".xml", datetime.now().date(), 'Failed to process'))
                connection.commit()
                print("Record inserted successfully into the fail table")
                cursor.close()
            except:
                print("Data Can not insert")

        getjson = {
            'applicationNumber': applicationNumber,
            'date': date,
            'documentType': documentType,
            'sections': sections
        }

        with open(self.cleanJsonPath + "/" + file, 'w') as f:
            json.dump(getjson, f, indent=4)

        # this block belongs to insert success data in database
        try:
            connection = self.con
            cursor = connection.cursor()
            conn = """
                            insert into success (file_name, time_stamp, status) values (%s, %s, %s)
                        """
            cursor.execute(conn, (fileName + ".xml", datetime.now().date(), 'success'))
            connection.commit()
            print("Record inserted successfully into the success table")
            cursor.close()
        except:
            print("Data Can not insert")

        shutil.move(self.xmlFilePath + "/" + fileName + ".xml",
                    self.CopyXmlPath + "/" + fileName + ".xml")
        os.remove(self.jsonFilePath + "/" + file)
        print(colored(f"\n{file} Successfully cleaned", 'green'))

    # this is the end of class where we are calling the function to convert json to clean json format
    def cleanjson(self, file):
        # for root, dirs, files in os.walk(self.jsonFilePath):
        #     for file in files:
        fileName = file.split('.json')[0]
        if file.endswith('.json'):
            sfile = file.split('-')[-1]
            sfile = sfile.split('.')[0]

            # if file type is SPEC then it will be converting it to SPEC.json
            if sfile == 'SPEC':
                self.clean_spec_file(file)
            # if file type is ABST then it will be converting it to ABST.json
            elif sfile == 'ABST':
                self.clean_abst_file(file)
            # if file type is CLM then it will be converting it to CLM.json
            elif sfile == 'CLM':
                self.clean_clm_file(file)
            else:
                # this block belongs to insert fail data in database
                try:
                    connection = self.con
                    cursor = connection.cursor()
                    conn = """
                                                insert into fail (file_name, time_stamp, status) values (%s, %s, %s)
                                            """
                    cursor.execute(conn,
                                   (fileName + ".xml", datetime.now().date(), 'File type should be SPEC, ABST or CLM'))
                    connection.commit()
                    print("Record inserted successfully into the fail table")
                    cursor.close()
                except:
                    print("Data Can not insert")


def main():
    # this is the main function where we are calling the class to convert json to clean json format
    xml_file = "c:/xmlfile"
    XmlToJsonConverter(xml_file)


if __name__ == '__main__':
    main()
