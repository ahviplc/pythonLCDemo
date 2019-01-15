#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
StudyPILDemo3.py
生成一张带有固定字符串的随机颜色的图片
Version: 0.1
Author: LC
DateTime: 2019年1月15日10:41:10
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random


def getRandomColor():
    '''获取一个随机颜色(r,g,b)格式的'''
    c1 = random.randint(0, 255)
    c2 = random.randint(0, 255)
    c3 = random.randint(0, 255)
    return (c1, c2, c3)


# 获取一个Image对象，参数分别是RGB模式。宽150，高30，随机颜色
image = Image.new('RGB', (150, 30), getRandomColor())

# 获取一个画笔对象，将图片对象传过去
draw = ImageDraw.Draw(image)

# 获取一个font字体对象参数是ttf的字体文件的目录，以及字体的大小 C:\\WINDOWS\\Fonts\\consola.ttf
# font = ImageFont.truetype("C:\\WINDOWS\\Fonts\\kumo.ttf", size=32)
font = ImageFont.truetype("C:\\WINDOWS\\Fonts\\SIMSUN.TTC", size=32)

# 在图片上写东西,参数是：定位，字符串，颜色，字体
draw.text((20, 0), 'LC Love Y', getRandomColor(), font=font)

# 保存到硬盘，名为test.png格式为png的图片
image.save(open('StudyPILDemo3.png', 'wb'), 'png')
