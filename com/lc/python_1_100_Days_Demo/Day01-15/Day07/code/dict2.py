"""

字典的常用操作

Version: 0.1
Author: LC
DateTime:2018年9月18日11:44:39
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""


def main():
	stu = {'name': 'LC', 'age': 38, 'gender': True}
	print(stu)
	print(stu.keys())
	print(stu.values())
	print(stu.items())
	for elem in stu.items():
		print(elem)
		print(elem[0], elem[1])
	if 'age' in stu:
		stu['age'] = 20
	print(stu)
	stu.setdefault('score', 60)
	print(stu)
	stu.setdefault('score', 100)
	print(stu)
	stu['score'] = 100
	print(stu)


if __name__ == '__main__':
	main()
