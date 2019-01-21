#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SeleniumDemoByLC.py
Selenium实例-打开然之协同网站
Version: 1.0
Author: LC
DateTime: 2019年1月21日16:48:36
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""
from selenium import webdriver
import time

# 声明一个司机，司机是个Chrome类的对象
# driver = webdriver.Chrome()
"""
 若不指向chromedriver.exe，则报错:
 selenium.common.exceptions.WebDriverException: Message:
'chromedriver.exe1' executable needs to be in PATH.
 Please see https://sites.google.com/a/chromium.org/chromedriver/home
"""

# # com/lc/demo/SeleniumDemo/chromedriver_win32下的chromedriver.exe放到C:\Program Files (x86)\Google\Chrome\Application\
# driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

# 或者直接指向项目文件夹chromedriver_win32下的chromedriver.exe【com/lc/demo/SeleniumDemo/chromedriver_win32/chromedriver.exe】
driver = webdriver.Chrome(executable_path='chromedriver_win32\chromedriver.exe')

# 让司机加载一个网页
driver.get("http://demo.ranzhi.org")  # 然之协同

# 给司机3秒钟去打开,睡3秒
time.sleep(3)

# 开始登录
# 1. 让司机找用户名的输入框
we_account = driver.find_element_by_css_selector('#account')
we_account.clear()
we_account.send_keys("demo")

# 2. 让司机找密码的输入框
we_password = driver.find_element_by_css_selector('#password')
we_password.clear()
we_password.send_keys("demo")

# 3. 让司机找 登录按钮 并 单击
driver.find_element_by_css_selector('#submit').click()
time.sleep(3)
