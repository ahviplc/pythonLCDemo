#!/usr/bin/python3
# coding: utf-8

"""
猜数字

Version: 0.1
Author: LC
DateTime: 2018年11月15日15:04:24
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

from random import randint


def main():
    answer = randint(1, 100)
    while True:
        number = int(input('请输入: '))
        if number < answer:
            print('大一点')
        elif number > answer:
            print('小一点')
        else:
            print('恭喜你猜对了!')
            break


if __name__ == '__main__':
    main()
