# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# import urllib
# urllib.request.Request
# from urllib.request import quote, urlopen, string, Request
from urllib.request import urlopen, Request

# import os
from os import path


class XiaohuapicscrapybylcPipeline(object):
    def process_item(self, item, spider):
        # 先把图片down到本地-F:\#MyXiaoHuaPic

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'}
        reqURL = Request(url=item['addr'], headers=headers)
        # reqURL = item['addr']

        res = urlopen(reqURL)
        file_name = path.join(r'F:\#MyXiaoHuaPic', item['name'] + '.jpg')  # 这个图片写入地址为电脑文件夹-F:\#MyXiaoHuaPic
        file_name2 = path.join(path.dirname(path.realpath(__file__)), item['name'] + '.jpg')  # 这个图片写入地址为项目本目录文件夹
        print(file_name, file_name2)

        # 图片文件写入本地
        # with open(file_name, 'wb') as fp:  # 这是使用file_name，自行替换即可
        #     fp.write(res.read())

        # 再return item
        # 这样的话命令>scrapy crawl xh -o xh.json也可以用了，不报错.
        return item
