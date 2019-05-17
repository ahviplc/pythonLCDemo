# -*- coding: utf-8 -*-

"""

jpgToRawApp.py
图片格式jpg转raw
Version: 1.0
Author: LC
DateTime: 2019年5月17日20:47:25
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

img = cv2.imread('../codeImg/xianYuDream.jpg')
# 这里需要我们在当前目录下放一张名为xianYuDream.jpg的文件
img.tofile('xianYuDreamRaw.raw')
# 利用numpy中array的函数tofile将数据写入文件
# 这时我们发现当前目录下新增了一个文件，名为xianYuDreamRaw.raw
# 我们先确定原图片的数据格式和大小，通道数，否者无法进行下一步转换
types = img.dtype  # 得到数据格式，如uint8和uint16等
width, height, channels = img.shape  # 得到图像大小和通道数 275 510 3

# 利用numpydefromfile函数读取raw文件，并指定数据格式
imgData = np.fromfile('xianYuDreamRaw.raw', dtype=types)

# 利用numpy中array的reshape函数将读取到的数据进行重新排列。
imgData = imgData.reshape(width, height, channels)

# 展示图像
cv2.imshow('img', imgData)
cv2.waitKey()
cv2.destroyAllWindows()
