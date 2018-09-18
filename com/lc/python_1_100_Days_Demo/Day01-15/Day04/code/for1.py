"""
用for循环实现 1~100 的 偶数 求和  方法1

Version: 0.1
Author: LC
DateTime:2018年9月18日10:26:34
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

# x %  2 ==0 就是x除以2余数为0 ，代表能被2整除 。 %是取余

sum = 0
for x in range(0, 101):
	if x % 2 == 0:
		sum += x
print(sum)