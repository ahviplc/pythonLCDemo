# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# models 类的集中地
# 集中管理所有的model
import datetime
from pony.orm import *  # 引入pony
# 其他 单独导入utils.util的方法 get_now_year_month
from utils.util import get_run_which_datetime_year_month
# 引入db
# 暴露db的数据库引擎给外面 get_dbs
from db.db import get_dbs

# 获取在db包 生成的 双db
db_mysql, db_oracle = get_dbs()

# # 使用时 再次声明全局变量 表示在这里使用的是全局变量，而不是局部变量
# global org_id
# global that_day_min
# global that_day_max
# print(org_id, that_day_min, that_day_max)


########################################################################
# MySQL - 数据提供者
# pony_orm_lmt_service.py 供lmt使用
# meter_report_month_202104
# get_run_which_datetime_year_month() 可动态获取 年月
class MeterReportMonth(db_mysql.Entity):
    _table_ = "meter_report_month_" + get_run_which_datetime_year_month()
    report_id = PrimaryKey(int, size=32, nullable=False, auto=False)  # 主键 int类型特有. 8,16,32,64 默认32，对应mysql定义的 INT(11)
    company_no = Optional(str, max_len=10, nullable=True, column="company_no", default=None)
    meter_comm_no = Optional(str, max_len=50, nullable=True, column="meter_comm_no", default=None)
    device_type = Optional(int, size=32, nullable=True, default=None)
    factory_code = Optional(str, max_len=50, nullable=True, default=None)

    meter_area_no = Optional(str, max_len=50, nullable=True, default=None)
    meter_define_no1 = Optional(str, max_len=50, nullable=True, default=None)
    meter_define_no2 = Optional(str, max_len=50, nullable=True, default=None)
    meter_define_no3 = Optional(str, max_len=50, nullable=True, default=None)
    meter_define_no4 = Optional(str, max_len=50, nullable=True, default=None)

    report_year = Optional(int, size=32, nullable=True, default=None)
    report_month = Optional(int, size=32, nullable=True, default=None)
    report_day = Optional(int, size=32, nullable=True, default=None)
    report_gen_time = Required(datetime.date, nullable=False, column="report_gen_time", default=datetime.date.today)
    std_sum = Optional(float, nullable=True, default=None)

    work_sum = Optional(float, nullable=True, default=None)
    this_day_sum = Optional(float, nullable=True, default=None)
    last_day_sum = Optional(float, nullable=True, default=None)
    this_cycle_sum = Optional(float, nullable=True, default=None)
    last_cycle_sum = Optional(float, nullable=True, default=None)

    remain_money = Optional(float, nullable=True, default=None)
    remain_volume = Optional(float, nullable=True, default=None)
    curr_price = Optional(float, nullable=True, default=None)
    meter_state = Optional(int, size=32, nullable=True, default=None)
    meter_stat_emsg = Optional(str, max_len=50, nullable=True, default=None)

    rssi = Optional(int, size=32, nullable=True, default=None)
    battery_voltage = Optional(float, nullable=True, default=None)
    battery_level = Optional(int, size=32, nullable=True, default=None)

    ext_data = Optional(str, max_len=50, nullable=True, default=None)
    ext_data2 = Optional(str, max_len=50, nullable=True, default=None)
    ext_data3 = Optional(str, max_len=50, nullable=True, default=None)
    ext_data4 = Optional(str, max_len=50, nullable=True, default=None)


