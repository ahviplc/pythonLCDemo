#!/usr/bin/env python
# -*- coding:utf-8 -*-
import decimal
# lmt 服务类 pony_orm_lmt_service.py
from pony.orm import db_session, select, delete, commit
# 其他 单独导入utils.util的方法 get_year_month_day_from_datetime和get_random_str_with_counts和get_real_year_month_day和get_float_str和grade3_price_volume
from utils.util import get_year_month_day_from_datetime,get_random_str_with_counts, get_real_year_month_day, get_float_str, grade3_price_volume
# 导入获取流水号方法
from utils.cx_Oracle_db_utils import get_sys_serial_no
# 从models导出类
from models.models_for_lmt import MeterReportMonth, ScadaReportXNMid, ScadaReportXNWeek

# 现在在db包下进行db初始化操作
# 引入db
# 暴露db的数据库引擎给外面 get_dbs
from db.db import get_dbs

# 获取在db包 生成的 双db
db_mysql, db_oracle = get_dbs()


# deal_with_data_for_mysql_mrm_select_all
# MeterReportMonth
# 查询所有
# 此MySQL数据库数据写入0080机构
# 无入参
# 返回查询出的list,和对应的<pony.orm.core.Query object>类型
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


# deal_with_data_for_mysql_mrm_select_where
# MeterReportMonth
# 条件查询 - 常用写法
# 根据年月日查询 查询一个日期时间范围
# 根据report_gen_time也可
# 此MySQL数据库数据写入0080机构
# 通过 report_gen_time 进行范围查询
# report_gen_time_min 查询开始时间
# report_gen_time_max 查询结束时间
# 返回查询出的list,和对应的<pony.orm.core.Query object>类型
@db_session
def deal_with_data_for_mysql_mrm_select_where(report_gen_time_min, report_gen_time_max):
    res = select(mrm for mrm in MeterReportMonth if mrm.report_gen_time >= report_gen_time_min and mrm.report_gen_time <= report_gen_time_max)
    res_list = res[:].to_list()
    print('...MySQL...deal_with_data_for_mysql_mrm_select_where...入Oracle库0080机构...查询MeterReportMonth总条数: ' + str(len(res_list)), ' 时间范围: ', report_gen_time_min, ' to ', report_gen_time_max)
    return res_list, res


# deal_with_data_for_oracle_srxm_select_where
# ScadaReportXNMid
# 查询所有也可
# 条件查询 - 常用写法
# that_day_min 或者 that_day_max 出一个即可 主要取其年月日 两个都是一样的
# 返回查询出的list,和对应的<pony.orm.core.Query object>类型
@db_session
def deal_with_data_for_oracle_srxm_select_where(that_day_min):
    # res = select(srxm for srxm in ScadaReportXNMid)  # 这是查询所有
    this_year, this_month, this_day = get_year_month_day_from_datetime(that_day_min)
    res = select(srxm for srxm in ScadaReportXNMid if srxm.YEAR == this_year and srxm.MONTH == this_month and srxm.DAY == this_day)  # 这是条件查询 过滤 年月日
    res_list = res[:].to_list()
    print('...Oracle...deal_with_data_for_oracle_srxm_select_where...查询ScadaReportXNMid总条数: ' + str(len(res_list)) + ' 对应年月日为: ' + this_year + this_month + this_day)
    return res_list, res


# deal_with_data_for_oracle_srxm_select_where_with_org_id
# ScadaReportXNMid
# 查询所有也可 - 带机构号 查询
# 条件查询 - 常用写法
# org_id 机构号
# that_day_min 或者 that_day_max 出一个即可 主要取其年月日 两个都是一样的
# 返回查询出的list,和对应的<pony.orm.core.Query object>类型
@db_session
def deal_with_data_for_oracle_srxm_select_where_with_org_id(org_id, that_day_min):
    this_year, this_month, this_day = get_year_month_day_from_datetime(that_day_min)
    res = select(srxm for srxm in ScadaReportXNMid if srxm.YEAR == this_year and srxm.MONTH == this_month and srxm.DAY == this_day and srxm.SRXM_ORG_ID == org_id)  # 这是条件查询 过滤 年月日
    res_list = res[:].to_list()
    print('...Oracle...deal_with_data_for_oracle_srxm_select_where_with_org_id...查询ScadaReportXNMid总条数: ' + str(len(res_list)) + ' 对应年月日为: ' + this_year + this_month + this_day)
    return res_list, res


