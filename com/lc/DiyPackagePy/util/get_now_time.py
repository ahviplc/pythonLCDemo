#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import datetime


def get_now_time():
    now_time_str = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
    print('当前时间 -> ', now_time_str)
    return now_time_str
