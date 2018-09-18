"""

输出斐波那契数列的前20个数
1 1 2 3 5 8 13 21 ...

Version: 0.1
Author: LC
DateTime:2018年9月18日11:11:44
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

a = 0
b = 1
for _ in range(20):
	(a, b) = (b, a + b)
	print(a, end=' ')
