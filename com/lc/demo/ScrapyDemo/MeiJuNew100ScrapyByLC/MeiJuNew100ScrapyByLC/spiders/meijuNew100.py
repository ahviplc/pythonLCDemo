#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
meijuNew100.py
爬虫-美剧天堂前100最新（http://www.meijutt.com/new100.html）

最近更新的美剧-美剧天堂
https://www.meijutt.com/new100.html

Version: 1.0
Author: LC
DateTime: 2019年1月23日12:19:48
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""
import scrapy

# 导入item中结构化数据模板
from MeiJuNew100ScrapyByLC.items import Meijunew100ScrapybylcItem


class MeijuNew100Spider(scrapy.Spider):
    name = "meiju"
    allowed_domains = ["meijutt.com"]
    start_urls = ['http://www.meijutt.com/new100.html']

    def parse(self, response):
        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        for each_movie in movies:
            item = Meijunew100ScrapybylcItem()
            item['name'] = each_movie.xpath('./h5/a/@title').extract()[0]
            item['movieUrl'] = 'https://www.meijutt.com' + each_movie.xpath('./h5/a/@href').extract()[0]
            yield item