# deal_with_data_for_oracle_srxm_select_where_with_org_id_and_flmeter_no
# ScadaReportXNMid
# 查询所有也可 - 带机构号 带表计编号 查询
# 条件查询 - 常用写法
# org_id 机构号
# flmeter_no 表计编号
# that_day_min 或者 that_day_max 出一个即可 主要取其年月日 两个都是一样的
# 返回查询出的list,和对应的<pony.orm.core.Query object>类型
@db_session
def deal_with_data_for_oracle_srxm_select_where_with_org_id_and_flmeter_no(org_id, flmeter_no, that_day_min):
    this_year, this_month, this_day = get_year_month_day_from_datetime(that_day_min)
    res = select(srxm for srxm in ScadaReportXNMid if srxm.YEAR == this_year and srxm.MONTH == this_month and srxm.DAY == this_day and srxm.SRXM_ORG_ID == org_id and srxm.FLMETER_NO == flmeter_no)  # 这是条件查询 过滤 年月日
    res_list = res[:].to_list()
    print('...Oracle...deal_with_data_for_oracle_srxm_select_where_with_org_id_and_flmeter_no...查询ScadaReportXNMid总条数: ' + str(len(res_list)) + ' 对应年月日为: ' + this_year + this_month + this_day, '机构号: ', org_id, '表号: ', flmeter_no)
    return res_list, res


# deal_with_data_for_oracle_srxm_del_all
# ScadaReportXNMid
# 批量删除 - for循环 传入实体 调用 delete() 删除
# srxms 是 <pony.orm.core.Query object>类型
# 无返回值
@db_session
def deal_with_data_for_oracle_srxm_del_all(srxms):
    srxms.show()
    for srxm in srxms:
        srxm.delete()


# deal_with_data_for_oracle_srxm_del_all_with_where
# ScadaReportXNMid
# 对应一个日期版本 只有一个年月日
# 批量删除 - 带条件 直接删
# org_id 机构号
# that_day_min 或者 that_day_max 出一个即可 主要取其年月日 两个都是一样的
# 返回 删除行数
@db_session
def deal_with_data_for_oracle_srxm_del_all_with_where(org_id, that_day_min):
    this_year, this_month, this_day = get_year_month_day_from_datetime(that_day_min)
    rowcount = delete(srxm for srxm in ScadaReportXNMid if srxm.YEAR == this_year and srxm.MONTH == this_month and srxm.DAY == this_day and srxm.SRXM_ORG_ID == org_id)
    print('...机构号:', org_id, '...Oracle...deal_with_data_for_oracle_srxm_del_all_with_where...删除ScadaReportXNMid总条数: ' + str(rowcount) + ' 对应年月日为: ' + this_year + this_month + this_day)
    return rowcount


# deal_with_data_for_oracle_srxm_del_all_with_where2
# deal_with_data_for_oracle_srxm_del_all_with_where() 基础上 更改版本
# ScadaReportXNMid
# 对应多个日期版本 多个年月日 针对 循环日期 对应年月 删除
# 批量删除 - 带条件 直接删
# org_id 机构号
# this_year 年
# this_month 月
# this_day 日
# 返回 删除行数
@db_session
def deal_with_data_for_oracle_srxm_del_all_with_where2(org_id, this_year, this_month, this_day):
    rowcount = delete(srxm for srxm in ScadaReportXNMid if srxm.YEAR == this_year and srxm.MONTH == this_month and srxm.DAY == this_day and srxm.SRXM_ORG_ID == org_id)
    print('...机构号:', org_id, '...Oracle...deal_with_data_for_oracle_srxm_del_all_with_where2...删除ScadaReportXNMid总条数: ' + str(rowcount) + ' 对应年月日为: ' + this_year + this_month + this_day)
    return rowcount


