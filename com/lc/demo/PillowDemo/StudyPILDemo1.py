#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
StudyPILDemo1.py
生成一张固定尺寸固定颜色的图片
Version: 0.1
Author: LC
DateTime: 2019年1月15日10:34:04
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""
from PIL import Image

# 获取一个Image对象，参数分别是RGB模式。宽150，高30，红色
image = Image.new('RGB', (150, 30), 'red')
# 保存到硬盘，名为test.png格式为png的图片
image.save(open('StudyPILDemo1.png', 'wb'), 'png')
