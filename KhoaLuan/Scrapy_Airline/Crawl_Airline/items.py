# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlAirlineItem(scrapy.Item):

    # define the fields for your item here like:
    # name = scrapy.Field()

    link = scrapy.Field()
    from_to = scrapy.Field()
    price = scrapy.Field()
    date = scrapy.Field()
    #airport = scrapy.Field()
    '''
    flight = scrapy.Field()
    date_go = scrapy.Field()
    date_back = scrapy.Field()
    price = scrapy.Field()
    '''


