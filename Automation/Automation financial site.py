import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

url = "http://eoddata.com/stocklist/NASDAQ/A.htm"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
table = soup.find('div', {'id': 'ctl00_cph1_divSymbols'})

elements = []
for tr in table.find_all('tr'):
    for td in tr.find_all('td'):
        element = td.text
        elements.append(element)
print(elements)


# symbols = []
# for y in range(0, x, 10):
#     symbols.append(elements[y])
#
# names = []
# for y in range(1, x, 10):
#     names.append(elements[y])
#
# # Pandas Dataframes
# df = pd.DataFrame(index=None)
# df['stock_symbol'] = symbols
# df['stock_name'] = names
# df.set_index('stock_symbol', inplace=True)
# # df.to_json('stock.json')
#
# with open('stock.json', 'r') as f:
#     data = json.load(f)
#
# data_str = json.dumps(data, indent=4)
# print(data_str)
















#########Using Automation###############

# url = "http://eoddata.com/stocklist/NASDAQ/A.htm"
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get(url)
#
# stock_symbol = driver.find_elements_by_css_selector('#ctl00_cph1_divSymbols > table > tbody > tr > td:nth-child(1) > a')
# symbol = []
# for x in stock_symbol:
#     sym = x.text
#     symbol.append(sym)

# time.sleep(5)
# driver.close()
# driver.quit()
# print('Thank for logged-in our website')
