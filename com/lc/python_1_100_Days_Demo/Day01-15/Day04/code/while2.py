"""

用while循环实现1~100之间的偶数求和

Version: 0.1
Author: LC
DateTime:2018年9月18日10:58:04
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

sum = 0
num = 2
while num <= 100:
	sum += num
	num += 2
print(sum)
