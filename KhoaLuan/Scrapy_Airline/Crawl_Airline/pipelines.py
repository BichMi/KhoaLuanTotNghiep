# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
class CrawlAirlinePipeline(object):
    """
    Sử dụng mongoDB để lưu data:
        DataBase_name : DBAirline
        Collection_name : Airline
    """

    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/').DBAirline
        self.collection = self.client.Airline

    def process_item(self, item, spider):
        self.collection.insert(item)

        return item

