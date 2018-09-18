"""

异常机制 - 处理程序在运行时可能发生的状态

Version: 0.1
Author: LC
DateTime:2018年9月18日15:07:48
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

input_again = True
while input_again:
	try:
		a = int(input('a = '))
		b = int(input('b = '))
		print('%d / %d = %f' % (a, b, a / b))
		input_again = False
	except (ValueError, ZeroDivisionError) as msg:
		print(msg)
