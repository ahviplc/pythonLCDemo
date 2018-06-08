#!/usr/bin/python3

# Python3 JSON 数据解析
# JSON (JavaScript Object Notation) 是一种轻量级的数据交换格式。它基于ECMAScript的一个子集。
#
# Python3 中可以使用 json 模块来对 JSON 数据进行编解码，它包含了两个函数：
#
# json.dumps(): 对数据进行编码。
# json.loads(): 对数据进行解码。

import json

# Python 字典类型转换为 JSON 对象
data = {
    'no' : 1,
    'name' : 'LC',
    'url' : 'http://www.oneplusone.top'
}

# 打印所有的key
print(data.keys())

print("新增之前：",data)

data.setdefault("age","18")

print("新增之后：",data)

print ("data1['url']: ", data['url'])

json_str = json.dumps(data)
print ("Python 原始数据：", repr(data))
print ("JSON 对象：", json_str)


# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print ("data2['name']: ", data2['name'])
print ("data2['url']: ", data2['url'])



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
