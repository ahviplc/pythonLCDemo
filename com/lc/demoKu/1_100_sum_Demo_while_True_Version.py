# Filename : calendarDemo.py
# author by : www.oneplusone.top
# 2018年9月20日10:07:38
# 1-100求和
# 输入一个数字 求1-此数字之间所有的和  while True 无限执行版本   这是运行五次退出


# Python判断变量的数据类型的两种方法
# Python中的数据类型有数字（int）、字符串，列表(list)、元组、字典(dict)、集合等。有两种方法判断一个变量的数据类型
# 1、isinstance(变量名，类型)
# 2、通过与其他已知类型的常量进行对比
import time

cishu=0

while True:
    cishu=cishu+1
    if cishu > 5 :
        print('运行了五次了，这是第六次！我退出了！此运行次数:'+str(cishu))
        time.sleep(3) #睡三秒 seconds 单位是:秒
        break
    else:
        print('我还可以浪，请继续输入！此运行次数:'+str(cishu))
        sumSum = 0
        # print(isinstance(sumSum, int))   #判断sumSum是否为int类型
        maxInt = int(input('输入一个数字：'))
        for i in range(1, maxInt + 1):
            sumSum = sumSum + i
        print(sumSum)
        print("1至%d之间的求和为 %d" % (maxInt, sumSum))
        continue


"""

pycharm如何将python文件打包为exe格式 - CSDN博客
https://blog.csdn.net/qq1877383144/article/details/81200471

“pyinstaller -F -w *.py” 就可以制作出exe。生成的文件放在同目录dist下。

    -F（注意大写）是所有库文件打包成一个exe，-w是不出黑色控制台窗口。

    不加-F参数生成一堆文件，但运行快。压缩后比单个exe文件还小一点点。

    加-F参数生成一个exe文件，运行起来慢。

打包成exe命令

pyinstaller -F E:\pycharm-professional-2018.1.3\Code\pythonLCDemo\com\lc\demoKu\1_100_sum_Demo_while_True_Version.py

Pyinstaller --version

pyinstaller --version

大小写都可以！

LC 2018年9月20日10:36:08
"""