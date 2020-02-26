#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
一些serial方法
Version: 1.0
Author: LC
DateTime: 2020年2月26日13:40:31
UpdateTime:
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
LC博客url: http://oneplusone.vip/index.html
一加壹.SNS LC - 又一个SNS社区: http://sns.oneplusone.vip
赞助一加壹博客最Top-LC万能收款码支持-支付宝、微信、QQ
http://lc.oneplusone.vip/donateMeByLC.html
"""
import serial

ser = serial.Serial('COM1', 9600, timeout=0.5)


# ser = serial.Serial('COM6', 9600)

# 方法:是否打开
def is_open():
    print(ser.name)
    print(ser.port)
    s = ser.read(10)  # 从端口读10个字节
    print(s)
    ser.write(str.encode('hello'))  # 向端口些数据
    s = ser.read(10)  # 从端口读10个字节
    print(s)
    # ser.baudrate = 9600  # 设置波特率
    # ser.isOpen() #看看这个串口是否已经被打开
    if not ser.isOpen():
        ser.open()
        print('com3 is open', ser.isOpen())
    else:
        print('此已打开')
        # ser.close()  # 关闭端口


# 获取一行信息
def recv(serial_data):
    data = ''
    while serial_data.inWaiting() > 0:
        print(serial_data.inWaiting())
        # data += str(serial.read(15)) # ok 要配合timeout 使用, 否则要传入已知 的 size
        # data += str(serial.readline())  # ok 要配合timeout 使用
        # data += str(serial.readlines())  # ok 要配合timeout 使用
        # data += str(serial.readall())     # ok 要配合timeout 使用
        data += str(serial_data.read_all())  # ok 要配合timeout 使用

        print("************************************")
        # print(serial.read(13))
        print('准备打印data')
        # data = str(serial.read(19))
        print(data)
        print('data:%s' % data)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return data


# main方法
if __name__ == '__main__':
    is_open()

    data = recv(ser)
    if data != '':
        print(data)
    else:
        print('data为空')
