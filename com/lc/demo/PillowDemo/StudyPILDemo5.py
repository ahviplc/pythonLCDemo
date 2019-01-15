#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
StudyPILDemo5.py
生成一张带有噪点的验证码图片
Version: 0.1
Author: LC
DateTime: 2019年1月15日10:46:02
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


def getRandomStr():
    '''获取一个随机字符串，每个字符的颜色也是随机的'''
    random_num = str(random.randint(0, 9))
    random_low_alpha = chr(random.randint(97, 122))
    random_upper_alpha = chr(random.randint(65, 90))
    random_char = random.choice([random_num, random_low_alpha, random_upper_alpha])

    return random_char


# 获取一个Image对象，参数分别是RGB模式。宽150，高30，随机颜色
image = Image.new('RGB', (150, 30), getRandomColor())

# 获取一个画笔对象，将图片对象传过去
draw = ImageDraw.Draw(image)

# 获取一个font字体对象参数是ttf的字体文件的目录，以及字体的大小 C:\\WINDOWS\\Fonts\\consola.ttf
# font = ImageFont.truetype("kumo.ttf", size=26)
font = ImageFont.truetype("C:\\WINDOWS\\Fonts\\consola.ttf", size=26)

for i in range(5):
    # 循环5次，获取5个随机字符串
    random_char = getRandomStr()

    # 在图片上一次写入得到的随机字符串,参数是：定位，字符串，颜色，字体
    draw.text((10 + i * 30, 0), random_char, getRandomColor(), font=font)

# 噪点噪线
width = 150
height = 30
# 划线
for i in range(5):
    x1 = random.randint(0, width)
    x2 = random.randint(0, width)
    y1 = random.randint(0, height)
    y2 = random.randint(0, height)
    draw.line((x1, y1, x2, y2), fill=getRandomColor())

# 画点
for i in range(30):
    draw.point([random.randint(0, width), random.randint(0, height)], fill=getRandomColor())
    x = random.randint(0, width)
    y = random.randint(0, height)
    draw.arc((x, y, x + 4, y + 4), 0, 90, fill=getRandomColor())
# 保存到硬盘，名为test.png格式为png的图片
image.save(open('StudyPILDemo5.png', 'wb'), 'png')
