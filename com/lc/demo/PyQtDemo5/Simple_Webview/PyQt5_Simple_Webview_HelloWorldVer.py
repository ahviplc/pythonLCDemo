#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PyQt5_Simple_Webview_HelloWorldVer.py
PyQt5程序样例:实现一个简单的浏览器
Version: 1.0
Author: LC
DateTime: 2019年1月11日16:50:32
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import *  # QIcon()在这里

app = QApplication([])
view = QWebEngineView()

# 设置窗口标题
view.setWindowTitle('My Simple Browser By LC')
# 设置窗口图标
view.setWindowIcon(QIcon('icons/penguin.png'))
# 设置窗口大小900*600
view.resize(900, 600)

view.load(QUrl("http://www.oneplusone.vip"))  # 一加壹博客最Top
view.show()
app.exec_()
