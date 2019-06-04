#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
WechatFriendsPicsMergeApp.py
获取微信好友头像并且拼接成大图
Version: 1.0
Author: LC
DateTime: 2019年6月4日14:50:14
UpdateTime:
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
LC博客url: http://oneplusone.vip/index.html
一加壹.SNS LC - 又一个SNS社区: http://sns.oneplusone.vip
赞助一加壹博客最Top-LC万能收款码支持-支付宝、微信、QQ
http://lc.oneplusone.vip/donateMeByLC.html

"""

import itchat
from PIL import Image
import os
import math
import json
import time
import uuid


# 下载好友头像
def download_images(frined_list):
    image_dir = "./images/"
    uuid_temp = get_uuid()
    num = 1
    for friend in frined_list:
        print(str(friend["PYQuanPin"]))
        image_name = str(num) + '-' + uuid_temp + '.jpg'
        num += 1
        img = itchat.get_head_img(userName=friend["UserName"])
        with open(image_dir + image_name, 'wb') as file:
            file.write(img)


# 合并所有好友头像
# path为存储头像图像的文件夹相对于当前路径的相对路径，这里应该为'images/'
def merge_images(path):
    print("Merging head images......")

    # 设置每个图片需要缩放到的大小
    photo_width = 200
    photo_height = 200

    # 保存所有本地图片的绝对地址
    photo_list = []
    # 头像图片文件夹的绝对路径
    dirName = os.getcwd() + path

    # os.walk用来遍历某一个文件夹下的所有文件夹和文件，递归便利，os是python自带库
    # 具体参数用法参考python手册
    for root, dirs, files in os.walk(dirName):
        for file in files:
            # 遍历所有文件，如果文件名包含jpg则获取该文件绝对路径添加到photo_list
            # os.path.join(root, file)拼接为这个文件的绝对路径
            if "jpg" in file and os.path.getsize(os.path.join(root, file)) > 0:
                photo_list.append(os.path.join(root, file))

    pic_num = len(photo_list)
    # 合并图片的列数
    line_max = int(math.sqrt(pic_num))
    # 合并图片的行数
    row_max = int(math.sqrt(pic_num))
    print(line_max, row_max, pic_num)

    # 如果好友太多行数大于20行则限制为20行
    if line_max > 20:
        line_max = 20
        row_max = 20

    num = 0
    # 需要合并的图片总数
    pic_max = line_max * row_max

    # 新建底图，长款为行数*200px,列数*200px
    toImage = Image.new('RGBA', (photo_width * line_max, photo_height * row_max))

    # 循环粘贴每一个头像图片
    for i in range(0, row_max):
        for j in range(0, line_max):
            # 读取对应的头像图片
            pic_fole_head = Image.open(photo_list[num])
            # 把图片伸缩到设置的大小（200px*200px）
            tmppic = pic_fole_head.resize((photo_width, photo_height))
            # 计算图片粘贴的位置
            loc = (int(j % row_max * photo_width), int(i % row_max * photo_height))
            # 把头像图片粘贴到底图对应位置
            toImage.paste(tmppic, loc)
            num = num + 1
            if num >= len(photo_list):
                break
        if num >= pic_max:
            break
    print(toImage.size)
    # 保存图片
    time_str = str(int(time.time()))
    print(time_str)  # 当前时间戳
    toImage.save(time_str + '_merged.png')


# 配置了这个,用其他微信给本登录的微信发文本消息，就可以获取微信消息
# Start auto replying.
# 你好
@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])


# 获取uuid
def get_uuid():
    uid = str(uuid.uuid4())
    suid = ''.join(uid.split('-'))
    return suid


if __name__ == '__main__':
    # 为了让实验过程更加方便（修改程序不用多次扫码），我们使用热启动 --> hotReload=True
    itchat.auto_login()

    friends = itchat.get_friends(update=True)  # 获取好友信息

    bJson = json.dumps(friends, ensure_ascii=False)  # 中文字符的时候，需要指定ensure_ascii=False
    print(bJson)

    download_images(friends)
    merge_images('/images/')

    # itchat.send('Hello, filehelper', toUserName='filehelper') # can run

    # itchat.send(msg='Message Content:Hello LC',toUserName='@741ad17e49964e03dca0e37e117eb87f')  # can run --> ahviplc 'UserName' key of friend dict :@741ad17e49964e03dca0e37e117eb87f

itchat.run()

# 退出程序后暂存登陆状态
# 通过如下命令登陆，即使程序关闭，一定时间内重新开启也可以不用重新扫码。
# itchat.auto_login(hotReload=True)
