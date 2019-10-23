# -*- coding=utf-8 -*-

"""
timeClockApp.py
timeClockDemo 时间闹钟 定时提醒器
备注：核心想法：就是每隔两天的晚上20:00用邮件发送给我邮件，提醒我给电瓶车充电.
其他说明: EmailConfig.py 为邮件的配置文件 emailUtil.py 发送邮件的工具类
Version: 1.0
Author: LC
DateTime: 2019年10月23日12:09:36
UpdateTime:
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
LC博客url: http://oneplusone.vip/index.html
一加壹.SNS LC - 又一个SNS社区: http://sns.oneplusone.vip
赞助一加壹博客最Top-LC万能收款码支持-支付宝、微信、QQ
http://lc.oneplusone.vip/donateMeByLC.html

"""

__author__ = 'LC'
from emailUtil import sendEmail
import threading
import time
import datetime


def hello(name):
    print("hello " + name)
    global timer
    timer = threading.Timer(2.0, hello, ["LC"])
    timer.start()


def runHello():
    timer = threading.Timer(2.0, hello, ["LC"])  # 每隔两秒调用函数hello
    timer.start()
    pass


def Email():
    sendEmail("timeClock测试一下 By LC")


def get_now_time():
    # 获得当前时间时间戳
    now = int(time.time())
    # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
    timeStruct = time.localtime(now)
    strTime = time.strftime("%Y-%m-%d %H:%M:%S", timeStruct)
    return strTime


# sec 每隔多少秒调用一次
# msg 要提醒干的事情
# call_me_hour 什么小时要提醒我
# call_me_min 什么小时要提醒我
# call_me_sec 什么小时要提醒我
def main(sec, call_me_hour, call_me_min, call_me_sec, msg):
    print("当前时间: " + get_now_time())
    # print("i am main - " + msg)
    # print(datetime.datetime.now().hour)
    hour_temp = datetime.datetime.now().hour
    min_temp = datetime.datetime.now().minute
    sec_temp = datetime.datetime.now().second
    if (str(hour_temp) == call_me_hour and str(min_temp) == call_me_min and str(sec_temp) == call_me_sec):
        # print("发送邮件")
        sendEmail(msg)
        # 然后睡3秒 防止无止境的消耗资源
        print("我要睡47小时55分钟-也就是172500秒")
        print("醒来时间:" + (datetime.datetime.now() + datetime.timedelta(seconds=+172500)).strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(172500)
        pass
    else:
        print("未到 20:00:00")
        pass
    timer = threading.Timer(sec, main, [sec, call_me_hour, call_me_min, call_me_sec, msg])  # 每隔sec秒调用函数main
    timer.start()


if __name__ == '__main__':
    # runHello()  # 测试demo
    # hello("LC")
    # Email()

    # main() 发送提醒的主方法
    # 每隔1秒调用函数main
    # 20:00:00提醒
    # 提醒内容:"☆提醒 - 电瓶车要充电了- By LC"
    main(1, "20", "00", "00", "☆提醒 - 电瓶车要充电了- By LC")
