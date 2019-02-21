#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
jsonDemo.py

Python3 JSON 数据解析
JSON (JavaScript Object Notation) 是一种轻量级的数据交换格式。它基于ECMAScript的一个子集。

Python3 中可以使用 json 模块来对 JSON 数据进行编解码，它包含了两个函数：
json.dumps(): 对数据进行编码。
json.loads(): 对数据进行解码。

Version: 1.0
Author: LC
DateTime: 2019年2月21日12:35:21
UpdateTime: None
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

import json

# 处理json，可以将原始json串，转成字典类型，再进行一些处理，提取数据的操作。

# Python 字典类型转换为 JSON 对象
# 字典类型data
data = {
    'no': 1,
    'name': 'LC',
    'url': 'http://www.oneplusone.top',
    "hey": "guy",
    "anumber": 243,
    "anobject": {
        "whoa": "nuts",
        "anarray": [
            1,
            2,
            3
        ],
        "more": "stuff"
    },
    "awesome": True,
    "bogus": False,
    "meaning": None,
    "japanese": "明日がある。",
    "link": "http://jsonview.com",
    "notLink": "http://jsonview.com is great"
}

# 打印所有的key
print(data.keys())

print("新增之前：", data)

data.setdefault("age", "18")

print("新增之后：", data)

print("data1['url']: ", data['url'])

json_str = json.dumps(data)
json_str_ensure_ascii = json.dumps(data, ensure_ascii=False)

print("Python 原始数据：", repr(data))
print("JSON 对象：", json_str)
print("JSON-ensure_ascii 对象：", json_str_ensure_ascii)

# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print("data2['name']: ", data2['name'])
print("data2['url']: ", data2['url'])

# ----------------------------------------------------------------------------------------------
print('----------------------------------------------------------------------------------------------')
print('输出嵌套-将 JSON 对象转换为 Python 字典-输出样例:')
print(data['anobject'])
print(data['japanese'])
print(data['anobject']['whoa'])
print(data['anobject']['more'])
print(data['anobject']['anarray'])
print(data['anobject']['anarray'][0])

# 如果你要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据。例如：

# # 写入 JSON 数据
# with open('data.json', 'w') as f:
#     json.dump(data, f)
#
# # 读取数据
# with open('data.json', 'r') as f:
#     data = json.load(f)

# 控制台显示示例

# dict_keys(['no', 'name', 'url'])
# 新增之前： {'no': 1, 'name': 'LC', 'url': 'http://www.oneplusone.top'}
# 新增之后： {'no': 1, 'name': 'LC', 'url': 'http://www.oneplusone.top', 'age': '18'}
# data1['url']:  http://www.oneplusone.top
# Python 原始数据： {'no': 1, 'name': 'LC', 'url': 'http://www.oneplusone.top', 'age': '18'}
# JSON 对象： {"no": 1, "name": "LC", "url": "http://www.oneplusone.top", "age": "18"}
# data2['name']:  LC
# data2['url']:  http://www.oneplusone.top


# 控制台显示示例2

# dict_keys(['no', 'name', 'url', 'hey', 'anumber', 'anobject', 'awesome', 'bogus', 'meaning', 'japanese', 'link', 'notLink'])
# 新增之前： {'no': 1, 'name': 'LC', 'url': 'http://www.oneplusone.top', 'hey': 'guy', 'anumber': 243, 'anobject': {'whoa': 'nuts', 'anarray': [1, 2, 3], 'more': 'stuff'}, 'awesome': True, 'bogus': False, 'meaning': None, 'japanese': '明日がある。', 'link': 'http://jsonview.com', 'notLink': 'http://jsonview.com is great'}
# 新增之后： {'no': 1, 'name': 'LC', 'url': 'http://www.oneplusone.top', 'hey': 'guy', 'anumber': 243, 'anobject': {'whoa': 'nuts', 'anarray': [1, 2, 3], 'more': 'stuff'}, 'awesome': True, 'bogus': False, 'meaning': None, 'japanese': '明日がある。', 'link': 'http://jsonview.com', 'notLink': 'http://jsonview.com is great', 'age': '18'}
# data1['url']:  http://www.oneplusone.top
# Python 原始数据： {'no': 1, 'name': 'LC', 'url': 'http://www.oneplusone.top', 'hey': 'guy', 'anumber': 243, 'anobject': {'whoa': 'nuts', 'anarray': [1, 2, 3], 'more': 'stuff'}, 'awesome': True, 'bogus': False, 'meaning': None, 'japanese': '明日がある。', 'link': 'http://jsonview.com', 'notLink': 'http://jsonview.com is great', 'age': '18'}
# JSON 对象： {"no": 1, "name": "LC", "url": "http://www.oneplusone.top", "hey": "guy", "anumber": 243, "anobject": {"whoa": "nuts", "anarray": [1, 2, 3], "more": "stuff"}, "awesome": true, "bogus": false, "meaning": null, "japanese": "\u660e\u65e5\u304c\u3042\u308b\u3002", "link": "http://jsonview.com", "notLink": "http://jsonview.com is great", "age": "18"}
# JSON-ensure_ascii 对象： {"no": 1, "name": "LC", "url": "http://www.oneplusone.top", "hey": "guy", "anumber": 243, "anobject": {"whoa": "nuts", "anarray": [1, 2, 3], "more": "stuff"}, "awesome": true, "bogus": false, "meaning": null, "japanese": "明日がある。", "link": "http://jsonview.com", "notLink": "http://jsonview.com is great", "age": "18"}
# data2['name']:  LC
# data2['url']:  http://www.oneplusone.top
# ----------------------------------------------------------------------------------------------
# 输出嵌套-将 JSON 对象转换为 Python 字典-输出样例:
# {'whoa': 'nuts', 'anarray': [1, 2, 3], 'more': 'stuff'}
# 明日がある。
# nuts
# stuff
# [1, 2, 3]
# 1

# 2019年2月21日12:33:22
