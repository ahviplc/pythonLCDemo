#!/usr/bin/python
# -*- coding: UTF-8 -*-

for i in  range(1,10):

    for j in range(1,i+1):
        print("%d*%d=%d" % (i, j, i*j), end='')
        print()

# -*- coding: UTF-8 -*-

# Filename : ninenine.py
# author by : www.oneplusone.top


# 九九乘法表 开始
for i in range(1, 10):
    for j in range(1, i + 1):
        print('{}x{}={}\t'.format(i, j, i * j), end='')
    print()

# 九九乘法表2 开始
for i in range(1, 10):
    for j in range(1, i + 1):
        print('{0}x{1}={2}\t'.format(i, j, i * j), end='')
    print()

# Python用format格式化字符串 - Xjng - 博客园
# http://www.cnblogs.com/Xjng/p/4092600.html
# LC 2018年11月14日12:09:57