import scrapy
import json


class LuluHypermarketSpider(scrapy.Spider):
    name = 'lulu_hypermarket'
    start_urls = ['https://www.luluhypermarket.com/en-ae/electronics']
    main_url = 'https://www.luluhypermarket.com'

    def parse(self, response):
        """
        Entry point of the spider. It parses the start URL and triggers the scraping process.
        """
        subcategories = response.css('.recommended-content > div > div > a')
        subcategory_names = subcategories.css('::text').getall()

        product_urls = [self.main_url + product.css('::attr(href)').get() for product in subcategories]

        for url in product_urls:
            yield scrapy.Request(url, callback=self.parse_product)

    def parse_product(self, response):
        """
        Parses the product page and extracts the product details.
        """
        subcategory_name = response.css('.product-sorting > div > h1::text').get().strip()

        sub_product_urls = response.css('.product-listing-sectionfashion-products .product-img a::attr(href)').getall()

        product_list = []
        for url in sub_product_urls:
            yield scrapy.Request(self.main_url + url, callback=self.parse_sub_product,
                                 meta={'subcategory_name': subcategory_name, 'product_list': product_list})

    def parse_sub_product(self, response):
        """
        Parses the sub-product page and extracts the sub-product details.
        """
        subcategory_name = response.meta['subcategory_name']

        product_name = response.css('.product-description h1::text').get().strip()
        product_price = response.css('.product-description span.item.price::text').get().strip().split('AED')[-1]

        product_summary = response.css('.product-description .description-block li::text').getall()
        product_summary = [summary.strip() for summary in product_summary]

        data = {
            "Title": product_name,
            "Price": "AED " + product_price,
            "Product Summary": product_summary
        }

        product_list = response.meta['product_list']
        product_list.append(data)
        self.save_product_details(subcategory_name, product_list)

    def save_product_details(self, subcategory_name, product_list):
        """
        Saves the product details to a JSON file.
        """
        product_details = {subcategory_name: product_list}
        with open('product_data.json', 'a') as f:
            json.dump(product_details, f, indent=4)


# Run the spider
if __name__ == '__main__':
    from scrapy.crawler import CrawlerProcess

    process = CrawlerProcess()
    process.crawl(LuluHypermarketSpider)
    process.start()
