"""

继承的应用
	- 抽象类
	- 抽象方法
	- 方法重写
	- 多态

Version: 0.1
Author: LC
DateTime:2018年9月18日14:05:47
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

from abc import ABCMeta, abstractmethod
from math import pi


class Shape(object, metaclass=ABCMeta):

	@abstractmethod
	def perimeter(self):
		pass

	@abstractmethod
	def area(self):
		pass


class Circle(Shape):

	def __init__(self, radius):
		self._radius = radius

	def perimeter(self):
		return 2 * pi * self._radius

	def area(self):
		return pi * self._radius ** 2

	def __str__(self):
		return '我是一个圆'


class Rect(Shape):

	def __init__(self, width, height):
		self._width = width
		self._height = height

	def perimeter(self):
		return 2 * (self._width + self._height)

	def area(self):
		return self._width * self._height

	def __str__(self):
		return '我是一个矩形'


if __name__ == '__main__':
	shapes = [Circle(5), Circle(3.2), Rect(3.2, 6.3)]
	for shape in shapes:
		print(shape)
		print('周长:', shape.perimeter())
		print('面积:', shape.area())
