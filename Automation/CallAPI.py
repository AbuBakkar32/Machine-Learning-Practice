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

data = requests.get("https://api.test.hotelbeds.com/activity-content-api/3.0/countries/en",
                    headers={
                        "Api-key": publicKey,
                        "X-Signature": encryption,
                        "Accept": "application/json",
                        "Content-Type": "application/json",
                    })
print(data)
