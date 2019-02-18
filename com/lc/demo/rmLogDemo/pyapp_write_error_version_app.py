#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
pyapp_write_error_version_app.py
去除log日志的某行-带'抛弃原文'的过滤出来，写入新的log日志
此是将正常的数据抛弃，异常的数据重新写入
Version: 1.0
Author: LC
DateTime: 2019年2月18日14:29:51
UpdateTime: None
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""


def main():
    with open("pyapp.log", "r", encoding="utf-8") as f:
        lines = f.readlines()
        # print(lines)
    with open("pyapp_error.log", "w", encoding="utf-8") as f_w:
        all_line_counts = 0
        for line in lines:
            if "抛弃原文" in line:
                print('异常的数据:-->' + line)
                all_line_counts = all_line_counts + 1
                f_w.write(line)
                continue  # 异常的数据重新写入
            pass  # 正常的数据抛弃
        print('总写入异常数据行' + str(all_line_counts))

        close_str_msg = input('Press Enter to exit...')
        print(close_str_msg)

if __name__ == '__main__':
    main()
