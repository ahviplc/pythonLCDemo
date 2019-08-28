# -*- coding: utf-8 -*-

"""

parsing_message_app.py
解析报文小工具 for lmt
Version: 1.0
Author: LC
DateTime: 2019年8月28日14:05:29
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
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QGridLayout
from print_msg_to_log_model import PrintLogger


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("罗美特报文解析小软件")
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
        Form.setWindowTitle(_translate("Form", "罗美特报文解析小软件"))
        self.label.setText(_translate("Form", "请输入报文:"))
        self.pushButton.setText(_translate("Form", "解析"))
        self.label_2.setText(_translate("Form", "报文解析结果:"))

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
            print("Im here QMessageBox")
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

        # 开始实际解析逻辑
        pass

        # 将解析结果写入 textBrowser 文本浏览框
        self.textBrowser.setPlainText("\n" + str3)
        for i in range(9000):
            self.textBrowser.append("\n" + "append " + str(i))
        # self.textBrowser.append("\n" + "append2")

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

    # sys.stdout = PrintLogger('parsing_message_app.py.log')  # 监听所有的print到log日志 封装类 如不需要打印所有输出print的log日志，隐掉这段即可

    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(widget)
    # widget.setWindowIcon(QtGui.QIcon('pmaLogo.png'))  # 增加icon图标，如果没有图片可以没有这句
    widget.setWindowIcon(QtGui.QIcon('pmaLogoByLC.png'))  # 增加icon图标，如果没有图片可以没有这句 或者使用绝对路径:E:\pycharm-professional-2018.1.3\Code\pythonLCDemo\com\lc\demo\PyQt5Demo\parsingMessageDemo\pmaLogoByLC.png
    widget.show()
    sys.exit(app.exec_())
