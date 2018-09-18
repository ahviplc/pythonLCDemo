"""

生成斐波拉切数列

Version: 0.1
Author: LC
DateTime:2018年9月18日11:44:46
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""


def main():
	f = [1 , 1]
	for i in range(2, 20):
		f += [f[i - 1] + f[i - 2]]
		# f.append(f[i - 1] + f[i - 2])
	for val in f:
		print(val, end=' ')


if __name__ == '__main__':
	main()
