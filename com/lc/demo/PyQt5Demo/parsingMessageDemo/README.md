### parsing_message_app.py By LC

报文解析小软件, 小工具

程序员之路：python3+PyQt5+pycharm桌面GUI开发 - 莫水千流 - 博客园 - 我就是按照这个配置pycharm的 - 图片失效

> https://www.cnblogs.com/zhoug2020/p/9039993.html

这个配置介绍的图片未失效-可以的-【和com/lc/demo/PyQt5Demo/parsingMessageDemo/uiKu/README.md中介绍的配置路径一样的 和上面失效的也是一样的】

Pycharm+Python+PyQt5使用 - 大蓝鲸 - 博客园
> https://www.cnblogs.com/dalanjing/p/6978373.html

【 分类 】- PyQt5基本窗口控件 - jia666666的博客 - CSDN博客 - 点我学习吧

> https://blog.csdn.net/jia666666/article/category/7916211

### 使用步骤

> python parsing_message_app.py

启动即可

### 打包 打包成二进制文件 可执行文件exe

pycharm如何将python文件打包为exe格式 - CSDN博客

> https://blog.csdn.net/qq1877383144/article/details/81200471

```
" pyinstaller -F -w *.py " 就可以制作出exe。生成的文件放在同目录dist下。

    -F（注意大写）是所有库文件打包成一个exe，-w是不出黑色控制台窗口。

    不加-F参数生成一堆文件，但运行快。压缩后比单个exe文件还小一点点。

    加-F参数生成一个exe文件，运行起来慢。
```

☆打包成exe命令如下:

> pyinstaller -F parsing_message_app.py

> Pyinstaller --version

> pyinstaller --version

> pyinstaller -F -w parsing_message_app_king.py

注意:打开cmd或者powershell

> PS E:\pycharm-professional-2018.1.3\Code\pythonLCDemo\com\lc\demo\PyQt5Demo\parsingMessageDemo> pyinstaller -F -w parsin
g_message_app.py

大小写都可以！

☆打包成dmg(For MacOS)命令如下: 
 
```
1、安装py2app，打开终端，执行

pip install py2app

2、在桌面新建一个文件夹，取名xxx，打包的程序dmgAppByLC.py放在里面

3、进入终端，切路径至该文件夹下，执行

py2applet --make-setup dmgAppByLC.py

4、开始打包应用，执行

python setup.py py2app

5、xxx文件下出现dist文件夹，打开后里面有个app，在MacOS下双击即可运行

```
### copy from:

py2app - Create standalone Mac OS X applications with Python — py2app 0.19 documentation
> https://py2app.readthedocs.io/en/latest/

使用 py2app 把 python 项目打包成mac下可执行的应用 - 服务器端攻城师 - CSDN博客
> https://blog.csdn.net/marujunyy/article/details/8988974

Mac系统下将python程序打包成mac应用程序 - 简书
> https://www.jianshu.com/p/75da02dfa1a3

**欢迎来到 [LC博客-一加壹博客最Top](http://www.oneplusone.vip)**

**欢迎来到 [LC-Gitlab](https://gitlab.com/ahviplc)**

**欢迎来到 [LC-Github](https://github.com/ahviplc)**

**欢迎来到 [LC-Github-pythonLCDemo](https://github.com/ahviplc/pythonLCDemo)**

> ### LC最寄语：永远不要放弃自己心中最初的最初的理想！~LC

> from **2019年8月28日16:28:33**

> to **future**
