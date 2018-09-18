"""

找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14

Version: 0.1
Author: LC
DateTime:2018年9月18日11:12:25
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""
import time
import math

start = time.clock()
for num in range(1, 10000):
	sum = 0
	for factor in range(1, int(math.sqrt(num)) + 1):
		if num % factor == 0:
			sum += factor
			if factor > 1 and num / factor != factor:
				sum += num / factor
	if sum == num:
		print(num)
end = time.clock()
print("执行时间:", (end - start), "秒")

# 通过比较上面两种不同的解决方案的执行时间 意识到优化程序的重要性
