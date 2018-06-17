"""

字符串常用操作

Version: 0.1
Author: LC
DateTime:2018年6月17日23:18:33
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

Python 字符串 | 教程
http://www.runoob.com/python/python-strings.html

"""

str1 = 'hello, world!'
print('字符串的长度是:', len(str1))
print('单词首字母大写: ', str1.title())
print('字符串变大写: ', str1.upper())
# str1 = str1.upper()
print('字符串是不是大写: ', str1.isupper())
print('字符串是不是以hello开头: ', str1.startswith('hello'))
print('字符串是不是以hello结尾: ', str1.endswith('hello'))
print('字符串是不是以感叹号开头: ', str1.startswith('!'))
print('字符串是不是一感叹号结尾: ', str1.endswith('!'))
# str2 = '- \u9a86\u660a'   骆昊
strLC = '-栗晨LC'
strlichen ='- \u6817\u6668'
str3 = str1.title() + ' ' + strLC.lower()+strLC+strlichen
print(str3)


listu = ['\\u751F\\u5316\\u5371\\u673A']

print(listu[0])

print(listu[0].encode('utf-8').decode('unicode_escape'))


print(strLC.encode("utf-8"))
print(strLC.encode("unicode_escape"))



"""
输出示例：
字符串的长度是: 13
单词首字母大写:  Hello, World!
字符串变大写:  HELLO, WORLD!
字符串是不是大写:  False
字符串是不是以hello开头:  True
字符串是不是以hello结尾:  False
字符串是不是以感叹号开头:  False
字符串是不是一感叹号结尾:  True
Hello, World! -栗晨lc-栗晨LC- 栗晨
\u751F\u5316\u5371\u673A
生化危机
b'-\xe6\xa0\x97\xe6\x99\xa8LC'
b'-\\u6817\\u6668LC'
"""