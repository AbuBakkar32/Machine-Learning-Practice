""""
Author: Abu Bakkar Siddikk
Email:abubakkar.swe@gmail.com
Date: 2023-06-09
"""

# Import Necessary Libraries
import json
import requests
from bs4 import BeautifulSoup


class LuluHypermarketScraper:
    def __init__(self, url):
        """
        Initialize the scraper with the URL and set up instance variables.
        """
        self.url = url
        self.main_url = 'https://www.luluhypermarket.com'
        self.product_details = {}

    def scrape_product_urls(self):
        """
        Scrape the product URLs from the website.
        """
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        product_urls = [f'{self.main_url}{product["href"]}' for product in
                        soup.select('.recommended-content > div > div > a')]
        return product_urls

    def scrape_product_details(self, product_urls):
        """
        Scrape the product details for each URL.
        """
        for product_url in product_urls:
            product_response = requests.get(product_url)
            product_soup = BeautifulSoup(product_response.content, 'html.parser')
            product_info = product_soup.find('div', class_='product-listing-sectionfashion-products').find_all('div',
                                                                                                               class_='product-img')
            subcategory_name = product_soup.select_one('.product-sorting > div > h1').get_text(strip=True)

            sub_product_urls = [f'{self.main_url}' + product.find('a')['href'] for product in product_info]
            product_list = []
            for sub_product_url in sub_product_urls:
                sub_product_response = requests.get(sub_product_url)
                sub_product_soup = BeautifulSoup(sub_product_response.content, 'html.parser')
                sub_product_info = sub_product_soup.find('div', class_="product-description")

                product_name = sub_product_info.find('h1').get_text(strip=True)
                product_price = sub_product_info.find('span', class_='item price').get_text(strip=True).split('AED')[-1]

                ul = sub_product_info.find('div', class_='description-block').find_all('li')
                product_summary = [li.get_text(strip=True) for li in ul]

                data = {
                    "Title": product_name,
                    "Price": "AED " + product_price,
                    "Product Summary": product_summary
                }
                product_list.append(data)
            self.product_details[subcategory_name] = product_list

    def save_to_json(self, filename):
        """
        Save the product details to a JSON file.
        """
        with open(filename, 'a') as f:
            json.dump(self.product_details, f, indent=4)


def main():
    """
    Call the Class to perform the scraping process from the main function.
    """
    url = 'https://www.luluhypermarket.com/en-ae/electronics'
    scraper = LuluHypermarketScraper(url)
    product_urls = scraper.scrape_product_urls()
    scraper.scrape_product_details(product_urls)
    scraper.save_to_json('product_data.json')


if __name__ == '__main__':
    # Call the main function
    main()
