"""

输出2~99之间的素数

Version: 0.1
Author: LC
DateTime:2018年9月18日11:12:36
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

import math

for num in range(2, 100):
	is_prime = True
	for factor in range(2, int(math.sqrt(num)) + 1):
		if num % factor == 0:
			is_prime = False
			break
	if is_prime:
		print(num, end=' ')
