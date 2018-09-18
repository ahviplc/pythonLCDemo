"""

找出100~999之间的所有水仙花数
水仙花数是各位立方和等于这个数本身的数
如: 153 = 1**3 + 5**3 + 3**3

Version: 0.1
Author: LC
DateTime:2018年9月18日11:12:07
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

for num in range(100, 1000):
	low = num % 10
	mid = num // 10 % 10
	high = num // 100
	if num == low ** 3 + mid ** 3 + high ** 3:
		print(num)
