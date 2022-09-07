# encoding: utf-8

import sys
import os
import platform

# 关闭端口号下所有进程工具 | My-Blog | 只支持 mac 和 linux
# https://apidocs.cn/blog/backend/python/kill_port.html

# attachment; filename=kill_port.py

if len(sys.argv) != 2:
    print("正确格式应为：python kill_port.py 8011 | ./kill_port 8011")
else:
    port = sys.argv[1]
    if not port.isdigit():
        print("端口号只能为数字：", port)
    sys = platform.system()
    if sys == 'Darwin' or sys == 'Linux':
        r = os.popen("lsof -i tcp:" + port)
        text = r.read()
        array = text.split("\n")
        print("进程个数为：", len(array) - 2)
        if len(array) > 1:
            print("当前进程信息：")
            for arr in array:
                if len(arr) > 1:
                    print(arr)
            input("输入回车键确认执行，取消请输入Control+Z！")
        for arr in array:
            ar = ' '.join(arr.split()).split(" ")
            if len(ar) > 1:
                pid = ar[1]
                if pid != 'PID':
                    os.system("kill -9 " + pid)
                    print('已关闭：', pid)
        r.close()
    else:
        print("系统暂不支持！")
