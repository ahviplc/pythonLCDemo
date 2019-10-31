# -*- coding=utf-8 -*-

"""

pyautogui_keyboard_app.py
备注:
Version: 1.0
Author: LC
DateTime: 2019年10月31日10:00:33
UpdateTime:
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
LC博客url: http://oneplusone.vip/index.html
一加壹.SNS LC - 又一个SNS社区: http://sns.oneplusone.vip
赞助一加壹博客最Top-LC万能收款码支持-支付宝、微信、QQ
http://lc.oneplusone.vip/donateMeByLC.html

"""

import pyautogui

# 中击
pyautogui.middleClick()
# 提示信息
pyautogui.alert(text='This is an alert box.', title='Test')
# 模拟输入信息
pyautogui.typewrite(message='Hello world LC!', interval=0.5)
# 点击ESC
pyautogui.press('esc')
pyautogui.keyDown('shift')
# 放开shift键
pyautogui.keyUp('shift')
# 模拟组合热键
pyautogui.hotkey('ctrl', 'c')
