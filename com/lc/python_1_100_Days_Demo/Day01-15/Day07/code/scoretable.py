"""

学生考试成绩表

Version: 0.1
Author: LC
DateTime:2018年9月18日11:45:42
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""


def main():
	names = ['关羽', '张飞', '赵云', '马超', '黄忠']
	subjs = ['语文', '数学', '英语']
	scores = [[0] * 3] * 5
	for row, name in enumerate(names):
		print('请输入%s的成绩' % name)
		for col, subj in enumerate(subjs):
			scores[row][col] = float(input(subj + ': '))
	print(scores)
#	for row, name in enumerate(names):
#		print('请输入%s的成绩' % name)
#		scores[row] = [None] * len(subjs)
#		for col, subj in enumerate(subjs):
#			score = float(input(subj + ': '))
#			scores[row][col] = score
#	print(scores)

if __name__ == '__main__':
	main()
