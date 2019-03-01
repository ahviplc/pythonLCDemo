#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""

ServerApp.py
socketserver服务端
Version: 1.0
Author: LC
DateTime: 2019年2月28日15:55:40
UpdateTime: None
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):  # 所有请求的交互都是在handle里执行的,
        while True:
            try:
                self.data = self.request.recv(1024).strip()  # 每一个请求都会实例化MyTCPHandler(socketserver.BaseRequestHandler):
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)  # print(self.data.decode('ascii'))  # 将bytes变为str 用decode()方法
                self.request.sendall(self.data.upper()+'-LC'.encode('utf-8'))  # sendall是重复调用send.  # '-LC'.encode('utf-8')  # '-LC'.encode('ascii')
            except ConnectionResetError as e:
                print("err ", e)
                break


if __name__ == "__main__":
    HOST, PORT = "192.168.0.10", 9999  # windows
    # HOST, PORT = "0.0.0.0", 9999 #Linux
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)  # 线程
    server.serve_forever()
