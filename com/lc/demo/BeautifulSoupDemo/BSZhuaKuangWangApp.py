# -*- coding: utf-8 -*-

"""
糗百成人版|糗事百科成人版成年手机版主页-各种丑事福利和搞笑图片-抓狂网
http://www.yicommunity.com
爬：抓狂网段子

Version: 1.0
Author: LC
DateTime: 2020年2月28日09:52:32
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""

# 确定 URL 并抓取页面代码 这是抓狂网最新笑话
# 首先我们确定好页面的 URL 是
# 第1页-zuixin
# http://www.yicommunity.com/zuixin/，
#
# 第2页-zuixin
# http://www.yicommunity.com/zuixin/index_2.html
# 其中最后一个数字2代表页数，我们可以传入不同的值来获得某一页的段子内容。

# 抓狂网 热门/热图笑话 处理与上面最新类似
# 热门
# 第1页-remen
# http://www.yicommunity.com/remen/
#
# 第2页-remen
# http://www.yicommunity.com/remen/index_2.html

# 热图
# 第1页-retu
# http://www.yicommunity.com/retu/
#
# 第2页-retu
# http://www.yicommunity.com/retu/index_2.html

import urllib
from urllib import error
from urllib import request
import re
from bs4 import BeautifulSoup
import os
import io
import sys
from print_msg_to_log_model import PrintLogger
from bs4.element import NavigableString

# 改变系统环境编码为简体中文utf-8-为了让oracle查询出的中文不乱码
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

# 抓狂网爬虫类
class ZK:
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

    def get_zk_zuixin_list(self, pageIndex, txtflie):
        # page = 1
        page = pageIndex
        url = '';
        if page == 1:
            url = 'http://www.yicommunity.com/zuixin/';  # 这个就是第一页
        else:
            url = 'http://www.yicommunity.com/zuixin/index_' + str(page) + '.html'
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

            itemZK = bs_content.find_all('div', class_=re.compile('^block untagged mb15 bs2'))  # 匹配字符串开头为block untagged mb15 bs2的class div
            # print(itemZK)
            # 输出类型
            # print(type(itemZK))  # <class 'bs4.element.ResultSet'>

            for item in itemZK:
                # print(item.contents[0]) # detail 详情页
                detailItem = BeautifulSoup(str(item.contents[0]), "html.parser").find_all('div', class_='detail')
                # print(type(detailItem))  # <class 'bs4.element.ResultSet'>
                # print(detailItem[0].text.strip())

                # 输出类型
                # print(type(detailItem[0]))  # <class 'bs4.element.Tag'>
                # print(type(detailItem[0].text))  # <class 'str'>
                # print(type(detailItem[0].text.strip()))  # <class 'str'>

                # print(detailItem[0].contents[0].get('href'))
                # print(detailItem[0].contents[0].get('src'))  # 这个详情里没有src

                # print(item.contents[3]) # qiushi_counts_140884 点赞等数量 不处理

                # print(item.contents[1]) # author 作者信息
                authorItem = BeautifulSoup(str(item.contents[1]), "html.parser").find_all('div', class_='author')
                # print(authorItem[0].text.strip())
                # # print(authorItem[0].contents[0].get('href'))
                # print(authorItem[0].contents[0].get('src'))  # 这个作者头像已失效 不处理

                # print(item.contents[2]) # content 正文内容
                contentHerfItem = BeautifulSoup(str(item.contents[2]), "html.parser").find_all('div', class_='content')
                # print(contentHerfItem[0].text.strip())

                # # 输出类型以及其判断 判断方法目前总结了以下三种 已测试 可用
                # print(type(contentHerfItem[0].contents[0]))  # <class 'bs4.element.NavigableString'>
                # # 方法1：if 类型 语句
                # if contentHerfItem[0].contents[0] != NavigableString:
                #     print(contentHerfItem[0].contents[0])
                #     print('if方法 是NavigableString类型')  # if方法 是NavigableString类型
                # else:
                #     print('if方法 不是NavigableString类型')
                #
                # # 方法2：isinstance
                # print(isinstance(contentHerfItem[0].contents[0], NavigableString))  # True 这个如果是True就是bs4.element.NavigableString类型 为False就不是
                #
                # # 方法3 type(contentHerfItem[0].contents[0])之后转成str判断
                # print(str(type(contentHerfItem[0].contents[0])) == "<class 'bs4.element.NavigableString'>")  # True 这个如果是True就是bs4.element.NavigableString类型 为False就不是
                # print(str(type(contentHerfItem[0].contents[0])))  # <class 'bs4.element.NavigableString'>

                printFormat2 = '抓狂网笑话'+' 作者:'+authorItem[0].text.strip()+' 正文:【http://www.yicommunity.com' + detailItem[0].contents[0].get('href') + '】: ' + contentHerfItem[0].text.strip()
                # print(printFormat2)  # 这个输出和下面的输出一样的
                print('抓狂网笑话','作者:'+ authorItem[0].text.strip(),'正文:【http://www.yicommunity.com' + detailItem[0].contents[0].get('href') + '】:',contentHerfItem[0].text.strip())
                # 写入txt
                txtflie.write(printFormat2 + '\n')
                print('---------------------------------------------------------------------------------------------------')
                # 写入txt
                txtflie.write('---------------------------------------------------------------------------------------------------' + '\n')
        except error.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)


if __name__ == "__main__":

    # sys.stdout = PrintLogger('BSZhuaKuangWangApp.py.log')  # 监听所有的print到log日志 封装类 如不需要打印所有输出print的log日志，隐掉这段即可 注意：这个放开line132需要隐掉

    # print(sys.getdefaultencoding())  # utf-8
    # print(sys.stdout.encoding)  # UTF-8
    # print('中文')  # 中文

    #  修改标准输出流的编码方式
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 注意如果加了这个,想要print实时输出,需要print('------开始爬虫了', flush=True)这样书写.

    # print(sys.getdefaultencoding(), flush=True)
    # print(sys.stdout.encoding, flush=True)
    # print('中文', flush=True)

    # 获取当前的文件路径 'C:\\_developSoftKu\\PyCharm 2019.1.3\\#CodeKu\\pythonLCDemo\\com\\lc\\demo\\BeautifulSoupDemo'
    cwd = os.getcwd()

    zhuaKuangResults_cwd = cwd + '/BSZhuaKuangWangApp.py.txt'
    f = open(zhuaKuangResults_cwd, 'a', encoding="utf-8")  # 打开txt文件
    # f.write('\nthe third writing...')
    # f.close()

    print('------开始爬虫了')
    # print('------开始爬虫了', flush=True)  # 这个为了解决加了io.TextIOWrapper处理后,print()内容就跟不上执行节奏，加个flush=True, print就能正常输出字符串了
    # 写入txt
    f.write('------开始爬虫了' + '\n')

    spider = ZK()

    # 页面动态传参
    # 最新笑话大全 - 抓狂网
    # http: // www.yicommunity.com / zuixin /
    # http://www.yicommunity.com/zuixin/index_2.html
    # 最大10页
    for i in range(1, 11):  # 包头不包尾
        print('ღ( ´･ᴗ･` )第' + str(i) + '页❤：')
        # 写入txt
        f.write('第' + str(i) + '页：' + '\n')
        # 调用爬虫方法，开始爬虫
        spider.get_zk_zuixin_list(i, f)
    print('------爬虫完毕')
    print('LC最寄语:要学会举一反三!~LC')
    # 写入txt
    f.write('------爬虫完毕' + '\n')
    f.write('LC最寄语:要学会举一反三!~LC' + '\n')
    # 关闭文本
    f.close()