"""

函数的定义和使用 - 计算组合数C(7,3)

Version: 0.1
Author: LC
DateTime:2018年9月18日11:32:04
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""


# 将求阶乘的功能封装成一个函数
def factorial(n):
	result = 1
	for num in range(1, n + 1):
		result *= num
	return result


print(factorial(7) // factorial(3) // factorial(4))
print(factorial(5))