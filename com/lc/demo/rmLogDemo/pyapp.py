#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
pyapp.py
去除log日志的某行-带'抛弃原文'的去掉
Version: 1.0
Author: LC
DateTime: 2019年2月18日12:29:06
UpdateTime: None
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""


def main():
    with open("pyapp.log", "r", encoding="utf-8") as f:
        lines = f.readlines()
        # print(lines)
    with open("pyapp_ok.log", "w", encoding="utf-8") as f_w:
        all_line_counts = 0
        for line in lines:
            if "抛弃原文" in line:
                print('剔除的数据:-->' + line)
                all_line_counts = all_line_counts + 1
                continue  # 符合的抛弃
            f_w.write(line)  # 不符合的重新写入
        print('总删除行' + str(all_line_counts))


def maintxt():
    with open("txt.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        # print(lines)
    with open("txt_ok.txt", "w", encoding="utf-8") as f_w:
        all_line_counts = 0
        for line in lines:
            if "tasting" in line:
                print('剔除的数据:-->' + line)
                all_line_counts = all_line_counts + 1
                continue  # 符合的抛弃
            f_w.write(line)  # 不符合的重新写入
        print('总删除行' + str(all_line_counts))


if __name__ == '__main__':
    # maintxt()
    main()
