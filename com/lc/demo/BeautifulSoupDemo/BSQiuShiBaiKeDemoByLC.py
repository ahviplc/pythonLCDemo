# -*- coding: utf-8 -*-

"""
糗事百科热门段子爬虫
24小时爆笑笑话大全 - 糗事百科
https://www.qiushibaike.com/hot/page/1/
爬：糗事百科段子

Version: 1.0
Author: LC
DateTime: 2018年12月21日14:15:19
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""

# 确定 URL 并抓取页面代码
# 首先我们确定好页面的 URL 是 http://www.qiushibaike.com/hot/page/1，其中最后一个数字1代表页数，我们可以传入不同的值来获得某一页的段子内容。

import urllib
from urllib import error
from urllib import request
import re
from bs4 import BeautifulSoup
import os
import io
import sys


# 糗事百科爬虫类
class QSBK:
    # 初始化方法，定义一些变量
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        # 初始化headers
        self.headers = {'User-Agent': self.user_agent}
        # 存放段子的变量，每一个元素是每一页的段子们
        self.stories = []
        # 存放程序是否继续运行的变量
        self.enable = False

    def get_douban_24h_hot_list(self, pageIndex,txtflie):
        # page = 1
        page = pageIndex
        url = 'https://www.qiushibaike.com/hot/page/' + str(page) + '/'
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent}
        try:
            req = request.Request(url, headers=headers)
            response = request.urlopen(req)
            # print(response.read())
            content = response.read().decode('utf-8')
            # print(content)
            bs_content = BeautifulSoup(str(content), "html.parser")
            # print(bs_content.find_all(id='content-left'))

            itemQSBK = bs_content.find_all('div', class_=re.compile('^article block'))  # 匹配字符串开头为article block的class
            # print(itemQSBK)

            for item in itemQSBK:
                # print(item.contents[1]) # 作者信息
                authorItem = BeautifulSoup(str(item.contents[1]), "html.parser").find_all('div',
                                                                                          class_='author clearfix')
                if (authorItem[0].contents[3].text.strip() != '匿名用户'):

                    printFormat1='用户名称:' + authorItem[0].contents[3].text.strip() + '丨' + '用户等级:' + authorItem[0].contents[5].text.strip() + '丨' + '用户主页:【https://www.qiushibaike.com' + authorItem[0].contents[1].get('href') + '】' + '丨' + '用户头像:【https://' + authorItem[0].contents[1].contents[1].get('src')[2:] + '】'
                    print(printFormat1)
                    # 写入txt
                    txtflie.write(printFormat1+'\n')

                else:
                    print(authorItem[0].contents[3].text.strip() + '丨')

                # print(item.contents[3]) # 正文内容
                # contentHerfItem=BeautifulSoup(str(item.contents[3]), "html.parser").find_all('a', class_='contentHerf')
                contentHerfItem = BeautifulSoup(str(item.contents[3]), "html.parser").find_all('a',class_='contentHerf')

                printFormat2 ='百科正文【https://www.qiushibaike.com'+contentHerfItem[0]['href']+'】:' + contentHerfItem[0].text.strip()
                print(printFormat2)
                # 写入txt
                txtflie.write(printFormat2 + '\n')

                # 正文内容 要是有图片的 输出图片
                contentHerfPicItem = BeautifulSoup(str(item.contents[7]), "html.parser").find_all('div', class_='thumb')
                # print(len(contentHerfPicItem))
                if (len(contentHerfPicItem) == 0):  # 如果 == 0 则是空的
                    pass
                else:
                    # print(contentHerfPicItem[0].contents[1].contents[1].get('src'))
                    printFormat3='百科正文图片:【https://' + contentHerfPicItem[0].contents[1].contents[1].get('src')[ 2:] + '】'
                    print(printFormat3)  # 截取第3个字符到结尾 原数据Demo：//pic.qiushibaike.com/system/avtnew/650/6507537/thumb/20160404212518.jpg?imageView2/1/w/90/h/90
                    # 写入txt
                    txtflie.write(printFormat3 + '\n')
                print('---------------------------------------------------------------------------------------------------')
                # 写入txt
                txtflie.write('---------------------------------------------------------------------------------------------------' + '\n')

            # print('无内容')
            # if type(just_movie) != element.NavigableString:
        except error.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)


if __name__ == "__main__":

    #  修改标准输出流的编码方式
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

    cwd = os.getcwd()

    douBanSpiderResults_cwd = cwd + '/douBanSpiderResults.txt'
    f = open(douBanSpiderResults_cwd, 'a', encoding="utf-8")  # 打开txt文件
    # f.write('\nthe third writing...')
    # f.close()

    # print(douBanSpiderResults) # E:\pycharm-professional-2018.1.3\Code\pythonLCDemo\com\lc\demo\BeautifulSoupDemo/douBanSpiderResults.txt

    print('------开始爬虫了')
    # 写入txt
    f.write('------开始爬虫了'+'\n')

    spider = QSBK()

    # spider.get_douban_24h_hot_list(2) # pageIndex写死版本调用示例

    # 页面动态传参
    # 24小时爆笑笑话大全 - 糗事百科
    # https://www.qiushibaike.com/hot/page/13/
    # 最大13页
    for i in range(1,14): # 包头不包尾

        print('ღ( ´･ᴗ･` )第'+str(i)+'页❤：')

        # 写入txt
        f.write('第'+str(i)+'页：' + '\n')

        # 调用爬虫方法，开始爬虫
        spider.get_douban_24h_hot_list(i,f)


    print('------爬虫完毕')
    print('LC最寄语:要学会举一反三!~LC')

    # 写入txt
    f.write('------爬虫完毕' + '\n')
    f.write('LC最寄语:要学会举一反三!~LC' + '\n')

    # 关闭文本
    f.close()
