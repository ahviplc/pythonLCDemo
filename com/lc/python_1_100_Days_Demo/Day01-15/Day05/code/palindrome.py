"""

判断输入的正整数是不是回文数
回文数是指将一个正整数从左往右排列和从右往左排列值一样的数

Version: 0.1
Author: LC
DateTime:2018年9月18日11:12:15
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

num = int(input('请输入一个正整数: '))
temp = num
num2 = 0
while temp > 0:
	num2 *= 10
	num2 += temp % 10
	temp //= 10
if num == num2:
	print('%d是回文数' % num)
else:
	print('%d不是回文数' % num)
