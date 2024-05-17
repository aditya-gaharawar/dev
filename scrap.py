import scrapy
from pymongo import MongoClient

class ExampleSpider(scrapy.Spider):
    name = "example"
    start_urls = ['http://example.com']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['socialmedia_db']
        self.collection = self.db['raw_data']

    def parse(self, response):
        for post in response.css('div.post'):
            item = {
                'title': post.css('h2.title::text').get(),
                'content': post.css('div.content::text').get(),
            }
            self.collection.insert_one(item)
