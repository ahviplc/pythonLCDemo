"""

列表常用操作
	- 列表连接
	- 获取长度
	- 遍历列表
	- 列表切片
	- 列表排序
	- 列表反转
	- 查找元素

Version: 0.1
Author: LC
DateTime:2018年9月18日11:45:11
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""


def main():
	fruits = ['grape', 'apple', 'strawberry', 'waxberry']
	fruits += ['pitaya', 'pear', 'mango']
	# 循环遍历列表元素
	for fruit in fruits:
		print(fruit.title(), end=' ')
	print()
	# 列表切片
	fruits2 = fruits[1:4]
	print(fruits2)
	# fruit3 = fruits  # 没有复制列表只创建了新的引用
	fruits3 = fruits[:]
	print(fruits3)
	fruits4 = fruits[-3:-1]
	print(fruits4)
	fruits5 = fruits[::-1]
	print(fruits5)


if __name__ == '__main__':
	main()
