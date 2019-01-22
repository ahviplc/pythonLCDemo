#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
get_lyric.py
Python爬虫获取网易云歌曲歌词的
Version: 1.0
Author: LC
DateTime: 2019年1月22日13:13:41
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""

import requests
import math
import random
from Crypto.Cipher import AES  # pycrypto->pip install pycrypto-安装步骤看note.txt
import codecs
import base64


# 生成16个随机字符
def generate_random_strs(length):
    string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    # 控制次数参数i
    i = 0
    # 初始化随机字符串
    random_strs = ""
    while i < length:
        e = random.random() * len(string)
        # 向下取整
        e = math.floor(e)
        random_strs = random_strs + list(string)[e]
        i = i + 1
    return random_strs


# AES加密
def AESencrypt(msg, key):
    # 如果不是16的倍数则进行填充(paddiing)
    padding = 16 - len(msg) % 16
    # 这里使用padding对应的单字符进行填充
    msg = msg + padding * chr(padding)
    # 用来加密或者解密的初始向量(必须是16位)
    iv = '0102030405060708'

    cipher = AES.new(key, AES.MODE_CBC, iv)
    # 加密后得到的是bytes类型的数据
    encryptedbytes = cipher.encrypt(msg)
    # 使用Base64进行编码,返回byte字符串
    encodestrs = base64.b64encode(encryptedbytes)
    # 对byte字符串按utf-8进行解码
    enctext = encodestrs.decode('utf-8')

    return enctext


# RSA加密
def RSAencrypt(randomstrs, key, f):
    # 随机字符串逆序排列
    string = randomstrs[::-1]
    # 将随机字符串转换成byte类型数据
    text = bytes(string, 'utf-8')
    seckey = int(codecs.encode(text, encoding='hex'), 16) ** int(key, 16) % int(f, 16)
    return format(seckey, 'x').zfill(256)


# 获取参数
def get_params(songid):
    # id为歌曲的id号,后面的lv和tv都是固定值
    msg = '{id: ' + str(songid) + ', lv: -1, tv: -1}'
    key = '0CoJUm6Qyw8W8jud'
    f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    e = '010001'
    enctext = AESencrypt(msg, key)
    # 生成长度为16的随机字符串
    i = generate_random_strs(16)

    # 两次AES加密之后得到params的值
    encText = AESencrypt(enctext, i)
    # RSA加密之后得到encSecKey的值
    encSecKey = RSAencrypt(i, e, f)
    return encText, encSecKey


def main():
    # Dream it possible
    # 歌曲id号
    songid = 38592976
    # params的长度为108,不要拿浏览器控制面板中的数据进行测试,那里的params长度为128,不符合
    params, encSecKey = get_params(songid)
    data = {'params': params, 'encSecKey': encSecKey}
    url = 'https://music.163.com/weapi/song/lyric?csrf_token='
    r = requests.post(url, data=data)
    # 状态码
    print(r.status_code)
    print(r.json())


if __name__ == "__main__":
    main()

"""
200
{'sgc': False, 'sfy': False, 'qfy': False, 'transUser': {'id': 38592976, 'status': 99, 'demand': 1, 'userid': 58612817, 'nickname': '_还有风景线', 'uptime': 1450679655737}, 'lyricUser': {'id': 38592976, 'status': 0, 'demand': 0, 'userid': 112955980, 'nickname': '我自静默向韶华收录1990', 'uptime': 1450076929022}, 'lrc': {'version': 4, 'lyric': '[00:08]I will run, I will climb, I will soar\n[00:13]I’m undefeated\n[00:16]Jumping out of my skin, pull the chord\n[00:21]Yeah I believe it\n[00:23]The past, is everything we were don’t make us who we are\n[00:26]So I’ll dream, until I make it real, and all I see is stars\n[00:37]Its not until you fall that you fly\n[00:43]When your dreams come alive you’re unstoppable\n[00:47]Take a shot, chase the sun, find the beautiful\n[00:51]We will glow in the dark turning dust to gold\n[00:55]And we’ll dream it possible\n[01:16]I will chase, I will reach, I will fly\n[01:20]Until I’m breaking, until I’m breaking\n[01:24]Out of my cage, like a bird in the night\n[01:28]I know I’m changing, I know I’m changing\n[01:31]In, into something big, better than before\n[01:39]And if it takes, takes a thousand lives\n[01:43]Then It’s worth fighting for\n[01:46]Its not until you fall that you fly\n[01:50]When your dreams come alive you’re unstoppable\n[01:55]Take a shot, chase the sun, find the beautiful\n[01:59]We will glow in the dark turning dust to gold\n[02:03]And we’ll dream it possible\n[02:23]From the bottom to the top\n[02:26]We’re sparking wild fire’s\n[02:28]Never quit and never stop\n[02:30]The rest of our lives\n[02:32]From the bottom to the top\n[02:34]We’re sparking wild fire’s\n[02:36]Never quit and never stop\n[02:39]Its not until you fall that you fly\n[02:45]When your dreams come alive you’re unstoppable\n[02:49]Take a shot, chase the sun, find the beautiful\n[02:53]We will glow in the dark turning dust to gold\n[02:57]And we’ll dream it possible possible\n'}, 'tlyric': {'version': 3, 'lyric': '[00:08]我奔跑，我攀爬，我会飞翔\n[00:13]永不言败\n[00:16]跳出我的皮肤，拨弄琴弦\n[00:21]哦，我相信。\n[00:23]往昔，逝去的光阴不会决定现在\n[00:26]所以我们梦想，直到变成真，看到满天星光\n[00:37]不怕跌倒，所以飞翔\n[00:43]当你的梦想成真，你是不可阻挡\n[00:47]挥着翅膀，追逐太阳，寻找美丽\n[00:51]在黑暗中闪耀点石成金\n[00:55]我们会梦想成真\n[01:16]我追逐，我奔驰，我要飞翔\n[01:20]直到坠落，直到崩溃\n[01:24]走出我的囚笼，像在黑夜里的莺\n[01:28]我知道我在变化，在蜕变\n[01:31]变成无比强大，从未有过\n[01:39]如果需要牺牲，需要无数的生命\n[01:43]那值得去奋斗\n[01:46]不怕跌倒，所以飞翔\n[01:50]当你的梦想成真，你是不可阻挡\n[01:55]挥着翅膀，追逐太阳，寻找美丽\n[01:59]在黑暗中闪耀点石成金\n[02:03]我们会梦想成真\n[02:23]从山谷到巅峰\n[02:26]我们正在迸发野火\n[02:28]永不放弃，永不停止\n[02:30]点燃未来\n[02:32]从山谷到巅峰\n[02:34]我们正在迸发野火\n[02:36]永不放弃，永不停止\n[02:39]不怕跌倒，所以飞翔\n[02:45]当你的梦想成真，你是不可阻挡\n[02:49]挥着翅膀，追逐太阳，寻找美\n[02:53]在黑暗中闪耀点石成金\n[02:57]我们会梦想成真'}, 'code': 200}
"""