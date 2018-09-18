"""

另一种创建类的方式

Version: 0.1
Author: LC
DateTime:2018年9月18日13:01:25
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""


def bar(self, name):
	self._name = name


def foo(self, course_name):
	print('%s正在学习%s.' % (self._name, course_name))


def main():
	Student = type('Student', (object,), dict(__init__=bar, study=foo))
	stu1 = Student('LC')
	stu1.study('Python程序设计')


if __name__ == '__main__':
	main()	
