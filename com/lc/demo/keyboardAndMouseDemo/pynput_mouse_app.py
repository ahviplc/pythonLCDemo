# -*- coding:utf-8 -*-

"""

pynput_mouse_app.py
备注:
Version: 1.0
Author: LC
DateTime: 2019年10月31日10:03:07
UpdateTime:
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
LC博客url: http://oneplusone.vip/index.html
一加壹.SNS LC - 又一个SNS社区: http://sns.oneplusone.vip
赞助一加壹博客最Top-LC万能收款码支持-支付宝、微信、QQ
http://lc.oneplusone.vip/donateMeByLC.html

"""

from pynput.mouse import Button, Controller

## ================================================
##              控制鼠标
## ================================================

# 读鼠标坐标
mouse = Controller()
print('The current pointer position is {0}'.format(mouse.position))
# 设置鼠标坐标pynput
mouse.position = (10, 20)
print('Now we have moved it to {0}'.format(mouse.position))
# 移动鼠标到相对位置
mouse.move(5, -5)
# 按住和放开鼠标
mouse.press(Button.left)  # 按住鼠标左键
mouse.release(Button.left)  # 放开鼠标左键
# 点击鼠标
mouse.click(Button.left, 2)  # 点击鼠标2下
# 鼠标滚轮
mouse.scroll(0, 2)  # 滚动鼠标

## 监听鼠标
from pynput.mouse import Listener


def on_move(x, y):
    # 监听鼠标移动
    print('Pointer moved to {0}'.format((x, y)))


def on_click(x, y, button, pressed):
    # 监听鼠标点击
    print('{0}{1} at {2}'.format(button, ' Pressed' if pressed else ' Released', (x, y)))
    # print(button)
    # 按住鼠标左键 退出程序
    if button == Button.left:
        # Stop listener
        print("Stop listener")
        return False

    # 按住鼠标按键 退出程序
    # if not pressed:
    #     # Stop listener
    #     print("Stop listener")
    #     return False


def on_scroll(x, y, dx, dy):
    # 监听鼠标滚轮
    print('Scrolled {0}'.format((x, y)))


# 连接事件以及释放
with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()
# 一个鼠标监听器是一个线程。线程，所有的回调将从线程调用。从任何地方调用pynput.mouse.Listener.stop，或者调用pynput.mouse.Listener.StopException或从回调中返回False来停止监听器。
