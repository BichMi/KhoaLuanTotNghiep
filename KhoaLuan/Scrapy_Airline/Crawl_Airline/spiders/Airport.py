# -*- coding: utf-8 -*-
from scrapy import Spider
from twisted.internet import reactor
from scrapy.utils.log import configure_logging
from scrapy.crawler import CrawlerProcess
from scrapy.utils.response import open_in_browser


class Airport(Spider):
    """
    Rút thông tin các nơi đi, đến của trang vietjets
    """
    name = "Airport"
    allowed_domains = ["vietjets.com.vn"]
    start_urls = ["https://vietjets.com.vn/"]

    def parse(self, response):
        open_in_browser(response)
        """
        response.css("option.grot::text").extract() => lấy ra một list các nước
        """
        airports = response.xpath('//*[@id="depAirport"]/option/text()').extract()#response.css("option::text").extract()

        for item in zip(airports):
            data2 = {
                'airport' : item[0],
            }
            yield data2

