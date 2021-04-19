#!/usr/bin/env python
# -*- coding:utf-8 -*-
# lmt 服务类 pony_orm_lmt_service.py
from pony.orm import db_session, select, delete, commit
# 其他 单独导入utils.util的方法 get_year_month_day_from_datetime和get_random_str_with_counts和get_real_year_month_day和get_float_str
from utils.util import get_year_month_day_from_datetime,get_random_str_with_counts, get_real_year_month_day, get_float_str
# 导入获取流水号方法
from utils.cx_Oracle_db_utils import get_sys_serial_no
# 从models导出类
from models.models_for_lmt import MeterReportMonth, ScadaReportXNMid

# 现在在db包下进行db初始化操作
# 引入db
# 暴露db的数据库引擎给外面 get_dbs
from db.db import get_dbs

# 获取在db包 生成的 双db
db_mysql, db_oracle = get_dbs()


# 查询所有
# MeterReportMonth
# 此MySQL数据库数据写入0080机构
@db_session
def deal_with_data_for_mysql_mrm_select_all():
    # res = MeterReportMonth.select_by_sql('SELECT * FROM meter_report_month_202104')
    # print(res)
    res = MeterReportMonth.select()
    # res.show()
    # to_list()
    res_list = res[:].to_list()
    print('...MySQL...deal_with_data_for_mysql_mrm_select_all...入Oracle库0080机构...查询MeterReportMonth总条数: ' + str(len(res_list)))
    return res_list, res


# 条件查询 - 常用写法
# 根据年月日查询
# 根据report_gen_time也可
# MeterReportMonth
# 此MySQL数据库数据写入0080机构
@db_session
def deal_with_data_for_mysql_mrm_select_where(report_gen_time_min, report_gen_time_max):
    res = select(mrm for mrm in MeterReportMonth if mrm.report_gen_time >= report_gen_time_min and mrm.report_gen_time <= report_gen_time_max)
    res_list = res[:].to_list()
    print('...MySQL...deal_with_data_for_mysql_mrm_select_where...入Oracle库0080机构...查询MeterReportMonth总条数: ' + str(len(res_list)), ' 时间范围: ', report_gen_time_min, ' to ', report_gen_time_max)
    return res_list, res


# 查询所有也可
# 条件查询 - 常用写法
# ScadaReportXNMid
# that_day_min 或者 that_day_max 出一个即可 主要取其年月日 两个都是一样的
@db_session
def deal_with_data_for_oracle_srxm_select_where(that_day_min):
    # res = select(srxm for srxm in ScadaReportXNMid)  # 这是查询所有
    this_year, this_month, this_day = get_year_month_day_from_datetime(that_day_min)
    res = select(srxm for srxm in ScadaReportXNMid if srxm.YEAR == this_year and srxm.MONTH == this_month and srxm.DAY == this_day)  # 这是条件查询 过滤 年月日
    res_list = res[:].to_list()
    print('...Oracle...deal_with_data_for_oracle_srxm_select_where...查询ScadaReportXNMid总条数: ' + str(len(res_list)) + ' 对应年月日为: ' + this_year + this_month + this_day)
    return res_list, res


# 批量删除
# srxms 是 <pony.orm.core.Query object>类型
# 无返回值
@db_session
def deal_with_data_for_oracle_srxm_del_all(srxms):
    srxms.show()
    for srxm in srxms:
        srxm.delete()


# 对应一个日期版本 只有一个年月日
# 批量删除 - 带条件 直接删
# that_day_min 或者 that_day_max 出一个即可 主要取其年月日 两个都是一样的
# 返回 删除行数
@db_session
def deal_with_data_for_oracle_srxm_del_all_with_where(org_id, that_day_min):
    this_year, this_month, this_day = get_year_month_day_from_datetime(that_day_min)
    rowcount = delete(srxm for srxm in ScadaReportXNMid if srxm.YEAR == this_year and srxm.MONTH == this_month and srxm.DAY == this_day and srxm.SRXM_ORG_ID == org_id)
    print('...机构号:', org_id, '...Oracle...deal_with_data_for_oracle_srxm_del_all_with_where...删除ScadaReportXNMid总条数: ' + str(rowcount) + ' 对应年月日为: ' + this_year + this_month + this_day)
    return rowcount


