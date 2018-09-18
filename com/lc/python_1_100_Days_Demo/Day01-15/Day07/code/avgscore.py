"""

输入学生考试成绩计算平均分

Version: 0.1
Author: LC
DateTime:2018年9月18日11:44:14
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""


def main():
	number = int(input('请输入学生人数: '))
	names = [None] * number
	scores = [None] * number
	for index in range(len(names)):
		names[index] = input('请输入第%d个学生的名字: ' % (index + 1))
		scores[index] = float(input('请输入第%d个学生的成绩: ' % (index + 1)))
	total = 0
	for index in range(len(names)):
		print('%s: %.1f分' % (names[index], scores[index]))
		total += scores[index]
	print('平均成绩是: %.1f分' % (total / number))


if __name__ == '__main__':
	main()
