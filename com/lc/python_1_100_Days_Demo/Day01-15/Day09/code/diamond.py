"""

多重继承
	- 菱形继承(钻石继承)
	- C3算法(替代DFS的算法)

Version: 0.1
Author: LC
DateTime:2018年9月18日13:54:56
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""


class A(object):

	def foo(self):
		print('foo of A')


class B(A):
	pass


class C(A):

	def foo(self):
		print('foo fo C')


class D(B, C):
	pass


class E(D):

	def foo(self):
		print('foo in E')
		super().foo()
		super(B, self).foo()
		super(C, self).foo()


if __name__ == '__main__':
	d = D()
	d.foo()
	e = E()
	e.foo()
