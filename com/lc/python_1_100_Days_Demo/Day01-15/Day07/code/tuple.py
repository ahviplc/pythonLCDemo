"""

元组的定义和使用

Version: 0.1
Author: LC
DateTime:2018年9月18日11:46:14
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""


def main():
	# 定义元组
	t = ('LC', 38, True, '❤SH')
	print(t)
	# 获取元组中的元素
	print(t[0])
	print(t[1])
	print(t[2])
	print(t[3])
	# 遍历元组中的值
	for member in t:
		print(member)
	# 重新给元组赋值
	# t[0] = '王大锤'		# TypeError
	# 变量t重新引用了新的元组 原来的元组被垃圾回收
	t = ('王大锤', 20, True, '云南昆明')
	print(t)
	# 元组和列表的转换
	person = list(t)
	print(person)
	person[0] = '李小龙'
	person[1] = 25
	print(person)
	fruits_list = ['apple', 'banana', 'orange']
	fruits_tuple = tuple(fruits_list)
	print(fruits_tuple)
	print(fruits_tuple[1])


if __name__ == '__main__':
	main()