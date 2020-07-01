import requests
from bs4 import BeautifulSoup

link = requests.get('https://www.data.gov/')
soup = BeautifulSoup(link.text, 'html.parser')
data = soup.find_all('small')

for i in data:
    a = i.find('a').text[0:]

print('This website has :{}'.format(a))


