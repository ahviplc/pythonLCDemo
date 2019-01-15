#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CaptchaFuncDemo.py
python中使用PIL制作并验证图片验证码-对验证码图片生成进行封装
Version: 0.1
Author: LC
DateTime: 2019年1月15日10:59:07
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""
# string模块自带数字、字母、特殊字符变量集合，不需要我们手写集合
import string
import random
import os
import uuid

from PIL import Image, ImageDraw, ImageColor, ImageFilter, ImageFont


class Code(object):
    # 生成随机生成数字或字母
    def random_hexdigits(self, len=1):
        return random.sample(string.hexdigits, len)

    # 生成干扰字符
    def punctuation(self, len=1):
        return tuple(random.sample(string.punctuation, len))

    # 定义干扰字符颜色
    def random_color(self, min=64, max=255):
        return tuple((random.randint(min, max) for i in range(3)))

    # 生成验证码
    def creat_code(self, width=80, height=24, color=(192, 192, 192)):
        image = Image.new('RGB', (width, height), color)

        # 建议下载几款字体，变换下风格，我在setting粒定义了static路径，这里就直接导入了
        font = ImageFont.truetype('C:\\WINDOWS\\Fonts\\consola.ttf', 20)
        draw = ImageDraw.Draw(image)
        self.fill_color(draw, image, 5)
        self.fill_dischar(draw, image, 10)

        code = self.fill_char(draw, image, 4, 10, font)

        # image_name = '{}.jpeg'.format(uuid.uuid4().hex)
        image_name = 'CaptchaFuncDemo.py.jpeg'

        print(os.path)  # <module 'ntpath' from 'E:\\python-3.6.5-amd64\\lib\\ntpath.py'>
        print(os.getcwd())  # 获取当前工作目录路径 E:\pycharm-professional-2018.1.3\Code\pythonLCDemo\com\lc\demo\PillowDemo
        print(os.path.abspath(
            os.curdir))  # 获取当前工作目录路径 E:\pycharm-professional-2018.1.3\Code\pythonLCDemo\com\lc\demo\PillowDemo

        # image_path = os.path.join(settings.STATICPATH, 'code/{}'.format(image_name))
        # image_path = os.path.join('', 'code/{}'.format(image_name))
        image_path = (os.getcwd() + '\codeImg\{}'.format(image_name))

        print(
            image_path)  # E:\pycharm-professional-2018.1.3\Code\pythonLCDemo\com\lc\demo\PillowDemo\codeImg\CaptchaFuncDemo.py.jpeg
        image.save(image_path)
        return {'code': code, 'image_path': image_path}

    # 填充颜色
    def fill_color(self, draw, image, interval):
        for i in range(0, image.width, interval):
            for j in range(0, image.height, interval):
                draw.point((i, j), fill=self.random_color())

    # 填充验证码
    def fill_dischar(self, draw, image, interval):
        for i in range(0, image.width, interval):
            dis = self.punctuation()
            j = random.randrange(3, image.height - 3)
            draw.text((i, j), dis[0], fill=self.random_color(64, 255))

    # 填充验证码 num代表生成的字符数
    def fill_char(self, draw, image, num, interval, font):
        code = ''
        for i in range(num):
            cha = self.random_hexdigits()
            code += str(cha[0])
            j = random.randrange(0, 5)
            # print(cha)
            # print(image.width*(i/num)+interval,j)
            draw.text((image.width * (i / num) + interval, j), cha[0], fill=self.random_color(32, 127), font=font)
        return code


if __name__ == "__main__":
    code = Code()
    print(code.creat_code())

# python中使用PIL制作并验证图片验证码_python_脚本之家
# https://www.jb51.net/article/136457.htm
