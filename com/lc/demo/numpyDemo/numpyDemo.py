#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
numpyDemo

Version: 0.1
Author: LC
DateTime: 2018年6月17日21:41:55
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""
import numpy

print ('使用列表生成一维数组')
data = [1,2,3,4,5,6]
x = numpy.array(data)
print (x) #打印数组
print (x.dtype) #打印数组元素的类型

print ('使用列表生成二维数组')
data = [[1,2],[3,4],[5,6]]
x = numpy.array(data)
print (x) #打印数组
print (x.ndim) #打印数组的维度
print (x.shape) #打印数组各个维度的长度。shape是一个元组

print ('使用zero/ones/empty创建数组:根据shape来创建')
x = numpy.zeros(6) #创建一维长度为6的，元素都是0一维数组
print (x)
x = numpy.zeros((2,3)) #创建一维长度为2，二维长度为3的二维0数组
print (x)
x = numpy.ones((2,3)) #创建一维长度为2，二维长度为3的二维1数组
print (x)
x = numpy.empty((3,3)) #创建一维长度为2，二维长度为3,未初始化的二维数组
print (x)

print ('使用arrange生成连续元素')
print (numpy.arange(6)) # [0,1,2,3,4,5,] 开区间
print (numpy.arange(0,6,2))  # [0, 2，4]

"""
python之numpy的基本使用 - cxmscb的博客 - CSDN博客
https://blog.csdn.net/cxmscb/article/details/54583415

注意：这里的代码python版本不是3.0+
"""
