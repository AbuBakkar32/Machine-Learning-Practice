import requests
import json

with open('test.json', 'r') as f:
    data = json.load(f)
print(len(data))
data_str = json.dumps(data, indent=4)
print("Total set of data are store:", len(data_str))
