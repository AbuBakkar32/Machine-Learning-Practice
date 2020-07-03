import requests
import json
import pandas as pd

r = requests.get('http://apps.who.int/gho/athena/api/GHO/MH_12/.json?filter=Year:2016')
data = r.json()

# Converting JSON data to Python List
list_of_data = []
for fact in data['fact']:
    for category in fact['Dim']:
        if category['category'] == 'COUNTRY':
            country_code = category['code']
        elif category['category'] == "SEX":
            sex = category['code']
    suicide_rate = fact['value']['numeric']
    list_of_data.append({'Country Code': country_code, 'Sex': sex, "Suicide Rate": suicide_rate})

print(list_of_data)


country_codes = []
for country in list_of_data:
    country_codes.append(country['Country Code'])

country_codes = set(country_codes)


# Store all data like this format in data_dictionary
data_dictionary = []
for country in country_codes:
    data_dictionary.append({'Country Code': country, 'Male Suicide Rate':'', 'Female Suicide Rate':'', 'Combined Suicide Rate':''})


# creating Python list with dictionary for each country
for data in list_of_data:
    for country in data_dictionary:
        if data['Country Code'] == country['Country Code']:
            if data['Sex'] == 'MLE':
                country['Male Suicide Rate'] = data['Suicide Rate']
            elif data['Sex'] == "FMLE":
                country['Female Suicide Rate'] = data['Suicide Rate']
            elif data['Sex'] == 'BTSX':
                country['Combined Suicide Rate'] = data['Suicide Rate']


# Create pandas dataFrame to import data as a table
suicide_rates = pd.DataFrame(data_dictionary, columns=['Country Code', 'Male Suicide Rate', 'Female Suicide Rate', 'Combined Suicide Rate'])
suicide_rates.set_index(['Country Code'], inplace=True)
suicide_rates.sort_index(inplace=True)


# country_names = []
# for country in data['dimension']:
#     country_names.append({'Country Code': country['label'], 'Country Name': country['display']})
#
# country_names_df = pd.DataFrame(country_names)
# country_names_df.set_index(['Country Code'], inplace=True)
# suicide_rates = suicide_rates.join(country_names_df, on=['Country Code'], how='inner')
# suicide_rates = suicide_rates[['Country Name', 'Combined Suicide Rate', 'Male Suicide Rate', 'Female Suicide Rate']]
#






