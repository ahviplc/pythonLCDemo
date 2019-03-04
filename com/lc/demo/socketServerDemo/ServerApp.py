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


class MyTCPHandler(socketserver.BaseRequestHandler):  # 必须继承这个类才能实现并发

    def setup(self):
        print("before handle,连接建立：", self.client_address)

    def handle(self):  # 所有请求的交互都是在handle里执行的,每个链接建立后都会自动执行该方法
        conn = self.request  # 这个是每个客户端的链接
        conn.sendall(bytes('conn ok', encoding='utf-8'))  # conn.sendall('conn ok'.encode('utf-8'))
        while True:
            try:
                self.data = self.request.recv(1024).strip()  # 每一个请求都会实例化MyTCPHandler(socketserver.BaseRequestHandler):
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)  # print(self.data.decode('ascii'))  # 将bytes变为str 用decode()方法
                self.request.sendall(self.data.upper()+'-LC'.encode('utf-8'))  # sendall是重复调用send.  # '-LC'.encode('utf-8')  # '-LC'.encode('ascii')
            except Exception as e:  # ConnectionError[ConnectionResetError,ConnectionAbortedError]
                print(self.client_address, "连接断开-err:", e)
                break
            finally:
                pass
                # self.request.close()

            # except ConnectionResetError as e:
            #     print("err ", e)
            #     break

    def finish(self):
        print("finish run after handle")


if __name__ == "__main__":
    HOST, PORT = "192.168.0.10", 9999  # windows
    # HOST, PORT = "0.0.0.0", 9999 #Linux
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)  # 线程
    server.serve_forever()
