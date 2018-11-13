#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import json
import codecs
import time

file = codecs.open(str(int(time.time()))+'_lmt_api_list.json','w',encoding='utf-8')#unix时间戳 秒级
#API
url = 'http://114.215.202.17:20004/xfwebapi/CIS/QueryMeterPrice'
# 参数列表
start=5
count=25
data1 = {'start':5,'count':25}
print(data1)
d1 = json.dumps(data1,sort_keys=True)
print(d1)
#r = requests.get(url, d1)
r = requests.post(url, json={"factoryCode":"0004","model":"0411","timestamp":"20181109134203","meterCode":"00086000000001","priceVer":1,"priceNo":"01","signature":"992A268BCAF416B059BF23C9C1F8D69A2323232323232323","companyCode":"051001"})
print(r)
r.encoding='UTF_8'
content=r.json()
print(content)
d2=json.dumps(content,ensure_ascii=False,indent=4,sort_keys=True)#json串 输出中文 格式化输出 排序  #是因为json.dumps 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False
file.write(d2)#json串输出  以上设置有效果
print(d2)
