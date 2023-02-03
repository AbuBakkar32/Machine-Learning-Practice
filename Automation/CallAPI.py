import hashlib
import json
from datetime import datetime

import requests

publicKey = "ff81875fcd84aeeb4324d40d5a90a594"
privetKey = "c83578204d"
timeAPI = requests.get("https://api.binance.com/api/v1/time")

servertime = json.loads(timeAPI.text)
time = servertime['serverTime']
assemble = (publicKey + privetKey + str(time))

encryption = hashlib.sha256(assemble.encode('utf-8')).hexdigest()
print(encryption)
data = requests.get("https://api.test.hotelbeds.com/activity-content-api/3.0/countries/en",
                    headers={
                        "Api-key": publicKey,
                        "X-Signature": "448742454195b526d719e586ae4f683fb0afaa8e4281a7456cdc269fb977b1a8",
                        "Accept": "application/json",
                        "Content-Type": "application/json",
                    })
print(json.dumps(data.json(), indent=4, sort_keys=True))
# import json
#
# import requests
# import hmac
# import hashlib
# import base64
#
# # Define the API endpoint URL
# url = "https://api.test.hotelbeds.com/activity-content-api/3.0/countries/en"
#
# # Define the API key and secret
# api_key = "ff81875fcd84aeeb4324d40d5a90a594"
# api_secret = "c83578204d"
#
# timeAPI = requests.get("https://api.binance.com/api/v1/time")
#
# servertime = json.loads(timeAPI.text)
# time = servertime['serverTime']
# assemble = (api_key + api_secret + str(time))
#
# signature = hashlib.sha256(assemble.encode()).hexdigest()
# print(signature)
# # Set the headers with the API key and X-Signature
# headers = {
#     "Api-Key": api_key,
#     "X-Signature": "448742454195b526d719e586ae4f683fb0afaa8e4281a7456cdc269fb977b1a8",
#     "Accept": "application/json",
#     "Content-Type": "application/json",
# }
#
# # Make the API request
# response = requests.get(url, headers=headers)
#
# # Check the status code of the response
# if response.status_code == 200:
#     # Do something with the response data
#     data = response.json()
#     print(data)
# else:
#     # Handle the error
#     print(f"Request failed with status code {response.status_code}")