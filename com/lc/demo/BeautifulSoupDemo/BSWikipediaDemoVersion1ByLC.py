# !/usr/bin/python
# coding: utf-8

"""
维基百科-网站分析
Version: 1.0
Author: LC
DateTime: 2018年12月24日17:04:53
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""

import requests
from bs4 import BeautifulSoup
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
r = requests.get("https://en.wikipedia.org/wiki/Wikipedia", headers=headers)
html = r.text
bsObj = BeautifulSoup(html, "lxml")

for link in bsObj.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])
