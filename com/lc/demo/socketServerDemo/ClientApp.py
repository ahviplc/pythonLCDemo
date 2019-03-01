#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""

ClientApp.py
socketserver客户端
Version: 1.0
Author: LC
DateTime: 2019年2月28日15:55:40
UpdateTime: None
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""
# 客户端
import socket

client = socket.socket()  # 定义协议类型,相当于生命socket类型,同时生成socket连接对象
client.connect(('192.168.0.10', 9999))
while True:
    msg = input(">>>").strip()
    if len(msg) == 0: continue
    client.send(msg.encode("utf-8"))
    data = client.recv(1024)  # 这里是字节1k
    print("recv:>", data.decode())
client.close()
