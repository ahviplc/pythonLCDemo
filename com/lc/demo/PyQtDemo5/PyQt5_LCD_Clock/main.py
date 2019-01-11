"""
DigitalClock.py 执行主方法
PyQt5程序样例:实现一个LCD电子时钟
Version: 1.0
Author: LC
DateTime: 2019年1月11日16:02:5
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""
from PyQt5.QtWidgets import QApplication
import sys
from DigitalClock import DigitalClock


def main():
    app = QApplication(sys.argv)
    clock = DigitalClock(None)
    clock.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
