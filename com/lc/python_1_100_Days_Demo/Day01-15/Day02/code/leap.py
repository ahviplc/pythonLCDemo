"""

输入年份 如果是闰年输出True 否则输出False

闰年定义：

公历闰年判定遵循的规律为: 四年一闰,百年不闰,四百年再闰.
公历闰年的简单计算方法（符合以下条件之一的年份即为闰年，反之则是平年）
1.能被4整除而不能被100整除。
2.能被100整除也能被400整除。

Version: 0.1
Author: LC
DateTime:2018年6月17日21:59:34
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

year = int(input('请输入年份: '))
# 如果代码太长写成一行不便于阅读 可以使用\或()折行
is_leap = (year % 4 == 0 and year % 100 != 0 or
           year % 400 == 0)
print(is_leap)
