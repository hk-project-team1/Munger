import scrapy
from Munger.items import TitleNewsItem

class NewsSpider(scrapy.Spider):
    name = "news"
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
            'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
            'news.middlewares.ScrapyWithSeleniumDownloaderMiddleware': 501,
        }
    }

    def start_requests(self):
        url = "https://finance.naver.com/news/news_search.naver?rcdate=&q=%B9%DD%B5%B5%C3%BC&x=23&y=9&sm=title.basic&pd=4&stDateStart=2020-01-01&stDateEnd=2022-03-15"     # url 설정 다시 해주기 
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        # response.css vs response.xpath 로 데이터 가져올 수 있음. 
        links = response.xpath('//*[@id="contents"]/div[2]/div/ul/li/div/a/@href').extract()
        links = list(map(response.urljoin, links))
        
        for link in links:
            yield scrapy.Request(link, callback=self.page_parse)     
    
    def page_parse(self, response):
        
        item =TitleNewsItem()
        title = response.xpath('//*[@id="contentarea_left"]/div[2]/dl/dt[1]/a').extract()
        #title2 = response.xpath('//*[@id="contents"]/div[1]/div[1]/div[2]/div[1]/text()').extract()
        item["title"] = response.xpath('//*[@id="contentarea_left"]/div[2]/dl/dt[1]/a/text()').extract()[0]
        item["date"] = response.xpath('//*[@id="contents"]/div[1]/div[1]/div[2]/div[2]/text()').extract()[0]
        item["id"] = response.xpath('//*[@id="contents"]/div[1]/div[1]/div[1]/div[1]/img/@src').extract()[0]
        yield item