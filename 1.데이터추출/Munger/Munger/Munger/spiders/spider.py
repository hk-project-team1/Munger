<<<<<<< HEAD:1.데이터추출/Munger/Munger/spiders/spider.py
from this import d
import scrapy
from Munger.items import TitleNewsItem
=======
import scrapy
from Munger.items import MungerItem
>>>>>>> a363bccae1a43cd8b711962445ea0283cc518f5a:1.데이터추출/Munger/Munger/Munger/spiders/spider.py

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
<<<<<<< HEAD:1.데이터추출/Munger/Munger/spiders/spider.py
        url = "http://playnomore.co.kr/category/bag/24/"
=======
        url = "https://finance.naver.com/news/news_search.naver?rcdate=&q=%B9%DD%B5%B5%C3%BC&x=21&y=11&sm=title.basic&pd=4&stDateStart=2022-01-01&stDateEnd=2022-03-14"
>>>>>>> a363bccae1a43cd8b711962445ea0283cc518f5a:1.데이터추출/Munger/Munger/Munger/spiders/spider.py
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        links = response.xpath('//*[@id="contents"]/div[2]/div/ul/li/div/a/@href').extract()
        links = list(map(response.urljoin, links))
<<<<<<< HEAD:1.데이터추출/Munger/Munger/spiders/spider.py
        
=======
>>>>>>> a363bccae1a43cd8b711962445ea0283cc518f5a:1.데이터추출/Munger/Munger/Munger/spiders/spider.py
        for link in links:
            yield scrapy.Request(link, callback=self.page_parse)     
    
    def page_parse(self, response):
<<<<<<< HEAD:1.데이터추출/Munger/Munger/spiders/spider.py
        item = TitleNewsItem()
        title1 = response.xpath('//*[@id="contents"]/div[1]/div[1]/div[2]/div[1]/font/text()').extract()
        #title2 = response.xpath('//*[@id="contents"]/div[1]/div[1]/div[2]/div[1]/text()').extract()
        item["title"] = "".join(title1) 
        item["date"] = response.xpath('//*[@id="contents"]/div[1]/div[1]/div[2]/div[2]/text()').extract()[0]
        item["img"] = "http:" + response.xpath('//*[@id="contents"]/div[1]/div[1]/div[1]/div[1]/img/@src').extract()[0]
=======
        item = MungerItem()
        title1 = response.xpath('//*[@id="contentarea_left"]/div[2]/dl/dd[1]/a').extract()
        # title2 = response.xpath('//*[@id="contents"]/div[1]/div[1]/div[2]/div[1]/text()').extract()
        item["title1"] = title1
        item["text"] = response.xpath('//*[@id="contentarea_left"]/div[2]/dl/dd[2]').extract()
        #item["price"] = response.xpath('//*[@id="contents"]/div[1]/div[1]/div[2]/div[2]/text()').extract()[0]
        #item["img"] = "http:" + response.xpath('//*[@id="contents"]/div[1]/div[1]/div[1]/div[1]/img/@src').extract()[0]
>>>>>>> a363bccae1a43cd8b711962445ea0283cc518f5a:1.데이터추출/Munger/Munger/Munger/spiders/spider.py
        item["link"] = response.url
        yield item