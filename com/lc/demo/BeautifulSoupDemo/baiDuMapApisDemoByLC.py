# !/usr/bin/python
# coding: utf-8

"""
百度地图API
Version: 1.1
Author: LC
DateTime: 2018年12月24日17:03:54
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""

import requests
import json


# 获取某城市所有公园的具体信息
def getjson(loc):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    pa = {
        'q': '公园',
        'region': loc,
        'scope': '2',
        'page_size': 20,
        'page_num': 0,
        'output': 'json',
        'ak': 'DDtVK6HPruSSkqHRj5gTk0rc'
    }
    r = requests.get("http://api.map.baidu.com/place/v2/search", params=pa, headers=headers)
    decodejson = json.loads(r.text)
    return decodejson


# getjson('北京市')
print(getjson('北京市'))

print('------------------------------------------------------------------------------------------------------------')

# 获取所有拥有公园的城市


# 执行获取,写入txt
province_list = ['江苏省', '浙江省', '广东省', '福建省', '山东省', '河南省', '河北省', '四川省', '辽宁省', '云南省',
                 '湖南省', '湖北省', '江西省', '安徽省', '山西省', '广西壮族自治区', '陕西省', '黑龙江省', '内蒙古自治区',
                 '贵州省', '吉林省', '甘肃省', '新疆维吾尔自治区', '海南省', '宁夏回族自治区', '青海省', '西藏自治区']
for eachprovince in province_list:
    decodejson = getjson(eachprovince)
    for eachcity in decodejson['results']:
        city = eachcity['name']
        num = eachcity['num']
        output = '\t'.join([city, str(num)]) + '\r\n'
        with open('cities_LC.txt', "a+", encoding='utf-8') as f:
            f.write(output)
            f.close()
print('完事了')
# {'status': 401, 'message': '当前并发量已经超过约定并发配额，限制访问'}

#


# 获取所有拥有公园的城市-加-'北京市','上海市','重庆市','天津市','香港特别行政区','澳门特别行政区'
decodejson = getjson('全国')
six_cities_list = ['北京市', '上海市', '重庆市', '天津市', '香港特别行政区', '澳门特别行政区', ]
for eachprovince in decodejson['results']:
    city = eachprovince['name']
    num = eachprovince['num']
    if city in six_cities_list:
        output = '\t'.join([city, str(num)]) + '\r\n'
        with open('cities_LC_all.txt', "a+", encoding='utf-8') as f:
            f.write(output)
            f.close()
