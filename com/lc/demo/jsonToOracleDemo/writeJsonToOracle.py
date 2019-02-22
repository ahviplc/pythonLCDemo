#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
writeJsonToOracle.py
json解析写入oracle
测试的oracle数据库表脚本文件也在-com/lc/demo/jsonToOracleDemo/AREA_INFO.sql
Version: 1.0
Author: LC
DateTime: 2019年2月21日19:53:27
UpdateTime: None
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""
import json
import cx_Oracle
import os

# 改变系统环境编码为简体中文utf-8-为了让oracle查询出的中文不乱码
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

# r 只能读
# r+ 可读可写 不会创建不存在的文件 从顶部开始写 会覆盖之前此位置的内容
# w+ 可读可写 如果文件存在 则覆盖整个文件不存在则创建
# w 只能写 覆盖整个文件 不存在则创建
# a 只能写 从文件底部添加内容 不存在则创建
# a+ 可读可写 从文件顶部读取内容 从文件底部添加内容 不存在则创建

# 从json里读取数据，经过业务逻辑处理，写入oracle
def json_write_to_oracle():
    with open('demo.json', 'r+', encoding='utf-8') as f:
        json_dict = json.load(f)
        print(json_dict)
        for i in json_dict:
            print(i)
            print(i['id'])
    print('all Done')


# oracle查询
def oracle_select_app():

    # conn = cx_Oracle.connect('用户名/密码@主机ip地址/orcl')  # 用自己的实际数据库用户名、密码、主机ip地址 替换即可
    # 注意:要将D:\all_develop_soft\oracle jdbc\instantclient_11_2配置到环境变量Path , D:\all_develop_soft\oracle jdbc\instantclient_11_2\oci.dll

    conn = cx_Oracle.connect('SCOTT/Lmt123456@###:1521/LMTPlat')  # 用自己的实际数据库用户名、密码、主机ip地址 替换即可--:1521-加不加端口号都行，默认1521
    curs = conn.cursor()

    sql = 'SELECT * FROM AREA_INFO'  # sql语句

    rr = curs.execute(sql)

    # 使用fetchone()方法获取一条数据
    row = curs.fetchone()
    print(row[0])

    # 获取所有数据
    all_data = curs.fetchall()

    # 获取部分数据，8条
    # many_data=curs.fetchmany(8)
    print('select ok')
    # 关闭
    curs.close()
    conn.close()


# oracle插入
def oracle_insert_app():

    # conn = cx_Oracle.connect('用户名/密码@主机ip地址/orcl')  # 用自己的实际数据库用户名、密码、主机ip地址 替换即可
    # 注意:要将D:\all_develop_soft\oracle jdbc\instantclient_11_2配置到环境变量Path , D:\all_develop_soft\oracle jdbc\instantclient_11_2\oci.dll

    conn = cx_Oracle.connect('SCOTT/Lmt123456@###:1521/LMTPlat')  # 用自己的实际数据库用户名、密码、主机ip地址 替换即可--:1521-加不加端口号都行，默认1521
    curs = conn.cursor()

    curs.execute('insert into SHORT_MESSAGE_CONFIG (SMC_ORG_ID, SMC_CODE, SMC_NAME) values(\'0004\',\'0007\',\'Test测试py\')')
    conn.commit()
    print('insert ok')
    # 关闭
    curs.close()
    conn.close()


# main方法
if __name__ == '__main__':
    json_write_to_oracle()
    oracle_select_app()
    oracle_insert_app()
