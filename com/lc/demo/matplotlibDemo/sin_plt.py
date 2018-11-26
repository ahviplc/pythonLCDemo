#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
sin函数的折线图

Version: 0.1
Author: LC
DateTime: 2018年11月26日14:02:49
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""

import matplotlib.pyplot as plt
import numpy as np
# 简单的绘图
x = np.linspace(0, 2 * np.pi, 50)
plt.plot(x, np.sin(x)) # 如果没有第一个参数 x，图形的 x 坐标默认为数组的索引
plt.show() # 显示图形


"""

十分钟入门Matplotlib - Jinlong_Xu的博客 - CSDN博客
https://blog.csdn.net/jinlong_xu/article/details/67646094

上面的代码将画出一个简单的正弦曲线。np.linspace(0, 2 * np.pi, 50) 这段代码将会生成一个包含 50 个元素的数组，这 50 个元素均匀的分布在 [0, 2pi] 的区间上。

plot 命令以一种简洁优雅的方式创建了图形。提醒一下，如果没有第一个参数 x，图形的 x 轴坐标将不再是 0 到 2pi，而应该是数组的索引范围。

最后一行代码 `plt.show() 将图形显示出来，如果没有这行代码图像就不会显示。

运行代码后应该会类似得到下面的图形
"""