import os

filename: any = None
readFile = None
for root, dirs, files in os.walk("C:/xmlfile"):
    for file in files:
        filename = file

with open("C:/xmlfile/" + filename, 'r') as f:
    readFile = f.read()
filename = '1' + filename

with open("C:/xmlfile/" + filename, 'w') as f:
    f.write(readFile)
