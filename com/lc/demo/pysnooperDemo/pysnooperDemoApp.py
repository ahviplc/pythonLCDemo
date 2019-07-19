#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
pysnooperDemoApp.py
Version: 1.0
Author: LC
DateTime: 2019年7月19日11:32:21
UpdateTime:
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
LC博客url: http://oneplusone.vip/index.html
一加壹.SNS LC - 又一个SNS社区: http://sns.oneplusone.vip
赞助一加壹博客最Top-LC万能收款码支持-支付宝、微信、QQ
http://lc.oneplusone.vip/donateMeByLC.html

# 运行需要安装pysnooper模块

"""

import pysnooper
import random


def foo():
    lst = []
    for i in range(10):
        lst.append(random.randrange(1, 1000))

    with pysnooper.snoop():
        lower = min(lst)
        upper = max(lst)
        mid = (lower + upper) / 2
        print(lower, mid, upper)


foo()

# 输出示例：
# 12 426.0 840
# New var:....... lst = [99, 290, 63, 301, 409, 93, 840, 12, 710, 199]
# New var:....... i = 9
# 17:19:51.831492 line        11         lower = min(lst)
# New var:....... lower = 12
# 17:19:51.831492 line        12CCCC         upper = max(lst)
# New var:....... upper = 840
# 17:19:51.831492 line        13         mid = (lower + upper) / 2
# New var:....... mid = 426.0
# 17:19:51.831492 line        14         print(lower, mid, upper)
