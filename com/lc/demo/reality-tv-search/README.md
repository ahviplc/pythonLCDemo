# reality-tv-search

> 真人秀视频搜索系统

> 爬虫视频,视频搜索,视频播放

## 安装依赖

`使用阿里镜像源 安装更快`

> pip install beautifulsoup4 -i https://mirrors.aliyun.com/pypi/simple/
> pip install pony -i https://mirrors.aliyun.com/pypi/simple/
> pip install PyMySQL -i https://mirrors.aliyun.com/pypi/simple/
> pip install ffmpy -i https://mirrors.aliyun.com/pypi/simple/

`使用requirements.txt安装类库 进行一次性安装`

> pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

## 配置好db

`reality-tv-search-py/db/db.py:6 配置好你自己的mysql连接`

## py脚本运行

> python main.py

## Links

```markdown
mysql

PyMySQL · PyPI
https://pypi.org/project/PyMySQL/

GitHub - PyMySQL/PyMySQL: Pure Python MySQL Client
https://github.com/PyMySQL/PyMySQL

Welcome to PyMySQL’s documentation! — PyMySQL 0.7.2 documentation
https://pymysql.readthedocs.io/en/latest/

PonyORM - Python ORM with beautiful query syntax
https://ponyorm.org/

API Reference — Pony ORM documentation
https://docs.ponyorm.org/api_reference.html

Beautiful Soup 中文文档
https://beautifulsoup.cn/

获取Bilibili视频直链并挂载至网站 - 腾讯云开发者社区-腾讯云
https://cloud.tencent.com/developer/article/1961851

GitHub - ahviplc/BotMan at BotMan-MySQL
https://github.com/ahviplc/BotMan/tree/BotMan-MySQL

Bilibili 网页版下载视频 B站下载MP4格式视频（不用下载工具）_Yian@的博客-CSDN博客_bilibili视频下载
https://blog.csdn.net/yanhaohui/article/details/128900538

哔哩哔哩(bilibili)视频解析下载 - 保存B站视频到手机、电脑
https://bilibili.iiilab.com/

B站视频在线解析提取下载工具 - 哔哩哔哩(bilibili)视频下载到手机相册、电脑本地
https://www.fodownloader.com/

03-requests模块携带UA请求头，携带参数，携带cookie，持久化存储_gemoumou的博客-CSDN博客_request ua
https://blog.csdn.net/qq_37978800/article/details/108110021

Pony ORM - 有着优美的查询语法的Python ORM - 简书
https://www.jianshu.com/p/8a6bd1d690c6

python可用ORM之Pony - 村口王铁匠 - 博客园
https://www.cnblogs.com/liao-lin/p/8433785.html

GitHub - niyuancheng/bilibili-service: 提供B站的弹幕和视频下载服务，只需输入B站视频的bvid即可获取下载超清以上的高画质视频和弹幕池信息！！！
https://github.com/niyuancheng/bilibili-service

GitHub - ahviplc/BotMan at BotMan-MySQL 端口9528
https://github.com/ahviplc/BotMan/tree/BotMan-MySQL

ffmpeg-python: Python bindings for FFmpeg — ffmpeg-python documentation
https://kkroening.github.io/ffmpeg-python/

GitHub - kkroening/ffmpeg-python: Python bindings for FFmpeg - with complex filtering support
https://github.com/kkroening/ffmpeg-python

python-ffmpeg
https://python-ffmpeg.readthedocs.io/en/latest/

GitHub - jonghwanhyeon/python-ffmpeg: A python binding for FFmpeg which provides sync and async APIs
https://github.com/jonghwanhyeon/python-ffmpeg

GitHub - jiashaokun/ffmpeg: 基于FFmpeg的python视频处理包-因疫情影响，工作比较繁忙，心情也没在视频上面再研究，该项目已经搁置，源码很简单，大家可以自己研究一下自己扩展
https://github.com/jiashaokun/ffmpeg

python 使用 ffmpeg 合并音频+视频_YUAYU-的博客-CSDN博客
https://blog.csdn.net/weixin_43835542/article/details/109493050
# 这是 ffmpeg 合并音频+视频的cmd写法
【ffmpeg -i {mp4_file} -i {mp3_file} -acodec copy -vcodec copy {outfile_name}】

* 使用的是这个 确定了
GitHub - Ch00k/ffmpy: Pythonic interface for FFmpeg/FFprobe command line
https://github.com/Ch00k/ffmpy

ffmpy · PyPI
https://pypi.org/project/ffmpy/

* 此教程使用【https://github.com/Ch00k/ffmpy】
使用Python+FFMPEG实现视频分割与合并 - 程序设计实验室 - 博客园
https://www.cnblogs.com/deali/p/14584495.html

# 这是使用 ffmpy 代码拼接成的合并音频+视频的cmd写法
【ffmpeg -i ./public/BV1vo4y1e75J.mp4 -i ./public/BV1vo4y1e75J.mp3 -vcodec copy -acodec copy ./public/BV1vo4y1e75J-new.mp4】

【Python】ffmpeg的安装配置和python中使用ffmpy（保姆级图文）_发现你走远了的博客-CSDN博客
https://blog.csdn.net/u011027547/article/details/122490254

FFmpeg
https://ffmpeg.org/

Builds - CODEX FFMPEG @ gyan.dev
https://www.gyan.dev/ffmpeg/builds/

Releases · BtbN/FFmpeg-Builds | 下载FFmpeg win | 可用 将此bin目录设置到系统环境变量
https://github.com/BtbN/FFmpeg-Builds/releases

static FFmpeg binaries for macOS 64-bit | 下载FFmpeg mac
https://evermeet.cx/ffmpeg/
```

