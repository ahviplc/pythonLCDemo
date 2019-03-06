#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""

GPRSServerPyVersion2.py
socketserver服务端-GPRSServerPyVersion2.py-远传协议-##2G远传
高级版本-真正逻辑集成
Version: 1.0
Author: LC
DateTime: 2019年3月1日14:37:03
UpdateTime: None
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

import socketserver
import time
import datetime


class MyTCPHandler(socketserver.BaseRequestHandler):  # 必须继承这个类才能实现并发

    def setup(self):
        print("before handle,连接建立：", self.client_address)

    def handle(self):  # 所有请求的交互都是在handle里执行的,每个链接建立后都会自动执行该方法
        conn = self.request  # 这个是每个客户端的链接
        conn.sendall(bytes('conn ok', encoding='utf-8'))  # conn.sendall('conn ok'.encode('utf-8'))
        while True:
            time_std = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()));  # 2019-03-01 14:32:40
            try:
                self.data = self.request.recv(1024).strip()  # 每一个请求都会实例化MyTCPHandler(socketserver.BaseRequestHandler):
                print("[{}]-[{}]-wrote:".format(time_std, self.client_address[0]))
                if not self.data:
                    print("connection lost")
                    # break
                # print(self.data)  # b'1' print(self.data.decode('ascii'))  # 将bytes变为str 用decode()方法
                # b'}1helloworld1LC'
                # 集体核心逻辑代码
                result_str_list = bytes_to_hex_string_return_list(self.data)  # 把byte[]转换成16进制字符串列表输出
                result_str = "".join(result_str_list)
                print("从连接号：", self.client_address, "接收原报文：" + result_str)

                result_str_translate_list = translate_7d_string(result_str_list);  # 翻译成正常报文，去除7D部分
                result_str_translate = "".join(result_str_translate_list)
                print("从连接号：", self.client_address, "接收翻译后报文：" + result_str_translate)

                receive_msg = message_read_to_msg(result_str_translate_list);  # 报文message转换成msg实体类

                if receive_msg is None:
                    #  无效数据，记录错误日志后不返回设备报文
                    pass
                else:
                    dw_conn_id = self.client_address[1]

                    # 根据msg的数据命令，选择不同的处理方法
                    send_str = deal_operation_by_msg(receive_msg, dw_conn_id, result_str_translate)

                    if send_str is not None:
                        print('do something')
                        send_bytes = send_str.encode('utf-8')
                        print(send_bytes)
                        # 接下來send回去-给客户端反馈消息(反馈报文)
                        pass
                    pass

                # 集体核心逻辑代码
                self.request.sendall(result_str_translate.encode('utf-8') + '-LC'.encode('utf-8'))  # sendall是重复调用send.  # '-LC'.encode('utf-8')  # '-LC'.encode('ascii')
                # self.request.sendall(self.data.upper() + '-LC'.encode('utf-8'))
            except Exception as e:  # ConnectionError[ConnectionResetError,ConnectionAbortedError]
                print(self.client_address, "连接断开-err:", e)
                break
            finally:
                pass
                # self.request.close()

    def finish(self):
        print("finish run after handle")


# 数据帧格式类
class Msg:
    SHOW_MSG = True

    # 数据帧格式类-具体字段定义-首先定义变量-给初始值
    startCharacter = ""  # 起始符，其值固定为68H
    RTUA = ""  # 终端逻辑地址，rtu通讯编号
    MSTAAndSEQ = ""  # 主站地址与命令序号
    startCharacter2 = ""  # 起始符2，其值固定为68H
    controllerCode = ""  # 控制码

    systemType = ""  # 系统类型
    elementType = ""  # 设备类型
    dataLength = ""  # 数据长度
    dataCommand = ""  # 数据命令 ❤
    data = ""  # 数据域

    checkCode = ""  # 校验码
    endCharacter = ""  # 结束码，其值固定为16H

    def __init__(self, startCharacter=startCharacter, RTUA=RTUA, MSTAAndSEQ=MSTAAndSEQ, startCharacter2=startCharacter2,
                 controllerCode=controllerCode, systemType=systemType, elementType=elementType,
                 dataLength=dataLength, dataCommand=dataCommand, data=data, checkCode=checkCode,
                 endCharacter=endCharacter):
        self.startCharacter = startCharacter  # 起始符，其值固定为68H
        self.RTUA = RTUA  # 终端逻辑地址，rtu通讯编号
        self.MSTAAndSEQ = MSTAAndSEQ  # 主站地址与命令序号
        self.startCharacter2 = startCharacter2  # 起始符2，其值固定为68H
        self.controllerCode = controllerCode  # 控制码

        self.systemType = systemType  # 系统类型
        self.elementType = elementType  # 设备类型
        self.dataLength = dataLength  # 数据长度
        self.dataCommand = dataCommand  # 数据命令 ❤
        self.data = data  # 数据域

        self.checkCode = checkCode  # 校验码
        self.endCharacter = endCharacter  # 结束码，其值固定为16H

    # 方法
    def get_method(self):
        try:
            res = "LC" + self.startCharacter
            print(res)
            return res
            pass
        except Exception as e:
            print('Exception Error:{}'.format(e))
        finally:
            pass


# 公共方法

