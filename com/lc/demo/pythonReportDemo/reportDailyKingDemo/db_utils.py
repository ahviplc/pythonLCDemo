#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
db_utils.py
工具类(启用)
Version: 1.0
Author: LC
DateTime: 2019年3月9日23:22:47
UpdateTime: 2019年3月9日23:48:44
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""
import time
import datetime
import calendar


# 取自动递增流水号
# @param ssn_org_id 机构号
# @param ssn_key_name 序列号名称
# @param ssn_year 序列号 年
# @param ssn_month 序列号 月
# @return 处理之后的流水号，以供使用
def get_sys_serial_no(db, ssn_org_id, ssn_key_name, ssn_year, ssn_month):
    print(123)
    sql = "select * from SYS_SERIAL_NO"
    fc = db.select_all(sql)
    for row in fc:
        print(row)
    print('select_all ok')
    pass
    return True
