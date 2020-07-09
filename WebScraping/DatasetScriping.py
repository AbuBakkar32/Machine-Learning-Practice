import requests
from bs4 import BeautifulSoup

link = requests.get('https://www.data.gov/')
soup = BeautifulSoup(link.text, 'html.parser')
data = soup.find_all('small')
print(data)
for i in data:
    a = i.find('a').text[0:]
    b = i.find('a').attrs['href']

print('This website has :{}'.format(a))
print('This website Url :{}'.format(b))


