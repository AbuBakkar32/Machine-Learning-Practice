import requests
from bs4 import BeautifulSoup

url = requests.get('http://google.com/')
soup = BeautifulSoup(url.text, 'html.parser')
link = soup.find_all('a')
for lin in link:
    #print(lin)
    if "Gmail" in lin:
        print(lin.text)
        print(lin.attrs['href'])
