#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PyQt5_Clock_Demo.py
PyQt5程序样例:实现一个简单的时钟
Version: 1.0
Author: LC
DateTime: 2019年1月11日14:56:39
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""

from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QDesktopWidget, QVBoxLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time
import sys


class ShiZhong(QWidget):
    def __init__(self):
        super(ShiZhong, self).__init__()
        self.initUI()
        self.init_timer()

    def initUI(self):
        self.resize(250, 150)
        self.setWindowTitle('电子时钟By LC')
        self.move_center()
        self.m = QPalette()
        self.m.setColor(QPalette.Background, Qt.green)
        self.setAutoFillBackground(True)
        self.setPalette(self.m)
        self.lcd = QLCDNumber()
        self.lcd.setDigitCount(10)
        self.lcd.setMode(QLCDNumber.Dec)
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        self.lcd.display(time.strftime("%X", time.localtime()))
        self.m_layout = QVBoxLayout()
        self.m_layout.addWidget(self.lcd)
        self.m_layout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.m_layout)
        self.show()

    def init_timer(self):
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        self.timer.timeout.connect(self.update_time)

    def update_time(self):
        self.lcd.display(time.strftime("%X", time.localtime()))

    def move_center(self):
        m_rect = self.frameGeometry()
        w_center_point = QDesktopWidget().availableGeometry().center()
        m_rect.moveCenter(w_center_point)
        self.move(m_rect.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    m_time = ShiZhong()
    m_time.show()
    sys.exit(app.exec_())
