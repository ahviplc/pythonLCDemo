#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""

python_fi_center_billing_app_king.py 封装了小时报表对象类以及将取自动递增流水方法提取到工具db_utils文件中,集成监听所有的print到log日志的封装类 【copy from python_report_hourly_app_king2.py】
中心计费脚本-计算写入数据库oracle的中心计费脚本
版本说明:1：跑所有机构的所有需要中心计费的表在SCADA_FLMETER_DATA里一段时间内产生的数据，根据数据，算出使用金额等相关信息；2:逻辑-【使用金额 = （这期抄数-上期抄数）* 单价】 3:整体脚本代码结构变更
备注:脚本一个小时运行一次的话 解决方案可如下: 写个一次性的，然后放到windows计划任务里去
Version: 1.0
Author: LC
DateTime: ##
UpdateTime:
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
LC博客url: http://oneplusone.vip/index.html
一加壹.SNS LC - 又一个SNS社区: http://sns.oneplusone.vip
赞助一加壹博客最Top-LC万能收款码支持-支付宝、微信、QQ
http://lc.oneplusone.vip/donateMeByLC.html

"""
import time
import datetime
import calendar
import os
import sys
import cx_Oracle
import operator
import json
# from ### import ###  # 导入中心计费对象类
from db_utils import get_sys_serial_no  # 导入获取流水号方法
from print_msg_to_log_model import PrintLogger

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


# 获取所有需要跑中心计费脚本的流量计信息
# 字段：{"fee_control_mode": "0003", "sfi_status": "1"} 计费控制模式为0003的为中心计费 sfi_status删除标识符为1的 未删除状态的
def get_all_scada_flmeter_infos_need_center_billing_run_py_command_script_from_select_db():
    sql = "select * from SCADA_FLMETER_INFO where FEE_CONTROL_MODE= :fee_control_mode and SFI_STATUS=:sfi_status"
    data = [{"fee_control_mode": "0003", "sfi_status": "1"}]
    fc = db.select_by_where_many_params_dict(sql, data)
    return fc


# 通过流量计编号获取其对应的 充值记录FI_CHARGE_RECORD
# @param flmeter_no 流量计编号
def get_fi_charge_record_list_by_flmeter_no_from_select_db(flmeter_no):
    sql = "select * from FI_CHARGE_RECORD where METER_NO= :meter_no"
    data = [{"meter_no": flmeter_no}]
    fc = db.select_by_where_many_params_dict(sql, data)
    return fc


# 更新对应的FI_CHARGE_RECORD的中心计费的相关字段
# @param rcr_org_id 机构号
# @param rcr_id ID
# @param flmeter_no 流量计编号
# @param total_billing_volume 累计结算方数（中心计费）
# @param last_total_billing_volume 上次累计结算方数（中心计费）
# @param billing_remain_money 结算余额
# @param last_billing_remain_money 上次结算余额
# @param billing_time 结算时间
# @param last_billing_time 上次结算时间
def update_fi_charge_record_for_center_billing(rcr_org_id, rcr_id, flmeter_no, total_billing_volume,
                                               last_total_billing_volume,
                                               billing_remain_money, last_billing_remain_money, billing_time,
                                               last_billing_time):
    sql = "UPDATE FI_CHARGE_RECORD fcr SET fcr.TOTAL_BILLING_VOLUME = '" + total_billing_volume + \
          "' ,  fcr.LAST_TOTAL_BILLING_VOLUME = '" + last_total_billing_volume + \
          "' ,  fcr.BILLING_REMAIN_MONEY = '" + billing_remain_money + \
          "' ,  fcr.LAST_BILLING_REMAIN_MONEY = '" + last_billing_remain_money + \
          "' ,  fcr.BILLING_TIME = to_timestamp('" + billing_time + "','yyyy-MM-DD HH24:mi:ss.ff') ,  fcr.LAST_BILLING_TIME = to_timestamp('" + last_billing_time + "','yyyy-MM-DD HH24:mi:ss.ff') where RCR_ORG_ID = :rcr_org_id and RCR_ID=:rcr_id"
    data = [{"rcr_org_id": rcr_org_id, "rcr_id": rcr_id}]
    db.dml_by_where(sql, data)
    print('update_fi_charge_record_for_center_billing ok')


# 从oracle数据库SCADA_FLMETER_DATA读取所有符合条件的数据
# 带参数查询
# @param  org_id 要查询机构号
# @param days 天数 代表几天，可以正值(n天后)，可以负值(n天前),0代表今天
# @param  hours 0代表当前小时 +n代表n小时后 -n代表n小时前
# @return 处理结果 True成功 False失败
def select_sfd_by_where_for_center_billing(org_id, flmeter_no, minTime, maxTime):
    sql = "select * from SCADA_FLMETER_DATA where SFD_ORG_ID= :orgid and FLMETER_NO = :flmeter_no and INSTANT_TIME between :minTime AND :maxTime "
    data = [{"orgid": org_id, "flmeter_no": flmeter_no, "minTime": minTime, "maxTime": maxTime}]
    fc = db.select_by_where_many_params_dict(sql, data)
    print("总共抄表数据:", len(fc))
    # for row in fc:
    #     print(row)
    return fc, data


# 通过流量计编号获取其对应的 充值记录FI_CHARGE_RECORD
# @param org_id 机构号
# @param flmeter_no 流量计编号
def get_price_info_by_price_no_from_select_db(org_id, price_no):
    sql = "select * from PRICE_INFO where  PI_ORG_ID= :pi_org_id and PRICE_NO= :price_no"
    data = [{"pi_org_id": org_id, "price_no": price_no}]
    fc = db.select_by_where_many_params_dict(sql, data)
    return fc


# 通过机构号与流量计编号获得其价格
# @param org_id 要查询机构号
# @param flmeter_no 流量计编号
# @param price_no 对应的价格编号
# @return 具体价格
# 逻辑:直接使用价格编号在价格信息表PRICE_INFO中拿到其价格信息，然后使用取价格的逻辑 直接拿阶梯1的价格 没有的话 拿普通价
def get_price_by_orgid_and_flmeter_no(org_id, flmeter_no, price_no):
    # 先定义一个具体价格的全局变量
    real_price = ""

    # print(price_no)
    price_info_list = get_price_info_by_price_no_from_select_db(org_id, price_no)

    # 如果通过这个价格编号无对应的PRICE_INFO直接抛出提示并且return None直接返回
    if not len(price_info_list) >= 1:
        # print(flmeter_no + "查询无对应的PRICE_INFO")
        return None

    # 程序走到这里代表通过价格编号查到了其价格信息
    # 取出价格信息
    price_info = price_info_list[0]
    # 先取阶梯价格的阶梯价格1
    real_price = price_info['GRADE_PRICE1']
    # 如果阶梯价格1为空，再去取普通价格
    if real_price is None:
        real_price = price_info['PRICE']
    # 若普通价格还是为None 则直接返回real_price
    return real_price


# 处理好数据FI_CENTER_BILLING_DETAIL写入oracle for 中心计费明细表
# @param  中心计费明细表的各个字段
#
# fcbd_org_id=fcbd_org_id,
# fcbd_id=fcbd_id,
# customer_no=customer_no,
# meter_no=meter_no,
# price_no=price_no,
#
# price=price,
# billing_volume=billing_volume,
# billing_money=billing_money,
# remain_volume=remain_volume,
# remain_money=remain_money,
#
# calc_msg=calc_msg,
# billing_time=billing_time,
# total_billing_volume=total_billing_volume,
# last_total_billing_volume=last_total_billing_volume,
# fcbd_status=fcbd_status
#
# @return 处理结果 True成功 False失败
def ok_processing_data_insert_into_oracle_for_fi_center_billing_detail(*args, **kwargs):
    fcbd_dict = kwargs  # 将传过来字典类型的字段值赋给fcbd_dict
    # print(fcbd_dict['meter_no'])
    insert_fi_center_billing_detail(fcbd_dict)
    pass
    return True


# 新增FI_CENTER_BILLING_DETAIL
# @param FI_CENTER_BILLING_DETAIL的各个字段
# @return null 插入成功或失败
def insert_fi_center_billing_detail(fcbd_dict):
    insert_sql = "INSERT INTO FI_CENTER_BILLING_DETAIL (FCBD_ORG_ID,FCBD_ID, CUSTOMER_NO,METER_NO,PRICE_NO," \
                 "PRICE,BILLING_VOLUME,BILLING_MONEY,REMAIN_VOLUME, REMAIN_MONEY," \
                 "CALC_MSG,BILLING_TIME,TOTAL_BILLING_VOLUME,LAST_TOTAL_BILLING_VOLUME,FCBD_STATUS) " \
                 "VALUES" \
                 "(:fcbd_org_id,:fcbd_id, :customer_no,:meter_no,:price_no," \
                 ":price,:billing_volume,:billing_money,:remain_volume, :remain_money," \
                 ":calc_msg,:billing_time,:total_billing_volume,:last_total_billing_volume,:fcbd_status)"
    data = [{"fcbd_org_id": fcbd_dict['fcbd_org_id'], "fcbd_id": fcbd_dict['fcbd_id'], "customer_no": fcbd_dict['customer_no'], "meter_no": fcbd_dict['meter_no'],"price_no": fcbd_dict['price_no'],
             "price": fcbd_dict['price'], "billing_volume": fcbd_dict['billing_volume'], "billing_money": fcbd_dict['billing_money'], "remain_volume": fcbd_dict['remain_volume'], "remain_money": fcbd_dict['remain_money'],
             "calc_msg": fcbd_dict['calc_msg'], "billing_time": fcbd_dict['billing_time'], "total_billing_volume": fcbd_dict['total_billing_volume'], "last_total_billing_volume": fcbd_dict['last_total_billing_volume'], "fcbd_status": fcbd_dict['fcbd_status']}]
    db.dml_by_where(insert_sql, data)  # ok
    print('insert_fi_center_billing_detail ok')


# json格式化时datetime处理类
# Object of type 'datetime' is not JSON serializable 解决方案
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)


# 数据处理-主逻辑处理-主要函数方法
# @param data_for_processing 要处理的原数据
# @param org_id 机构号
# @param flmeter_no 流量计编号
# @param 字典传参 query_datetime 查询操作的日期
# @return 处理结果 True成功 False失败
def data_processing(data_for_processing, org_id, flmeter_no, params_data, **kwargs):
    print(data_for_processing)
    # print(json.dumps(data_for_processing, cls=DateEncoder))  # cls=DateEncoder

    # 对sfd_lists进行空判断
    if len(data_for_processing) == 1:
        print(flmeter_no, "【", params_data[0]['minTime'], params_data[0]['maxTime'], "】", "内只有一条抄表数据,无法进行中心计费逻辑计算")
        return

    # 此表计数据字典列表 排序 按照采集时间INSTANT_TIME排序 默认升序 如果要降序排序,可以指定reverse=True
    sorted_sfd_data_list = sorted(data_for_processing, key=operator.itemgetter('INSTANT_TIME'), reverse=False)

    # 在sorted_sfd_data_list中[0]为之前的时间 [len(sorted_sfd_data_list) - 1]为之后的时间
    # 接下来开始数据处理 【SUM_TOTAL 控制器总累积量（卡控中存储累计用气量）】 标况使用量
    # 周期内标况使用量（之后的时间 - 之前的时间）
    # 周期内使用额（单价 * 周期内标况使用量）结果四舍五入
    after_time_sum_total = sorted_sfd_data_list[len(sorted_sfd_data_list) - 1]['SUM_TOTAL']
    before_time_sum_total = sorted_sfd_data_list[0]['SUM_TOTAL']
    after_time_sum_total = '1'
    # 首先判断after_time_sum_total与before_time_sum_total值是否相同
    if float(after_time_sum_total) == float(before_time_sum_total):
        print(flmeter_no, "【", params_data[0]['minTime'], params_data[0]['maxTime'], "】", "区间内的周期内标况使用量为零,未产生使用,无需进行中心计费计算")
        return

    # 再判断after_time_sum_total<before_time_sum_total是否为true 如果为true 则代表 之后时间的SUM_TOTAL小于之前时间的SUM_TOTAL,出现问题,请核查
    if float(after_time_sum_total) < float(before_time_sum_total):
        print(flmeter_no, "【", params_data[0]['minTime'], params_data[0]['maxTime'], "】", "之后时间的SUM_TOTAL小于之前时间的SUM_TOTAL,出现问题,请核查")
        return

    # 走到这里代表数据正常 可以进行真正的中心计费计算逻辑了
    # 通过流量计编号去取价格的逻辑 这里封装成方法
    price_no_temp = kwargs['price_no']  # 价格编号
    # 对price_no进行空判断
    if price_no_temp is None:
        print(org_id, flmeter_no, "无对应的价格编号")
        return
    # 能走到这里代表其对应的价格编号不为空 下面开始取具体使用的价格的逻辑
    real_price_temp = get_price_by_orgid_and_flmeter_no(org_id, flmeter_no, price_no_temp)

    # 判断real_price_temp是否为None 如果是代表查询无对应的PRICE_INFO
    if real_price_temp is None:
        print(flmeter_no + "查询无对应的PRICE_INFO或对应的PRICE_INFO里阶梯价格1与普通价格都没有值")
        return

    # 程序走到这里代表通过价格编号查到了其价格信息,并且返回了其具体使用的价格
    # print(real_price_temp)
    # 接下来 开始重头戏 算 结算金额(使用金额) = 周期内使用额（单价 * 周期内标况使用量）结果四舍五入
    # 结算金额 = 结算气量 * 单价
    billing_volume_temp = float(after_time_sum_total) - float(before_time_sum_total)  # 结算气量
    billing_money_temp = round((billing_volume_temp * real_price_temp), 2)  # 结算金额 = 结算气量 * 单价

    # 当前时间 现在时间
    now_datetime = datetime.datetime.today()

    # 更新FI_CHARGE_RECORD
    # 更新对应的FI_CHARGE_RECORD的中心计费的相关字段
    this_fi_charge_record_temp = kwargs['this_fi_charge_record']  # 获取当前操作表计的FI_CHARGE_RECORD对象信息
    # 主要是结算方数(本次)与结算余额(本次)写入上一次的结算方数与结算余额,之后结算方数(本次)与结算余额(本次)减去此次计算出的结算值,写入本次
    before_total_billing_volume = this_fi_charge_record_temp['TOTAL_BILLING_VOLUME']  # 本次累计结算方数（中心计费）
    before_last_total_billing_volume = this_fi_charge_record_temp['LAST_TOTAL_BILLING_VOLUME']  # 上次累计结算方数（中心计费）
    before_billing_remain_money = this_fi_charge_record_temp['BILLING_REMAIN_MONEY']  # 本次累计结算余额（中心计费）
    before_last_billing_remain_money = this_fi_charge_record_temp['LAST_BILLING_REMAIN_MONEY']  # 上次累计结算余额（中心计费）
    before_billing_time = this_fi_charge_record_temp['BILLING_TIME']  # 本次结算时间（中心计费）
    before_last_billing_time = this_fi_charge_record_temp['LAST_BILLING_TIME']  # 上次结算时间（中心计费）

    # 要传入数据库逻辑的数据
    db_total_billing_volume = float(before_total_billing_volume) - billing_volume_temp
    db_last_total_billing_volume = float(before_total_billing_volume)

    db_billing_remain_money = float(before_billing_remain_money) - billing_money_temp
    db_last_billing_remain_money = float(before_billing_remain_money)

    db_billing_time = str(params_data[0]['maxTime'])  # 跑此次脚本的时间区间的最大值就是本次的结算时间
    db_last_billing_time = str(before_billing_time)

    # 更新FI_CHARGE_RECORD
    update_fi_charge_record_for_center_billing(this_fi_charge_record_temp['RCR_ORG_ID'],
                                               this_fi_charge_record_temp['RCR_ID'], flmeter_no,
                                               str(db_total_billing_volume),
                                               str(db_last_total_billing_volume),
                                               str(db_billing_remain_money),
                                               str(db_last_billing_remain_money),
                                               db_billing_time,
                                               db_last_billing_time)

    # 准备 中心计费明细账FI_CENTER_BILLING_DETAIL 所有需要写入的字段
    # 机构号 流水号ID 客户编号 表计编号 价格编号 价格 结算气量 结算金额 余量 余额 计算报告，阶梯计费描述用 结算时间 累计结算方数（中心计费）上次累计结算方数（中心计费）删除状态: 1 未删除 9已删除
    # fi_center_billing_detail

    # 新增中心计费明细账 以下是准备所需字段的值

    # 当前时间 拆分年月
    # now_datetime = datetime.datetime.today()
    now_year = str(now_datetime.year)
    now_month = now_datetime.month
    # 如果月份小于10 补零 让9变为09月
    if len(str(now_month)) < 2:
        now_month = "0" + str(now_month)
    else:
        now_month = str(now_month)

    # 记录ID-取自动递增流水号
    ssn_org_id = org_id  # 传入过来的org_id
    ssn_key_name = "FI_CENTER_BILLING_DETAIL"  # 如需修改为其他表的递增流水，请自行修改
    ok_fcbd_id = get_sys_serial_no(db, ssn_org_id, ssn_key_name, now_year, now_month)  # 导入获取流水号方法
    # print(ok_fcbd_id)

    fcbd_org_id = org_id
    fcbd_id = ssn_org_id + now_year + now_month + ok_fcbd_id
    customer_no = kwargs['customer_no']
    meter_no = flmeter_no
    price_no = price_no_temp

    price = real_price_temp
    billing_volume = billing_volume_temp
    billing_money = billing_money_temp
    remain_volume = sorted_sfd_data_list[len(sorted_sfd_data_list) - 1]['REMAIN_VOLUME']  # 查询区间的sfd最后一条
    remain_money = sorted_sfd_data_list[len(sorted_sfd_data_list) - 1]['REMAIN_MONEY']  # 查询区间的sfd最后一条

    calc_msg = '结算气量' + str(billing_volume) + ' 单价:' + str(price) + ' 结算金额:' + str(billing_money_temp)
    billing_time = params_data[0]['maxTime']  # 跑此次脚本的时间区间的最大值就是本次的结算时间
    total_billing_volume = str(db_total_billing_volume)
    last_total_billing_volume = str(db_last_total_billing_volume)
    # 未完待续
    fcbd_status = '1'  # 默认为1 未删除状态

    # 新增add FI_CENTER_BILLING_DETAIL
    is_success = ok_processing_data_insert_into_oracle_for_fi_center_billing_detail(fcbd_org_id=fcbd_org_id,
                                                                                    fcbd_id=fcbd_id,
                                                                                    customer_no=customer_no,
                                                                                    meter_no=meter_no,
                                                                                    price_no=price_no,

                                                                                    price=price,
                                                                                    billing_volume=billing_volume,
                                                                                    billing_money=billing_money,
                                                                                    remain_volume=remain_volume,
                                                                                    remain_money=remain_money,

                                                                                    calc_msg=calc_msg,
                                                                                    billing_time=billing_time,
                                                                                    total_billing_volume=total_billing_volume,
                                                                                    last_total_billing_volume=last_total_billing_volume,
                                                                                    fcbd_status=fcbd_status)
    print('----------------------------------------------------------------------------------------')
    return True


# main方法
# @param db 数据库实例
# @param need_sfi_list 需要中心计费的流量计对象全部信息
# @return main方法运行处理结果 执行完毕即可
def main(db, need_sfi_list):
    print("☆I am main()开始--------------------------------------------------------------------------------")

    # 首先拿出need_sfi_list的表计号(流量计编号)
    flmeter_no_temp = need_sfi_list['FLMETER_NO']

    # 对应的价格编号
    price_no_temp = need_sfi_list['PRICE_NO']

    # 根据流量计编号取出对应的FI_CHARGE_RECORD
    fi_charge_record_list = get_fi_charge_record_list_by_flmeter_no_from_select_db(flmeter_no_temp)
    # print(len(fi_charge_record_list))

    # 如果无对应的FI_CHARGE_RECORD直接抛出提示并且return直接返回
    if not len(fi_charge_record_list) >= 1:
        print(flmeter_no_temp + "无对应的FI_CHARGE_RECORD")
        return

    # 能够走到这个位置代表其有对应的FI_CHARGE_RECORD

    # 取出上次结算时间
    last_billing_time_temp = fi_charge_record_list[0]['LAST_BILLING_TIME']

    # 得到当前时间datetime
    now_datetime = datetime.datetime.today()

    # 如果上次结算时间last_billing_time_temp为None 则直接把当前时间更新进去 【fi_charge_record_list[0]['LAST_BILLING_TIME']】 然后 return
    # print(last_billing_time_temp)
    if last_billing_time_temp is None:
        # print("☆")
        # 更新对应的FI_CHARGE_RECORD的中心计费的相关字段
        update_fi_charge_record_for_center_billing(fi_charge_record_list[0]['RCR_ORG_ID'],
                                                   fi_charge_record_list[0]['RCR_ID'], flmeter_no_temp,
                                                   str("0") if fi_charge_record_list[0]['TOTAL_BILLING_VOLUME'] is None else fi_charge_record_list[0]['TOTAL_BILLING_VOLUME'],
                                                   str("0") if fi_charge_record_list[0]['LAST_TOTAL_BILLING_VOLUME'] is None else fi_charge_record_list[0]['LAST_TOTAL_BILLING_VOLUME'],
                                                   str("0") if fi_charge_record_list[0]['BILLING_REMAIN_MONEY'] is None else fi_charge_record_list[0]['BILLING_REMAIN_MONEY'],
                                                   str("0") if fi_charge_record_list[0]['LAST_BILLING_REMAIN_MONEY'] is None else fi_charge_record_list[0]['LAST_BILLING_REMAIN_MONEY'],
                                                   str(now_datetime),
                                                   str(now_datetime))
        print('☆last_billing_time_temp is None 置为当前时间 return掉了--------------------------------------------------------')
        return
        pass

    # 走到这里代表其对应的FI_CHARGE_RECORD里的上次结算时间不空 继续接下来的逻辑
    # print(last_billing_time_temp)

    # 然后INSTANT_TIME以上次结算时间到当前时间为区间 以orgId和流量计编号为参数 在SCADA_FLMETER_DATA查询其抄表数
    sfd_lists, params_data = select_sfd_by_where_for_center_billing(need_sfi_list['SFI_ORG_ID'], need_sfi_list['FLMETER_NO'], last_billing_time_temp, now_datetime)

    # 对sfd_lists进行空判断
    if not len(sfd_lists) >= 1:
        print(flmeter_no_temp, "【", params_data[0]['minTime'], params_data[0]['maxTime'], "】", "内查询SCADA_FLMETER_DATA无抄表数据")
        return

    # 如果走到这里代表其在此查询区间里有抄表数据 继续接下来的逻辑 处理抄表的数据
    data_processing(sfd_lists, need_sfi_list['SFI_ORG_ID'], need_sfi_list['FLMETER_NO'], params_data, price_no=price_no_temp, customer_no=need_sfi_list['CUSTOMER_NO'], this_fi_charge_record=fi_charge_record_list[0])

    # 其对应的FI_CHARGE_RECORD里
    pass
    print("☆main结束--------------------------------------------------------------------------------")


if __name__ == '__main__':

    # sys.stdout = PrintLogger('python_fi_center_billing_app_king.py.log')  # 监听所有的print到log日志 封装类 如不需要打印所有输出print的log日志，隐掉这段即可

    print("============================================================================================================================================================分隔符")

    db = MyOracle()  # MyOracle()类实例化

    # 程序运行时间计算
    begin_time = None  # 接收程序运行开始时间
    end_time = None  # 接收程序运行结束时间
    begin_time = datetime.datetime.now()
    # print("程序运行开始时间:", begin_time)

    begin_time_clock = None  # 接收程序运行开始时间
    end_time_clock = None  # 接收程序运行结束时间
    begin_time_clock = time.clock()
    # print("程序运行开始time.clock():", begin_time_clock)

    # 实际逻辑
    # 查询出所有需要跑中心计费脚本的流量计
    need_sfi_lists = get_all_scada_flmeter_infos_need_center_billing_run_py_command_script_from_select_db()  # 查询出所有需要跑中心计费脚本的流量计

    # 接下来开始处理查询出数据
    if len(need_sfi_lists) > 0:
        print('----------------------------------------------------------------------------------------')
        # print(need_sfi_lists[0]['SFI_ORG_ID'])
        for need_sfi_list in need_sfi_lists:
            # print(need_sfi_list)
            # 首先调用main方法执行中心计费逻辑
            main(db,need_sfi_list)
        pass
    else:
        print("无需要中心计费的流量计")
        print("----------------------------------------------------------------------------------------")
    pass

    print("☆----------------------------------------------------------------------------------------")
    end_time = datetime.datetime.now()
    print("程序运行开始时间", begin_time)
    print("程序运行结束时间:", end_time)
    print("整个程序运行总时间:", (end_time - begin_time).seconds,"秒")  # (end_time - begin_time).microseconds, "微秒 "1秒 = 10的6次方微秒

    print("☆----------------------------------------------------------------------------------------")
    end_time_clock = time.clock()
    print("程序运行开始time.clock():", begin_time_clock)
    print("程序运行结束time.clock():", end_time_clock)
    print("整个程序运行总时间time.clock()差:", (end_time_clock - begin_time_clock), "秒")
    print("----------------------------------------------------------------------------------------")
