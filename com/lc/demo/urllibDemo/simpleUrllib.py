#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
simpleUrllib.py
快速爬取一个网页
Version: 1.0
Author: LC
DateTime: 2019年1月15日15:07:54
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""
from urllib import request
import time


def main():
    file = request.urlopen('http://oneplusone.vip')  # 一加壹博客最Top-一起共创1+1>2的力量！~LC

    data = file.read()  # 读取全部

    # dataline = file.readline()  # 读取一行内容
    # print(dataline)

    savepage = open("./simpleUrllib.html", "wb")  # 将爬取的网页保存在本地
    savepage.write(data)
    savepage.close()


if __name__ == '__main__':
    startTime = time.time()
    main()
    endTime = time.time()
    print('Done, Time cost: %s ' % (endTime - startTime))

# Python3中urllib是一个URL处理包，这个包中集合了一些处理URL的模块，包括了request模块、error模块、parse模块和robotparser模块。
#
# · urllib.request模块是用来打开和读取URL的；
#
# · urllib.error模块包含一些有urllib.request产生 的错误，可以使用try进行捕捉处理；
#
# · urllib.parse模块包含了一些解析URLs的方法；
#
# · urllib.robotparser模块用来解析robots.txt文本文件.它提供了一个单独的RobotFileParser类，通过该类提供的can_fetch()方法测试爬虫是否可以下载一个页面。