## 小技巧

https://www.bilibili.com/video/BV16o4y1i71r?from=search
获取相关哔哩哔哩视频信息接口

> https://api.bilibili.com/x/web-interface/view?bvid=BV16o4y1i71r

封面 pic | http://i0.hdslb.com/bfs/archive/c1c10a9e987c8ff7c6fe7fad79ca998dd4befd65.jpg
标题 title | 这部综艺就是陈学冬的历劫记吧，狂热男粉非要和他共睡一间房
时长 duration | 162

> 使用b站官方接口获取视频流地址
> https://github.com/niyuancheng/bilibili-service
> https://github.com/niyuancheng/bilibili-service/blob/master/index.js
> https://github.com/niyuancheng/bilibili-service/blob/master/parseDash.js
> https://github.com/niyuancheng/bilibili-service/blob/master/spider.py

```markdown
1. 根据bvid获取cvid【cvid其实就是cid】
   `https://api.bilibili.com/x/player/pagelist?bvid=${bvid}`
   https://api.bilibili.com/x/player/pagelist?bvid=BV1qj411N7iS
2. 根据bvid,cvid请求avid【avid其实就是aid】
   `https://api.bilibili.com/x/web-interface/view?cid=${cvid}&bvid=${bvid}`
   https://api.bilibili.com/x/web-interface/view?cid=1011588705&bvid=BV1qj411N7iS
3. 根据cvid请求弹幕池文件
   `https://api.bilibili.com/x/v1/dm/list.so?oid=${cvid}`
4. 根据avid,cvid请求视频流文件
   `https://api.bilibili.com/x/player/playurl?fnval=80&avid=${avid}&cid=${cvid}`
   https://api.bilibili.com/x/player/playurl?fnval=80&avid=436920621&cid=1011588705

针对BV1qj411N7iS这个bvid来说
其实 `https://api.bilibili.com/x/web-interface/view?bvid=BV1qj411N7iS` 一下子可以获取cid aid啊
bvid=BV1qj411N7iS
cid=1011588705
aid=436920621
可以的
```

> 此可以获得真实视频地址 这个不好使
https://www.fodownloader.com/csgeturl?urlInfo=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV16o4y1i71r&lang=zh-cn

`BV1UM4y1S79c`

> https://upos-sz-mirrorali.bilivideo.com/upgcxcode/52/27/1010482752/1010482752-1-208.mp4?e=ig8euxZM2rNcNbhz7WdVhwdlhzhBhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&nbs=1&deadline=1676549070&gen=playurlv2&os=alibv&oi=795565499&trid=b627e97d98c14a2591030ba772899afbT&mid=538947867&platform=html5&upsig=8ca6ffa6f317dc6d0a0a115dd14892b0&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&bw=335906&orderid=0,1&logo=80000000

## MySQL数据脚本

数据库设计

id B站视频AV/BV号 视频标题 视频播放url  简介 观看量 弹幕数量 上传时间 上传up主昵称 封面图片 真实播放地址 时长 视频分类

字段说明
视频分类 all 代表综合排序 | click代表最多点击 | pubdate代表最新发布|dm代表最多弹幕|stow代表最多收藏

`docs/sql/reality-tv-search.sql`

