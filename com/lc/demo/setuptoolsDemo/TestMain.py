#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TestMain.py
测试diy的setuptools的样例
Version: 1.0
Author: LC
DateTime: 2019年1月28日12:08:51
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""
import setuptoolsDemoByLC
from setuptoolsDemoByLC.funcLib.IamFunc import sumHe
from setuptoolsDemoByLC.funcLib.IamFunc import sumHe as SH


def main():
    print(setuptoolsDemoByLC.test())
    print(sumHe(1, 1))
    print(SH(2, 1))


if __name__ == '__main__':
    main()

# hello world!setuptools Demo!~LC
# None
# 2
# None
# 3
# None