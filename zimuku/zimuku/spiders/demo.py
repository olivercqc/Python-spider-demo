# -*- coding: utf-8 -*-
import scrapy
from zimuku.items import ZimukuItem

class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['zimuku.la']
    start_urls = ['http://zimuku.la/']

    def parse(self, response):
        name = response.xpath('//b/text()').extract()[1]
        items = {}
        items["第一个"] = name
        return items
