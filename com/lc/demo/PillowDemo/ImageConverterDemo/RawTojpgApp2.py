# -*- coding: utf-8 -*-

"""

RawTojpgApp2.py
图片格式raw转jpg
Version: 1.0
Author: LC
DateTime: 2019年5月17日21:30:15
UpdateTime:
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
LC博客url: http://oneplusone.vip/index.html
一加壹.SNS LC - 又一个SNS社区: http://sns.oneplusone.vip
赞助一加壹博客最Top-LC万能收款码支持-支付宝、微信、QQ
http://lc.oneplusone.vip/donateMeByLC.html

"""

import rawpy
import imageio
# import matplotlib.pylab as plt

# raw = rawpy.imread('xianYuDreamRaw.raw')
#
# #直接调用postprocess可能出现偏色问题
# rgb = raw.postprocess()
#
# #以下两行可能解决偏色问题，output_bps=16表示输出是 16 bit (2^16=65536)需要转换一次
# #im = raw.postprocess(use_camera_wb=True, half_size=False, no_auto_bright=True, output_bps=16)
# #rgb = np.float32(im / 65535.0*255.0)
# #rgb = np.asarray(rgb,np.uint8)
#
# imageio.imsave('xianYuDreamJpg2_ok.jpg', rgb)


# import numpy as np
# from PIL import Image
# from rawkit.raw import Raw
# filename = 'image.cr2'
# raw_image = Raw(filename)
# buffered_image = np.array(raw_image.to_buffer())
# image = Image.frombytes('RGB', (raw_image.metadata.width, raw_image.metadata.height), buffered_image)
# image.save('image.png', format='png')

# import Image
# rawData = open("I.raw" 'rb').read()
# im = Image.fromstring("F", (512,512), rawData, "raw", "F;32F")
# # "F" 指定图像的mode为“F”
# # (512,512)为 图像大小
# # rawdata 为存放数据的变量
# # "raw" 指定图像为raw格式
# # "F;32F" 指定数据在内存中的格式，为32位浮点型
# # 如此im中就保存的读入的数据，但并没有做格式和类型转换
# out = im.point(lambda i : i * (1.0/4.0)) # 对图像逐像素进行处理
# out.show()