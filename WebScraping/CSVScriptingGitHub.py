import requests
import pandas as pd
import csv

# Create your views here.
url = requests.get('https://raw.githubusercontent.com/justmarkham/trump-lies/master/trump_lies.csv')
decode = (line.decode('utf-8') for line in url.iter_lines())
reader = list(csv.reader(decode))

lists = []

for row in reader[1:]:
    temp = {
        'date': row[0],
        'lie': row[1],
        'explanation': row[2],
        'url': row[3]
    }
    lists.append(temp)
    print(lists)
"""for row in reader[1:]:
    if row[0] == '2017-04-29':
        date = row[0:]
print(date)"""

df = pd.DataFrame(lists, columns=['Date', 'Lie', 'Explanation', 'URL'])
df.to_csv('Turmp_Press.csv', index=False, encoding='utf-8')
