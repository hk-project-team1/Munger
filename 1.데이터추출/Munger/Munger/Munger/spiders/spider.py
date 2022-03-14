import scrapy
from Munger.items import MungerItem

class MungerSpider(scrapy.Spider):
    name = "Munger"
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
            'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
            'Munger.middlewares.ScrapyWithSeleniumDownloaderMiddleware': 501,
        }
    }

    def start_requests(self):
        url = "https://finance.naver.com/news/news_search.naver?rcdate=&q=%B9%DD%B5%B5%C3%BC&x=21&y=11&sm=title.basic&pd=4&stDateStart=2022-01-01&stDateEnd=2022-03-14"
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        links = response.xpath('//*[@id="contents"]/div[2]/div/ul/li/div/a/@href').extract()
        links = list(map(response.urljoin, links))
        for link in links:
            yield scrapy.Request(link, callback=self.page_parse)     
    
    def page_parse(self, response):
        item = MungerItem()
        title1 = response.xpath('//*[@id="contentarea_left"]/div[2]/dl/dd[1]/a').extract()
        # title2 = response.xpath('//*[@id="contents"]/div[1]/div[1]/div[2]/div[1]/text()').extract()
        item["title1"] = title1
        item["text"] = response.xpath('//*[@id="contentarea_left"]/div[2]/dl/dd[2]').extract()
        #item["price"] = response.xpath('//*[@id="contents"]/div[1]/div[1]/div[2]/div[2]/text()').extract()[0]
        #item["img"] = "http:" + response.xpath('//*[@id="contents"]/div[1]/div[1]/div[1]/div[1]/img/@src').extract()[0]
        item["link"] = response.url
        yield item