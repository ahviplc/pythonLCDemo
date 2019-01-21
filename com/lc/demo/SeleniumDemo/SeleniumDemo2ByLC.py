#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SeleniumDemo2ByLC.py
Selenium实例2-打开LC博客url: http://oneplusone.top/index.html网站
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
driver.get("http://oneplusone.top/index.html")  # 一加壹博客最Top

# 给司机3秒钟去打开,睡3秒
time.sleep(3)

# 开始搜索
# 1. 让司机找搜索框的输入框
we_search = driver.find_element_by_css_selector('#q')
we_search.clear()
we_search.send_keys("python")

# 2. 让司机找 搜索按钮 并 单击-用这个xpath来找到搜索button按钮-以下两者写法都可以
# html代码：【<button type="submit" class="btn btn-default">搜索</button>】

# driver.find_element_by_xpath(".//button[@class='btn btn-default' and @type='submit']").click()
driver.find_element_by_xpath(".//button[@type='submit']").click()

time.sleep(3)
