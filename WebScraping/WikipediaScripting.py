from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.wikipedia.org/')
bs = BeautifulSoup(html, "html.parser")
nameList = bs.findAll('a', attrs={'class': 'link-box'})


data = []
for name in nameList:
    strong = name.find('strong').text
    span = name.find('small').text
    print(strong)
    print(span+'\n')
    # print(name.get_text())

