import pandas as pd
import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.worldometers.info/world-population/')
soup = BeautifulSoup(url.text, 'lxml')

# Find The Table which table data we exactly want
table = soup.find('table', class_='table table-striped table-bordered table-hover table-condensed table-list')
header = []

# Retrive all Column Data As a single Row
for i in table.find_all('th'):
    title = i.text
    header.append(title)

# Create DataFrame using Column name
df = pd.DataFrame(columns=header)

# Insert All table row data in a row one by one
for j in table.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [tr.text for tr in row_data]
    length = len(df)
    df.loc[length] = row

# # for Save In CSV Format
# report = df.to_csv('World Population Report.csv')