# datas_from_mysql_to_oracle
# ScadaReportXNMid
# Mysql数据处理 和 MySQLToOracle入库
# org_id 机构号
# mrm_list 从MySQL查询出 待处理 待转入 Oracle的数据 list 列表存储
# mrm_qr 是 <pony.orm.core.Query object>类型
@db_session
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
        print('...机构号:', org_id, '...Oracle...datas_from_mysql_to_oracle...meter_comm_no通讯编号: ' + mrn.meter_comm_no, '入库成功', '对应srxm_id为:', srxm_id)
    pass
# and so on.

# =============================================================================================================================================================

# for app2.py


# datas_from_mid_to_week_wash_data_oracle
# 周数据清洗(周二到下周一)版
# 数据从表SCADA_REPORT_XN_MID清洗到表SCADA_REPORT_XN_WEEK
# from ScadaReportXNMid to ScadaReportXNWeek
# org_id 机构号
# srxm_list_that_week_min 从Oracle查询出 【SCADA_REPORT_XN_MID】表 对应 周二期初mid数据 【下面srxm_list_that_week_max是周一期末mid数据数据 通过org_id, flmeter_no, that_week_max查询出】
# srxm_qr 是 <pony.orm.core.Query object>类型
# that_week_min 周二期初日期
# that_week_max 周一期末日期
@db_session
def datas_from_mid_to_week_wash_data_oracle(org_id, srxm_list_that_week_min, srxm_qr, that_week_min, that_week_max):
    # 请洗之前 先根据主键REPORT_BEGIN_DATE判断在SCADA_REPORT_XN_WEEK有没有 有的话 先删除 再清洗入库
    deal_with_data_for_oracle_srxw_del_all_with_where(org_id, that_week_min)
    # 继续清洗数据的逻辑
    # 对 mrm_list_that_week_min 进行循环遍历 拿出其 SCADA_REPORT_XN_MID 的 表计编号
    for srxm in srxm_list_that_week_min:
        flmeter_no = srxm.FLMETER_NO
        # print(flmeter_no)
        # 通过 flmeter_no 和 org_id 和 that_week_max 再去 SCADA_REPORT_XN_MID 拿数据 拿七天之后 周一的数据
        # 首先判空 空的话 跳出本次循环
        if flmeter_no == None:
            continue
        # 不空的话 开始查询周一期末mid数据数据
        srxm_list_that_week_max, srxm_qr = deal_with_data_for_oracle_srxm_select_where_with_org_id_and_flmeter_no(org_id, flmeter_no, that_week_max)
        # 定义一些公关变量吧
        # 周二期初数据 mrm_list_that_week_min
        begin_std_sum = srxm.STD_SUM
        begin_price = srxm.PRICE
        begin_this_cycle_sum = srxm.THIS_CYCLE_SUM
        # 周一期末数据
        end_std_sum = None
        end_price = None
        end_this_cycle_sum = None
        # 这个 END_THIS_CYCLE_SUM <=GRADE_VOLUME1 的标识符 如果成立 为True 不成立 为False
        is_end_this_cycle_sum_less_than_gv1_flag = None
        # 阶梯价格 阶梯限量
        gp1, gv1, gp2, gv2, gp3 = None, None, None, None, None
        # 将上面的公共数据 在一系列赋值之后 来个判空操作 为None的 赋值为 0
        # begin_std_sum = srxm.STD_SUM
        # begin_price = srxm.PRICE
        # begin_this_cycle_sum = srxm.THIS_CYCLE_SUM
        # end_std_sum = None
        # end_price = None
        # end_this_cycle_sum = None
        # gp1, gv1, gp2, gv2, gp3 = None, None, None, None, None
        # 再次定义需要计算 才可出的参数 还是为入库准备数据
        price1_volume = None
        price1_money = None
        price2_volume = None
        price2_money = None
        price3_volume = None
        price3_money = None
        use_money = None
        # 从SCADA_FLOWMETER_INFO拿出price_no,customer_no
        price_no = None
        customer_no = None
        price_no_list = db_oracle.select('PRICE_NO,CUSTOMER_NO FROM SCADA_FLMETER_INFO where SFI_ORG_ID = \'' + str(org_id) + '\' and FLMETER_NO = \'' + str(flmeter_no) + '\'')
        if len(price_no_list) >= 1:
            price_no = price_no_list[0][0]
            customer_no = price_no_list[0][1]
            # 根据PRICE_NO从price_info表拿出阶梯价格信息到week表
            price_list = db_oracle.select('GRADE_PRICE1,GRADE_VOLUME1,GRADE_PRICE2,GRADE_VOLUME2,GRADE_PRICE3 FROM PRICE_INFO where PI_ORG_ID = \'' + str(org_id) + '\' and PRICE_NO = \'' + str(price_no) + '\'')
            if len(price_list) >= 1:
                # print(price_list[0])
                gp1, gv1, gp2, gv2, gp3 = price_list[0][0], price_list[0][1], price_list[0][2], price_list[0][3], price_list[0][4]
            else:
                print(org_id, flmeter_no, price_no, '根据此价格编号查询PRICE_INFO, 无数据')
        else:
            print(org_id, flmeter_no, '根据此表计编号查询SCADA_FLMETER_INFO, 无PRICE_NO数据')
        # 判断 mrm_list_that_week_max 是否有对应一条数据 有 使用即可 没有 后续判断None 均按照为0处理
        if len(srxm_list_that_week_max) >= 1:
            # 查询出数据 给 end_* 赋值
            print('...机构号:', org_id, '...Oracle...srxm_list...len...查询ScadaReportXNMid总条数: ' + str(len(srxm_list_that_week_max)), ' 时间: ', that_week_max, '机构号: ', org_id, '表号: ', flmeter_no, '查询出对应周一结束日期数据一条 去正常处理')
            # 给 周一期末数据 赋值
            end_srxm = srxm_list_that_week_max[0]
            end_std_sum = end_srxm.STD_SUM
            end_price = end_srxm.PRICE
            end_this_cycle_sum = end_srxm.THIS_CYCLE_SUM
            pass
        else:
            # 未查询出数据 输出提示即可
            # 都置成0 入库 continue掉 即可
            # 入库 continue 掉即可 写一个就行
            tmp = ScadaReportXNWeek(SRXW_ORG_ID=org_id, FLMETER_NO=flmeter_no, COMM_NO=srxm.COMM_NO,
                                    CUSTOMER_NO=customer_no,
                                    REPORT_BEGIN_DATE=that_week_min.date(),
                                    BEGIN_STD_SUM=begin_std_sum,
                                    BEGIN_PRICE=begin_price,
                                    BEGIN_THIS_CYCLE_SUM=begin_this_cycle_sum,
                                    REPORT_END_DATE=that_week_max.date(),
                                    END_STD_SUM=("0" if (end_std_sum is None) else str(end_std_sum)),
                                    END_PRICE=("0" if (end_price is None) else str(end_price)),
                                    END_THIS_CYCLE_SUM=("0" if (end_this_cycle_sum is None) else str(end_this_cycle_sum)),
                                    USE_VOLUME_STD="0",
                                    PRICE1_VOLUME=("0" if (price1_volume is None) else str(price1_volume)),
                                    PRICE1_MONEY=("0" if (price1_money is None) else str(price1_money)),
                                    PRICE2_VOLUME=("0" if (price2_volume is None) else str(price2_volume)),
                                    PRICE2_MONEY=("0" if (price2_money is None) else str(price2_money)),
                                    PRICE3_VOLUME=("0" if (price3_volume is None) else str(price3_volume)),
                                    PRICE3_MONEY=("0" if (price3_money is None) else str(price3_money)),
                                    USE_MONEY=("0" if (use_money is None) else str(use_money)),
                                    REMAIN_MONEY="0",
                                    REMAIN_VOLUME="0",
                                    PRICE_NO=price_no,
                                    GRADE_PRICE1=("0" if (gp1 is None) else str(gp1)),
                                    GRADE_VOLUME1=("0" if (gv1 is None) else str(gv1)),
                                    GRADE_PRICE2=("0" if (gp2 is None) else str(gp2)),
                                    GRADE_VOLUME2=("0" if (gv2 is None) else str(gv2)),
                                    GRADE_PRICE3=("0" if (gp3 is None) else str(gp3)))
            commit()  # 提交事务
            print('...机构号:', org_id, '...Oracle...srxm_list...len...查询ScadaReportXNMid总条数: ' + str(len(srxm_list_that_week_max)), ' 时间: ', that_week_max, '机构号: ', org_id, '表号: ', flmeter_no, '没有查询出对应周一结束日期数据一条 均按照为0处理 入库 同时continue掉 进行下一个循环')
            continue
        # 初始化数据完毕 开始数据清洗 数据收集 最后入库前的处理
        # 截取最后一位为价格判断符price_flag
        price_flag = None
        if price_no is None:
            # 为空 单一价格处理 赋值价格判断符为5 后续判断是否为5 为5的话 即可 视为 单一价格
            price_flag = int('5')
            # 当price_no为None时 记住其 gp1, gv1, gp2, gv2, gp3 也均为None 看后续如何处理 后续用不到 gp gv 的
        else:
            # 当price_no不为null
            price_flag = int(price_no[-1])
            # 给 is_end_this_cycle_sum_less_than_gv1_flag 赋值
            is_end_this_cycle_sum_less_than_gv1_flag = decimal.Decimal(end_this_cycle_sum) <= decimal.Decimal(gv1)
        # 计算得出值 标况用量use_volume_std = 结束标况总量end_std_sum-开始标况总量begin_std_sum
        use_volume_std = decimal.Decimal(end_std_sum) - decimal.Decimal(begin_std_sum)
        # 公式
        # 当price_no为空或者Price_no>0080000003或者END_THIS_CYCLE_SUM <=GRADE_VOLUME1时当单一价格处理
        # PRICE1_VOLUME= USE_VOLUME_STD，PRICE1_MONEY = END_PRICE×USE_VOLUME_STD
        # PRICE2_VOLUME = 0，PRICE2_MONEY = 0，
        # PRICE3_VOLUME = 0，PRICE3_MONEY = 0，
        # USE_MONEY = END_PRICE×USE_VOLUME_STD。
        # 当week表的Price_no<=0080000003且BEGIN_THIS_CYCLE_SUM >GRADE_VOLUME2时
        # 全部按END_PRICE计算，
        # PRICE1_VOLUME= 0，PRICE1_MONEY = 0，
        # PRICE2_VOLUME = 0，PRICE2_MONEY = 0，
        # PRICE3_VOLUME = USE_VOLUME_STD，PRICE3_MONEY = END_PRICE×USE_VOLUME_STD，
        # USE_MONEY = END_PRICE×USE_VOLUME_STD。
        # 其他具体看文档
        # 开始判断price_flag吧
        if price_flag == 5 or price_flag > 3 or is_end_this_cycle_sum_less_than_gv1_flag:
            price1_volume = use_volume_std
            price1_money = decimal.Decimal(end_price) * use_volume_std
            # 其他均为0
            price2_volume, price2_money, price3_volume, price3_money = 0, 0, 0, 0
            use_money = price1_money
        elif price_flag <= 3 and (decimal.Decimal(begin_this_cycle_sum) > decimal.Decimal(gv2)):
            # 全部按END_PRICE计算
            price1_volume, price1_money, price2_volume, price2_money = 0, 0, 0, 0
            price3_volume = use_volume_std
            price3_money = decimal.Decimal(end_price) * use_volume_std
            use_money = price3_money
        else:
            print("...datas_from_mid_to_week_wash_data_oracle...进入else...", flmeter_no)
            begin_price1_volume, begin_price1_money, begin_price2_volume, begin_price2_money, begin_price3_volume, begin_price3_money, begin_use_money = grade3_price_volume(begin_this_cycle_sum, gp1, gv1, gp2, gv2, gp3)
            end_price1_volume, end_price1_money, end_price2_volume, end_price2_money, end_price3_volume, end_price3_money, end_use_money = grade3_price_volume(end_this_cycle_sum, gp1, gv1, gp2, gv2, gp3)
            price1_volume= decimal.Decimal(end_price1_volume) - decimal.Decimal(begin_price1_volume)
            price1_money= decimal.Decimal(end_price1_money) - decimal.Decimal(begin_price1_money)
            price2_volume=decimal.Decimal(end_price2_volume) - decimal.Decimal(begin_price2_volume)
            price2_money=decimal.Decimal(end_price2_money) - decimal.Decimal(begin_price2_money)
            price3_volume=decimal.Decimal(end_price3_volume) - decimal.Decimal(begin_price3_volume)
            price3_money=decimal.Decimal(end_price3_money) - decimal.Decimal(begin_price3_money)
            use_money =decimal.Decimal(end_use_money) - decimal.Decimal(begin_use_money)
        # 入库 continue 掉即可 写一个就行
        tmp = ScadaReportXNWeek(SRXW_ORG_ID=org_id, FLMETER_NO=flmeter_no, COMM_NO=srxm.COMM_NO,
                                CUSTOMER_NO=customer_no,
                                REPORT_BEGIN_DATE=that_week_min.date(),
                                BEGIN_STD_SUM=begin_std_sum,
                                BEGIN_PRICE=begin_price,
                                BEGIN_THIS_CYCLE_SUM=begin_this_cycle_sum,
                                REPORT_END_DATE=that_week_max.date(),
                                END_STD_SUM=("0" if (end_std_sum is None) else str(end_std_sum)),
                                END_PRICE=("0" if (end_price is None) else str(end_price)),
                                END_THIS_CYCLE_SUM=("0" if (end_this_cycle_sum is None) else str(end_this_cycle_sum)),
                                USE_VOLUME_STD=("0" if (use_volume_std is None) else str(use_volume_std)),
                                PRICE1_VOLUME=("0" if (price1_volume is None) else str(price1_volume)),
                                PRICE1_MONEY=("0" if (price1_money is None) else str(price1_money)),
                                PRICE2_VOLUME=("0" if (price2_volume is None) else str(price2_volume)),
                                PRICE2_MONEY=("0" if (price2_money is None) else str(price2_money)),
                                PRICE3_VOLUME=("0" if (price3_volume is None) else str(price3_volume)),
                                PRICE3_MONEY=("0" if (price3_money is None) else str(price3_money)),
                                USE_MONEY=("0" if (use_money is None) else str(use_money)),
                                REMAIN_MONEY=srxm_list_that_week_max[0].REMAIN_MONEY,  # 从期末拿
                                REMAIN_VOLUME=srxm_list_that_week_max[0].REMAIN_VOLUME,
                                PRICE_NO=price_no,
                                GRADE_PRICE1=("0" if (gp1 is None) else str(gp1)),
                                GRADE_VOLUME1=("0" if (gv1 is None) else str(gv1)),
                                GRADE_PRICE2=("0" if (gp2 is None) else str(gp2)),
                                GRADE_VOLUME2=("0" if (gv2 is None) else str(gv2)),
                                GRADE_PRICE3=("0" if (gp3 is None) else str(gp3)))
        commit()  # 提交事务
        print('Done...机构号:', org_id, '...Oracle...datas_from_mid_to_week_wash_data_oracle...flmeter_no表计编号: ' + flmeter_no, '清洗成功 入库ScadaReportXNWeek成功', '对应REPORT_BEGIN_DATE为:', that_week_min)
    pass


# deal_with_data_for_oracle_srxw_del_all_with_where
# SCADA_REPORT_XN_WEEK
# 对应一个【报表开始日期，周二】 通过 REPORT_BEGIN_DATE 进行条件判断
# 批量删除 - 带条件 直接删
# org_id 机构号
# that_week_min 周二期初日期【其就是 REPORT_BEGIN_DATE】传入即可
# 返回 删除行数
@db_session
def deal_with_data_for_oracle_srxw_del_all_with_where(org_id, that_week_min):
    this_date = that_week_min.date()
    rowcount = delete(srxw for srxw in ScadaReportXNWeek if srxw.REPORT_BEGIN_DATE == this_date and srxw.SRXW_ORG_ID == org_id)
    print('...清洗之前...先删除...机构号:', org_id, '...Oracle...deal_with_data_for_oracle_srxw_del_all_with_where...删除ScadaReportXNWeek总条数: ' + str(rowcount) + ' 对应REPORT_BEGIN_DATE周二开始周期时间为: ', that_week_min)
    return rowcount


pass
