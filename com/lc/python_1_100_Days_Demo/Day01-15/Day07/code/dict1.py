"""

定义和使用字典

Version: 0.1
Author: LC
DateTime:2018年9月18日11:44:25
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""


def main():
	scores = {'LC': 95, '白元芳': 78, '狄仁杰': 82}
	print(scores['LC'])
	print(scores['狄仁杰'])
	for elem in scores:
		print('%s\t--->\t%d' % (elem, scores[elem]))
	scores['白元芳'] = 65
	scores['诸葛王朗'] = 71
	scores.update(冷面=67, 方启鹤=85)
	print(scores)
	if '武则天' in scores:
		print(scores['武则天'])
	print(scores.get('武则天'))
	print(scores.get('武则天', 60))
	print(scores.popitem())
	print(scores.popitem())
	print(scores.pop('LC', 100))
	scores.clear()
	print(scores)


if __name__ == '__main__':
	main()
