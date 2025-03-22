import scrapy
# from code_test.items import Product
from lxml import html

class Code_testSpider(scrapy.Spider):
    name = "code_test"
    start_urls = ["https://example.com"]

    def parse(self, response):
        parser = html.fromstring(response.text)
        print("Visited:", response.url)
