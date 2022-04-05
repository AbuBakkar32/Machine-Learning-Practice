import os
# check if file not exists then create a new one
import shutil
#Github Access Token: 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

if not os.path.exists('c:/xmlfile'):
    os.makedirs('c:/xmlfile')
else:
    print("file already exists")

file_exists = os.path.exists('D:/copyxml/12001267-FAAZ01XAPPOPPY5-SPEC.xml')
shutil.move('D:/xmlfile/12001267-FAAZ01XAPPOPPY5-SPEC.xml', 'D:/copyxml/')
print(file_exists)
