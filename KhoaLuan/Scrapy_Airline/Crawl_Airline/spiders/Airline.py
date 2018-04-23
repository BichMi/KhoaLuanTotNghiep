# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.utils.response import open_in_browser


class Airline(Spider):
    """
    Rút thông tin các vé khuyến mãi trên trang vietjets
    """
    name = "Airline"
    allowed_domains = ["vietjets.com.vn"]
    start_urls = ["https://vietjets.com.vn/"]

    def parse(self, response):
        open_in_browser(response)
        links = response.xpath('//*[@id="specials_0_refreshspecials_0_pnlSpecials"]/div[3]/ul/li/a/@href').extract()#response.css("div.results li a::attr(href)").extract()
        from_tos = response.xpath('//*[@id="specials_0_refreshspecials_0_pnlSpecials"]/div[3]/ul/li/a/span[1]/text()').extract()#response.css("div.results span.dest::text").extract()
        prices = response.xpath('//*[@id="specials_0_refreshspecials_0_pnlSpecials"]/div[3]/ul/li/a/span/strong/text()').extract()#response.css("span.price strong::text").extract()
        dates = response.xpath('//*[@id="specials_0_refreshspecials_0_pnlSpecials"]/div[3]/ul/li/a/span[3]/text()').extract()#response.css("div.results span.period::text").extract()
        for item in zip(links, from_tos, prices, dates):
            data = {
                'link' : item[0],
                'from_to': item[1],
                'price': item[2],
                'date': item[3],
            }
            yield data

