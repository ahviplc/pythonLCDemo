#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
writeJsonToOracleForLMT.py
json解析写入oracle For 罗美特 纯净版
测试的oracle数据库表脚本文件也在-com/lc/demo/jsonToOracleDemo/AREA_INFO.sql -SHORT_MESSAGE_CONFIG.sql
Version: 1.0
Author: LC
DateTime: 2019年2月22日15:53:06
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


# 从json里读取数据，经过业务逻辑处理，写入oracle
def json_write_to_oracle():
    with open('ICRechargeRecord.txt', 'r+', encoding='utf-8') as f:
        json_dict_list = json.load(f)
        # print(json_dict_list)
        # for i in json_dict_list:
        #     print(i)
        #     print(i['Id'])
    return json_dict_list
    print('all Done')


# 时间戳转date方法工具
def timestamp_to_date(timestampStr):
    # timestampStr='/Date(1510639156973+0800)/';
    jie_qu_timestampStr=timestampStr[6:16]
    # print(jie_qu_timestampStr)
    datetimes = datetime.datetime.fromtimestamp(int(jie_qu_timestampStr))
    # print(datetimes)
    return datetimes

# 定义类
class MyOracle:
    SHOW_SQL = True

    def __init__(self, host='###', port=1521, user='SCOTT', password='Lmt123456',
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

# 带参数 插入数据 ICRechargeRecord
def ins_by_param_icrechargerecord(json_dict_list):

    # 15个键值对-数据库操作
    sql = "INSERT INTO FI_CHARGE_RECORD (RCR_ORG_ID, RCR_ID, CHARGE_TIME,CUSTOMER_NO,METER_NO,PRICE_NO,PRICE,TOTAL_VOLUME,TOTAL_MONEY,CHARGE_TIMES,METER_TYPE,CHARGE_OPERATOR,RECEIPT_NO,IC_CHARGE_VOLUME,IC_CHARGE_MONEY)  VALUES (:rcrOrgId, :Id, :chargeTime,:customerNo,:meterNo, :priceNo ,:Price,:totalVolume,:totalMoney, :chargeTimes, :meterTypeNo,:chargeOperator,:ReceiptNo,:chargeVolume,:chargeMoney)"

    # print(json_dict_list)
    # 数据处理
    for i in json_dict_list:

        # print(i)

        chargeTime_timestampStr=i['chargeTime']
        datetime_ok = timestamp_to_date(chargeTime_timestampStr)  # 时间戳转date
        i['chargeTime'] = datetime_ok

        i['rcrOrgId'] = '0013'  # 机构编号-需要自定义更改

        # 删除未使用的多余键值对
        del i['CalcMsg']
        del i['ICWriteMark']
        del i['chargeBranchNo']
        del i['chargePosNo']
        del i['chargeType']
        del i['factoryNo']
        # print(i['Id'])

    # print(json_dict_list)
    data = json_dict_list
    db.dml_by_where(sql, data)  # ok

    print('输出影响行数:' +str(len(data)))
    print('ins_by_param_icrechargerecord ok')

# main方法
if __name__ == "__main__":

    db = MyOracle()
    json_dict_list_return = json_write_to_oracle()
    ins_by_param_icrechargerecord(json_dict_list_return)
    print('转存到oracle成功！')
