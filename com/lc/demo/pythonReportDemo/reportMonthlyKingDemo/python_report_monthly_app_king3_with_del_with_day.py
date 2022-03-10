#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""

python_report_monthly_app_king3_with_del_with_day.py 白天跑 修复大bug 月份支持传入-n了 加强版本3 新增月数据之前 先直接删除原有数据 再新增新的月报表数据 封装了月报表对象类以及将取自动递增流水方法提取到工具db_utils文件中,集成监听所有的print到log日志的封装类
月报表-计算写入数据库oracle的报表脚本
版本说明:1：跑所有机构的月报表；2:逻辑变更-【周期内工况使用量（本期期末数-上期期末数）】【周期内标况使用量（本期期末数-上期期末数）】 3:整体脚本代码结构变更
Version: 1.0
Author: LC
DateTime: 2020年6月30日13:34:03
UpdateTime: 2021年1月20日14:33:53
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
LC博客url: http://oneplusone.vip/index.html
一加壹.SNS LC - 又一个SNS社区: http://sns.oneplusone.vip
赞助一加壹博客最Top-LC万能收款码支持-支付宝、微信、QQ
http://lc.oneplusone.vip/donateMeByLC.html

"""
import math
import time
import datetime
import calendar
import os
import sys
import cx_Oracle
import operator
from python_report_monthly_model import ReportMonthlyModel  # 导入月报表对象类
from db_utils import get_sys_serial_no  # 导入获取流水号方法
from print_msg_to_log_model import PrintLogger

# 改变系统环境编码为简体中文utf-8-为了让oracle查询出的中文不乱码
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


# 定义类 MyOracle
class MyOracle:
    SHOW_SQL = True

    def __init__(self, host='172.19.110.129', port=1521, user='SCOTT', password='Lmt123456',
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
# @param  n,types,isFormat; n代表几天，可以正值(n天后)，可以负值(n天前),0代表今天 ;
#                          types取值有max和min,max代表输出当前时间最大时间，min代表输出当前时间最小时间;
#                          isFormat是否格式化输出，布尔值为True,格式化输出str类型时间,为False,不格式化输出，直接返回datetime类型时间。
# @return 符合要求的datetime格式日期
# 使用示例:
# print(to_n_datetime_max_min_time(2,"max", False))-2019-03-09 23:59:59.999999
# print(to_n_datetime_max_min_time(0,"min", False))-2019-03-07 00:00:00
# print(to_n_datetime_max_min_time(-1,"min", False))-2019-03-06 00:00:00
# print(to_n_datetime_max_min_time(-5, "max", True))-2019-03-02 23:59:59
def to_n_datetime_max_min_time(n, types, is_format):
    if types == "max":
        return_time = datetime.datetime.combine(datetime.date.today() + datetime.timedelta(days=n), datetime.time.max)
    elif types == "min":
        return_time = datetime.datetime.combine(datetime.date.today() + datetime.timedelta(days=n), datetime.time.min)
    if (is_format):
        return_time = return_time.strftime('%Y-%m-%d %H:%M:%S')
    return return_time


# 获取间隔n月的第一天的最小时间和最后一天的最大时间 此方法 n为-1时 传first 有bug 其他传 -n n很大 都有bug
# 此方法弃用 存在严重bug 请使用【to_get_month_first_last_day_datetime_max_min_time_pro】方法.
# @param  n,first_or_last_type,types,isFormat; n代表几月，可以正值(n月后)，可以负值(n月前),0代表当前月 ;
#                          first_or_last_type取值有first和last,first代表月的第一天,last代表月的最后一天
#                          types取值有max和min,max代表输出当前时间最大时间，min代表输出当前时间最小时间;
#                          isFormat是否格式化输出，布尔值为True,格式化输出str类型时间,为False,不格式化输出，直接返回datetime类型时间。
# @return 符合要求的datetime格式日期
def to_get_month_first_last_day_datetime_max_min_time(n, first_or_last_type, types, is_format):
    if first_or_last_type == "first":
        return_time_day = datetime.datetime(datetime.date.today().year, datetime.date.today().month + n, 1)
    elif first_or_last_type == "last":
        if datetime.date.today().month + 1 + n == 13:  # 如果这个if满足，代表当前月是12月份，取last直接下面操作即可,得到2019-12-31 00:00:00 (备注:12月不可以加1月那样操作了,因为没有月份中没有13月)
            return_time_day = datetime.datetime(datetime.date.today().year, datetime.date.today().month, 31)
        else:  # 其他情况 都是 先获得当前月份加上1月的第一天再减去1天 来得到当前月份的最后一天
            return_time_day = datetime.datetime(datetime.date.today().year, datetime.date.today().month + 1 + n, 1) - datetime.timedelta(1)

    if types == "max":
        return_time = datetime.datetime.combine(return_time_day + datetime.timedelta(days=0), datetime.time.max)
    elif types == "min":
        return_time = datetime.datetime.combine(return_time_day + datetime.timedelta(days=0), datetime.time.min)

    if (is_format):
        return_time = return_time.strftime('%Y-%m-%d %H:%M:%S')
    return return_time


# 获取间隔n月的第一天的最小时间和最后一天的最大时间 此方法 n为-1时 传first 有bug 其他传 -n n很大 都有bug 这是方法【to_get_month_first_last_day_datetime_max_min_time】bug修复版本
# 此方法彻底修复bug
# @param  n,first_or_last_type,types,isFormat; n代表几月，可以正值(n月后)，可以负值(n月前),0代表当前月 ;
#                          first_or_last_type取值有first和last,first代表月的第一天,last代表月的最后一天
#                          types取值有max和min,max代表输出当前时间最大时间，min代表输出当前时间最小时间;
#                          isFormat是否格式化输出，布尔值为True,格式化输出str类型时间,为False,不格式化输出，直接返回datetime类型时间。
# @return 符合要求的datetime格式日期
def to_get_month_first_last_day_datetime_max_min_time_pro(n, first_or_last_type, types, is_format):
    if first_or_last_type == "first":
        return_time_day = get_datetime_year_month_for_monthly(n, 1)
    elif first_or_last_type == "last":
        # 后一月的1号 减 1天 就是 月 的最后一天
        return_time_day = get_datetime_year_month_for_monthly(n + 1, 1) - datetime.timedelta(1)

    if types == "max":
        return_time = datetime.datetime.combine(return_time_day + datetime.timedelta(days=0), datetime.time.max)
    elif types == "min":
        return_time = datetime.datetime.combine(return_time_day + datetime.timedelta(days=0), datetime.time.min)

    if (is_format):
        return_time = return_time.strftime('%Y-%m-%d %H:%M:%S')
    return return_time


# 月份加减的函数 获取 datetime
# param n: 要加(减)的月份数量
# param which_day: 哪一天 用来拼接datetime
# return: datetime
# 测试
# print(add_month('201501', 5))
# print(add_month("202101", 0))  # 202101
# print(add_month("202101", 1))  # 202102
# print(add_month("202101", 2))  # 202103
# print(add_month("202101", -1))  # 202012
# print(add_month("202101", -2))  # 202011
def get_datetime_year_month_for_monthly(n, which_day):
    # 处理年
    this_year = str(datetime.date.today().year)
    # 处理月
    this_month = str(datetime.date.today().month)
    # print(len(str(rdm.month)))
    # 如果月份小于10 补零 让9变为09月
    if len(this_month) < 2:
        this_month = "0" + this_month
    str_year_month = add_month(this_year + this_month, n)
    return datetime.datetime(int(str_year_month[0:4]), int(str_year_month[4:6]), which_day)


# 月份加减的函数
# param data_month: 时间(201501)
# param num: 要加(减)的月份数量
# return: 时间(str)
# 测试
# print(add_month('201501', 5))
def add_month(data_month, num):
    """
    月份加减函数,返回字符串类型
    :param data_month: 时间(201501)
    :param num: 要加(减)的月份数量
    :return: 时间(str)
    """
    months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    data_month = int(data_month)
    num = int(num)
    year = data_month // 100
    new_list = []
    s = math.ceil(abs(num) / 12)
    for i in range(int(-s), s + 1):
        new_list += [str(year + i) + x for x in months]
    new_list = [int(x) for x in new_list]
    return str(new_list[new_list.index(data_month) + num])


# 从oracle数据库SCADA_FLMETER_DATA读取所有符合条件的数据
# 带参数查询
# @param  org_id 要查询机构号
# @param  days 0代表今天 +n代表n天后 -n代表n天前
# @return 处理结果 True成功 False失败
def select_sfd_by_where(org_id, days):
    sql = "select * from SCADA_FLMETER_DATA where SFD_ORG_ID= :orgid and INSTANT_TIME between :minTime AND :maxTime "
    yesterday_min = to_n_datetime_max_min_time(days, "min", False)
    yesterday_max = to_n_datetime_max_min_time(days, "max", False)
    data = [{"orgid": org_id, "minTime": yesterday_min, "maxTime": yesterday_max}]
    fc = db.select_by_where_many_params_dict(sql, data)
    print("总共抄表数据:", len(fc))
    # for row in fc:
    #     print(row)
    return fc, data


# 从oracle数据库SCADA_FLMETER_DATA读取所有符合条件的数据 for 月报表
# 带参数查询
# @param  org_id 要查询机构号
# @param  months 要查询的月 0代表当前月 -n代表前n月 +n代表后n月
# @return 处理结果 True成功 False失败
def select_sfd_by_where_for_monthly(org_id, months):
    sql = "select * from SCADA_FLMETER_DATA where SFD_ORG_ID= :orgid and INSTANT_TIME between :minTime AND :maxTime "
    month_first_min = to_get_month_first_last_day_datetime_max_min_time_pro(months, "first", "min", False)  # 方法:获取间隔n月的第一天的最小时间和最后一天的最大时间
    month_last_max = to_get_month_first_last_day_datetime_max_min_time_pro(months, "last", "max", False)
    data = [{"orgid": org_id, "minTime": month_first_min, "maxTime": month_last_max}]
    fc = db.select_by_where_many_params_dict(sql, data)
    print("总共抄表数据:", len(fc))
    # for row in fc:
    #     print(row)
    return fc, data


# 从oracle数据库SCADA_FLMETER_DATA读取所有符合条件的数据 for 月报表 v2
# select_sfd_by_where_for_monthly_last_min_and_last_max 得到月份的最后一天的最小时间和最后一天的最大时间之间的数据
# 带参数查询
# @param  org_id 要查询机构号
# @param  months 要查询的月 0代表当前月 -n代表前n月 +n代表后n月
# @return 处理结果 True成功 False失败
def select_sfd_by_where_for_monthly_last_min_and_last_max(org_id, months):
    sql = "select * from SCADA_FLMETER_DATA where SFD_ORG_ID= :orgid and INSTANT_TIME between :minTime AND :maxTime "
    month_first_min = to_get_month_first_last_day_datetime_max_min_time_pro(months, "last", "min", False)  # 方法:获取间隔n月的最后一天的最小时间和最后一天的最大时间
    month_last_max = to_get_month_first_last_day_datetime_max_min_time_pro(months, "last", "max", False)
    data = [{"orgid": org_id, "minTime": month_first_min, "maxTime": month_last_max}]
    fc = db.select_by_where_many_params_dict(sql, data)
    print("总共抄表数据:", len(fc))
    # for row in fc:
    #     print(row)
    return fc, data


# 处理好数据写入oracle for 日报表
# @param  日报表对象report_daily_model-主键【srd_org_id 机构号,srd_id 记录ID 】其他字段
# @return 处理结果 True成功 False失败
def ok_processing_data_insert_into_oracle(report_daily_model, *args, **kwargs):
    print(report_daily_model.flmeter_no)
    fc = select_scada_report_daily_is_null_or_not(report_daily_model.srd_org_id, report_daily_model.flmeter_no,report_daily_model.year,report_daily_model.month, report_daily_model.day)
    print("总列表长度:", len(fc))
    if len(fc) == 0:  # 如果为0 代表无数据 先生成一条
        insert_scada_report_daily(report_daily_model)
        pass
    else:  # 如果不为0 则根据SRD_ORG_ID，SRD_ID直接删除此条数据 再新增一条
        ok_srd_id = fc[0]['SRD_ID']
        del_scada_report_daily(report_daily_model.srd_org_id, ok_srd_id)
        insert_scada_report_daily(report_daily_model)
        pass
    # print(args)  # (1, 2, 3, '123')
    # print(kwargs)
    print(report_daily_model.flmeter_no+"处理好数据已写入oracle")
    pass
    return True


# 处理好数据写入oracle for 月报表
# @param  月报表对象report_monthly_model-主键【srd_org_id 机构号,srd_id 记录ID 】其他字段
# @return 处理结果 True成功 False失败
def ok_processing_data_insert_into_oracle_for_monthly(report_monthly_model, *args, **kwargs):
    print(report_monthly_model.flmeter_no)
    fc = select_scada_report_monthly_is_null_or_not(report_monthly_model.srm_org_id, report_monthly_model.flmeter_no,report_monthly_model.year,report_monthly_model.month)
    print("总列表长度:", len(fc))
    if len(fc) == 0:  # 如果为0 代表无数据 先生成一条
        insert_scada_report_monthly(report_monthly_model)
        pass
    else:  # 如果不为0 则根据SRD_ORG_ID，SRD_ID直接删除此条数据 再新增一条
        ok_srm_id = fc[0]['SRM_ID']
        del_scada_report_monthly(report_monthly_model.srm_org_id, ok_srm_id)
        insert_scada_report_monthly(report_monthly_model)
        pass
    # print(args)  # (1, 2, 3, '123')
    # print(kwargs)
    print(report_monthly_model.flmeter_no+"处理好数据已写入oracle")
    pass
    return True


# 查询SCADA_REPORT_DAILY表中 此当前年月日数据 是否存在 不存在 新增 存在的话 删除 再新增
# @param srd_org_id 机构号
# @param flmeter_no 流量计编号
# @param year  年
# @param month  月
# @param day  日
# @return 返回查询出的数据list
def select_scada_report_daily_is_null_or_not(srd_org_id, flmeter_no, year, month, day):
    sql = "select * from SCADA_REPORT_DAILY where SRD_ORG_ID= :srd_org_id  and FLMETER_NO= :flmeter_no and YEAR = :year and MONTH = :month and DAY = :day"
    data = [{"srd_org_id": srd_org_id, "flmeter_no": flmeter_no, "year": year, "month": month, "day": day}]
    fc = db.select_by_where_many_params_dict(sql, data)
    return fc


# 查询SCADA_REPORT_MONTHLY表中 此当前年月数据 是否存在 不存在 新增 存在的话 删除 再新增 for 月报表
# @param srm_org_id 机构号
# @param flmeter_no 流量计编号
# @param year  年
# @param month  月
# @return 返回查询出的数据list
def select_scada_report_monthly_is_null_or_not(srm_org_id, flmeter_no, year, month):
    sql = "select * from SCADA_REPORT_MONTHLY where SRM_ORG_ID= :srm_org_id  and FLMETER_NO= :flmeter_no and YEAR = :year and MONTH = :month"
    data = [{"srm_org_id": srm_org_id, "flmeter_no": flmeter_no, "year": year, "month": month}]
    fc = db.select_by_where_many_params_dict(sql, data)
    return fc


# 新增SCADA_REPORT_DAILY
# @param report_daily_model 日报表对象类
# @return null 插入成功或失败
def insert_scada_report_daily(report_daily_model):
    insert_sql = "INSERT INTO SCADA_REPORT_DAILY (SRD_ORG_ID,SRD_ID, RTU_NO,FLMETER_NO,CUSTOMER_NO," \
                 "REPORT_TIME,YEAR,MONTH,DAY, HOUR," \
                 "STD_SUM,WORK_SUM,STD_FLOW,WORK_FLOW,TEMPERATURE," \
                 "PRESSURE,PRICE,USE_VOLUME_WORK, USE_VOLUME_STD,USE_MONEY," \
                 "SUM_TOTAL_VOLUME,SUM_TOTAL_MONEY,TOTAL_BUY_VOLUME,TOTAL_BUY_MONEY,REMAIN_MONEY," \
                 "REMAIN_VOLUME,FM_STATE,RTU_STATE,VALVE_STATE,POWER_VOLTAGE," \
                 "BATTERY_VOLTAGE,BATTERY_LEVEL,PRESS_IN,PRESS_OUT,TEMP_IN," \
                 "TEMP_OUT,RSSI, SRD_STATUS ) " \
                 "VALUES" \
                 "(:srd_org_id,:srd_id, :rtu_no,:flmeter_no,:customer_no," \
                 ":report_time,:year,:month,:day, :hour," \
                 ":std_sum,:work_sum,:std_flow,:work_flow,:temperature," \
                 ":pressure,:price,:use_volume_work, :use_volume_std,:use_money," \
                 ":sum_total_volume,:sum_total_money,:total_buy_volume,:total_buy_money,:remain_money," \
                 ":remain_volume,:fm_state,:rtu_state,:valve_state,:power_voltage," \
                 ":battery_voltage,:battery_level,:press_in,:press_out,:temp_in," \
                 ":temp_out,:rssi, :srd_status)"
    data = [{"srd_org_id": report_daily_model.srd_org_id, "srd_id": report_daily_model.srd_id, "rtu_no": report_daily_model.rtu_no, "flmeter_no": report_daily_model.flmeter_no,"customer_no": report_daily_model.customer_no,
             "report_time": report_daily_model.report_time, "year": report_daily_model.year, "month": report_daily_model.month, "day": report_daily_model.day, "hour": report_daily_model.hour,
             "std_sum": report_daily_model.std_sum, "work_sum": report_daily_model.work_sum, "std_flow": report_daily_model.std_flow, "work_flow": report_daily_model.work_flow, "temperature": report_daily_model.temperature,
             "pressure": report_daily_model.pressure, "price": report_daily_model.price, "use_volume_work": report_daily_model.use_volume_work, "use_volume_std": report_daily_model.use_volume_std, "use_money": report_daily_model.use_money,
             "sum_total_volume": report_daily_model.sum_total_volume, "sum_total_money": report_daily_model.sum_total_money, "total_buy_volume": report_daily_model.total_buy_volume, "total_buy_money": report_daily_model.total_buy_money, "remain_money": report_daily_model.remain_money,
             "remain_volume": report_daily_model.remain_volume, "fm_state": report_daily_model.fm_state, "rtu_state": report_daily_model.rtu_state, "valve_state": report_daily_model.valve_state, "power_voltage": report_daily_model.power_voltage,
             "battery_voltage": report_daily_model.battery_voltage, "battery_level": report_daily_model.battery_level, "press_in": report_daily_model.press_in, "press_out": report_daily_model.press_out, "temp_in": report_daily_model.temp_in,
             "temp_out": report_daily_model.temp_out, "rssi": report_daily_model.rssi, "srd_status": report_daily_model.srd_status}]
    db.dml_by_where(insert_sql, data)  # ok
    print('insert_scada_report_daily ok')


# 新增SCADA_REPORT_MONTHLY
# @param model 月报表对象类
# @return null 插入成功或失败
def insert_scada_report_monthly(model):
    insert_sql = "INSERT INTO SCADA_REPORT_MONTHLY (SRM_ORG_ID,SRM_ID, RTU_NO,FLMETER_NO,CUSTOMER_NO," \
                 "REPORT_TIME,YEAR,MONTH,DAY, STD_SUM," \
                 "WORK_SUM,MAX_STD_FLOW,MIN_STD_FLOW,AVG_STD_FLOW,MAX_STD_FLOW_TIME," \
                 "MIN_STD_FLOW_TIME,MAX_WORK_FLOW,MIN_WORK_FLOW,AVG_WORK_FLOW,MAX_WORK_FLOW_TIME," \
                 "MIN_WORK_FLOW_TIME,MAX_TEMPERATURE,MIN_TEMPERATURE,AVG_TEMPERATURE,MAX_TEMP_TIME," \
                 "MIN_TEMP_TIME,MAX_PRESS,MIN_PRESS,AVG_PRESS,MAX_PRESS_TIME," \
                 "MIN_PRESS_TIME,PRICE,USE_VOLUME_WORK,USE_VOLUME_STD,USE_MONEY," \
                 "SUM_TOTAL_VOLUME,SUM_TOTAL_MONEY,TOTAL_BUY_VOLUME,TOTAL_BUY_MONEY,REMAIN_MONEY," \
                 "REMAIN_VOLUME,FM_STATE,FM_STATE_MSG,RTU_STATE,RTU_STATE_MSG,VALVE_STATE,VALVE_STATE_MSG,POWER_VOLTAGE," \
                 "BATTERY_VOLTAGE,BATTERY_LEVEL,PRESS_IN,PRESS_OUT,TEMP_IN," \
                 "TEMP_OUT,RSSI,SRM_STATUS )"\
                 "VALUES" \
                 "(:srm_org_id,:srm_id, :rtu_no,:flmeter_no,:customer_no," \
                 ":report_time,:year,:month,:day, :std_sum," \
                 ":work_sum,:max_std_flow,:min_std_flow,:avg_std_flow,:max_std_flow_time," \
                 ":min_std_flow_time,:max_work_flow,:min_work_flow, :avg_work_flow,:max_work_flow_time," \
                 ":min_work_flow_time,:max_temperature,:min_temperature,:avg_temperature,:max_temp_time," \
                 ":min_temp_time,:max_press,:min_press,:avg_press,:max_press_time," \
                 ":min_press_time,:price,:use_volume_work,:use_volume_std,:use_money," \
                 ":sum_total_volume,:sum_total_money,:total_buy_volume,:total_buy_money,:remain_money," \
                 ":remain_volume,:fm_state,:fm_state_msg,:rtu_state,:rtu_state_msg,:valve_state,:valve_state_msg,:power_voltage," \
                 ":battery_voltage,:battery_level,:press_in,:press_out,:temp_in," \
                 ":temp_out,:rssi, :srm_status)"
    data = [{"srm_org_id": model.srm_org_id, "srm_id": model.srm_id, "rtu_no": model.rtu_no, "flmeter_no": model.flmeter_no,"customer_no": model.customer_no,
             "report_time": model.report_time, "year": model.year, "month": model.month, "day": model.day, "std_sum": model.std_sum,
             "work_sum": model.work_sum, "max_std_flow": model.max_std_flow, "min_std_flow": model.min_std_flow, "avg_std_flow": model.avg_std_flow, "max_std_flow_time": model.max_std_flow_time,
             "min_std_flow_time": model.min_std_flow_time, "max_work_flow": model.max_work_flow, "min_work_flow": model.min_work_flow, "avg_work_flow": model.avg_work_flow, "max_work_flow_time": model.max_work_flow_time,
             "min_work_flow_time": model.min_work_flow_time, "max_temperature": model.max_temperature, "min_temperature": model.min_temperature, "avg_temperature": model.avg_temperature, "max_temp_time": model.max_temp_time,
             "min_temp_time": model.min_temp_time, "max_press": model.max_press, "min_press": model.min_press, "avg_press": model.avg_press, "max_press_time": model.max_press_time,
             "min_press_time": model.min_press_time, "price": model.price, "use_volume_work": model.use_volume_work,"use_volume_std": model.use_volume_std, "use_money": model.use_money,
             "sum_total_volume": model.sum_total_volume, "sum_total_money": model.sum_total_money, "total_buy_volume": model.total_buy_volume, "total_buy_money": model.total_buy_money,"remain_money": model.remain_money,
             "remain_volume": model.remain_volume, "fm_state": model.fm_state,"fm_state_msg": model.fm_state_msg, "rtu_state": model.rtu_state,"rtu_state_msg": model.rtu_state_msg, "valve_state": model.valve_state, "valve_state_msg": model.valve_state_msg,"power_voltage": model.power_voltage,
             "battery_voltage": model.battery_voltage, "battery_level": model.battery_level, "press_in": model.press_in, "press_out": model.press_out, "temp_in": model.temp_in,
             "temp_out": model.temp_out, "rssi": model.rssi, "srm_status": model.srm_status}]
    db.dml_by_where(insert_sql, data)  # ok
    print('insert_scada_report_monthly ok')


# 删除SCADA_REPORT_DAILY 带条件参数 删除数据
# @param srd_org_id 机构号
# @param srd_id 记录id
# @return null 删除成功或失败
def del_scada_report_daily(srd_org_id, srd_id):
    sql = "delete from SCADA_REPORT_DAILY where SRD_ORG_ID = :1 and SRD_ID=:2"
    data = [(srd_org_id, srd_id)]
    db.dml_by_where(sql, data)
    print('del_by_where ok')


# 删除SCADA_REPORT_MONTHLY 带条件参数 删除数据 for 月报表
# @param srm_org_id 机构号
# @param srm_id 记录id
# @return null 删除成功或失败
def del_scada_report_monthly(srm_org_id, srm_id):
    sql = "delete from SCADA_REPORT_MONTHLY where SRM_ORG_ID = :1 and SRM_ID=:2"
    data = [(srm_org_id, srm_id)]
    db.dml_by_where(sql, data)
    print('del_by_where ok')


# 删除SCADA_REPORT_MONTHLY 带条件参数 删除数据 删除所有 指定到年月
# @param srh_year 年
# @param srh_month 月
# @return null 删除成功或失败
def del_all_scada_report_monthly_by_year_month(srh_year, srh_month):
    sql = "delete from SCADA_REPORT_MONTHLY where YEAR=:1 and MONTH=:2"
    data = [(srh_year, srh_month)]
    db.dml_by_where(sql, data)
    print('del_all_scada_report_monthly_by_year_month ok')


# 获取所有需要跑脚本的机构信息
# 字段：ORG_REPORT_GENERATE 是否计算生成报表：0不生成，1夜间生成，2白天生成
# 根据 ORG_ID 排序,倒叙
def get_all_org_id_for_run_py_command_script_from_select_db():
    sql = "select * from ORGANIZATION where ORG_REPORT_GENERATE= :org_report_generate order by ORG_ID desc"
    data = [{"org_report_generate": "2"}]
    fc = db.select_by_where_many_params_dict(sql, data)
    return fc


# 周期内平均值计算方法
# @param data_list 计算的字典列表 key 对应的键
# @return 处理之后的周期内平均值-返回四舍五入-再处理成str类型返回
def get_average_period(data_list, key):
    count_nums = 0
    total_size = len(data_list)
    for x in data_list:
        if x[key] is not None:
            if is_number(x[key]):
                if float(x[key]) < 0:
                    x[key] = 0
                count_nums += float(x[key])
            else:
                count_nums += 0
        else:
            count_nums += 0
    ok_value = count_nums // total_size
    return str(round(ok_value, 2))  # 返回四舍五入


# 数据处理-主逻辑处理-主要函数方法
# @param data_for_processing 要处理的原数据
# @param last_data_for_processing 要处理的原数据-上一次的
# @param org_id 机构号
# @param 字典传参 query_datetime 查询操作的日期
# @return 处理结果 True成功 False失败
def data_processing(data_for_processing, last_data_for_processing, org_id, **kwargs):
    rm_repeat_sfd_data_list = []  # 用于临时存放已删除重复的字典数据
    last_rm_repeat_sfd_data_list = []  # 用于临时存放已删除重复的字典数据 上一月的 上一次的

    flmeter_no_set = set()  # set是一个无序且不重复的元素集合-注意在创建空集合的时候只能使用s=set()，因为s={}创建的是空字典
    for x in data_for_processing:
        flmeter_no_set.add(x['FLMETER_NO'])
    print('不同的表计号共有个数:', len(flmeter_no_set))  # 19

    print('根据表计号，进行数据的再次筛选，处理，写入数据库')
    print('----------------------------------------------------------------------------------------')

    # 根据表计号，进行数据的再次筛选，处理，写入数据库
    flmeter_no_set_copy = flmeter_no_set.copy()
    for fno in flmeter_no_set:
        print(fno)
        # 以下为处理逻辑
        # 首先根据表计号，在原字典数据【data_for_processing】中筛选出所有此表计的数据
        for xx in data_for_processing:
            if xx['FLMETER_NO'] == fno:
                rm_repeat_sfd_data_list.append(xx)
            # print(rm_repeat_sfd_data_list)
        # print(len(rm_repeat_sfd_data_list))

        # 在查询当月的上一月数据中 for循环
        for xx in last_data_for_processing:
            if xx['FLMETER_NO'] == fno:
                last_rm_repeat_sfd_data_list.append(xx)

        # 将std_flow，work_flow，temperature,pressure 全部转为float,再继续操作,为后面数字排序做准备
        for xyz in rm_repeat_sfd_data_list:
            if xyz["STD_FLOW"] is None:
                xyz["STD_FLOW"] = float(0)
            else:
                xyz["STD_FLOW"] = float(xyz["STD_FLOW"])

            if xyz["WORK_FLOW"] is None:
                xyz["WORK_FLOW"] = float(0)
            else:
                xyz["WORK_FLOW"] = float(xyz["WORK_FLOW"])

            if xyz["TEMPERATURE"] is None:
                xyz["TEMPERATURE"] = float(0)
            else:
                xyz["TEMPERATURE"] = float(xyz["TEMPERATURE"])

            if  xyz["PRESSURE"] is None:
                xyz["PRESSURE"] = float(0)
            else:
                xyz["PRESSURE"] = float(xyz["PRESSURE"])

        # 查询当月的上一月数据中 将std_flow，work_flow，temperature,pressure 全部转为float,再继续操作,为后面数字排序做准备
        if len(last_rm_repeat_sfd_data_list) > 0:  # 如果大于0 进行以下操作
            for xyz in last_rm_repeat_sfd_data_list:
                if xyz["STD_FLOW"] is None:
                    xyz["STD_FLOW"] = float(0)
                else:
                    xyz["STD_FLOW"] = float(xyz["STD_FLOW"])

                if xyz["WORK_FLOW"] is None:
                    xyz["WORK_FLOW"] = float(0)
                else:
                    xyz["WORK_FLOW"] = float(xyz["WORK_FLOW"])

                if xyz["TEMPERATURE"] is None:
                    xyz["TEMPERATURE"] = float(0)
                else:
                    xyz["TEMPERATURE"] = float(xyz["TEMPERATURE"])

                if xyz["PRESSURE"] is None:
                    xyz["PRESSURE"] = float(0)
                else:
                    xyz["PRESSURE"] = float(xyz["PRESSURE"])
                # xyz["STD_FLOW"] = float(xyz["STD_FLOW"])
                # xyz["WORK_FLOW"] = float(xyz["WORK_FLOW"])
                # xyz["TEMPERATURE"] = float(xyz["TEMPERATURE"])
                # xyz["PRESSURE"] = float(xyz["PRESSURE"])

        # print(rm_repeat_sfd_data_list)
        print("此查询区间,当前编号下总共抄表记录:", len(rm_repeat_sfd_data_list))
        print("此查询区间,上一月最后一天内当前编号下总共抄表记录:", len(last_rm_repeat_sfd_data_list))

        # 此表计数据字典列表 排序 按照采集时间INSTANT_TIME排序 默认升序 如果要降序排序,可以指定reverse=True
        sorted_rm_repeat_sfd_data_list = sorted(rm_repeat_sfd_data_list, key=operator.itemgetter('INSTANT_TIME'), reverse=False)

        # 上一月总抄表记录 排序 按照采集时间INSTANT_TIME排序 默认升序 如果要降序排序,可以指定reverse=True
        last_sorted_rm_repeat_sfd_data_list = []
        if len(last_rm_repeat_sfd_data_list) > 0:  # 如果大于0 进行以下操作
            last_sorted_rm_repeat_sfd_data_list = sorted(last_rm_repeat_sfd_data_list, key=operator.itemgetter('INSTANT_TIME'), reverse=False)

        # 排序完成之后，具体字段补充

        # 新建一个月报表类，用于接收收据
        rdm = ReportMonthlyModel()

        # 机构号
        rdm.srm_org_id = sorted_rm_repeat_sfd_data_list[0]['SFD_ORG_ID']

        # 记录id srd_id 移到line385

        # RTU编号
        rdm.rtu_no = sorted_rm_repeat_sfd_data_list[0]['RTU_NO']
        # 流量计编号
        rdm.flmeter_no = sorted_rm_repeat_sfd_data_list[0]['FLMETER_NO']
        # 客户编号
        rdm.customer_no = sorted_rm_repeat_sfd_data_list[0]['CUSTOMER_NO']

        # 得到当前时间datetime
        now_datetime = datetime.datetime.today()
        # print(now_datetime.year, now_datetime.month, now_datetime.day, now_datetime.hour, now_datetime.minute,now_datetime.second)  # 2019 3 8 12 52 10

        # 报表时间 年 月 日 时
        rdm.report_time = now_datetime

        # 将查询时间的年月日 分别赋值到对应字段
        # 处理年
        rdm.year = str(kwargs['query_datetime'].year)
        # 处理月
        # print(len(str(rdm.month)))
        # 如果月份小于10 补零 让9变为09月
        if len(str(kwargs['query_datetime'].month)) < 2:
            rdm.month = "0" + str(kwargs['query_datetime'].month)
        else:
            rdm.month = str(kwargs['query_datetime'].month)

        # 处理日 不处理了 togo
        # print(len(str(rdm.day)))
        # 如果日小于10 补零 让9变为09日
        # if len(str(kwargs['query_datetime'].day)) < 2:
        #     rdm.day = "0" + str(kwargs['query_datetime'].day)
        # else:
        #     rdm.day = str(kwargs['query_datetime'].day)

        # 处理小时 不处理了 togo
        # print(len(str(rdm.hour)))
        # 如果小时小于10 补零 让9变为09小时
        # if len(str(now_datetime.hour)) < 2:
        #     rdm.hour = "0" + str(now_datetime.hour)
        # else:
        #     rdm.hour = str(now_datetime.hour)

        # 记录ID-取自动递增流水号
        ssn_org_id = org_id  # 传入过来的org_id
        ssn_key_name = "SCADA_REPORT_MONTHLY"  # 如需修改为其他表的递增流水，请自行修改
        ok_srm_id = get_sys_serial_no(db, ssn_org_id, ssn_key_name, rdm.year, rdm.month)  # 导入获取流水号方法
        print(ok_srm_id)
        rdm.srm_id = ssn_org_id + rdm.year + rdm.month + ok_srm_id

        # 标况总量（期末数）
        rdm.std_sum = sorted_rm_repeat_sfd_data_list[len(sorted_rm_repeat_sfd_data_list) - 1]['STD_SUM']  # 默认升序，列表最后一个元素，值最大
        # 工况总量（期末数）
        rdm.work_sum = sorted_rm_repeat_sfd_data_list[len(sorted_rm_repeat_sfd_data_list) - 1]['WORK_SUM']  # 默认升序，列表最后一个元素，值最大

        # 通过标况流量 STD_FLOW 排序 默认升序 如果要降序排序,可以指定reverse=True
        sorted_rm_repeat_sfd_data_list_by_std_flow = sorted(rm_repeat_sfd_data_list, key=operator.itemgetter('STD_FLOW'), reverse=False)
        # 标况流量（周期内最大值）
        rdm.max_std_flow = str(sorted_rm_repeat_sfd_data_list_by_std_flow[len(sorted_rm_repeat_sfd_data_list_by_std_flow) - 1]['STD_FLOW'])
        # 标况流量（周期内最小值）
        rdm.min_std_flow = str(sorted_rm_repeat_sfd_data_list_by_std_flow[0]['STD_FLOW'])
        # 标况流量（周期内平均值）- rdm.std_flow
        rdm.avg_std_flow = get_average_period(sorted_rm_repeat_sfd_data_list, "STD_FLOW")  # 使用周期内平均值计算方法 计算平均值
        # 最大标况流量时间
        rdm.max_std_flow_time = sorted_rm_repeat_sfd_data_list_by_std_flow[len(sorted_rm_repeat_sfd_data_list_by_std_flow) - 1]['RECEIV_TIME']

        # 最小标况流量时间
        rdm.min_std_flow_time = sorted_rm_repeat_sfd_data_list_by_std_flow[0]['RECEIV_TIME']

        # 通过工况流量 WORK_FLOW 排序 默认升序 如果要降序排序,可以指定reverse=True
        sorted_rm_repeat_sfd_data_list_by_work_flow = sorted(rm_repeat_sfd_data_list, key=operator.itemgetter('WORK_FLOW'), reverse=False)
        # 工况流量（周期内最大值）
        rdm.max_work_flow = str(sorted_rm_repeat_sfd_data_list_by_work_flow[len(sorted_rm_repeat_sfd_data_list_by_work_flow) - 1]['WORK_FLOW'])
        # 工况流量（周期内最小值）
        rdm.min_work_flow = str(sorted_rm_repeat_sfd_data_list_by_work_flow[0]['WORK_FLOW'])
        # 工况流量（周期内平均值）-rdm.work_flow
        rdm.avg_work_flow = get_average_period(sorted_rm_repeat_sfd_data_list, "WORK_FLOW")
        # 最大工况流量时间
        rdm.max_work_flow_time = sorted_rm_repeat_sfd_data_list_by_work_flow[len(sorted_rm_repeat_sfd_data_list_by_work_flow) - 1]['RECEIV_TIME']

        # 最小工况流量时间
        rdm.min_work_flow_time = sorted_rm_repeat_sfd_data_list_by_work_flow[0]['RECEIV_TIME']

        # 通过温度 TEMPERATURE 排序 默认升序 如果要降序排序,可以指定reverse=True
        sorted_rm_repeat_sfd_data_list_by_temperature = sorted(rm_repeat_sfd_data_list,key=operator.itemgetter('TEMPERATURE'), reverse=False)
        # 温度（周期内最大值）
        rdm.max_temperature = str(sorted_rm_repeat_sfd_data_list_by_temperature[len(sorted_rm_repeat_sfd_data_list_by_temperature) - 1]['TEMPERATURE'])
        # 温度（周期内最小值）
        rdm.min_temperature = str(sorted_rm_repeat_sfd_data_list_by_temperature[0]['TEMPERATURE'])
        # 温度（周期内平均值）-rdm.temperature
        rdm.avg_temperature = get_average_period(sorted_rm_repeat_sfd_data_list, "TEMPERATURE")
        # 最高温度时间
        rdm.max_temp_time = sorted_rm_repeat_sfd_data_list_by_temperature[len(sorted_rm_repeat_sfd_data_list_by_temperature) - 1]['RECEIV_TIME']

        # 最低温度时间
        rdm.min_temp_time = sorted_rm_repeat_sfd_data_list_by_temperature[0]['RECEIV_TIME']

        # 通过温度 PRESSURE 排序 默认升序 如果要降序排序,可以指定reverse=True
        sorted_rm_repeat_sfd_data_list_by_pressure = sorted(rm_repeat_sfd_data_list,key=operator.itemgetter('PRESSURE'), reverse=False)

        # 压力（周期内最高值）
        rdm.max_press = str(sorted_rm_repeat_sfd_data_list_by_pressure[len(sorted_rm_repeat_sfd_data_list_by_pressure) - 1]['PRESSURE'])
        # 压力（周期内最低值）
        rdm.min_press = str(sorted_rm_repeat_sfd_data_list_by_pressure[0]['PRESSURE'])
        # 压力（周期内平均值）-rdm.pressure
        rdm.avg_press = get_average_period(sorted_rm_repeat_sfd_data_list, "PRESSURE")
        # 最高压力时间
        rdm.max_press_time = sorted_rm_repeat_sfd_data_list_by_pressure[len(sorted_rm_repeat_sfd_data_list_by_pressure) - 1]['RECEIV_TIME']

        # 最低压力时间
        rdm.min_press_time = sorted_rm_repeat_sfd_data_list_by_pressure[0]['RECEIV_TIME']

        # 单价（期末数）
        rdm.price = sorted_rm_repeat_sfd_data_list[len(sorted_rm_repeat_sfd_data_list) - 1]['PRICE']

        # 周期内工况使用量（周期内期末数-期初数）
        max_work_sum = sorted_rm_repeat_sfd_data_list[len(sorted_rm_repeat_sfd_data_list) - 1]['WORK_SUM']
        min_work_sum = sorted_rm_repeat_sfd_data_list[0]['WORK_SUM']
        if max_work_sum is None:
            max_work_sum = str(0)
        if min_work_sum is None:
            min_work_sum = str(0)
        if len(last_rm_repeat_sfd_data_list) > 0:  # （本期期末数-上期期末数）
            last_max_work_sum = last_sorted_rm_repeat_sfd_data_list[len(last_rm_repeat_sfd_data_list) - 1]['WORK_SUM']
            if last_max_work_sum is None:
                last_max_work_sum = str(0)
            rdm.use_volume_work = str(round(float(max_work_sum) - float(last_max_work_sum), 2))
        else:  # （本周期内期末数-本周期内期初数）
            rdm.use_volume_work = str(round(float(max_work_sum) - float(min_work_sum), 2))
        if float(rdm.use_volume_work) < 0:  # 如果use_volume_work计算出来小于0，则直接置为0
            rdm.use_volume_work = str(0)
            print(rdm.flmeter_no, "☆ use_volume_work <0 置为0")

        # 周期内标况使用量（周期内期末数 - 期初数）
        max_std_sum = sorted_rm_repeat_sfd_data_list[len(sorted_rm_repeat_sfd_data_list) - 1]['SUM_TOTAL']  # 默认升序，列表最后一个元素，值最大
        min_std_sum = sorted_rm_repeat_sfd_data_list[0]['SUM_TOTAL']  # 默认升序，列表第一个元素，值最小
        if max_std_sum is None:
            max_std_sum = str(0)
        if min_std_sum is None:
            min_std_sum = str(0)
        if len(last_rm_repeat_sfd_data_list) > 0:  # （本期期末数-上期期末数）
            if last_sorted_rm_repeat_sfd_data_list[len(last_rm_repeat_sfd_data_list) - 1]['SUM_TOTAL'] is None:
                last_sorted_rm_repeat_sfd_data_list[len(last_rm_repeat_sfd_data_list) - 1]['SUM_TOTAL'] = str(0)
            rdm.use_volume_std = str(round(float(max_std_sum) - float(last_sorted_rm_repeat_sfd_data_list[len(last_rm_repeat_sfd_data_list) - 1]['SUM_TOTAL']), 2))
        else:  # 周期内标况使用量（周期内期末数-期初数）
            rdm.use_volume_std = str(round(float(max_std_sum) - float(min_std_sum), 2))
        if float(rdm.use_volume_std) < 0:  # 如果use_volume_std计算出来小于0，则直接置为0
            rdm.use_volume_std = str(0)
            print(rdm.flmeter_no, "☆ use_volume_std <0 置为0")

        # 周期内使用额（单价（期末数）* 周期内标况使用量）结果四舍五入
        if rdm.price is None:
            rdm.price = str(0)
        rdm.use_money = str(round((float(rdm.use_volume_std) * float(rdm.price)), 2))

        # 总累积使用量（期末数）
        rdm.sum_total_volume = sorted_rm_repeat_sfd_data_list[len(sorted_rm_repeat_sfd_data_list) - 1]['SUM_TOTAL']
        if rdm.sum_total_volume is None:
            rdm.sum_total_volume = str(0)
            print(rdm.flmeter_no, "☆ sum_total_volume is None 置为0")
        # 累购气量（期末数）
        rdm.total_buy_volume = sorted_rm_repeat_sfd_data_list[len(sorted_rm_repeat_sfd_data_list) - 1]['TOTAL_BUY_VOLUME']
        # 累购金额（期末数）
        rdm.total_buy_money = sorted_rm_repeat_sfd_data_list[len(sorted_rm_repeat_sfd_data_list) - 1]['TOTAL_BUY_MONEY']
        # 剩余金额（期末数）
        rdm.remain_money = sorted_rm_repeat_sfd_data_list[len(sorted_rm_repeat_sfd_data_list) - 1]['REMAIN_MONEY']
        # 总累计使用金额（期末累购金额-期末剩余金额）
        if rdm.total_buy_money is None:  # total_buy_money为None的话 置为0查询计算
            rdm.total_buy_money = str(0)
        if rdm.remain_money is None:  # remain_money为None的话 置为0查询计算
            rdm.remain_money = str(0)
        rdm.sum_total_money = float(rdm.total_buy_money) - float(rdm.remain_money)
        if rdm.sum_total_money < 0:  # 如果sum_total_money计算出来小于0，则直接置为0
            rdm.sum_total_money = str(0)
            print(rdm.flmeter_no, "☆ sum_total_money <0 置为0")

        # 剩余数量（期末数）
        rdm.remain_volume = sorted_rm_repeat_sfd_data_list[len(sorted_rm_repeat_sfd_data_list) - 1]['REMAIN_VOLUME']
        # 流量计(表)状态（期末数）
        rdm.fm_state = sorted_rm_repeat_sfd_data_list[len(sorted_rm_repeat_sfd_data_list) - 1]['FM_STATE']
        # 表状态解析（按位解析）（期末数）
        rdm.fm_state_msg = sorted_rm_repeat_sfd_data_list[len(sorted_rm_repeat_sfd_data_list) - 1]['FM_STATE_MSG']
        # RTU状态（期末数）
        rdm.rtu_state = sorted_rm_repeat_sfd_data_list[len(sorted_rm_repeat_sfd_data_list) - 1]['RTU_STATE']
        # RTU状态解析（按字节解析）（期末数）
        rdm.rtu_state_msg = sorted_rm_repeat_sfd_data_list[len(sorted_rm_repeat_sfd_data_list) - 1]['RTU_STATE_MSG']
        # 阀门控制器状态（期末数）
        rdm.valve_state = sorted_rm_repeat_sfd_data_list[len(sorted_rm_repeat_sfd_data_list) - 1]['VALVE_STATE']
        # 阀门控制器状态解析（期末数）
        rdm.valve_state_msg = sorted_rm_repeat_sfd_data_list[len(sorted_rm_repeat_sfd_data_list) - 1]['VALVE_STATE_MSG']
        # 供电电压（周期内平均值）
        rdm.power_voltage = sorted_rm_repeat_sfd_data_list[len(sorted_rm_repeat_sfd_data_list) - 1]['POWER_VOLTAGE']

        # 电池电压（期末数）
        rdm.battery_voltage = sorted_rm_repeat_sfd_data_list[len(sorted_rm_repeat_sfd_data_list) - 1]['BATTERY_VOLTAGE']
        # 电池电量（期末数）
        rdm.battery_level = sorted_rm_repeat_sfd_data_list[len(sorted_rm_repeat_sfd_data_list) - 1]['BATTERY_LEVEL']
        # 入口压力（周期内平均值）
        rdm.press_in = get_average_period(sorted_rm_repeat_sfd_data_list, "PRESSURE")
        # 出口压力（周期内平均值）
        rdm.press_out = get_average_period(sorted_rm_repeat_sfd_data_list, "PRESSURE")
        # 入口温度（周期内平均值）
        rdm.temp_in = get_average_period(sorted_rm_repeat_sfd_data_list, "TEMPERATURE")

        # 出口温度（周期内平均值）
        rdm.temp_out = get_average_period(sorted_rm_repeat_sfd_data_list, "TEMPERATURE")
        # 信号强度（平均值）
        rdm.rssi = get_average_period(sorted_rm_repeat_sfd_data_list, "RSSI")
        # 删除标识符 1正常，9不正常已删除 默认置为1
        rdm.srm_status = "1"

        # print(sorted_rm_repeat_sfd_data_list)
        # print(len(sorted_rm_repeat_sfd_data_list), sorted_rm_repeat_sfd_data_list[0]['FLMETER_NO'], max_std_sum,min_std_sum, ok_std_sum)
        # print('----------------------------------------------------------------------------------------')

        # 写入数据库
        is_success = ok_processing_data_insert_into_oracle_for_monthly(rdm)  # 将完善好数据的月报表对象rdm传入
        print('----------------------------------------------------------------------------------------')

        # 处理数据完毕 清除临时使用数据
        flmeter_no_set_copy.remove(fno)
        rm_repeat_sfd_data_list.clear()
        last_rm_repeat_sfd_data_list.clear()
    pass
    return True


# 判断"字符串"是否为数字
# @param s 要检测的字符串
# @return 处理结果 True是数字 False不是数字
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


# main方法
# @param db 数据库实例
# @param org_id 机构号
# @param months 天数
# @return main方法运行处理结果 执行完毕即可
def main(db, org_id, months):

    print("💗 I am main()")

    # 记录ID - 取自动递增流水号
    # 设置机构号(传参接收过来了)和序列号名称代码位置
    # com/lc/demo/pythonReportDemo/reportMonthlyKingDemo/python_report_monthly_app_king2.py:614

    # 设置查询的机构,要查询哪一月(脚本)
    # fist = datetime.datetime(datetime.date.today().year, datetime.date.today().month, 1)  # 当前月的第一天
    # last = datetime.datetime(datetime.date.today().year, datetime.date.today().month+1, 1) - datetime.timedelta(1)  # 当前月的最后一天
    return_data, params_data = select_sfd_by_where_for_monthly(org_id, months)  # @param org_id 要查询机构号 @param months 0代表当前月 +n代表n月后 -n代表n月前 默认为-1 跑上个月的数据

    # 获取查询当月(脚本)的上月最后一天最小时间到最大时间的数据
    print("下面是查询当月的上一月最后一天内数据-总共抄表数据")
    last_return_data, last_params_data = select_sfd_by_where_for_monthly_last_min_and_last_max(org_id, months-1)

    # print(return_data)
    # print(len(return_data))

    # 接下来开始处理查询出数据
    if len(return_data) > 0:
        print(params_data[0]['orgid'], [params_data[0]['minTime'].strftime('%Y-%m-%d %H:%M:%S'),params_data[0]['maxTime'].strftime('%Y-%m-%d %H:%M:%S')], "开始进行计算月报表数据处理")
        is_ok = data_processing(return_data, last_return_data, params_data[0]['orgid'],query_datetime=params_data[0]['minTime'])  # 数据处理函数，处理月报表 , 月报表数据计算，写入数据库操作
        if is_ok:
            print(params_data[0]['orgid'], "data_processing is ok")
            print('----------------------------------------------------------------------------------------')
        pass
    else:
        print(params_data[0]['orgid'], [params_data[0]['minTime'].strftime('%Y-%m-%d %H:%M:%S'),params_data[0]['maxTime'].strftime('%Y-%m-%d %H:%M:%S')], "期间无抄表数据，请等待重新计算月报表")
        print("----------------------------------------------------------------------------------------")
    pass

# del_first_before_main方法
# @param db 数据库实例
# @param months 月数
# @return main方法运行之前删除数据处理结果 完成返回True 否则为False
def del_first_before_main(db, months):
    month_first_min = to_get_month_first_last_day_datetime_max_min_time_pro(months, "first", "min", False)  # 方法:获取间隔n月的第一天的最小时间和最后一天的最大时间
    this_year = month_first_min.year
    this_month = month_first_min.month

    # 处理月
    # print(len(str(this_month)))
    # 如果月份小于10 补零 让9变为09月
    if len(str(this_month)) < 2:
        this_month = "0" + str(this_month)
    else:
        this_month = str(this_month)

    print('为了月报表计算数据,接下来要删除SCADA_REPORT_MONTHLY月报表数据,对应年月为:', str(this_year), this_month)
    print('----------------------------------------------------------------------------------------------------')
    del_all_scada_report_monthly_by_year_month(str(this_year), this_month)
    print('开始此次月报表计算操作--------------------------------------------------')
    return True
    # print(yesterday_min, yesterday_max)  # 2020-04-16 00:00:00 2020-04-16 23:59:59.999999

if __name__ == '__main__':

    # sys.stdout = PrintLogger('python_report_monthly_app_king3_with_del_with_day.py.log')  # 监听所有的print到log日志 封装类 如不需要打印所有输出print的log日志，隐掉这段即可

    print("============================================================================================================================================================分隔符")

    db = MyOracle()  # MyOracle()类实例化

    begin_time = None  # 接收程序运行开始时间
    end_time = None  # 接收程序运行结束时间
    begin_time = datetime.datetime.now()
    # print("程序运行开始时间:", begin_time)

    begin_time_clock = None  # 接收程序运行开始时间
    end_time_clock = None  # 接收程序运行结束时间
    begin_time_clock = time.clock()
    # print("程序运行开始time.clock():", begin_time_clock)

    # 查询出所有需要跑脚本的机构id
    org_list = get_all_org_id_for_run_py_command_script_from_select_db()  # 查询出所有需要跑脚本的机构id

    # which_month 代表跑哪月
    which_month = 0
    if del_first_before_main(db, which_month):
        # 循环 org_list @param db实例  # @param org_id 要查询机构号 @param months 0代表当前月 +n代表n月后 -n代表n月前 默认为-1 跑上个月的数据
        for x in org_list:
            print("此机构:", x['ORG_ID'])
            main(db, x['ORG_ID'], which_month)  # 传入的机构,设置要查询哪月！运行main方法，将db带过去，机构id， -1跑上个月的数据！用于下面的操作！

    print("all done-月报表整个处理流程完成")
    print("----------------------------------------------------------------------------------------")
    end_time = datetime.datetime.now()
    print("程序运行开始时间", begin_time)
    print("程序运行结束时间:", end_time)
    print("整个程序运行总时间:", (end_time - begin_time).seconds, "秒")  # (end_time - begin_time).microseconds, "微秒 "1秒 = 10的6次方微秒

    print("----------------------------------------------------------------------------------------")
    end_time_clock = time.clock()
    print("程序运行开始time.clock():", begin_time_clock)
    print("程序运行结束time.clock():", end_time_clock)
    print("整个程序运行总时间time.clock()差:", (end_time_clock - begin_time_clock), "秒")
    print("----------------------------------------------------------------------------------------")