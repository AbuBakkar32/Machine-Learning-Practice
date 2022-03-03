import unicodedata

import pandas as pd
import requests
from bs4 import BeautifulSoup
from termcolor import colored

# 'https://chaldal.com/'
base_url = 'https://chaldal.com/'


def crawl(category):
    product_name = []
    product_price = []
    unit = []

    for i in range(len(category) - 1):
        try:
            product_name.append(category[i].find('div', class_='name').text)
            if category[i].find('div', class_='discountedPrice') is None:
                product_price.append(category[i].find('div', class_='price').text.split()[1])
            else:
                product_price.append(category[i].find('div', class_='discountedPrice').text.split()[1])
            unit.append(category[i].find('div', class_='subText').text)
        except:
            print('You Enter a wrong Keywords')

    product_name = pd.Series(product_name)
    product_price = pd.Series(product_price)
    unit = pd.Series(unit)

    product_data = pd.DataFrame({'Product Name': product_name, 'unit': unit, 'Product Price': product_price})
    print(product_data)
    try:
        product_data
    except Exception as e:
        e.args
    return product_data
    # product_data.to_csv('product_data.csv', index=False)


def check_response(response):
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        content = soup.find('div', class_='categorySection miscCategorySection onlyMiscCategorySection')
        category = content.find_all('div', class_='product')
    else:
        print('d')
    return category


def find_all_product(url, item='popular'):
    response = requests.get(url + item)
    category = check_response(response)
    try:
        product_info = crawl(category)
    except Exception as e:
        e.args
    return product_info


def get_data(base_url):
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, "html.parser")
    if soup.find('ul', class_='hasSelection level-0') is None:
        ul = soup.find('ul', class_='level-0')
    else:
        ul = soup.find('ul', class_='hasSelection level-0')

    li = ul.find_all('li')
    categories = []

    for i in range(len(li)):
        data = unicodedata.normalize("NFKD", li[i].text)
        categories.append(data)

    for i, j in enumerate(categories):
        print(f"{i + 1} {j}")

    num = int(input(colored(f'\nPlease Select the product Category as Number 1-{len(categories)}: ', 'red')))
    selected_category = categories[num - 1]
    select_item = selected_category.strip().replace(" ", "-").lower()
    print(f'You Have Selected {colored(select_item, "green")} Item \n')
    try:
        get_data = find_all_product(base_url, select_item)
    except Exception as e:
        e.args
    return get_data


if __name__ == '__main__':
    try:
        while True:
            get_data(base_url)
    except Exception as e:
        e.args
