import os
import time

filename: any = None
readFile: any = None
for root, dirs, files in os.walk("c:/search-ai-lab-bdr-landing-zone/2022-04-10"):
    for file in files:
        if file.endswith(".xml"):
            filename = file
        else:
            pass

with open("c:/search-ai-lab-bdr-landing-zone/2022-04-10/" + filename, 'r') as f:
    readFile = f.read()

t1 = time.time()
for i in range(1, 1000):
    filename1 = str(i) + filename
    with open("c:/search-ai-lab-bdr-landing-zone/2022-04-10/" + filename1, 'w') as f:
        f.write(readFile)
t2 = time.time()
print("Time taken to write files: ", t2 - t1)
