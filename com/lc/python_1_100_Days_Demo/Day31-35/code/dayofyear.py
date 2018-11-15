"""
输入年月日执行 看是今年的多少天

Version: 0.1
Author: LC
DateTime: 2018年11月15日14:27:36
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""
import sys
import calendar as mycal


def main():
    if len(sys.argv) != 4:
        print('Not enough arguments')
        return 
    year = int(sys.argv[1])
    month = int(sys.argv[2])
    day = int(sys.argv[3])
    total = 0
    for m in range(1, month):
        #total += mycal.get_days(year, m)
        monthRangeYZ=mycal.monthrange(year, m) #返回元组 (3,30) ！输出的是一个元组，第一个元素是所查月份的第一天对应的是星期几（0-6），第二个元素是这个月的天数。以上实例输出的意思为 2016 年 9 月份的第一天是星期四，该月总共有 30 天。
        print(monthRangeYZ)
        total +=monthRangeYZ[1]
    total += day
    print(f'{year}年{month}月{day}日是{year}年的第{total}天')


if __name__ == '__main__':
    main()


"""
E:\pycharm-professional-2018.1.3\Code\pythonLCDemo\venv\Scripts\python.exe E:/pycharm-professional-2018.1.3/Code/pythonLCDemo/com/lc/python_1_100_Days_Demo/Day31-35/code/dayofyear.py 2018 11 15
LC 自己已完成功能！

(0, 31)
(3, 28)
(3, 31)
(6, 30)
(1, 31)
(4, 30)
(6, 31)
(2, 31)
(5, 30)
(0, 31)
2018年11月15日是2018年的第319天

"""