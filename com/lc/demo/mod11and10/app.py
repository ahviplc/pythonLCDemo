#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
MOD 11，10算法(python版本)（GB/T 17710-1999 校验码算法）
Version: 1.0
Author: LC
DateTime: 2020年10月30日11:15:09
UpdateTime:
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
LC博客url: http://oneplusone.vip/index.html
一加壹.SNS LC - 又一个SNS社区: http://sns.oneplusone.vip
赞助一加壹博客最Top-LC万能收款码支持-支付宝、微信、QQ
http://lc.oneplusone.vip/donateMeByLC.html

MOD 11，10算法(python版本)（GB/T 17710-1999 校验码算法）_mhn910的博客-CSDN博客
https://blog.csdn.net/qq_42672327/article/details/88535406

MOD 11，10算法（GB/T 17710-1999 数据处理 校验码系统 ）的 Python实现 - 奔四少年 - 博客园
https://www.cnblogs.com/phpwechat/p/6531030.html
"""


# 求Pn
def getPn(n, arr1):
    if n == 1:
        return 10
    else:
        return mod10(getSn(n - 1, arr1)) * 2


# 求特定的取余10的结果
def mod10(num):
    if num % 10 == 0:
        return 10
    else:
        return num % 10


# 求Sn
def getSn(n, arr1):
    return getPn(n, arr1) % 11 + int(arr1[14 - n + 1])


# 求校验码
def getCheckCode(code):
    c = code + 'x,'
    arr1 = []
    for i in reversed(c):
        arr1.append(i)
    for j in range(0, 10):
        arr1[1] = str(j)
        if getSn(14, arr1) % 10 == 1:
            result = ''.join(list(reversed(arr1)))
            return result[:len(result) - 1]


# GB/T 17710 双模校验算法
def getCheckCode2(str):
    str = str.replace(' ', '')
    p = 10
    for j in range(1, 15):
        numerator = (p + int(str[j - 1])) % 10
        if (numerator == 0):
            numerator = 10
        p = (numerator * 2) % 11
    return 11 - p


if __name__ == '__main__':
    # 前13位许可证号数字
    xkzCode = '1530825001410'
    # 全部14位许可证号
    print(getCheckCode(xkzCode))
    print(getCheckCode2('110108018718049'))
