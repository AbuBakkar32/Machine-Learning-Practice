import requests
import pandas as pd
from bs4 import BeautifulSoup

url = requests.get('https://www.prothomalo.com/')
soup = BeautifulSoup(url.text, 'html.parser')
data = soup.find_all('a')

link = []

for i in range(len(data)):
    a = data[i]['href']
    link.append(a)

count = 0
for l in link:
    if l.startswith('https:'):
        count += 1
        print(l)
print('totall Link: ', count)