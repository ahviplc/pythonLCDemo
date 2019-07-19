#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
pysnooperDemoApp2.py
Version: 1.0
Author: LC
DateTime: 2019年7月19日11:33:51
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


@pysnooper.snoop()
def number_to_bits(number):
    if number:
        bits = []
        while number:
            number, remainder = divmod(number, 2)
            bits.insert(0, remainder)
        return bits
    else:
        return [0]


number_to_bits(6)

# 输出示例
# Starting var:.. number = 6
# 17:26:28.777294 call         5 def number_to_bits(number):
# 17:26:28.777294 line         6     if number:
# 17:26:28.777294 line         7         bits = []
# New var:....... bits = []
# 17:26:28.777294 line         8         while number:
# 17:26:28.777294 line         9             number, remainder = divmod(number, 2)
# Modified var:.. number = 3
# New var:....... remainder = 0
# 17:26:28.777294 line        10             bits.insert(0, remainder)
# Modified var:.. bits = [0]
# 17:26:28.777294 line         8         while number:
# 17:26:28.777294 line         9             number, remainder = divmod(number, 2)
# Modified var:.. number = 1
# Modified var:.. remainder = 1
# 17:26:28.777294 line        10             bits.insert(0, remainder)
# Modified var:.. bits = [1, 0]
# 17:26:28.777294 line         8         while number:
# 17:26:28.777294 line         9             number, remainder = divmod(number, 2)
# Modified var:.. number = 0
# 17:26:28.777294 line        10             bits.insert(0, remainder)
# Modified var:.. bits = [1, 1, 0]
# 17:26:28.777294 line         8         while number:
# 17:26:28.777294 line        11         return bits
# 17:26:28.777294 return      11         return bits
# Return value:.. [1, 1, 0]
