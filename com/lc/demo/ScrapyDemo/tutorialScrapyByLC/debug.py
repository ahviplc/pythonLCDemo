#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
debug.py
debug模式跑Scrapy-just run this.
Version: 1.0
Author: LC
DateTime: 2019年1月23日12:19:48
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""

from scrapy.cmdline import execute

execute('scrapy crawl quotes'.split())

# 设置核心做法:
#
# 在scrapy项目的spider目录下，建一个main.py
#
# 输入以下内容
#
# from scrapy.cmdline import execute
# execute('scrapy crawl 爬虫名'.split())
# 爬虫文件中设置断点，在main.py 点debug 按钮
# ------------------------------------------------------------
# execute(['scrapy', 'crawl', 'quotes'])
# ------------------------------------------------------------
# scrapy 配置debug模式 - Darkman_EX的博客 - CSDN博客
# https://blog.csdn.net/Darkman_EX/article/details/80615436
