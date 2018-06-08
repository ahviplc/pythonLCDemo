# Filename : calendarDemo.py
# author by : www.oneplusone.top
# 2018年6月9日00:35:01
# 1-100求和
sumSum = 0

# Python判断变量的数据类型的两种方法
# Python中的数据类型有数字（int）、字符串，列表(list)、元组、字典(dict)、集合等。有两种方法判断一个变量的数据类型
# 1、isinstance(变量名，类型)
# 2、通过与其他已知类型的常量进行对比

print(isinstance(sumSum,int))

maxInt=int(input('输入一个数字：'))

for i in range(1,maxInt+1):
    sumSum=sumSum+i

print(sumSum)

print("1至%d之间的求和为 %d" % (maxInt, sumSum))
