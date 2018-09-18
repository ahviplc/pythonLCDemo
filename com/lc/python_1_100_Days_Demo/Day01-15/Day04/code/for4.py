"""

输入一个正整数判断它是不是素数

Version: 0.1
Author: LC
DateTime:2018年9月18日10:56:21
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

from math import sqrt

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
	if num % x == 0:
		is_prime = False
		break
if is_prime and num != 1:
	print('%d是素数' % num)
else:
	print('%d不是素数' % num)
