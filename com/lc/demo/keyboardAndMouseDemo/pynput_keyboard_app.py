# -*- coding:utf-8 -*-

"""

pynput_keyboard_app.py
备注:
Version: 1.0
Author: LC
DateTime: 2019年10月31日10:01:57
UpdateTime:
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
LC博客url: http://oneplusone.vip/index.html
一加壹.SNS LC - 又一个SNS社区: http://sns.oneplusone.vip
赞助一加壹博客最Top-LC万能收款码支持-支付宝、微信、QQ
http://lc.oneplusone.vip/donateMeByLC.html

"""

## ================================================
##              控制键盘
## ================================================

from pynput.keyboard import Key, Controller

keyboard = Controller()
# 按键盘和释放键盘
keyboard.press(Key.space)
keyboard.release(Key.space)

# 按小写的a
keyboard.press('a')
keyboard.release('a')

# 按大写的A
keyboard.press('A')
keyboard.release('A')

# 按住shift在按a
with keyboard.pressed(Key.shift):
    # Key.shift_l, Key.shift_r, Key.shift
    keyboard.press('a')
    keyboard.release('a')

# 直接输入 LC Hello World
keyboard.type(' LC Hello World')

## 监听键盘
from pynput.keyboard import Key, Listener


def on_press(key):
    # 监听按键
    print('{0} pressed'.format(key))


def on_release(key):
    # 监听释放
    print('{0} release'.format(key))
    if key == Key.esc:
        # Stop listener
        print("Stop listener")
        return False


# 连接事件以及释放
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
