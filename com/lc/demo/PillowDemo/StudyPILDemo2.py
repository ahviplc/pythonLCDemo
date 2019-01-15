#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
StudyPILDemo2.py
生成一张随机颜色的图片
Version: 0.1
Author: LC
DateTime: 2019年1月15日10:36:48
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""
from PIL import Image
import random


def getRandomColor():
    '''获取一个随机颜色(r,g,b)格式的'''
    c1 = random.randint(0, 255)
    c2 = random.randint(0, 255)
    c3 = random.randint(0, 255)
    return (c1, c2, c3)


# 获取一个Image对象，参数分别是RGB模式。宽150，高30，随机颜色
image = Image.new('RGB', (150, 30), getRandomColor())
# 保存到硬盘，名为test.png格式为png的图片
image.save(open('StudyPILDemo2.png', 'wb'), 'png')
