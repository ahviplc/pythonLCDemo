#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
lockThisWindowsPyByLC.py
python对windows系统进行锁屏的功能实现
Version: 1.0
Author: LC
DateTime: 2019年1月11日15:29:56
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""
from ctypes import *


# 锁屏功能实现函数
def lockThisWindowsFuc():
    user32 = windll.LoadLibrary('user32.dll')
    msg = user32.LockWorkStation()
    # print(msg)  # 如果msg为1 则代表windows锁屏成功
    if (msg == 1):
        print("锁屏成功")
    else:
        print("锁屏失败")
    # print("lockThisWindowsFuc done")


# 主函数
def main():
    lockThisWindowsFuc()
    # print("main done")


# 运行主函数，调用
if __name__ == '__main__':
    main()
