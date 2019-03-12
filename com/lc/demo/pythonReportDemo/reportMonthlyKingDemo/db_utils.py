#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""

db_utils.py
工具类(启用) for 月报表
Version: 1.0
Author: LC
DateTime: 2019年3月9日23:22:47
UpdateTime: 2019年3月12日12:19:49
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""
import time
import datetime
import calendar


# 取自动递增流水号
# @param db 数据库对象
# @param ssn_org_id 机构号
# @param ssn_key_name 序列号名称
# @param ssn_year 序列号 年
# @param ssn_month 序列号 月
# @return 处理之后的流水号，以供使用
def get_sys_serial_no(db, ssn_org_id, ssn_key_name, ssn_year, ssn_month):
    print("开始取自动递增流水号逻辑")
    fc_again = None
    fc = select_sys_serial_no_is_null_or_not(db, ssn_org_id, ssn_key_name, ssn_year, ssn_month)  # 查询SYS_SERIAL_NO
    print("总列表长度:", len(fc))
    if len(fc) == 0:  # 如果为0 代表无数据 先生成一条 再将ssn_value+1更新 update 再get取其值使用
        insert_sys_serial_no(db, ssn_org_id, ssn_key_name, ssn_year, ssn_month)
        # update 将ssn_value+1更新 再取其值使用
        update_sys_serial_no_with_ssn_value_plus_one(db, ssn_org_id, ssn_key_name, ssn_year, ssn_month)
        # 再select 取值 使用
        fc_again = select_sys_serial_no_is_null_or_not(db, ssn_org_id, ssn_key_name, ssn_year,ssn_month)  # 再次查询SYS_SERIAL_NO
    else:  # 如果不为0 直接更新ssn_value+1 update 再get
        # update 将ssn_value+1更新 再取其值使用
        update_sys_serial_no_with_ssn_value_plus_one(db, ssn_org_id, ssn_key_name, ssn_year, ssn_month)
        # 再select 取值 使用
        fc_again = select_sys_serial_no_is_null_or_not(db, ssn_org_id, ssn_key_name, ssn_year,ssn_month)  # 再次查询SYS_SERIAL_NO
    print(fc_again)
    ok_ssn_value = fc_again[0]['SSN_VALUE']
    return ok_ssn_value


# 查询SYS_SERIAL_NO
# @param db 数据库对象
# @param ssn_org_id 机构号
# @param ssn_key_name 序列号名称
# @param ssn_year 序列号 年
# @param ssn_month 序列号 月
# @return 返回查询出的数据list
def select_sys_serial_no_is_null_or_not(db, ssn_org_id, ssn_key_name, ssn_year, ssn_month):
    sql = "select * from SYS_SERIAL_NO where SSN_ORG_ID= :ssn_org_id and SSN_KEY_NAME = :ssn_key_name and SSN_YEAR = :ssn_year and SSN_MONTH = :ssn_month"
    data = [{"ssn_org_id": ssn_org_id, "ssn_key_name": ssn_key_name, "ssn_year": ssn_year, "ssn_month": ssn_month}]
    fc = db.select_by_where_many_params_dict(sql, data)
    return fc


# 插入SYS_SERIAL_NO
# @param db 数据库对象
# @param ssn_org_id 机构号
# @param ssn_key_name 序列号名称
# @param ssn_year 序列号 年
# @param ssn_month 序列号 月
# @return null 插入成功或失败
def insert_sys_serial_no(db, ssn_org_id, ssn_key_name, ssn_year, ssn_month):
    insert_sql = "INSERT INTO SYS_SERIAL_NO (SSN_ORG_ID, SSN_KEY_NAME,SSN_YEAR,SSN_MONTH,SSN_VALUE, SSN_KEY_TYPE,SSN_KEY_DESCRIPTION)  VALUES(:ssn_org_id, :ssn_key_name, :ssn_year, :ssn_month, :ssn_value, :ssn_key_type, :ssn_key_description)"
    data = [{"ssn_org_id": ssn_org_id, "ssn_key_name": ssn_key_name, "ssn_year": ssn_year, "ssn_month": ssn_month,
             "ssn_value": "0000000000", "ssn_key_type": "2", "ssn_key_description": ssn_year + ssn_month + "月报表"}]
    db.dml_by_where(insert_sql, data)  # ok
    print('insert sys_serial_no ok')


# update 将ssn_value+1更新 再取其值使用
# @param db 数据库对象
# @param ssn_org_id 机构号
# @param ssn_key_name 序列号名称
# @param ssn_year 序列号 年
# @param ssn_month 序列号 月
# @return null 更新成功或失败
def update_sys_serial_no_with_ssn_value_plus_one(db, ssn_org_id, ssn_key_name, ssn_year, ssn_month):
    sql = "update SYS_SERIAL_NO set SSN_VALUE= trim(To_Char(SSN_VALUE+1,'0000000000')) where SSN_ORG_ID= :ssn_org_id and SSN_KEY_NAME = :ssn_key_name and SSN_YEAR = :ssn_year and SSN_MONTH = :ssn_month"
    data = [{"ssn_org_id": ssn_org_id, "ssn_key_name": ssn_key_name, "ssn_year": ssn_year, "ssn_month": ssn_month}]
    db.dml_by_where(sql, data)
    print('update sys_serial_no ok')