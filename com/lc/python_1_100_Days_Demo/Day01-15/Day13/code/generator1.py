"""

生成器 - 生成器语法

Version: 0.1
Author: LC
DateTime:2018年11月14日16:09:52
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html


"""

seq = [x * x for x in range(10)]
print(seq)

gen = (x * x for x in range(10))
print(gen)
for x in gen:
	print(x)

num = 10
gen = (x ** y for x, y in zip(range(1, num), range(num - 1, 0, -1)))
print(gen)
n = 1
while n < num:
	print(next(gen))
	n += 1
