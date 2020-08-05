# python3+PyQt5+pycharm桌面GUI开发

###### 如何生成使用ui？

###### 如何玩转PyQt5(其控件等)?

程序员之路：python3+PyQt5+pycharm桌面GUI开发 - 莫水千流 - 博客园 - 我就是按照这个配置pycharm的 废弃 图片已失效

> https://www.cnblogs.com/zhoug2020/p/9039993.html

Python3+PyQt5+PyCharm 桌面GUI开发环境搭建 - 整合侠 - 博客园 可以的
> https://www.cnblogs.com/lizm166/p/10286555.html

【 分类 】- PyQt5基本窗口控件 - jia666666的博客 - CSDN博客 - 点我学习吧

> https://blog.csdn.net/jia666666/article/category/7916211

## 安装所需库

推荐使用pip安装：

> pip install PyQt5

> pip install PyQt5-tools

## 配置PyCharm
 
打开Pycharm，然后按照下面路径打开Extrernal Tools：

> File->Tools->Extrernal Tools->点击“+”号->弹出对话框，配置如下：

(1).增加QT设计界面“Qt Designer” — 这个就是设计Qt界面的工具 - 这步也就是为了可以快速打开

Program选择PyQt安装目录中 designer.exe 的路径 注意：designer.exe 并不在PyQt5-tools根目录

> E:\pycharm-professional-2018.1.3\Code\pythonLCDemo\venv\Scripts\designer.exe

Work directory 使用变量 $ProjectFileDir$ （点击后面的…）

> $ProjectFileDir$

(2).增加“PyUIC” — 这个主要是用来将 Qt界面 转换成 py代码 .ui -> .py

Program选择 python.exe

> E:\pycharm-professional-2018.1.3\Code\pythonLCDemo\venv\Scripts\python.exe

Arguments设置为 -m PyQt5.uic.pyuic  $FileName$ -o $FileNameWithoutExtension$.py

> -m PyQt5.uic.pyuic  $FileName$ -o $FileNameWithoutExtension$.py

Work directory 设置为 $ProjectFileDir$ （点击后面的…）

> $ProjectFileDir$

点击Apply应用即可 已测试 可以的

#### 备注:配置图片在com/lc/demo/PyQt5Demo/parsingMessageDemo/uiKu文件夹中

## 具体使用步骤

备注:在PyCharm中操作

1:右键点击一下 External Tools->Qt Designer

2:打开之后 尽情的拖拽控件 完成之后 生成*.ui文件

3:生成ui文件之后,选中jiexiwo.ui,右键点击一下

4:选择External Tools->PyUIC

其实PyUIC也就是执行下面指令
> python -m PyQt5.uic.pyuic jiexiwo.ui -o jiexiwo.py

5:就可以将jiexiwo.ui生成jiexiwo.py文件

6:在py文件中 直接添加如下代码即可运行

```
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
```