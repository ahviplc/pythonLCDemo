"""

输入两个正整数计算最大公约数和最小公倍数

Version: 0.1
Author: LC
DateTime:2018年9月18日10:57:37
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

x = int(input('x = '))
y = int(input('y = '))
if x > y:
	(x, y) = (y, x)
for factor in range(x, 0, -1):
	if x % factor == 0 and y % factor == 0:
		print('%d和%d的最大公约数是%d' % (x, y, factor))
		print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
		break
