# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from __future__ import unicode_literals
import codecs
from itemadapter import ItemAdapter
# from pymongo import MongoClient
# import MySQLdb
import json
import spiders
import aiohttp
class MungerPipeline:
    async def __init__(self):
        self.file = codecs.open('Munger.json', 'w', encoding='utf-8')

    async def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    
    async def spider_closed(self, spider):
        self.file.close()

class MySpiderAsyncio(spiders):
    async def parse(self, response):
        async with aiohttp.ClientSession() as session:

