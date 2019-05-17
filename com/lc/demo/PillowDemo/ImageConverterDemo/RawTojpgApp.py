# -*- coding: utf-8 -*-

"""

RawTojpgApp.py
图片格式raw转jpg
Version: 1.0
Author: LC
DateTime: 2019年5月17日21:16:17
UpdateTime:
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
LC博客url: http://oneplusone.vip/index.html
一加壹.SNS LC - 又一个SNS社区: http://sns.oneplusone.vip
赞助一加壹博客最Top-LC万能收款码支持-支付宝、微信、QQ
http://lc.oneplusone.vip/donateMeByLC.html

"""

import numpy as np
import cv2

img = cv2.imread('xianYuDreamJpg.jpg')
types = img.dtype  # 得到数据格式，如uint8和uint16等
width, height, channels = img.shape  # 得到图像大小和通道数 275 510 3

print(types, width, height, channels)

rawImg = np.fromfile('xianYuDreamRaw.raw', dtype=np.uint8)

rawImg = rawImg.reshape(275, 510, 3) # 275 510 3

cv2.imwrite('xianYuDreamJpg.jpg', rawImg)
