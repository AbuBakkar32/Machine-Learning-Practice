import os
import time

filename: any = None
readFile: any = None
for root, dirs, files in os.walk("C:/xmlfile"):
    for file in files:
        filename = file

with open("C:/xmlfile/" + filename, 'r') as f:
    readFile = f.read()

t1 = time.time()
for i in range(1, 100):
    filename1 = str(i) + filename
    with open("C:/xmlfile/" + filename1, 'w') as f:
        f.write(readFile)
t2 = time.time()
print("Time taken to write files: ", t2 - t1)
