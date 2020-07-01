import requests
import pandas as pd
from bs4 import BeautifulSoup

link = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')
soup = BeautifulSoup(link.text, 'html.parser')
results = soup.find_all('span', attrs={'class': 'short-desc'})

records = []

for result in results:
    date = result.find('strong').text[0:-1] + ', 2017'
    lie = result.contents[0][1:-2]
    explanation = result.find('a').text[1:-1]
    url = result.find('a')['href']
    records.append((date, lie, explanation, url))

#print(records)

df = pd.DataFrame(records, columns=['Date', 'Lie', 'Explanation', 'URL'])
df['date'] = pd.to_datetime(df['date'])
df.to_csv('Result.csv', index=True, encoding='utf-8')
