import json

from bs4 import BeautifulSoup
import requests

url = requests.get('https://en.wikipedia.org/wiki/Toy_Story_3')
soup = BeautifulSoup(url.content, features="lxml")

info_box = soup.find(class_='infobox vevent')
info_row = info_box.find_all('tr')


# for row in info_row:
#     print(row.get_text())


def get_content_value(row_data):
    if row_data.find('li'):
        return [i.get_text(" ", strip=True).replace('\xa0', ' ') for i in row_data.find_all('li')]
    else:
        return row_data.get_text(" ", strip=True).replace('\xa0', ' ')

movie_info = {}

for index, row in enumerate(info_row):
    if index == 0:
        movie_info['Title'] = row.find('th').get_text(" ", strip=True)
    elif index == 1:
        continue
    else:
        content_key = row.find('th').get_text(" ", strip=True)
        content_value = get_content_value(row.find('td'))
        movie_info[content_key] = content_value


# with open('test.json', 'a') as f:
#     json.dump(movie_info, f, indent=2)

with open('test.json', 'r') as f:
    data = json.load(f)

data = json.dumps(data, indent=4)
print(data)


