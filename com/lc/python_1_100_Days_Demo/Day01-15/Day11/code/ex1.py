"""

异常机制 - 处理程序在运行时可能发生的状态

Version: 0.1
Author: LC
DateTime:2018年9月18日15:05:38
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
	except ValueError:
		print('请输入整数')
	except ZeroDivisionError:
		print('除数不能为0')
# 处理异常让代码不因异常而崩溃是一方面
# 更重要的是可以通过对异常的处理让代码从异常中恢复过来
