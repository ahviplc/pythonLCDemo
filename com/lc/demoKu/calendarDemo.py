# Filename : calendarDemo.py
# author by : www.oneplusone.top

# 引入日历模块
import calendar

# 输入指定年月
yy = int(input("输入年份: "))
mm = int(input("输入月份: "))

# 显示日历
print(calendar.month(yy,mm))

calendarstr=calendar.month(yy,mm).__str__()

# Python count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
print(calendarstr.count("1"))

# 输入年份: 2018
# 输入月份: 6
#      June 2018
# Mo Tu We Th Fr Sa Su
#              1  2  3
#  4  5  6  7  8  9 10
# 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24
# 25 26 27 28 29 30
#
# 14