# 对应多个日期版本 多个年月日 针对 循环日期 对应年月 删除
# 批量删除 - 带条件 直接删
# that_day_min 或者 that_day_max 出一个即可 主要取其年月日 两个都是一样的
# 返回 删除行数
# deal_with_data_for_oracle_srxm_del_all_with_where() 基础上 更改版本
@db_session
def deal_with_data_for_oracle_srxm_del_all_with_where2(org_id, this_year, this_month, this_day):
    rowcount = delete(srxm for srxm in ScadaReportXNMid if srxm.YEAR == this_year and srxm.MONTH == this_month and srxm.DAY == this_day and srxm.SRXM_ORG_ID == org_id)
    print('...机构号:', org_id, '...Oracle...deal_with_data_for_oracle_srxm_del_all_with_where...删除ScadaReportXNMid总条数: ' + str(rowcount) + ' 对应年月日为: ' + this_year + this_month + this_day)
    return rowcount


@db_session
# Mysql数据处理 和 MySQLToOracle入库
# org_id 机构号
# mrm_list 从MySQL查询出 待处理 待转入 Oracle的数据 list 列表存储
# mrm_qr 是 <pony.orm.core.Query object>类型
def datas_from_mysql_to_oracle(org_id, mrm_list, mrm_qr):
    # 记录ID-取自动递增流水号 - 公共变量
    ssn_org_id = org_id  # 传入过来的org_id
    ssn_key_name = "SCADA_REPORT_XN_MID"  # 如需修改为其他表的递增流水，请自行修改
    # 导入引入 cx_Oracle db
    from core import cx_Oracle_DBHelper as cod
    db = cod.DBHelper()
    for mrn in mrm_list:
        # print(mrn.meter_comm_no)
        # 引入真正的 流水
        ok_srd_id = get_sys_serial_no(db, ssn_org_id, ssn_key_name, get_real_year_month_day(mrn.report_year), get_real_year_month_day(mrn.report_month))  # 导入获取流水号方法
        print(ok_srd_id)
        # 如果ok_srd_id等于None 代表get_sys_serial_no()报错
        # 则使用continue 跳出本次for循环
        if ok_srd_id == None:
            continue
            print('...cx_Oracle_db_utils.py...get_sys_serial_no...ok_srd_id 为None,使用continue 跳出本次for循环...')
        # 如果ok_srd_id不等于None 则为正常值 继续后续逻辑
        srxm_id = ssn_org_id + get_real_year_month_day(mrn.report_year) + get_real_year_month_day(mrn.report_month) + ok_srd_id
        # 通过机构号和通讯编号 查询出其在lmt系统中对应的设备编号
        comm_no = mrn.meter_comm_no
        flmeterNoList = db_oracle.select('FLMETER_NO FROM SCADA_FLMETER_INFO where SFI_ORG_ID = \'' + str(org_id) + '\' and COMM_NO = \'' + str(comm_no) + '\'')
        flmeterNo = ''
        if len(flmeterNoList) >= 1:
            flmeterNo = flmeterNoList[0]
        # 假流水 随机数 测试使用
        # srxm_id = get_random_str_with_counts(8)
        # 这就是在Oracle中 新增数据
        # 包含数据的再次加工
        tmp = ScadaReportXNMid(SRXM_ORG_ID=org_id, SRXM_ID=srxm_id, FLMETER_NO=flmeterNo, COMM_NO=mrn.meter_comm_no,
                               YEAR=get_real_year_month_day(mrn.report_year),
                               MONTH=get_real_year_month_day(mrn.report_month),
                               DAY=get_real_year_month_day(mrn.report_day), STD_SUM=get_float_str(mrn.std_sum),
                               WORK_SUM=get_float_str(mrn.work_sum), PRICE=get_float_str(mrn.curr_price),
                               THIS_CYCLE_SUM=get_float_str(mrn.this_cycle_sum),
                               THIS_DAY_SUM=get_float_str(mrn.this_day_sum),
                               REMAIN_MONEY=get_float_str(mrn.remain_money),
                               REMAIN_VOLUME=get_float_str(mrn.remain_volume), FM_STATE=str(mrn.meter_state),
                               BATTERY_VOLTAGE=get_float_str(mrn.battery_voltage), BATTERY_LEVEL=str(mrn.battery_level),
                               RSSI=str(mrn.rssi), FM_STATE_MSG=mrn.meter_stat_emsg)
        commit()  # 提交事务
        print('...机构号:', org_id, '...datas_from_mysql_to_oracle...meter_comm_no通讯编号: ' + mrn.meter_comm_no, '入库成功', '对应srxm_id为:', srxm_id)
    pass
# and so on.
