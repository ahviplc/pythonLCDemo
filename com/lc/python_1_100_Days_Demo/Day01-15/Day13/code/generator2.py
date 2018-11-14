"""

生成器 - 使用yield关键字

Version: 0.1
Author: LC
DateTime:2018年11月14日16:10:00
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html


"""


def fib(num):
	n, a, b = 0, 0, 1
	while n < num:
		yield b
		a, b = b, a + b
		n += 1


for x in fib(20):
	print(x)
