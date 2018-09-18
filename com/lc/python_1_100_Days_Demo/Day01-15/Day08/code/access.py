"""

Version: 0.1
Author: LC
DateTime:2018年9月18日12:55:06
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""


class Test:

	def __init__(self, foo):
		self.__foo = foo

	def __bar(self):
		print(self.__foo)
		print('__bar')


def main():
	test = Test('hello')
	test._Test__bar()
	print(test._Test__foo)


if __name__ == "__main__":
	main()
