# -*- coding: utf-8 -*-
import scrapy
import requests
from scrapy.utils.response import open_in_browser


class Airline(scrapy.Spider):
    """
    Rút thông tin các vé máy bay trên trang Vietjets:
        Giả lập Request (done)
        Chờ trang load dữ liệu & rút thông tin
    """
    name = "RequestAirline"
    allowed_domains = ['vietjets.com.vn']
    start_urls = ['https://vietjets.com.vn/']

    def parse(self, response):
        req = requests.get('https://vietjets.com.vn/')
        header = {
            'Host': 'https://vietjets.com.vn/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://vietjets.com.vn/',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '174',
            'Cookie': str(req.cookies),
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
        airport = ['TP.Hồ+Chí+Minh+(SGN)', 'Hải+Phòng+(HPH)', 'Hà+Nội+(HAN)', 'Huế+(HUI)']
        for i in range(len(airport)):
            for j in range(i + 1, len(airport)):
                formdata = {
                    'flightType': '0',
                    'depAirport': airport[i],
                    'arvAirport': airport[j],
                    'depDate': '09/01/2018',
                    'adultNo': '1',
                    'childNo': '0',
                    'infantNo': '0',
                    'rdoTravelPref': 'on'
                }
                yield scrapy.FormRequest.from_response(response,
                                                       formdata=formdata,
                                                       callback=self.parse_item,)

    def parse_item(self, response):
        """
        Dữ liệu cần rút
        """
        flights = response.xpath('//*[@id="DataTables_Table_0"]/tbody/tr/td[2]/text()').extract()
        date_gos = response.xpath('//*[@id="DataTables_Table_0"]/tbody/tr/td[3]/text()').extract()
        date_backs = response.xpath('//*[@id="DataTables_Table_0"]/tbody/tr/td[4]/text()').extract()
        prices = response.xpath('//*[@id="DataTables_Table_0"]/tbody/tr/td[6]/span/text()').extract()

        open_in_browser(response)
        for item in zip(flights, date_gos, date_backs, prices):
            data = {
                'flight' : item[0],
                'date_go': item[1],
                'date_back': item[2],
                'price': item[3],
            }
            yield data

