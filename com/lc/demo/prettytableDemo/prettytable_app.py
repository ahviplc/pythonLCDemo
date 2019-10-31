#!usr/bin/env python
# -*- coding=utf-8 -*-

"""

prettytable_app.py
备注:PrettyTable 模块使用
Version: 1.0
Author: LC
DateTime: 2019年10月31日10:39:10
UpdateTime:
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
LC博客url: http://oneplusone.vip/index.html
一加壹.SNS LC - 又一个SNS社区: http://sns.oneplusone.vip
赞助一加壹博客最Top-LC万能收款码支持-支付宝、微信、QQ
http://lc.oneplusone.vip/donateMeByLC.html

"""

'''
__Author__:LC
功能：  PrettyTable 模块使用
'''

import prettytable
from prettytable import from_csv
from prettytable import PrettyTable


def testFunc1():
    '''
    '''
    table = PrettyTable()
    table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
    table.add_row(["Adelaide", 1295, 1158259, 600.5])
    table.add_row(["Brisbane", 5905, 1857594, 1146.4])
    table.add_row(["Darwin", 112, 120900, 1714.7])
    table.add_row(["Hobart", 1357, 205556, 619.5])
    table.add_row(["Sydney", 2058, 4336374, 1214.8])
    table.add_row(["Melbourne", 1566, 3806092, 646.9])
    table.add_row(["Perth", 5386, 1554769, 869.4])
    print('=================================table1====================================')

    print(table)

    table.add_column("City name", ["Adelaide", "Brisbane", "Darwin", "Hobart", "Sydney", "Melbourne", "Perth"])
    table.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
    table.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092, 1554769])
    table.add_column("Annual Rainfall", [600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9, 869.4])
    print('=================================table2-随机样式====================================')
    # 随机样式 还有其他【prettytable.RANDOM prettytable.MSWORD_FRIENDLY  prettytable.PLAIN_COLUMNS  prettytable.DEFAULT 】
    table.set_style(prettytable.RANDOM)
    print(table)


def testFunc2(data):
    '''
    从 csv 文件中加载数据
    '''
    mycsv = open(data)
    print(mycsv.readline())
    table = from_csv(mycsv)
    mycsv.close()
    print('===========================================table3-from csv==============================================')

    print(table)

    print('=================================table:SepalLength_Species====================================')

    print(table.get_string(fields=['SepalLength', 'Species']))

    print('=======================================table:60=>80 rows======================================')

    print(table.get_string(start=60, end=80))


if __name__ == '__main__':
    testFunc1()
    # testFunc2(data='address.csv')
