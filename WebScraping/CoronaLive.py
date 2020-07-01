import requests
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = requests.get('https://www.worldometers.info/coronavirus/')
soup = BeautifulSoup(url.text, 'html.parser')
table = soup.find('table', id='main_table_countries_today')
table_data = table.tbody.find_all("tr")

dic = {}

for i in range(8, 222):
    try:
        key = table_data[i].find_all("a", href=True)[0].string
    except:
        key = table_data[i].find_all("td")[0].string
    value = [j.string for j in table_data[i].find_all("td")]
    dic[key] = value

column_name = ["Total Cases", "New Cases", "Total Deaths", "New Deaths", "Total Recovered", "Active Cases",
               "Serious,Critical", "Tot Cases/ 1M pop", "Deaths/1M pop", "Total Tests", "Tests/1M pop"]

df = pd.DataFrame(dic).iloc[1:, :].T.iloc[:, :11]
df.columns = column_name
df.to_csv('Corona.csv', index=False, encoding='utf-8')