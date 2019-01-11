#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PyQt5Demo.py
LC的第一个PyQt5程序:Hello World
Version: 1.0
Author: LC
DateTime: 2019年1月11日14:56:39
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""
import sys, time, datetime
from PyQt5.QtWidgets import (QMainWindow, QMessageBox, QWidget, QToolTip, QPushButton, QApplication, QGestureEvent,
                             QLabel, QDesktopWidget)
from PyQt5.QtGui import QFont, QIcon


class Example(QWidget):
    # 构造函数
    def __init__(self):
        super().__init__()
        self.initGUI();

    # 初始化函数
    def initGUI(self):
        # 设置窗体frame
        self.setGeometry(500, 300, 300, 300)
        # 窗体title
        self.setWindowTitle('LC的第一个程序,PyQt5')
        # 添加label
        self.lable = QLabel('Hello World!PyQt5!~LC', self)
        # 自动换行
        self.lable.setWordWrap(True)
        # lable的frame
        self.lable.setGeometry(50, 100, 200, 150)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
