#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
pysnooperDemoApp3.py
Version: 1.0
Author: LC
DateTime: 2019年7月19日11:33:02
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
def lc_app_diy():
    for i in range(1, 10):
        print(i ** 2)


lc_app_diy()

# 输出示例
# 1
# 4
# 17:36:49.564385 call         5 def lc_app_diy():
# 9
# 16
# 25
# 17:36:49.564385 line         6     for i in range(1, 10):
# 36
# 49
# New var:....... i = 1
# 64
# 17:36:49.564385 line         7         print(i ** 2)
# 17:36:49.564385 line         6     for i in range(1, 10):
# 81
# Modified var:.. i = 2
# 17:36:49.564385 line         7         print(i ** 2)
# 17:36:49.564385 line         6     for i in range(1, 10):
# Modified var:.. i = 3
# 17:36:49.564385 line         7         print(i ** 2)
# 17:36:49.564385 line         6     for i in range(1, 10):
# Modified var:.. i = 4
# 17:36:49.564385 line         7         print(i ** 2)
# 17:36:49.564385 line         6     for i in range(1, 10):
# Modified var:.. i = 5
# 17:36:49.564385 line         7         print(i ** 2)
# 17:36:49.564385 line         6     for i in range(1, 10):
# Modified var:.. i = 6
# 17:36:49.564385 line         7         print(i ** 2)
# 17:36:49.564385 line         6     for i in range(1, 10):
# Modified var:.. i = 7
# 17:36:49.564385 line         7         print(i ** 2)
# 17:36:49.564385 line         6     for i in range(1, 10):
# Modified var:.. i = 8
# 17:36:49.564385 line         7         print(i ** 2)
# 17:36:49.564385 line         6     for i in range(1, 10):
# Modified var:.. i = 9
# 17:36:49.564385 line         7         print(i ** 2)
# 17:36:49.564385 line         6     for i in range(1, 10):
# 17:36:49.564385 return       6     for i in range(1, 10):
# Return value:.. None
