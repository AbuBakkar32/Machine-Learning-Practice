import json
import os
import shutil
import time
from xml.dom import minidom
from xml.parsers import expat

import xmltodict
from termcolor import colored


# def initialize(xml_file="c:/xmlfile"):
#     return XmlToJsonConverter(xmlFilePath=xml_file)

class XmlToJsonConverter:
    def __init__(self, xmlFilePath: any = None):
        self.xmlFilePath = xmlFilePath  # path of xml file

        self.jsonFilePath = 'c:/jsonfile'  # path of json where json file will be created
        self.cleanJsonPath = 'c:/cleanjson'  # path of json where clean json file will be created
        self.CopyXmlPath = 'c:/copyxml'  # path of xml file where xml file will be stored after cleaning
        # self.con = self.db_con()  # Established connection to database (postgres database)

        path = ['c:/jsonfile', 'c:/cleanjson', 'c:/copyxml']
        for p in path:
            if not os.path.exists(p):
                os.mkdir(p)
                print(colored("Directory " + p + " Created", 'green'))
            else:
                pass

        # call convert_xml_file_to_json function for processing xml file to json file
        self.convert_xml_file_to_json()

    # def db_con(self):
    #     try:
    #         connection = psycopg2.connect(user="postgres", password="asl123", host="localhost", port="5433",
    #                                       database="automation")
    #         self.con = connection
    #         return self.con
    #
    #     except (Exception, psycopg2.Error) as error:
    #         print("Database Can't Connected Successfully", error)

    ### This Content Belong Database fail and success Properties where data will be insert

    # def success_db_message(self, file):
    #     try:
    #         connection = self.con
    #         cursor = connection.cursor()
    #         conn = """
    #                   insert into success (file_name, time_stamp, status) values (%s, %s, %s)
    #             """
    #         cursor.execute(conn, (file + ".xml", datetime.now().date(), 'success'))
    #         connection.commit()
    #         print("Record inserted successfully into the success table")
    #         cursor.close()
    #     except:
    #         print("Data Can not insert")

    # def fail_db_message(self, file):
    #     # this block belongs to insert fail data in database
    #     try:
    #         connection = self.con
    #         cursor = connection.cursor()
    #         conn = """
    #                                             insert into fail (file_name, time_stamp, status) values (%s, %s, %s)
    #                                         """
    #         cursor.execute(conn, (
    #             file + ".xml", datetime.now().date(), 'File Not Converted XML to JSON'))
    #         connection.commit()
    #         print("Record inserted successfully into the fail table")
    #         cursor.close()
    #     except:
    #         print("Data Can not insert")

    def convert_xml_file_to_json(self):
        # for handle the exception using try and case
        t1 = time.time()
        for root, dirs, files in os.walk(self.xmlFilePath):
            if len(files) > 0:
                for file in files:
                    if file.endswith('.xml'):
                        if not os.path.exists(self.CopyXmlPath + '/' + file):  # check this file already clean or not
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
                                self.clean_json(json_file)
                            except:
                                # self.fail_db_message(file)
                                print(f"{file} File Not Converted XML to JSON")
                        else:
                            print(f"{file} File already exists")
            else:
                print(f"No XML file found in this {self.xmlFilePath} folder")
        t2 = time.time()
        print(f"Total time taken to convert xml to json file is {t2 - t1}")

    def new_spec_xml_format_clean_to_json(self, data, fileName, file):
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
            try:
                if 'boundary-data' in data['us-patent-application']['description']['p'][i]:
                    if type(data['us-patent-application']['description']['p'][i]['boundary-data']) == dict:
                        try:
                            text = data['us-patent-application']['description']['p'][i]['text'].strip()
                            text = " ".join(text.split())
                            section = {
                                "text": text,
                                "type": data['us-patent-application']['description']['p'][i]['boundary-data'][
                                    'type']
                            }
                            sections.append(section)
                        except:
                            section = {
                                "text": " ",
                                "type": data['us-patent-application']['description']['p'][i]['boundary-data'][
                                    'type']
                            }
                            sections.append(section)
                    elif type(data['us-patent-application']['description']['p'][i]['boundary-data']) == list:
                        try:
                            text = data['us-patent-application']['description']['p'][i]['text'].strip()
                            text = " ".join(text.split())
                            section = {
                                "text": text,
                                "type": data['us-patent-application']['description']['p'][i]['boundary-data'][0][
                                    'type']
                            }
                            sections.append(section)
                        except:
                            section = {
                                "text": " ",
                                "type": data['us-patent-application']['description']['p'][i]['boundary-data'][0][
                                    'type']
                            }
                            sections.append(section)
            except Exception as e:
                pass
                # self.fail_db_message(file)

        getjson = {
            'applicationNumber': applicationNumber,
            'date': date,
            'documentType': documentType,
            'sections': sections
        }

        with open(self.cleanJsonPath + "/" + file, 'w') as f:
            json.dump(getjson, f, indent=4)

        # self.success_db_message(fileName)

        shutil.copy(self.xmlFilePath + "/" + fileName + ".xml",
                    self.CopyXmlPath + "/" + fileName + ".xml")
        # os.remove(self.jsonFilePath + "/" + file)

        print(colored(f"\n{file} Successfully cleaned", 'green'))

    def old_spec_xml_format_clean_to_json(self, data, fileName, file):
        applicationNumber = \
            int(data['SpecificationDocument']['DocumentHeaderDetails']['ApplicationHeaderDetails'][
                    'ApplicationNumber'])
        date = \
            data['SpecificationDocument']['MailRoomDate']
        documentType = 'SPEC'
        sections = []
        try:
            for i in range(len(data['SpecificationDocument']['Specification']['P'])):
                try:
                    text = data['SpecificationDocument']['Specification']['P'][i]['text']
                    text = ' '.join(text.split())
                    section = {
                        "text": text,
                        "type": data['SpecificationDocument']['Specification']['P'][i]['id']
                    }
                    sections.append(section)
                except:
                    section = {
                        "text": " ",
                        "type": data['SpecificationDocument']['Specification']['P'][i]['id']
                    }
                    sections.append(section)

        except Exception as e:
            pass
            # self.fail_db_message(fileName)
        getjson = {
            'applicationNumber': applicationNumber,
            'date': date,
            'documentType': documentType,
            'sections': sections
        }

        with open(self.cleanJsonPath + "/" + file, 'w') as f:
            json.dump(getjson, f, indent=4)

        # self.success_db_message(fileName)

        shutil.copy(self.xmlFilePath + "/" + fileName + ".xml",
                    self.CopyXmlPath + "/" + fileName + ".xml")
        # os.remove(self.jsonFilePath + "/" + file)

        print(colored(f"\n{file} Successfully cleaned", 'green'))

    def clean_spec_file(self, file):
        fileName = file.split('.json')[0]
        with open(self.jsonFilePath + "/" + file, 'r') as f:
            data = json.load(f)
        data = json.dumps(data, indent=4)
        data = data.replace("\\t", "")
        data = data.replace("\\n", "")
        data = data.replace("#", "")
        data = data.replace("ns0:", "")
        data = data.replace("ns2:", "")
        data = data.replace("xsi:", "")
        data = json.loads(data)
        if 'us-patent-application' in data:
            # this method will be cleaned new SPEC type of xml file into json file
            self.new_spec_xml_format_clean_to_json(data, fileName,
                                                   file)
        elif 'SpecificationDocument' in data:
            # this method will be cleaned old SPEC type of xml file into json file
            self.old_spec_xml_format_clean_to_json(data, fileName,
                                                   file)

    def clean_new_old_abst_file_to_json(self, file):
        fileName = file.split('.json')[0]
        with open(self.jsonFilePath + "/" + file, 'r') as f:
            data = json.load(f)
        data = json.dumps(data, indent=4)
        data = data.replace("\\t", "")
        data = data.replace("\\n", "")
        data = data.replace("#", "")
        data = data.replace("ns0:", "")
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
        except Exception as e:
            pass
            # self.fail_db_message(fileName)

        getjson = {
            'applicationNumber': applicationNumber,
            'date': date,
            'documentType': documentType,
            'sections': sections
        }

        with open(self.cleanJsonPath + "/" + file, 'w') as f:
            json.dump(getjson, f, indent=4)

        # self.success_db_message(fileName)

        shutil.copy(self.xmlFilePath + "/" + fileName + ".xml",
                    self.CopyXmlPath + "/" + fileName + ".xml")
        # os.remove(self.jsonFilePath + "/" + file)
        print(colored(f"\n{file} Successfully cleaned", 'green'))

    def new_clm_xml_format_clean_to_json(self, data, fileName, file):
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
                        try:
                            text = data['us-patent-application']['claims']['claim'][i]['claim-text']['text']
                            text = " ".join(text.split())
                            section = {
                                "text": text,
                                "id": data['us-patent-application']['claims']['claim'][i]['id']
                            }
                            sections.append(section)
                        except TypeError:
                            text = data['us-patent-application']['claims']['claim'][i]['claim-text']
                            text = " ".join(text.split())
                            section = {
                                "text": text,
                                "id": data['us-patent-application']['claims']['claim'][i]['id']
                            }
                            sections.append(section)
                        except:
                            section = {
                                "text": ' ',
                                "id": data['us-patent-application']['claims']['claim'][i]['id']
                            }
                            sections.append(section)
                    elif type(data['us-patent-application']['claims']['claim'][i]['claim-text']) == list:
                        try:
                            text = data['us-patent-application']['claims']['claim'][i]['claim-text'][0]['text']
                            text = " ".join(text.split())
                            section = {
                                "text": text,
                                "id": data['us-patent-application']['claims']['claim'][i]['id']
                            }
                            sections.append(section)
                        except TypeError:
                            try:
                                text = data['us-patent-application']['claims']['claim'][i]['claim-text'][-1]['text']
                                text = " ".join(text.split())
                                section = {
                                    "text": text,
                                    "id": data['us-patent-application']['claims']['claim'][i]['id']
                                }
                                sections.append(section)
                            except TypeError:
                                text = data['us-patent-application']['claims']['claim'][i]['claim-text']
                                section = {
                                    "text": text,
                                    "id": data['us-patent-application']['claims']['claim'][i]['id']
                                }
                                sections.append(section)
                        except:
                            section = {
                                "text": ' ',
                                "id": data['us-patent-application']['claims']['claim'][i]['id']
                            }
                            sections.append(section)
        except Exception as e:
            pass
            # self.fail_db_message(fileName)
        getjson = {
            'applicationNumber': applicationNumber,
            'date': date,
            'documentType': documentType,
            'sections': sections
        }

        with open(self.cleanJsonPath + "/" + file, 'w') as f:
            json.dump(getjson, f, indent=4)
        # self.success_db_message(fileName)
        shutil.copy(self.xmlFilePath + "/" + fileName + ".xml",
                    self.CopyXmlPath + "/" + fileName + ".xml")
        # os.remove(self.jsonFilePath + "/" + file)
        print(colored(f"\n{file} Successfully cleaned", 'green'))

    def old_clm_xml_format_clean_to_json(self, data, fileName, file):
        applicationNumber = \
            int(data['ClaimsDocument']['DocumentHeaderDetails']['ApplicationHeaderDetails'][
                    'ApplicationNumber'])
        date = data['ClaimsDocument']['MailRoomDate']
        documentType = 'CLM'
        sections = []
        if 'ClaimsDocument' in data:
            try:
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
            except Exception as e:
                pass
                # self.fail_db_message(fileName)
            getjson = {
                'applicationNumber': applicationNumber,
                'date': date,
                'documentType': documentType,
                'sections': sections
            }
            with open(self.cleanJsonPath + "/" + file, 'w') as f:
                json.dump(getjson, f, indent=4)
            # self.success_db_message(fileName)
            shutil.copy(self.xmlFilePath + "/" + fileName + ".xml",
                        self.CopyXmlPath + "/" + fileName + ".xml")
            # os.remove(self.jsonFilePath + "/" + file)
            print(colored(f"\n{file} Successfully cleaned", 'green'))

    def clean_clm_file(self, file):
        fileName = file.split('.json')[0]
        with open(self.jsonFilePath + "/" + file, 'r') as f:
            data = json.load(f)
        data = json.dumps(data, indent=4)
        data = data.replace("\\t", "")
        data = data.replace("\\n", "")
        data = data.replace("#", "")
        data = data.replace("ns0:", "")
        data = json.loads(data)
        if 'ClaimsDocument' in data:
            # this method will be cleaned old CLM type of xml file into json file
            self.old_clm_xml_format_clean_to_json(data, fileName, file)
        else:
            # this method will be cleaned new CLM type of xml file into json file
            self.new_clm_xml_format_clean_to_json(data, fileName, file)

    def clean_json(self, file):
        fileName = file.split('.json')[0]
        if file.endswith('.json'):
            sfile = file.split('-')[-1]
            sfile = sfile.split('.')[0]

            # if file type is SPEC then it will be converting it to SPEC.json
            if sfile == 'SPEC':
                self.clean_spec_file(file)
            # if file type is ABST then it will be converting it to ABST.json
            elif sfile == 'ABST':
                self.clean_new_old_abst_file_to_json(file)
            # if file type is CLM then it will be converting it to CLM.json
            elif sfile == 'CLM':
                self.clean_clm_file(file)
            else:
                print(f"This {fileName}.xml file Suffix should be CLM, ABST & SPEC format")
                # self.fail_db_message(fileName)


def main():
    # this is the main function where we are calling the class to convert json to clean json format
    xml_file = "c:/xmlfile"
    XmlToJsonConverter(xml_file)


if __name__ == '__main__':
    main()
