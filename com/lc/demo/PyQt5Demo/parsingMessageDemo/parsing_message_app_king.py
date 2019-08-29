# -*- coding: utf-8 -*-

"""

parsing_message_app_king.py
解析报文小工具 for LMT King版本
备注：此版本是具体实现版本,在parsing_message_app.py的基础上
Version: 1.0
Author: LC
DateTime: 2019年8月29日09:26:09
UpdateTime:
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
LC博客url: http://oneplusone.vip/index.html
一加壹.SNS LC - 又一个SNS社区: http://sns.oneplusone.vip
赞助一加壹博客最Top-LC万能收款码支持-支付宝、微信、QQ
http://lc.oneplusone.vip/donateMeByLC.html

"""

# Form implementation generated from reading ui file 'jiexiwo.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

""" 弹出框的demo:
            infoBox = QMessageBox()  ##Message Box that doesn't run
            print("Im here")
            infoBox.setIcon(QMessageBox.Information)
            infoBox.setText("Informações Adicionais")
            infoBox.setInformativeText("Informative Text")
            infoBox.setWindowTitle("Window Title")
            infoBox.setDetailedText("Detailed Text")
            infoBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            infoBox.setEscapeButton(QMessageBox.Close)
            infoBox.exec_()
            
   LC完善版 弹出框demo:
            infoBox = QMessageBox()  ##Message Box that doesn't run
            print("Im here QMessageBox")
            infoBox.setIcon(QMessageBox.Critical)
            infoBox.setText("解析报文为空")
            infoBox.setInformativeText("请输入解析报文,再操作")
            infoBox.setWindowTitle("提示")
            infoBox.setDetailedText("请输入需要解析的报文，不能为空")
            infoBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            infoBox.setEscapeButton(QMessageBox.Close)
            reply = infoBox.exec_()
            print(reply)
            if reply == QtWidgets.QMessageBox.Yes:
                print("yes")
            else:
                print("no")
   
   当前时间:print(str(datetime.datetime.now()))
   
   测试python语句:
        # 测试
        # # 将解析结果写入 textBrowser 文本浏览框
        # self.textBrowser.setPlainText("\n" + str3)
        # for i in range(9000):
        #     self.textBrowser.append("\n" + "append " + str(i))
        # # self.textBrowser.append("\n" + "append2")
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QGridLayout
from print_msg_to_log_model import PrintLogger
import json


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("LMT报文解析小软件")
        Form.resize(1117, 862)
        # textEdit 文本编辑框 QTextEdit
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(70, 40, 541, 181))
        self.textEdit.setObjectName("textEdit")
        # label
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 20, 91, 16))
        self.label.setObjectName("label")
        # textBrowser 文本浏览框 QTextBrowser
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(70, 250, 981, 571))
        self.textBrowser.setObjectName("textBrowser")
        # 设置按钮
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(650, 110, 75, 23))
        self.pushButton.setObjectName("pushButton")
        # 按钮提示
        self.pushButton.setToolTip('点击我，解析报文')
        # 点击鼠标触发事件
        self.pushButton.clicked.connect(self.clickbtn)
        # 文本
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 230, 91, 16))
        self.label_2.setObjectName("label_2")
        # grid

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "LMT报文解析小软件"))
        self.label.setText(_translate("Form", "请输入报文:"))
        self.pushButton.setText(_translate("Form", "解析"))
        self.label_2.setText(_translate("Form", "报文解析结果:"))
        # 新增模拟数据 测试用 正式发布的时候 需要隐掉 谨记
        # self.textEdit.setPlainText("680064304101000003600000006519082902560001004A000360000000652200640100010113080A0800000000030000000200000000012B03DD035E000000002100000000000725000000000000000000000000000000000000000000FD32224D7F6816")

    # parsing_message_for_func_code_3041_demo 功能码 3041 具体解析方法 demo 此为demo 模拟数据版本
    def parsing_message_for_func_code_3041_demo(self, msg):
        # json输出版本
        dict_parsing_message_main_temp = {}  # 报文解析结果 主要字典

        dict_parsing_message_main_temp['功能码'] = 3041
        dict_parsing_message_main_temp['功能码介绍'] = '后付费或预付费后台结算表下主动上报'
        dict_parsing_message_main_temp['通讯类型'] = 'UDP/TCP/CoAP'
        dict_parsing_message_main_temp['功能说明'] = '表具自醒后，主动上报数据，并主动向平台发送从上次上报后到当前的采集记录。每帧发送固定条数数据，分帧发送.'

        # 报文头
        dict_message_head = {}  # 报文头 字典
        dict_message_head['who'] = '报文头'

        dict_message_head['报文长度'] = 128
        dict_message_head['功能码'] = 3041
        dict_message_head['传送方向'] = 3041
        dict_message_head['请求响应标志'] = '00请求'
        dict_message_head['RTU表具编号'] = '00030000000001'

        dict_message_head['报文ID'] = '19080000000348'

        dict_message_head_list = []  # 报文头 列表
        dict_message_head_list.append(dict_message_head)

        dict_parsing_message_main_temp[
            '报文头'] = dict_message_head_list  # 将 报文头 赋给 主字典 dict_parsing_message_main_temp

        # 请求报文数据域定义
        dict_request_message_data = {}  # 请求报文数据域定义 字典
        dict_request_message_data['who'] = '请求报文数据域定义'

        dict_request_message_data['流量计表编号'] = '00030000000001'
        dict_request_message_data['信号强度 '] = '88'
        dict_request_message_data['电源类型'] = '00电池'
        dict_request_message_data['电池电量'] = '99%'
        dict_request_message_data['最后一帧标志'] = '01'

        dict_request_message_data['帧序号'] = '0001'
        dict_request_message_data['本帧明细记录数'] = '03'

        dict_request_message_data_list = []  # 请求报文数据域定义 列表
        dict_request_message_data_list.append(dict_request_message_data)

        dict_parsing_message_main_temp['请求报文数据域定义'] = dict_request_message_data_list  # 将 请求报文数据域定义 赋给 主字典 dict_parsing_message_main_temp

        # 日抄表明细
        dict_daily_transcription = {}  # 日抄表明细 字典 具体每帧的数据用list存放
        dict_daily_transcription['who'] = '日抄表明细'
        dict_daily_transcription['serial_no'] = '1'

        dict_daily_transcription['读数日期'] = '190829'
        dict_daily_transcription['读数时间'] = '1053'
        dict_daily_transcription['累积工况总量'] = '1'
        dict_daily_transcription['累积标况总量'] = '2'
        dict_daily_transcription['标况瞬时流量'] = '3'

        dict_daily_transcription['温度'] = '22'
        dict_daily_transcription['压力'] = '33'
        dict_daily_transcription['阀门状态'] = '00开'
        dict_daily_transcription['工况瞬时流量转换系数'] = '90'
        dict_daily_transcription['状态字'] = '000000000000'

        dict_daily_transcription['工况瞬时流量'] = '11'
        dict_daily_transcription['电池电压'] = '13'
        dict_daily_transcription['预留字节'] = '0000000000000000000000000000000000000000'

        dict_daily_transcription_list = []  # 日抄表明细 列表
        dict_daily_transcription_list.append(dict_daily_transcription)

        dict_request_message_data['日抄表明细'] = dict_daily_transcription_list  # 将 日抄表明细 赋给 主字典 dict_parsing_message_main_temp

        # 密文数据域
        dict_ciphertext_data = {}  # 密文数据域 字典
        dict_ciphertext_data['who'] = '密文数据域'

        dict_ciphertext_data['密钥版本'] = '00'
        dict_ciphertext_data['密文'] = '00000000'

        dict_ciphertext_data_list = []  # 密文数据域 列表
        dict_ciphertext_data_list.append(dict_ciphertext_data)

        dict_parsing_message_main_temp['密文数据域'] = dict_ciphertext_data_list  # 将 密文数据域 赋给 主字典 dict_parsing_message_main_temp

        # 数据转成json 用于输出到textBrowser
        json_dicts = json.dumps(dict_parsing_message_main_temp, indent=4, ensure_ascii=False)

        return json_dicts

    # 解析温度的函数方法
    def translate_temptrue(self, temptrue):
        temptrue_temp = ''
        temptrue_temp = bin(int(temptrue, 16))
        temptrue_temp = '0000000000000000' + str(temptrue_temp)[2:]
        temptrue_temp = temptrue_temp[-16:]
        # print('温度', temptrue_temp)
        if temptrue_temp[0:1] == '1':
            temptrue_temp = "-" + str(int(temptrue_temp[1:], 2)/10)
        else:
            temptrue_temp = str(int(temptrue_temp[1:], 2) / 10)
        return temptrue_temp

    # parsing_message_for_func_code_3041 功能码 3041 具体解析方法
    def parsing_message_for_func_code_3041(self, msg):

        # json输出版本
        dict_parsing_message_main_temp = {}  # 报文解析结果 主要字典

        dict_parsing_message_main_temp['功能码'] = 3041
        dict_parsing_message_main_temp['功能码介绍'] = '后付费或预付费后台结算表下主动上报'
        dict_parsing_message_main_temp['通讯类型'] = 'UDP/TCP/CoAP'
        dict_parsing_message_main_temp['功能说明'] = '表具自醒后，主动上报数据，并主动向平台发送从上次上报后到当前的采集记录。每帧发送固定条数数据，分帧发送.'

        # 报文头
        dict_message_head = {}  # 报文头 字典
        dict_message_head['who'] = '报文头'

        dict_message_head['报文长度'] = str(int(msg[2:6], 16))  # 报文长度 16进制 包含起始符和结束符 这里有16进制转换10进制处理
        dict_message_head['功能码'] = msg[6:10]
        dict_message_head['传送方向'] = msg[10:12]
        dict_message_head['请求响应标志'] = msg[12:14]
        dict_message_head['RTU表具编号'] = msg[14:28]

        dict_message_head['报文ID'] = msg[28:42]

        data_content_length = msg[42:46]  # 此代表报文内容的长度 16进制
        data_content_length_dec = int(msg[42:46], 16)  # 转成10进制 代表n字节 2n字符

        # 报文内容 data_content_msg
        data_content_msg = msg[46: 46 + data_content_length_dec * 2]  # 46 至 46+2n字符 即为 报文内容

        dict_message_head_list = []  # 报文头 列表
        dict_message_head_list.append(dict_message_head)

        dict_parsing_message_main_temp['报文头'] = dict_message_head_list  # 将 报文头 赋给 主字典 dict_parsing_message_main_temp

        # 请求报文数据域定义
        dict_request_message_data = {}  # 请求报文数据域定义 字典
        dict_request_message_data['who'] = '请求报文数据域定义'

        dict_request_message_data['流量计表编号'] = data_content_msg[0:14]
        dict_request_message_data['信号强度 '] = data_content_msg[14:16]
        dict_request_message_data['电源类型'] = data_content_msg[16:18]
        dict_request_message_data['电池电量'] = str(int(data_content_msg[18:20], 16)) + '%'
        dict_request_message_data['最后一帧标志'] = data_content_msg[20:22]

        dict_request_message_data['帧序号'] = data_content_msg[22:26]
        dict_request_message_data['本帧明细记录数'] = data_content_msg[26:28]  # 16进制

        #  本帧明细记录数 16进制转10进制
        serial_count_int = int(data_content_msg[26:28], 16)
        print('本帧明细记录数', serial_count_int)

        # 处理具体帧数据报文
        serial_no_msg = data_content_msg[28: 28 + serial_count_int * 110]  # 乘以110 因为一帧的数据(一帧日抄表明细数据) 为 110字符

        dict_request_message_data_list = []  # 请求报文数据域定义 列表
        dict_request_message_data_list.append(dict_request_message_data)

        dict_parsing_message_main_temp['请求报文数据域定义'] = dict_request_message_data_list  # 将 请求报文数据域定义 赋给 主字典 dict_parsing_message_main_temp

        # 日抄表明细
        dict_daily_transcription_list = []  # 日抄表明细 列表
        # 具体计算解析抄表明细
        for i in range(0, serial_count_int):
            # print(i)

            # 日抄表明细 字典 dict_daily_transcription
            dict_daily_transcription = {}  # 日抄表明细 字典 具体每帧的数据用list存放

            dict_daily_transcription['who'] = '日抄表明细'
            dict_daily_transcription['serial_no'] = i + 1

            dict_daily_transcription['读数日期'] = serial_no_msg[i * 110 + 0:i * 110 + 6]
            dict_daily_transcription['读数时间'] = serial_no_msg[i * 110 + 6: i * 110 + 10]
            dict_daily_transcription['累积工况总量'] = str(int(serial_no_msg[i * 110 + 10: i * 110 + 18], 16)) + ' m³/H' # 此为16进制需要转10机制
            dict_daily_transcription['累积标况总量'] = str(int(serial_no_msg[i * 110 + 18: i * 110 + 26], 16)) + ' m³/H'  # 此为16进制需要转10机制
            dict_daily_transcription['标况瞬时流量'] = str(int(serial_no_msg[i * 110 + 26: i * 110 + 34], 16)/100) + ' m³/H'  # 此为16进制需要转10机制 然后除以100

            dict_daily_transcription['温度'] = self.translate_temptrue(serial_no_msg[i * 110 + 34: i * 110 + 38]) + ' ℃/摄氏度'  # 解析温度 写个解析温度的方法
            dict_daily_transcription['压力'] = str(int(serial_no_msg[i * 110 + 38: i * 110 + 42], 16)/10) + ' KPa' # 此为16进制需要转10机制 然后除以10
            dict_daily_transcription['阀门状态'] = serial_no_msg[i * 110 + 42: i * 110 + 44]  # 1字节 2字符
            # dict_daily_transcription['工况瞬时流量转换系数'] = serial_no_msg[i * 110 + 44: i * 110 + 46]  # 不使用 废弃 1字节 2字符
            dict_daily_transcription['状态字'] = serial_no_msg[i * 110 + 46: i * 110 + 58]  # 6字节 12字符

            dict_daily_transcription['工况瞬时流量'] = str(int(serial_no_msg[i * 110 + 58: i * 110 + 66], 16)/100) + ' m³/H'  # 此为16进制需要转10机制 然后除以100

            battery_voltage_msg = serial_no_msg[i * 110 + 66: i * 110 + 70]  # 电池电压
            dict_daily_transcription['电池电压'] = str(int(battery_voltage_msg[0:2], 16) + int(battery_voltage_msg[2:4], 16) / 100) + ' V'

            dict_daily_transcription['预留字节'] = serial_no_msg[i * 110 + 70: i * 110 + 110]
            # 将当前list append进 dict_daily_transcription_list
            dict_daily_transcription_list.append(dict_daily_transcription)

        dict_request_message_data['日抄表明细'] = dict_daily_transcription_list  # 将 日抄表明细 赋给 主字典 dict_parsing_message_main_temp

        # 密文数据域
        dict_ciphertext_data = {}  # 密文数据域 字典
        dict_ciphertext_data['who'] = '密文数据域'

        dict_ciphertext_data['密钥版本'] = data_content_msg[-10:-8]
        dict_ciphertext_data['密文'] = data_content_msg[-8:]

        dict_ciphertext_data_list = []  # 密文数据域 列表
        dict_ciphertext_data_list.append(dict_ciphertext_data)

        dict_parsing_message_main_temp['密文数据域'] = dict_ciphertext_data_list  # 将 密文数据域 赋给 主字典 dict_parsing_message_main_temp

        # 数据转成json 用于输出到textBrowser
        json_dicts = json.dumps(dict_parsing_message_main_temp, indent=4, ensure_ascii=False)

        return json_dicts

    # 点击鼠标触发函数
    def clickbtn(self):

        # 每一次 执行方法之前 清空 文本浏览框
        self.textBrowser.clear()

        # 打印出输入框的信息
        # print("111")
        # # 从代码中将字符串显示到textEdit：
        # str = '要显示的字符串'
        # self.textEdit.setText(str)
        # # 追加字符串：
        # str1 = '要显示的字符串'
        # self.textEdit_2.append(str1)
        # # 显示数字到textEdit：数字必须要转换成字符串
        # count=10
        # str2=str(count)
        # self.textEdit.setText(str2)
        # # 读取textEdit中的文字：textEdit和LineEdit中的文字读取方法是不一样的

        str3 = self.textEdit.toPlainText()
        print("解析原报文的字符创度为:", len(str3))

        # 判断输入框报文是不是为空
        if len(str3) < 1:
            infoBox = QMessageBox()  # Message Box that doesn't run
            print("Im here QMessageBox - 解析报文不能为空提示 ")
            infoBox.setIcon(QMessageBox.Information)  # 消息对话框，用来告诉用户关于提示信息
            # infoBox.setIcon(QMessageBox.Question)  # 提问对话框，用来告诉用户关于提问消息
            # infoBox.setIcon(QMessageBox.Warning)  # 警告对话框，用来告诉用户关于不寻常的错误消息
            # infoBox.setIcon(QMessageBox.Critical)  #  严重错误对话框，用来告诉用户关于严重的错误消息
            infoBox.setText("解析报文为空")
            infoBox.setInformativeText("请输入解析报文,再操作")
            infoBox.setWindowTitle("提示")
            infoBox.setDetailedText("请输入需要解析的报文，不能为空")
            # infoBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Close | QMessageBox.Cancel)  # 多个按钮
            infoBox.setStandardButtons(QMessageBox.Yes)
            # infoBox.setEscapeButton(QMessageBox.Close)
            reply = infoBox.exec_()
            print("QMessageBox的按钮号码:", reply)
            if reply == QtWidgets.QMessageBox.Yes:
                print("你选择了yes")
            else:
                print("你选择了no")
            print("-------------------------------------------------------------------------------------------------")
            return

        # 开始实际的处理逻辑
        begin_time = datetime.datetime.now()
        # print("-------------------------------------------------------------------------------------------------")
        print("解析开始时间【", begin_time, "】")
        # 用toPlainText()方法
        print("解析原报文为:", str3)

        msg = str3  # 要解析的原报文

        # 开始实际解析逻辑
        # 从msg中拿到功能码FUNC_CODE
        start_character = msg[0:2]  # 头68 起始符
        msg_length = msg[2:6]  # 报文长度 16进制 包含起始符和结束符
        func_code =  msg[6:10]
        print(func_code)
        if func_code == '3041':
            json_dicts = self.parsing_message_for_func_code_3041(msg)
        elif func_code == '3042':
            json_dicts = '3042'
            pass
        elif func_code == '3043':
            json_dicts = '3043'
            pass
        elif func_code == '3044':
            json_dicts = '3044'
            pass
        elif func_code == '3045':
            json_dicts = '3045'
            pass
        elif func_code == '3046':
            json_dicts = '3046'
            pass
        else:
            json_dicts = '不是功能码为【3041 3042 3043 3044 3045 3046】的报文,或者报文格式不正确,请检查后重新输入！'

        # 将json_dicts的结果 赋到 textBrowser
        self.textBrowser.setPlainText(json_dicts)

        print('具体解析内容开始:')
        print(json_dicts)  # 打印输出具体解析内容
        print('具体解析内容结束')
        end_time = datetime.datetime.now()
        print("解析成功,解析结束时间【", end_time, "】")
        print("整个程序运行总时间:", (end_time - begin_time).seconds, "秒")
        print("-------------------------------------------------------------------------------------------------")

    # 以Html的格式输出多行文本框，字体红色，字号6号
    def clickbtn2(self):
        str3 = self.textEdit.toPlainText()
        self.textBrowser.setHtml("<font color='red' size='6'><red>Hello PyQt5 By LC!\n单击按钮。</font>")


if __name__ == "__main__":
    import sys, datetime
    from PyQt5.QtGui import QIcon

    sys.stdout = PrintLogger('parsing_message_app_king.py.log')  # 监听所有的print到log日志 封装类 如不需要打印所有输出print的log日志，隐掉这段即可

    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(widget)
    # widget.setWindowIcon(QtGui.QIcon('pmaLogo.png'))  # 增加icon图标，如果没有图片可以没有这句
    widget.setWindowIcon(QtGui.QIcon('pmaLogoByLC.png'))  # 增加icon图标，如果没有图片可以没有这句 或者使用绝对路径:E:\pycharm-professional-2018.1.3\Code\pythonLCDemo\com\lc\demo\PyQt5Demo\parsingMessageDemo\pmaLogoByLC.png
    widget.show()
    sys.exit(app.exec_())
