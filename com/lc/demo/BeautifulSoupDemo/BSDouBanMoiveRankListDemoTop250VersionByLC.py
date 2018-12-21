# -*- coding: utf-8 -*-
"""
豆瓣电影排行榜
https://movie.douban.com/chart
LC 2018-12-20 18:24:29
爬右下角的：豆瓣电影TOP250

Version: 1.0
Author: LC
DateTime: 2018年12月21日14:16:26
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""

from bs4 import BeautifulSoup
from bs4 import element
import requests, sys


def get_movie_top_list(self):
    req = requests.get(url=self)
    html = req.text
    div_bf = BeautifulSoup(html, "html.parser")

    div = div_bf.find_all('div', class_='indent')
    # print(div[0])
    # print(div[1]) # top250

    divTop250 = div_bf.find_all('div', class_='douban-top250-bd')
    # print(divTop250)

    top250_list_bf_a = BeautifulSoup(str(divTop250), "html.parser")
    a = top250_list_bf_a.find_all('dl')
    top250_list_bf_b = BeautifulSoup(str(a), "html.parser")
    # print(a)

    # 方法一:
    for just_movie in top250_list_bf_b.contents:
        # print(just_movie)
        if type(just_movie) != element.NavigableString:
            # print(BeautifulSoup(str(just_movie), "html.parser").find_all('a'))

            # print(BeautifulSoup(str(just_movie), "html.parser").find_all('a')[0].contents[1]['src'])
            # print(BeautifulSoup(str(just_movie), "html.parser").find_all('a')[0].contents[1]['class'])
            # 与上面形式等价
            picHref = BeautifulSoup(str(just_movie), "html.parser").find_all('a')[0].contents[1].get('src')
            # print(picHref)
            # print(BeautifulSoup(str(just_movie), "html.parser").find_all('a')[0].contents[1].get('class'))

            # print(BeautifulSoup(str(just_movie), "html.parser").find_all('a')[1])
            douBanHref = BeautifulSoup(str(just_movie), "html.parser").find_all('a')[1].get('href')
            # print(douBanHref)
            movieName = BeautifulSoup(str(just_movie), "html.parser").find_all('a')[1].text.strip()
            # print(movieName)

            # 格式化输出
            print('电影名称：{0} ，图片链接: {1} ， 豆瓣链接: {2} '.format(movieName, picHref, douBanHref))

    # 方法二
    # b_dt = top250_list_bf_b.find_all('dt')
    # for a_movie in b_dt:
    #     print((a_movie.contents)[1].get('href'))
    #     print(((a_movie.contents)[1].contents)[1].get('src'))
    #
    # b_dd = top250_list_bf_b.find_all('dd')
    # for b_movie in b_dd:
    #     print(b_movie.text.strip())
    #     #print((b_movie.contents)[1].get('href'))

    print('------爬虫完毕')
    print('LC最寄语:永远不要放弃!~LC')


if __name__ == "__main__":
    print('------开始爬虫了')
    get_movie_top_list("https://movie.douban.com/chart")

"""
1.strip()：把头和尾的空格去掉

2.lstrip()：把左边的空格去掉

3.rstrip()：把右边的空格去掉

4.replace('c1','c2')：把字符串里的c1替换成c2。故可以用replace(' ','')来去掉字符串里的所有空格

5.split()：通过指定分隔符对字符串进行切片，如果参数num 有指定值，则仅分隔 num 个子字符串
"""
