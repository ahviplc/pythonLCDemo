#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SeleniumDemo3ByLC.py
Selenium实例3-打开LC博客url: http://oneplusone.top/index.html网站的后台管理地址:http://oneplusone.top/login.jsp 并自动登录
Version: 1.0
Author: LC
DateTime: 2019年1月21日17:33:21
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
driver.get("http://oneplusone.top/login.jsp")  # 一加壹博客最Top后台管理页面

# 给司机3秒钟去打开,睡3秒
time.sleep(3)

# 开始登录
# 1. 让司机找用户名的输入框
we_account = driver.find_element_by_css_selector('#userName')
we_account.clear()
we_account.send_keys("admin")

# 2. 让司机找密码的输入框
we_password = driver.find_element_by_css_selector('#password')
we_password.clear()
we_password.send_keys("admin_password_demo")  # 使用真实密码即可登录成功

# 2. 让司机找 登录按钮 并 单击-用这个xpath来找到登录button按钮-以下两者写法都可以
# html代码：【<input type="submit" style="background: rgb(0, 142, 173); padding: 7px 10px; border-radius: 4px; border: 1px solid rgb(26, 117, 152); border-image: none; color: rgb(255, 255, 255); font-weight: bold;" value="登录">】

# driver.find_element_by_xpath(".//input[@type='submit']").click()
driver.find_element_by_xpath(".//input[@type='submit' and @value='登录']").click()

time.sleep(3)
