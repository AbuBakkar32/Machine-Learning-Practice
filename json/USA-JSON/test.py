# check if file not exists then create a new one
# Github Access Token: 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

# if not os.path.exists('c:/xmlfile'):
#     os.makedirs('c:/xmlfile')
# else:
#     print("file already exists")
#
# file_exists = os.path.exists('D:/copyxml/12001267-FAAZ01XAPPOPPY5-SPEC.xml')
# shutil.move('D:/xmlfile/12001267-FAAZ01XAPPOPPY5-SPEC.xml', 'D:/copyxml/')
# print(file_exists)


# def append_new_line(file_name, text_to_append):
#     with open(file_name, "a+") as file_object:
#         file_object.seek(0)
#         data = file_object.read(100)
#         if len(data) > 0:
#             file_object.write("\n")
#         file_object.write(text_to_append)

# s = "str?in4g. !(Wit#$&h1.    Pun35ctu^)ati6on?"
# s = s.translate(str.maketrans('', '', string.punctuation))
# s = re.sub(r'[^\w\s]', '', s)
# print(s)

# with open('c:/copyxml' + '/' + "file.txt", 'r') as f:
#     if "12001267-FAAZ01Z3PPOPPY5-ABST.xml" in f.read():
#         print("file exists")
#     else:
#         print("file not exists")

# with open('c:/copyxml' + '/' + "file.txt", 'a') as f:
#     f.seek(0)
#     f.write("\n12001267-FAAZ01Z3PPOPPY5-ABST.xml")

# for create a text file
# xmlFilePath = Path("c:/xmlfile/")
# with open(xmlFilePath.joinpath('xml_file.txt'), 'w') as f:
#     f.write("")

# if 'xml_file.txt' in os.listdir(xmlFilePath):
#     print("file exists")

##### Date time format #####

# import datetime
#
# date_time = datetime.datetime.now()
#
# date_today = date_time.strftime("%Y-%m-%d")
# xml_file = f"c:/search-ai-lab-bdr-landing-zone/{date_today}"
# date_pre = datetime.datetime.today() - datetime.timedelta(days=1)
# date_pre = date_pre.strftime("%Y-%m-%d")
# print(date_pre)
