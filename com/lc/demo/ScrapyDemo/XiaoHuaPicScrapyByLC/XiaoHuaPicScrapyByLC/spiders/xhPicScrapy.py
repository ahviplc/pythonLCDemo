#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
xhPicScrapy.py
爬虫-爬取校花网（http://www.xiaohuar.com/list-1-1.html）

执行命令:>scrapy crawl xh -o xh.json #该命令获取校花图，并写入json文件

最新大学校花-校花网
http://www.xiaohuar.com/list-1-1.html

Version: 1.0
Author: LC
DateTime: 2019年1月23日13:34:04
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""

import scrapy

# 导入item中结构化数据模板
from XiaoHuaPicScrapyByLC.items import XiaohuapicscrapybylcItem


class XhSpider(scrapy.Spider):
    # 爬虫名称，唯一
    name = "xh"
    # 允许访问的域
    allowed_domains = ["xiaohuar.com"]
    # 初始URL
    start_urls = ['http://www.xiaohuar.com/list-1-1.html']

    def parse(self, response):
        # 获取所有图片的a标签
        allPics = response.xpath('//div[@class="img"]/a')
        for pic in allPics:
            # 分别处理每个图片，取出名称及地址
            item = XiaohuapicscrapybylcItem()
            name = pic.xpath('./img/@alt').extract()[0]
            addr = pic.xpath('./img/@src').extract()[0]
            addr = 'http://www.xiaohuar.com' + addr
            item['name'] = name
            item['addr'] = addr
            # 返回爬取到的数据
            yield item
