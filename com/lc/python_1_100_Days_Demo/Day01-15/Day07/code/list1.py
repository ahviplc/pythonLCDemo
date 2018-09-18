"""

定义和使用列表
	- 用下标访问元素
	- 添加元素
	- 删除元素

Version: 0.1
Author: LC
DateTime:2018年9月18日11:45:02
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""


def main():
	fruits = ['grape', '@pple', 'strawberry', 'waxberry']
	print(fruits)
	# 通过下标访问元素
	print(fruits[0])
	print(fruits[1])
	print(fruits[-1])
	print(fruits[-2])
	# print(fruits[-5]) # IndexError
	# print(fruits[4])	# IndexError
	fruits[1] = 'apple'
	print(fruits)
	# 添加元素
	fruits.append('pitaya')
	fruits.insert(0, 'banana')
	print(fruits)
	# 删除元素
	del fruits[1]
	fruits.pop()
	fruits.pop(0)
	fruits.remove('apple')
	print(fruits)


if __name__ == '__main__':
	main()
