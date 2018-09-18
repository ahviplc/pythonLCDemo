"""

定义和使用学生类

Version: 0.1
Author: LC
DateTime:2018年9月18日13:02:50
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""


def _foo():
	print('test')


class Student(object):

	# __init__是一个特殊方法用于在创建对象时进行初始化操作
	# 通过这个方法我们可以为学生对象绑定name和age两个属性
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def study(self, course_name):
		print('%s正在学习%s.' % (self.name, course_name))

	# PEP 8要求标识符的名字用全小写多个单词用下划线连接
	# 但是很多程序员和公司更倾向于使用驼峰命名法(驼峰标识)
	def watch_av(self):
		if self.age < 18:
			print('%s只能观看《熊出没》.' % self.name)
		else:
			print('%s正在观看岛国爱情动作片.' % self.name)


def main():
	stu1 = Student('LC', 25)
	stu1.study('Python程序设计')
	stu1.watch_av()
	stu2 = Student('王大锤', 15)
	stu2.study('思想品德')
	stu2.watch_av()


if __name__ == '__main__':
	main()