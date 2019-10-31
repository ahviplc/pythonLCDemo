# -*- coding=utf-8 -*-

"""

apscheduler_app.py
备注:python 定时任务APScheduler
Version: 1.0
Author: LC
DateTime: 2019年10月31日09:50:28
UpdateTime:
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
LC博客url: http://oneplusone.vip/index.html
一加壹.SNS LC - 又一个SNS社区: http://sns.oneplusone.vip
赞助一加壹博客最Top-LC万能收款码支持-支付宝、微信、QQ
http://lc.oneplusone.vip/donateMeByLC.html

"""

import time
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler


def func():
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('do func time :', ts)


def func2():
    # 耗时2S
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('do func2 time：', ts)
    time.sleep(2)
    ts2 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('do func2 time done：', ts2)


def dojob():
    # 创建调度器：BlockingScheduler
    scheduler = BlockingScheduler()
    # 添加任务,时间间隔2S
    scheduler.add_job(func, 'interval', seconds=2, id='test_job1')
    # 添加任务,时间间隔5S
    scheduler.add_job(func2, 'interval', seconds=3, id='test_job2')
    scheduler.start()


def dojob2():
    # 创建调度器：BlockingScheduler
    scheduler = BlockingScheduler()
    # 添加任务,时间间隔2S
    scheduler.add_job(func, 'cron', second='*/5', id='test_job3')
    # 添加任务,时间间隔5S 也可以使用 run_date=datetime(2019, 4, 15, 17, 30, 5) 或者 next_run_time=(datetime.datetime.now() + datetime.timedelta(seconds=10))
    scheduler.add_job(func2, 'date', next_run_time=(datetime.datetime.now() + datetime.timedelta(seconds=10)),
                      id='test_job4')
    scheduler.start()


if __name__ == '__main__':
    print('now time: ', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # dojob()
    dojob2()
