#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import json
import codecs
import time

file = codecs.open(str(time.time())+'_douban_movie_api_list.json','w',encoding='utf-8')
#API
url = 'http://api.douban.com/v2/movie/top250'
# 参数列表
start=5
count=25
r = requests.get(url, params={'start': start, 'count': count})
r.encoding='UTF_8'
content=r.json()
#file.write(json.dumps(content,ensure_ascii=False))#json串输出
file.write(json.dumps(content,ensure_ascii=False,indent=4))#json串格式化输出
