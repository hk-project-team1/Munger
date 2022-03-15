# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

<<<<<<< HEAD:1.데이터추출/Munger/Munger/items.py
class TitleNewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    id = scrapy.Field()
    link = scrapy.Field()
    
class BodyItem(scrapy.Item):
    date = scrapy.Field()
    body = scrapy.Field()
=======
class MungerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    #price = scrapy.Field()
    #img = scrapy.Field()
    link = scrapy.Field()
    text = scrapy.Field()
    
>>>>>>> a363bccae1a43cd8b711962445ea0283cc518f5a:1.데이터추출/Munger/Munger/Munger/items.py
