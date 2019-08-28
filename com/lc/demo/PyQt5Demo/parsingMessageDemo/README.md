### parsing_message_app.py By LC

报文解析小软件, 小工具

程序员之路：python3+PyQt5+pycharm桌面GUI开发 - 莫水千流 - 博客园 - 我就是按照这个配置pycharm的

> https://www.cnblogs.com/zhoug2020/p/9039993.html

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

打包成exe命令如下:

> pyinstaller -F parsing_message_app.py

> Pyinstaller --version

> pyinstaller --version

注意:打开cmd或者powershell

> PS E:\pycharm-professional-2018.1.3\Code\pythonLCDemo\com\lc\demo\PyQt5Demo\parsingMessageDemo> pyinstaller -F -w parsin
g_message_app.py

大小写都可以！

**欢迎来到 [LC博客-一加壹博客最Top](http://www.oneplusone.vip)**

**欢迎来到 [LC-Gitlab](https://gitlab.com/ahviplc)**

**欢迎来到 [LC-Github](https://github.com/ahviplc)**

**欢迎来到 [LC-Github-pythonLCDemo](https://github.com/ahviplc/pythonLCDemo)**

> ### LC最寄语：永远不要放弃自己心中最初的最初的理想！~LC

> from **2019年8月28日16:28:33**

> to **future**