# 把byte[]转换成16进制字符串-这里我们可以将byte通过int()转换成int，然后利用hex()来转换成16进制字符串
# @param bytes_data 输入:b'1helloworld1LC}'
# @return 输出:3168656c6c6f776f726c64314c437d
def bytes_to_hex_string(bytes_data):
    if not bytes_data:
        return None
    bits = ""
    l = [hex(int(i)) for i in bytes_data]
    ll = [i[2:] for i in l]  # 切片处理，去掉0x
    bits = "".join(ll)
    return bits


# 把byte[]转换成16进制字符串列表输出-这里我们可以将byte通过int()转换成int，然后利用hex()来转换成16进制字符串
# @param bytes_data 输入:b'1helloworld1LC}'
# @return 输出:['7d', '31', '68', '65', '6c', '6c', '6f', '77', '6f', '72', '6c', '64', '31', '4c', '43']
def bytes_to_hex_string_return_list(bytes_data):
    if not bytes_data:
        return None
    l = [hex(int(i)) for i in bytes_data]
    ll = [i[2:] for i in l]  # 切片处理，去掉0x
    return ll


# 接收可能含有7D数据的报文进行翻译,翻译成正常报文 - ''.join(real_return_list)
# @param return_list 可能包含7D的数据 列表
# @return real_return_list 翻译结果字符串 列表
def translate_7d_string(return_list):
    real_return_list = []
    for i in range(len(return_list)):
        if (return_list[i] == "7d" or return_list[i] == "7D"):
            if return_list[i + 1] != None:
                result = int(return_list[i + 1], 16) ^ 0x20
                result_str = hex(result)[2:]
                real_return_list.append(result_str)
                del return_list[i]
                return_list.append(None)
                pass
            else:
                pass
        else:
            result = return_list[i]
            if result == None:
                pass
            else:
                real_return_list.append(result)
    if real_return_list[0] == "68" and real_return_list[1] == "68":
        del real_return_list[1]  # 删除索引(下标)为1的列表元素
    return real_return_list


# 报文message转换成msg实体类-从原始报文读取到Msg实体类中(未做任何处理，具体处理方法另外调用)
# @param result_str_translate_list 列表 -socket获取的直接报文
# @return Msg对象
def message_read_to_msg(result_str_translate_list):  # 转换成msg实体类
    msg = Msg()

    # 将socket获取的直接报文 list 转成字符串
    result_str_translate_msg = "".join(result_str_translate_list)
    print(len(result_str_translate_msg))

    if len(result_str_translate_msg) < 32 or len(result_str_translate_msg) % 2 == 1:
        return None

    if result_str_translate_list[0] == "68" and result_str_translate_list[1] == "68":
        del result_str_translate_list[1]  # 删除索引(下标)为1的列表元素


    # 将报文具体解析写入报文类Msg
    print(result_str_translate_list[0])
    msg.startCharacter = result_str_translate_list[0]

    print(result_str_translate_list[1:6])  # -['68', '65', '6c', '6c', '6f']
    msg.RTUA = "".join(result_str_translate_list[1:6])  # 将列表list拼接成字符串-'68656c6c6f'

    print(result_str_translate_list[6:8])  # -
    msg.MSTAAndSEQ = "".join(result_str_translate_list[6:8])

    print(result_str_translate_list[8])
    msg.startCharacter2 = result_str_translate_list[8]

    print(result_str_translate_list[9])
    msg.controllerCode = result_str_translate_list[9]

    print(result_str_translate_list[10])
    msg.systemType = result_str_translate_list[10]

    print(result_str_translate_list[11])
    msg.elementType = result_str_translate_list[11]

    print(result_str_translate_list[12:14])
    msg.dataLength = "".join(result_str_translate_list[12:14])

    print(result_str_translate_list[14:16])
    msg.dataCommand = "".join(result_str_translate_list[14:16])

    print(result_str_translate_list[16:-2])
    msg.data = "".join(result_str_translate_list[16:-2])

    print(result_str_translate_list[-2])
    msg.checkCode = result_str_translate_list[-2]

    print(result_str_translate_list[-1])
    msg.endCharacter = result_str_translate_list[-1]

    if msg.startCharacter != "68" or msg.endCharacter != "16":
        return None

    return msg


# 根据msg的数据命令，选择不同的处理方法
# @param msg
# @return send_str
def deal_operation_by_msg(receive_msg, dw_conn_id, result_str_translate):
    # 使用if else判断具体命令 然后进行不同的处理
    pass
    send_str = '123lclclc123'
    return send_str


# main方法
def main():
    HOST, PORT = "192.168.0.10", 10010  # windows
    # HOST, PORT = "0.0.0.0", 10010 #Linux
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)  # 线程
    server.serve_forever()


if __name__ == "__main__":
    main()
    # msg = Msg()
    # msg.get_method()

    # s = "}1helloworld1LC"
    #
    # sb = bytes(s, encoding="utf8")
    # print(sb)
    # print(bytes_to_hex_string(sb))
    # # 0x7D 0x31 0x68 0x65 0x6c 0x6c 0x6f 0x77 0x6f 0x72 0x6c 0x64 0x31 0x4c 0x43
    # # 7d3168656c6c6f776f726c64314c43
    # print(int(49 ^ 0x20))
    # print(hex(17)[2:])
    # print(str(17))
    # print(int('31', 16))
    # print(translate_7d_string(['7d', '31', '7d', '68', '7d', '65', '6c', '6c', '6f', '77', '6f', '72', '6c', '64', '31', '4c', '43', '7d']))
