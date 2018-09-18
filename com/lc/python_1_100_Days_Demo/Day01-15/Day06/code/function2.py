"""

函数的定义和使用 - 求最大公约数和最小公倍数

Version: 0.1
Author: LC
DateTime:2018年9月18日11:32:13
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""


def gcd(x, y):
	if x > y:
		(x, y) = (y, x)
	for factor in range(x, 1, -1):
		if x % factor == 0 and y % factor == 0:
			return factor
	return 1


def lcm(x, y):
	return x * y // gcd(x, y)


print(gcd(15, 27))
print(lcm(15, 27))
