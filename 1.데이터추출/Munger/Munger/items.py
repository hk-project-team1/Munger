# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

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
