"""

输入非负整数n计算n!

Version: 0.1
Author: LC
DateTime:2018年9月18日10:55:56
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

n = int(input('n = '))
result = 1
for x in range(1, n + 1):
	result *= x
print('%d! = %d' % (n, result))
