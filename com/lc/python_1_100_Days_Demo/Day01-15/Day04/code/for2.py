"""

用for循环实现1~100之间的偶数求和  方法2

Version: 0.1
Author: LC
DateTime:2018年9月18日10:53:24
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

sum = 0
for x in range(2, 101, 2):
	sum += x
print(sum)
