import scrapy
class ArticleSpider(scrapy.Spider):
    name = 'finance'

    def start_requests(self):
        url = [
            ''
        ]