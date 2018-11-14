"""
时间客户端

Version: 0.1
Author: LC
DateTime:2018年11月14日16:31:46
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""
from socket import socket


def main():
    client = socket()
    client.connect(('10.7.152.69', 6789))
    print(client.recv(1024).decode('utf-8'))
    client.close()


if __name__ == '__main__':
    main()