########################################################################
# Oracle - 数据接收者
# ScadaReportXNMid
# pony_orm_lmt_service.py 供lmt使用
class ScadaReportXNMid(db_oracle.Entity):
    _table_ = "SCADA_REPORT_XN_MID"
    SRXM_ORG_ID = Optional(str, max_len=6, nullable=True)
    SRXM_ID = PrimaryKey(str, max_len=20, nullable=False, auto=False)  # 主键
    FLMETER_NO = Optional(str, max_len=20, nullable=True, default=None)
    COMM_NO = Optional(str, max_len=20, nullable=True, default=None)
    REPORT_TIME = Required(datetime.datetime, nullable=False, column="REPORT_TIME", default=datetime.datetime.today)

    YEAR = Optional(str, max_len=10, nullable=True, default=None)
    MONTH = Optional(str, max_len=10, nullable=True, default=None)
    DAY = Optional(str, max_len=10, nullable=True, default=None)
    STD_SUM = Optional(str, max_len=18, nullable=True, default=None)
    WORK_SUM = Optional(str, max_len=18, nullable=True, default=None)

    PRICE = Optional(str, max_len=18, nullable=True, default=None)
    THIS_CYCLE_SUM = Optional(str, max_len=18, nullable=True, default=None)
    CYCLE_USE_MONEY = Optional(str, max_len=18, nullable=True, default=None)
    THIS_DAY_SUM = Optional(str, max_len=18, nullable=True, default=None)
    SUM_TOTAL_MONEY = Optional(str, max_len=18, nullable=True, default=None)

    TOTAL_BUY_VOLUME = Optional(str, max_len=18, nullable=True, default=None)
    TOTAL_BUY_MONEY = Optional(str, max_len=18, nullable=True, default=None)
    REMAIN_MONEY = Optional(str, max_len=18, nullable=True, default=None)
    REMAIN_VOLUME = Optional(str, max_len=18, nullable=True, default=None)
    FM_STATE = Optional(str, max_len=50, nullable=True, default=None)

    BATTERY_VOLTAGE = Optional(str, max_len=18, nullable=True, default=None)
    BATTERY_LEVEL = Optional(str, max_len=18, nullable=True, default=None)
    RSSI = Optional(str, max_len=10, nullable=True, default=None)
    FM_STATE_MSG = Optional(str, max_len=200, nullable=True, default=None)


# ScadaReportXNWeek
# pony_orm_lmt_service.py 供lmt使用
class ScadaReportXNWeek(db_oracle.Entity):
    _table_ = "SCADA_REPORT_XN_WEEK"
    SRXW_ORG_ID = Optional(str, max_len=6, nullable=True)
    FLMETER_NO = Optional(str, max_len=20, nullable=True, default=None)
    COMM_NO = PrimaryKey(str, max_len=20, nullable=False, auto=False)  # 主键
    CUSTOMER_NO = Optional(str, max_len=20, nullable=True, default=None)
    REPORT_TIME = Required(datetime.datetime, nullable=False, column="REPORT_TIME", default=datetime.datetime.today)

    REPORT_BEGIN_DATE = Required(datetime.date, nullable=False, column="REPORT_BEGIN_DATE", default=datetime.date.today())
    BEGIN_STD_SUM = Optional(str, max_len=18, nullable=True, default=None)
    BEGIN_PRICE = Optional(str, max_len=18, nullable=True, default=None)
    BEGIN_THIS_CYCLE_SUM = Optional(str, max_len=18, nullable=True, default=None)
    REPORT_END_DATE = Required(datetime.date, nullable=False, column="REPORT_END_DATE", default=datetime.date.today())

    END_STD_SUM = Optional(str, max_len=18, nullable=True, default=None)
    END_PRICE = Optional(str, max_len=18, nullable=True, default=None)
    END_THIS_CYCLE_SUM = Optional(str, max_len=18, nullable=True, default=None)
    USE_VOLUME_STD = Optional(str, max_len=18, nullable=True, default=None)
    PRICE1_VOLUME = Optional(str, max_len=20, nullable=True, default=None)

    PRICE1_MONEY = Optional(str, max_len=20, nullable=True, default=None)
    PRICE2_VOLUME = Optional(str, max_len=20, nullable=True, default=None)
    PRICE2_MONEY = Optional(str, max_len=20, nullable=True, default=None)
    PRICE3_VOLUME = Optional(str, max_len=20, nullable=True, default=None)
    PRICE3_MONEY = Optional(str, max_len=120, nullable=True, default=None)

    USE_MONEY = Optional(str, max_len=18, nullable=True, default=None)
    REMAIN_MONEY = Optional(str, max_len=18, nullable=True, default=None)
    REMAIN_VOLUME = Optional(str, max_len=18, nullable=True, default=None)
    PRICE_NO = Optional(str, max_len=20, nullable=True, default=None)
    GRADE_PRICE1 = Optional(str, max_len=20, nullable=True, default=None)

    GRADE_VOLUME1 = Optional(str, max_len=20, nullable=True, default=None)
    GRADE_PRICE2 = Optional(str, max_len=20, nullable=True, default=None)
    GRADE_VOLUME2 = Optional(str, max_len=20, nullable=True, default=None)
    GRADE_PRICE3 = Optional(str, max_len=20, nullable=True, default=None)
