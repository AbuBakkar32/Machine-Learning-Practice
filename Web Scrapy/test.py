import requests
from bs4 import BeautifulSoup

base_url = 'https://chaldal.com/popular'
response = requests.get(base_url)
soup = BeautifulSoup(response.content, "lxml")
soup = soup.html
if soup.find('ul', class_='hasSelection level-0') is None:
    ul = soup.find('ul', class_='level-0')
    print(ul.li)
else:
    ul = soup.find('ul', class_='hasSelection level-0')
    li = ul.find_all('li')
    print(li[2])
