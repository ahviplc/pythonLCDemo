#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PIIncludeBirthday.py
圆周率值中包含你的生日吗?Does PI include your birthday?
Version: 1.0
Author: LC
DateTime: 2019年1月18日10:21:07
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""
filename = 'PIIncludeBirthday_pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
