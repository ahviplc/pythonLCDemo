"""
chat 客户端

Version: 0.1
Author: LC
DateTime:2018年11月14日16:18:38
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

from socket import socket
from threading import Thread


def main():

    class RefreshScreenThread(Thread):

        def __init__(self, client):
            super().__init__()
            self._client = client

        def run(self):
            while running:
                data = self._client.recv(1024)
                print(data.decode('utf-8'))

    nickname = input('请输入你的昵称: ')
    myclient = socket()
    myclient.connect(('192.168.0.4', 12345))
    running = True
    RefreshScreenThread(myclient).start()
    while running:
        content = input('请发言: ')
        if content == 'byebye':
            myclient.send(content.encode('utf-8'))
            running = False
        else:
            msg = nickname + ': ' + content
            myclient.send(msg.encode('utf-8'))


if __name__ == '__main__':
    main()
