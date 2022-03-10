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

class MungerPipeline:
    def __init__(self):
        self.file = codecs.open('Munger.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    
    def spider_closed(self, spider):
        self.file.close()


# class MySQLPipeline(object):
#     """
#     Item을 MySQL에 저장하는 Pipeline
#     """

#     def open_spider(self, spider):
#         """
#         Spider를 시작할 때, MySQL서버에 접속합니다.
#         items 테이블이 존재하지 않으면 생성합니다.
#         """
#         # settings.py 설정을 읽어 들입니다.
#         settings = spider.settings
#         params={
#             'host' : settings.get('MYSQL_HOST', 'localhost'),
#             'db' : settings.get('MYSQL_DATABASE', 'scraping'),
#             'user' : settings.get('MYSQL_USER', ''),
#             'passwd':settings.get('MYSQL_PASSWORD', ''),
#             'charset':settings.get('MYSQL_CHARSET', 'utfmb4'),
#         }

#         # MySQL 서버에 접속합니다.
#         self.conn = MySQLdb.connect(**params)
#         # 커서를 추출합니다.
#         self.c = self.conn.cursor()
#         # items 테이블이 존재하지 않으면 생성합니다.
#         self.c.execute()
#         # 변경을 커밋합니다.
#         self.conn.commit()
    
#     def close_spider(self, spider):
#         """
#         Spider가 종료될때 MySQL서버와의 접속을 끊습니다.
#         """
#         self.conn.close()
    
#     def process_item(self, item, spider):
#         """
#         Item을 items 테이블에 삽입합니다.
#         """
#         self.c.execute('INSERT INTO items (title) VALUES (%(title)s)', dict(item))
#         self.conn.commit()
#         return item


