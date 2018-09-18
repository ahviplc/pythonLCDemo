"""

输出乘法口诀表(九九表)

Version: 0.1
Author: LC
DateTime:2018年9月18日11:12:44
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

for i in range(1, 10):
	for j in range(1, i + 1):
		print('%d*%d=%d' % (i, j, i * j), end='\t')
	print()
