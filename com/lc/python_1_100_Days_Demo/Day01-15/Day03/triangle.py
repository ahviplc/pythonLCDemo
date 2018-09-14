"""

判断输入的边长能否构成三角形
如果能则计算出三角形的周长和面积

Version: 0.1
Author: LC
DateTime:2018年9月14日17:19:36
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
	print('周长: %f' % (a + b + c))
	p = (a + b + c) / 2
	area = math.sqrt(p * (p - a) * (p - b) * (p - c))
	print('面积: %f' % (area))
else:
	print('不能构成三角形')
