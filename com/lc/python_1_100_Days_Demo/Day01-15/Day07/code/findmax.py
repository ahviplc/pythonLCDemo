"""

找出列表中最大或最小的元素

Version: 0.1
Author: LC
DateTime:2018年9月18日11:44:54
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""


def main():
	fruits = ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya']
	# 直接使用内置的max和min函数找出列表中最大和最小元素
	# print(max(fruits))
	# print(min(fruits))
	max_value = min_value = fruits[0]
	for index in range(1, len(fruits)):
		if fruits[index] > max_value:
			max_value = fruits[index]
		elif fruits[index] < min_value:
			min_value = fruits[index]
	print('Max:', max_value)
	print('Min:', min_value)


if __name__ == '__main__':
	main()
# 想一想如果最大的元素有两个要找出第二大的又该怎么做 
