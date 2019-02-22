#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
writeJsonToOracleForLMT.py
json解析写入oracle For 罗美特
测试的oracle数据库表脚本文件也在-com/lc/demo/jsonToOracleDemo/AREA_INFO.sql -SHORT_MESSAGE_CONFIG.sql
Version: 1.0
Author: LC
DateTime: 2019年2月22日09:48:14
UpdateTime: None
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""
import json
import cx_Oracle
import os
import datetime

# 改变系统环境编码为简体中文utf-8-为了让oracle查询出的中文不乱码
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

# with open 参数介绍
# r 只能读
# r+ 可读可写 不会创建不存在的文件 从顶部开始写 会覆盖之前此位置的内容
# w+ 可读可写 如果文件存在 则覆盖整个文件不存在则创建
# w 只能写 覆盖整个文件 不存在则创建
# a 只能写 从文件底部添加内容 不存在则创建
# a+ 可读可写 从文件顶部读取内容 从文件底部添加内容 不存在则创建

class MyOracle:
    SHOW_SQL = True

    def __init__(self, host='101.132.236.137', port=1521, user='SCOTT', password='Lmt123456',
                 sid='LMTPlat'):  # 注意###里改为自己所需要的ip
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.sid = sid

    # 连接数据库
    def get_con(self):
        try:
            dsn_tns = cx_Oracle.makedsn(self.host, self.port, self.sid)
            # 如果是Oracle 12c 数据库需要替换sid 为service_name
            dsn_tns = dsn_tns.replace('SID', 'SERVICE_NAME')
            conn = cx_Oracle.connect(self.user, self.password, dsn_tns)
            return conn
        except Exception as e:
            print("Exception Error:%s" % e)
        finally:
            pass

    # 查询所有
    def select_all(self, sql):
        try:
            con = self.get_con()
            # print con
            cur = con.cursor()
            cur.execute(sql)
            fc = cur.fetchall()
            return fc
        except Exception as e:
            print("Exception Error:%s" % e)
        finally:
            cur.close()
            con.close()

    # 自定义查询
    def select_by_where(self, sql, data):
        try:
            con = self.get_con()
            # print(con)
            d = (data,)
            cur = con.cursor()
            cur.execute(sql, d)
            fc = cur.fetchall()
            # if len(fc) > 0:
            #     for e in range(len(fc)):
            #         print(fc[e])
            return fc
        except Exception as e:
            print("Exception Error:%s" % e)
        finally:
            cur.close()
            con.close()

    # 带参数 执行自定义sql语句
    def dml_by_where(self, sql, params):
        try:
            con = self.get_con()
            cur = con.cursor()

            for d in params:
                if self.SHOW_SQL:
                    print('执行sql:[{}],参数:[{}]'.format(sql, d))
                cur.execute(sql, d)
            print('输出影响行数:' + str(cur.rowcount))  # 输出影响行数
            con.commit()

        except Exception as e:
            con.rollback()
            print("Exception Error:%s" % e)
        finally:
            cur.close()
            con.close()

    # 不带参数的更新方法
    def dml_nowhere(self, sql):
        try:
            con = self.get_con()
            cur = con.cursor()
            count = cur.execute(sql)
            con.commit()
            return count
        except Exception as e:
            con.rollback()
            print("Exception Error:%s" % e)
        finally:
            cur.close()
            con.close()


# 开始测试函数

# 查询全部
def select_all():
    sql = "select * from AREA_INFO"
    fc = db.select_all(sql)
    for row in fc:
        print(row)


# 带参数查询
def select_by_where():
    sql = "select * from AREA_INFO where AREA_NO=:1"
    data = '0008000001'
    fc = db.select_by_where(sql, data)
    for row in fc:
        print(row)
    print('select_by_where ok')


# 带参数 插入数据
def ins_by_param():
    sql = "insert into SHORT_MESSAGE_CONFIG (SMC_ORG_ID, SMC_CODE, SMC_NAME) values(:1,:2,:3)"
    date = datetime.datetime.now()  # 当前日期
    data = [('0004', '0007', 'test1'), ('0004', '0008', 'test2')]
    db.dml_by_where(sql, data)
    print('ins_by_param ok')


# 带参数 插入数据2
def ins_by_param2():
    sql = "INSERT INTO SHORT_MESSAGE_CONFIG (SMC_ORG_ID, SMC_CODE, SMC_NAME)  VALUES(:orgid, :code, :smcname)"
    data = [{"orgid": '0004', "code": "0007", "smcname": 'test1'}]
    data2 = [{"orgid": '0004', "code": "0007", "smcname": 'test11'},
             {"orgid": '0004', "code": "0008", "smcname": 'test22'}]
    # db.dml_by_where(sql, data2) #ok
    db.dml_by_where(sql, data)  # ok
    print('ins_by_param2 ok')


if __name__ == "__main__":

    db = MyOracle()

    ins_by_param2()

    date = datetime.datetime.now()  # 当前日期
    print(date)  # 2019-02-22 12:18:25.949246

    # select_all()
    # select_by_where()
    # ins_by_param()
    # ins_by_param2()




# 执行sql:[INSERT INTO SHORT_MESSAGE_CONFIG (SMC_ORG_ID, SMC_CODE, SMC_NAME)  VALUES(:orgid, :code, :smcname)],参数:[{'orgid': '0004', 'code': '0007', 'smcname': 'test1'}]
# 输出影响行数1
# ins_by_param2 ok
