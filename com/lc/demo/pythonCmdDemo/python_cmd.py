#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
python_cmd.py python操作cmd命令 在Windows下执行exe二进制文件
Version: 1.0
Author: LC
DateTime: 2019年9月16日00:43:09
UpdateTime:
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
LC博客url: http://oneplusone.vip/index.html
一加壹.SNS LC - 又一个SNS社区: http://sns.oneplusone.vip
赞助一加壹博客最Top-LC万能收款码支持-支付宝、微信、QQ
http://lc.oneplusone.vip/donateMeByLC.html

"""

import os
import time

print(int(time.time()))

# 第一种
# print('测试开始1')
# # os.system('echo 测试开始1')
# os.system('dir')
# os.system('ping 192.168.1.1')
# print('测试结束1')
# # os.system('echo 测试结束1')

# 第二种
import subprocess

# print('测试开始2')
# subprocess.Popen('dir', shell=True)
# subprocess.Popen('ping 192.168.1.1', shell=True)
# print('测试结束2')

# 第三种 执行exe
# print(os.getcwd()) # D:\all_develop_soft\pycharm-professional-2018.1.3\codeKu\pythonLCDemo\com\lc\demo\pythonCmdDemo

# 首先cd进去
# subprocess.Popen('cd '+os.getcwd(), shell=True)
# subprocess.Popen('pwd', shell=True)
# 执行exe
p = subprocess.Popen('hello.exe', shell=True)
# print(p)
