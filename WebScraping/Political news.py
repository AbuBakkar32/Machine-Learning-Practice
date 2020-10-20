# import time
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import json
#
# url = "https://www.bbc.com/news/blogs-the-papers-54405341"
# page = requests.get(url)
# soup = BeautifulSoup(page.text, 'lxml')
# div = soup.find_all('div', {'class': 'css-83cqas-RichTextContainer'})
#
# newslist = []
# for news in div:
#     n = news.text
#     newslist.append(n)
#
# print(newslist)
#
# for n, i in enumerate(newslist):
#     print(f"{n}. {i}")


# ********************************************Using Automation********************************************

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.maximize_window()
browser.implicitly_wait(3)

browser.get("https://www.bbc.com/news/blogs-the-papers-54405341")
div = browser.find_elements_by_class_name('css-83cqas-RichTextContainer')

newslist = []
for news in div:
    n = news.text
    newslist.append(n)

print(newslist)

for n, i in enumerate(newslist):
    print(f"{n}. {i}")


browser.close()
browser.quit()
