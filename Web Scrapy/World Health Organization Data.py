import requests
import json
import pandas as pd

r = requests.get('http://apps.who.int/gho/athena/api/GHO/MH_12/.json?filter=Year:2016')
data = r.json()
print(json.dumps(data, indent=2))


list_of_data = []
for fact in data['fact']:
    for category in fact['Dim']:
        if category['category'] == 'COUNTRY':
            country_code = category['code']
        elif category['category'] == "SEX":
            sex = category['code']
    suicide_rate = fact['value']['numeric']
    list_of_data.append({'Country Code': country_code, 'Sex': sex, "Suicide Rate": suicide_rate})

country_codes = []
for country in list_of_data:
    country_codes.append(country['Country Code'])

country_codes = set(country_codes)

data_dictionary = []
for country in country_codes:
    data_dictionary.append(
        {'Country Code': country, 'Male Suicide Rate': '', 'Female Suicide Rate': '', 'Combined Suicide Rate': ''})
