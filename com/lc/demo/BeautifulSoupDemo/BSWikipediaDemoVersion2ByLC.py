# !/usr/bin/python
# coding: utf-8

"""
维基百科-项目实施（深度优先的递归爬虫）
Version: 2.0
Author: LC
DateTime: 2018年12月24日17:05:17
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""

import requests
from bs4 import BeautifulSoup
import time
import requests
import re

exist_url = []
news_ids = []
g_writecount = 0


def scrappy(url, depth=1):
    global g_writecount
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        r = requests.get("https://en.wikipedia.org/wiki/" + url, headers=headers)
        html = r.text
    except Exception as e:
        print('Failed downloading and saving', url)
        print(e)
        exist_url.append(url)
        return None

    exist_url.append(url)
    link_list = re.findall('<a href="/wiki/([^:#=<>]*?)".*?</a>', html)
    unique_list = list(set(link_list) - set(exist_url))

    for eachone in unique_list:
        g_writecount += 1
        output = "No." + str(g_writecount) + "\t Depth:" + str(depth) + "\t" + url + ' -> ' + eachone + '\n'
        print (output)
        with open('link_wikipedia_v2_By_BSWikipediaDemoVersion2ByLC.txt', "a+") as f:
            f.write(output)
            f.close()

        if depth < 2:
            scrappy(eachone, depth + 1)


scrappy("Wikipedia")
print('done')
