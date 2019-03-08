#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
db_utils.py
工具类(待启用)
Version: 1.0
Author: LC
DateTime: 2019年3月8日14:14:20
UpdateTime: None
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""


# 待启用
class dogs:
    def __init__(self, name='灰灰', age=1, type='哈士奇', desc='一条可爱的狗'):
        self.name = name
        self.age = age
        self.type = type
        self.desc = desc

    # 小狗行为:叫
    def jiao(self):
        print("wangwang")


def get_no_func(db):
    print("get_no_func")
    return 123
    print(db)

# 使用方法


# 方法使用
# from  db_utils import get_no_func as gnf #用法1

# import db_utils  # db_utils.get_no_func(db) #用法2
#  取自动递增流水号
#     ok_no = db_utils.get_no_func(db)


# 类使用
# xka = db_utils.dogs()
#     print(xka.jiao())
