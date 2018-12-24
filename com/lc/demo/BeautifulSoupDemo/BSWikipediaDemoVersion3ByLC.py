# !/usr/bin/python
# coding: utf-8

"""
维基百科-项目进阶（广度优先的多线程爬虫）
Version: 3.0
Author: LC
DateTime: 2018年12月24日17:10:15
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""

import threading
import requests
import re
import time

g_mutex = threading.Condition()
g_pages = []  # 从中解析所有url链接
g_queueURL = []  # 等待爬取的url链接列表
g_existURL = []  # 已经爬取过的url链接列表
g_writecount = 0  # 找到的链接数


class Crawler:
    def __init__(self, url, threadnum):
        self.url = url
        self.threadnum = threadnum
        self.threadpool = []

    def craw(self):  # 爬虫的控制大脑，包括爬取网页，更新队列
        global g_queueURL
        g_queueURL.append(url)
        depth = 1
        while (depth < 3):
            print('Searching depth ', depth, '...\n')
            self.downloadAll()
            self.updateQueueURL()
            g_pages = []
            depth += 1

    def downloadAll(self):  # 调用多线程爬虫，在小于线程最大值和没爬完队列之前，会增加线程
        global g_queueURL
        i = 0
        while i < len(g_queueURL):
            j = 0
            while j < self.threadnum and i + j < len(g_queueURL):
                threadresult = self.download(g_queueURL[i + j], j)
                j += 1
            i += j
            for thread in self.threadpool:
                thread.join(30)
            threadpool = []
        g_queueURL = []

    def download(self, url, tid):  # 调用多线程爬虫
        crawthread = CrawlerThread(url, tid)
        self.threadpool.append(crawthread)
        crawthread.start()

    def updateQueueURL(self):  # 完成一个深度的爬虫之后，更新队列
        global g_queueURL
        global g_existURL
        newUrlList = []
        for content in g_pages:
            newUrlList += self.getUrl(content)
        g_queueURL = list(set(newUrlList) - set(g_existURL))

    def getUrl(self, content):  # 从获取的网页中解析url
        link_list = re.findall('<a href="/wiki/([^:#=<>]*?)".*?</a>', content)
        unique_list = list(set(link_list))
        return unique_list


class CrawlerThread(threading.Thread):  # 爬虫线程
    def __init__(self, url, tid):
        threading.Thread.__init__(self)
        self.url = url
        self.tid = tid

    def run(self):
        global g_mutex
        global g_writecount
        try:
            print(self.tid, "crawl ", self.url)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
            r = requests.get("https://en.wikipedia.org/wiki/" + self.url, headers=headers)
            html = r.text

            link_list2 = re.findall('<a href="/wiki/([^:#=<>]*?)".*?</a>', html)
            unique_list2 = list(set(link_list2))
            for eachone in unique_list2:
                g_writecount += 1
                content2 = "No." + str(g_writecount) + "\t Thread" + str(
                    self.tid) + "\t" + self.url + '->' + eachone + '\n'
                with open('link_wikipedia_v3_By_BSWikipediaDemoVersion3ByLC.txt', "a+") as f:
                    f.write(content2)
                    f.close()
        except Exception as e:
            g_mutex.acquire()
            g_existURL.append(self.url)
            g_mutex.release()
            print('Failed downloading and saving', self.url)
            print(e)
            return None
        g_mutex.acquire()
        g_pages.append(html)
        g_existURL.append(self.url)
        g_mutex.release()


if __name__ == "__main__":
    url = "Wikipedia"
    threadnum = 5
    crawler = Crawler(url, threadnum)
    crawler.craw()
