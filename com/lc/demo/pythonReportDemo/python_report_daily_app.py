#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
python_report_daily_app.py
日报表-计算写入数据库oracle的报表脚本
Version: 1.0
Author: LC
DateTime: 2019年3月7日14:16:04
UpdateTime: None
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""
import time
import datetime
import calendar
import os
import cx_Oracle

# 改变系统环境编码为简体中文utf-8-为了让oracle查询出的中文不乱码
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


# 定义类 MyOracle
class MyOracle:
    SHOW_SQL = True

    def __init__(self, host='192.168.0.7', port=1521, user='SCOTT', password='Lmt123456',
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

    # 自定义查询 一个参数可用
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

    # 自定义查询 带多个参数
    def select_by_where_many_params(self, sql, params):
        try:
            con = self.get_con()
            # print(con)
            for d in params:
                cur = con.cursor()
                cur.execute(sql, d)
            fc = cur.fetchall()
            pass
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


# 公共方法


# 获取间隔n天时间的最小时间(0点)和最大时间(23点59分59秒)-datetime.timedelta(days=1)可以处理天，datetime.timedelta(weeks=1)也可以处理周等
# @param  n,type,isFormat; n代表几天，可以正值(n天后)，可以负值(n天前),0代表今天 ;
#                          type取值有max和min,max代表输出当前时间最大时间，min代表输出当前时间最小时间;
#                          isFormat是否格式化输出，布尔值为True,格式化输出str类型时间,为False,不格式化输出，直接返回datetime类型时间。
# @return 符合要求的datetime格式日期
# 使用示例:
# print(to_n_datetime_max_min_time(2,"max", False))-2019-03-09 23:59:59.999999
# print(to_n_datetime_max_min_time(0,"min", False))-2019-03-07 00:00:00
# print(to_n_datetime_max_min_time(-1,"min", False))-2019-03-06 00:00:00
# print(to_n_datetime_max_min_time(-5, "max", True))-2019-03-02 23:59:59
def to_n_datetime_max_min_time(n, type, is_format):
    if type == "max":
        return_time = datetime.datetime.combine(datetime.date.today() + datetime.timedelta(days=n), datetime.time.max)
    elif type == "min":
        return_time = datetime.datetime.combine(datetime.date.today() + datetime.timedelta(days=n), datetime.time.min)
    if (is_format):
        return_time = return_time.strftime('%Y-%m-%d %H:%M:%S')
    return return_time


# 从oracle数据库SCADA_FLMETER_DATA读取所有符合条件的数据
# 带参数查询
def select_sfd_by_where():
    sql = "select * from SCADA_FLMETER_DATA where SFD_ORG_ID= :orgid and INSTANT_TIME between :minTime AND :maxTime "
    yesterday_min = to_n_datetime_max_min_time(-1, "min", False)
    yesterday_max = to_n_datetime_max_min_time(-1, "max", False)
    data = [{"orgid": "0005", "minTime": yesterday_min, "maxTime": yesterday_max}]
    fc = db.select_by_where_many_params_dict(sql, data)
    print("总共数据:", len(fc))
    for row in fc:
        print(row)


def main():
    pass


if __name__ == '__main__':
    main()
    db = MyOracle()
    select_sfd_by_where()
