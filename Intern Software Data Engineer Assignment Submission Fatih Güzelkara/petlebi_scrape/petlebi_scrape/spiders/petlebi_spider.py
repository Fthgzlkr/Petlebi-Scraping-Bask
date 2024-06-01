import scrapy
from scrapy.crawler import CrawlerProcess
import json

class petlebi_Spider(scrapy.Spider):
    name = 'petlebi'
    start_urls = ['https://www.petlebi.com/alisveris/ara?page={}'.format(page) for page in range(0, 220)]

    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI': 'petlebi_products.json',
        'FEED_EXPORT_ENCODING': 'utf-8'    }

    def parse(self, response):
        products = response.css('.card-body.pb-0.pt-2.pl-3.pr-3')

        for product in products:
            product_json = json.loads(product.css('a.p-link::attr(data-gtm-product)').get())
            product_id = product_json['id']
            product_name = product_json['name']
            product_price = product_json['price']
            product_brand = product_json['brand']
            product_stock = product_json['dimension2']
            product_category = product_json['category']
            product_url = product.css('a.p-link::attr(href)').get()
            product_image = product.css('img::attr(data-original)').get()

            yield {
                'product_id': product_id,
                'product_name': product_name,
                'product_price': product_price,
                'product_stock': product_stock,
                'product_category': product_category,
                'product_brand': product_brand,
                'product_url': product_url,
                'product_image': product_image     }
            
process = CrawlerProcess()
process.crawl(petlebi_Spider)
process.start()