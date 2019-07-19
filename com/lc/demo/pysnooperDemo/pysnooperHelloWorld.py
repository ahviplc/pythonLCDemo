#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
pysnooperHelloWorld.py
pysnooper HelloWorld 输出
Version: 1.0
Author: LC
DateTime: 2019年7月19日11:33:28
UpdateTime:
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
LC博客url: http://oneplusone.vip/index.html
一加壹.SNS LC - 又一个SNS社区: http://sns.oneplusone.vip
赞助一加壹博客最Top-LC万能收款码支持-支付宝、微信、QQ
http://lc.oneplusone.vip/donateMeByLC.html

# 运行需要安装pysnooper模块

"""

import time
import os
import pysnooper


# print('hello world 2019-7-4 11:31:24！')


@pysnooper.snoop()
def app():
    print(time.localtime())


# for i in range(1, 5):
#     print(i)

# print(os.cpu_count())
#
# print(os.altsep)
#
# print(os.devnull)

app()

# 11:19:12.428050 call         9 def app():
# time.struct_time(tm_year=2019, tm_mon=7, tm_mday=19, tm_hour=11, tm_min=19, tm_sec=12, tm_wday=4, tm_yday=200, tm_isdst=0)
# 11:19:12.428050 line        10     print(time.localtime())
# 11:19:12.428050 return      10     print(time.localtime())
# Return value:.. None
