"""
main.py 执行主方法
PyQt5程序样例:简易画板 Simple PaintBoard/Simple Sketchpad
Version: 1.0
Author: LC
DateTime: 2019年1月11日16:03:08
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""

from MainWidget import MainWidget
from PyQt5.QtWidgets import QApplication

import sys


def main():
    app = QApplication(sys.argv)

    mainWidget = MainWidget()
    mainWidget.show()

    exit(app.exec_())


if __name__ == '__main__':
    main()
