"""

分段函数求值
		3x - 5	(x > 1)
f(x) =	x + 2	(-1 <= x <= 1)
		5x + 3	(x < -1)

Version: 0.1
Author: LC
DateTime:2018年9月14日17:17:33
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

x = float(input('x = '))
if x > 1:
	y = 3 * x - 5
elif x >= -1:
	y = x + 2
else:
	y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))
