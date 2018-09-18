"""

引发异常和异常栈

Version: 0.1
Author: LC
DateTime:2018年9月18日15:10:35
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""


def f1():
	raise AssertionError('发生异常')


def f2():
	f1()


def f3():
	f2()


f3()
