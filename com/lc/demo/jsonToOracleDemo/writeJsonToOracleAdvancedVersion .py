#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
writeJsonToOracleAdvancedVersion .py 高级版
Python3-cx_Oracle模块-数据库操作之Oracle-Oracle 数据库操作（使用类封装基本的增删改查）
json解析写入oracle-oracle
测试的oracle数据库表脚本文件也在-com/lc/demo/jsonToOracleDemo/AREA_INFO.sql  SHORT_MESSAGE_CONFIG.sql
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

    def __init__(self, host='###', port=1521, user='SCOTT', password='Lmt123456', sid='LMTPlat'):  # 注意###里改为自己所需要的ip
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
            # print(con)
            cur = con.cursor()
            cur.execute(sql)
            fc = cur.fetchall()
            return fc
        except Exception as e:
            print("Exception Error:%s" % e)
        finally:
            cur.close()
            con.close()

    # 自定义查询 一个参数可用
    def select_by_where(self, sql, data):
        try:
            con = self.get_con()
            # print con
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

    # 自定义查询 带多个参数
    def select_by_where_many_params(self, sql, params):
        try:
            con = self.get_con()
            # print(con)
            for d in params:
                cur = con.cursor()
                cur.execute(sql, d)
            fc = cur.fetchall()
            return fc
        except Exception as e:
            print("Exception Error:%s" % e)
        finally:
            cur.close()
            con.close()

    # 自定义查询 带多个参数 返回字典样式列表
    def select_by_where_many_params_dict(self, sql, params):
        try:
            con = self.get_con()
            # print(con)
            for d in params:
                cur = con.cursor()
                cur.execute(sql, d)
                cur.rowfactory = self.makedict(cur)
            fc = cur.fetchall()
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

    # 数据库查询返回字典
    def makedict(self, cursor):
        cols = [d[0] for d in cursor.description]

        def createrow(*args):
            return dict(zip(cols, args))

        return createrow

    # oracle查询 -简单写法
    def oracle_select_app(self):

        conn = self.get_con()

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


# 开始测试函数

# 查询全部
def select_all():
    sql = "select * from AREA_INFO"
    fc = db.select_all(sql)
    for row in fc:
        print(row)
    print('select_all ok')


# 带参数查询
def select_by_where():
    sql = "select * from AREA_INFO where AREA_NO=:1"
    data = '0008000001'
    fc = db.select_by_where(sql, data)
    for row in fc:
        print(row)


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


# 带条件参数 删除数据
def del_by_where():
    sql = "delete from SHORT_MESSAGE_CONFIG where SMC_ORG_ID = :1 and SMC_CODE=:2"
    data = [('0004', '0008')]
    db.dml_by_where(sql, data)
    print('del_by_where ok')


# 带参数 更新数据
def update_by_where():
    sql = "update SHORT_MESSAGE_CONFIG set SMC_NAME=:1 where SMC_ORG_ID=:2 AND SMC_CODE=:2"
    data = [('TEST UPDATE NAME', '0004', '0007')]
    db.dml_by_where(sql, data)
    print('update_by_where ok')


# 删除了所有数据
def del_nowhere():
    sql = "delete from SHORT_MESSAGE_CONFIG"
    print(db.dml_nowhere(sql))
    print('del_nowhere ok')


if __name__ == "__main__":
    db = MyOracle()
    db.oracle_select_app()

    select_all()

    # db.oracle_select_app() #ok 查询简单写法
    # 运行示例：
    # 0008
    # select ok

    # select_all() #ok
    # 运行示例:
    # ('0008', '0008000001', '默认区域', '默区', None, '1')
    # ('0003', '0003000002', '奉贤区', None, None, '1')
    # ('0003', '0003000003', '徐汇区', None, None, '1')
    # ('0005', '0005000001', '默认区域', '默区', None, '1')
    # ('0007', '0007000001', '默认区域', '默区', None, '1')
    # ('0009', '0009000001', '默认区域', '默区', None, '1')
    # ('0011', '0011000001', '默认区域', '默区', None, '1')
    # ('0012', '0012000001', '默认区域', '默区', None, '1')
    # ('0001', '0001000010', '1', '1', '1', '9')
    # ('0001', '0001000011', None, None, None, '1')
    # ('0001', '0001000013', 'test11', 'test21', 'test11', '1')
    # ('0003', '0003000001', '默认区域', '默区', None, '1')
    # ('0002', '0002000001', '默认区域', '默区', None, '1')
    # ('0001', '0001000014', '..', '.', '.', '1')
    # ('0001', '0001000001', '默认区域', '默区', '默认的区域啊！', '1')
    # ('0001', '0001000003', 'test0001', 'test', 'test', '1')
    # ('0001', '0001000002', 'demo', 'demo', 'demo1', '1')
    # ('0001', '0001000005', '黄埔区1', '黄埔区1', '黄埔区1', '9')
    # ('0001', '0001000004', '西安', None, None, '9')
    # ('0001', '0001000009', '请问', '请问', '请问', '9')
    # ('0010', '0010000001', '默认区域', '默区', None, '1')
    # ('0006', '0006000001', '默认区域', '默区', None, '1')

    #
    # select_by_where() #ok
    # 运行示例:
    # ('0008', '0008000001', '默认区域', '默区', None, '1')

    # ins_by_param() #ok
    # 运行示例:
    # 执行sql: [insert into SHORT_MESSAGE_CONFIG(SMC_ORG_ID, SMC_CODE, SMC_NAME) values(:1,: 2,:3)], 参数: [('0004', '0007', 'test1')]
    # 执行sql: [insert into SHORT_MESSAGE_CONFIG(SMC_ORG_ID, SMC_CODE, SMC_NAME) values(:1,: 2,:3)], 参数: [('0004', '0008', 'test2')]
    # ins_by_param ok

    # del_by_where() #ok
    # 运行示例:
    # 执行sql: [delete from SHORT_MESSAGE_CONFIG where SMC_ORG_ID =:1 and SMC_CODE =:2], 参数: [('0004', '0008')]
    # del_by_where ok

    # update_by_where() #ok
    # 运行示例:
    # 执行sql:[update SHORT_MESSAGE_CONFIG set SMC_NAME=:1 where SMC_ORG_ID=:2 AND SMC_CODE=:2],参数:[('TEST UPDATE NAME', '0004', '0007')]
    # update_by_where ok

    # del_nowhere() #ok 删除所有数据
    # 运行示例:
    # None
    # del_nowhere ok

    # ins_by_param2() #ok
    # 运行示例:
    # 执行sql:[INSERT INTO SHORT_MESSAGE_CONFIG (SMC_ORG_ID, SMC_CODE, SMC_NAME)  VALUES(:orgid, :code, :smcname)],参数:[{'orgid': '0004', 'code': '0007', 'smcname': 'test1'}]
    # ins_by_param2 ok
