import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the website
url = 'https://www.luluhypermarket.com/en-ae/electronics'
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Scrape subcategories
subcategories = soup.find('div', class_='recommended-content').find_all('a')
print(subcategories)
subcategory_names = [subcategory.get_text(strip=True) for subcategory in subcategories]

# Scrape product listings and URLs
products = soup.select('.plp-product-name')
product_names = [product.get_text(strip=True) for product in products]
product_urls = [product.find('a')['href'] for product in products]

# Scrape product details
product_details = []
for product_url in product_urls:
    product_response = requests.get(product_url)
    product_soup = BeautifulSoup(product_response.content, 'html.parser')
    product_info = product_soup.select_one('.product-info')
    if product_info:
        product_details.append(product_info.get_text(strip=True))
    else:
        product_details.append('')

# Write data to CSV file
with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Category', 'Product', 'Details'])
    for category, product, details in zip(subcategory_names, product_names, product_details):
        writer.writerow([category, product, details])
