#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
SQLServerToOracleAppKing.py
SQLServer数据库数据迁移至Oracle数据库-万能小工具-包含从SQLServer导出数据至json与从json中解析并向oracle导入数据
Version: 1.0
Author: LC
DateTime: 2019年2月25日09:42:02
UpdateTime: None
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""
import cx_Oracle
import pymssql
import os
import json
from datetime import date, datetime
import sys
import getopt
import decimal
import time

# 改变系统环境编码为简体中文utf-8-为了让oracle查询出的中文不乱码
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


# 定义类-MyOracle
class MyOracle:
    SHOW_SQL = True

    # host    数据库服务器名称或IP
    # port    端口
    # user      用户名
    # password  密码
    # sid/SERVICE_NAME  数据库名称

    def __init__(self, host='###', port=1521, user='SCOTT', password='Lmt123456',
                 sid='LMTPlat'):  # 注意host###里改为自己所需要的ip
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

    # 从ICChargeRecord.json里读取数据
    def json_read_from_icr(self):
        with open('ICChargeRecord.json', 'r+', encoding='utf-8') as f:
            json_dict_list = json.load(f)
            # print(json_dict_list)
            # for i in json_dict_list:
            #     print(i)
            #     print(i['Id'])
        return json_dict_list
        print('ICChargeRecord.json all Done')

    # 解析ICChargeRecord.json写入oracle
    def export_icr_to_oracle(self):

        db = MyOracle()

        json_dict_list = self.json_read_from_icr()  # 从ICChargeRecord.json里读取数据

        # 15个键值对-数据库操作
        sql = "INSERT INTO FI_CHARGE_RECORD (RCR_ORG_ID, RCR_ID, CHARGE_TIME,CUSTOMER_NO,METER_NO,PRICE_NO,PRICE,TOTAL_VOLUME,TOTAL_MONEY,CHARGE_TIMES,METER_TYPE,CHARGE_OPERATOR,RECEIPT_NO,IC_CHARGE_VOLUME,IC_CHARGE_MONEY)  VALUES (:rcrOrgId, :Id, :chargeTime,:customerNo,:meterNo, :priceNo ,:Price,:totalVolume,:totalMoney, :chargeTimes, :meterTypeNo,:chargeOperator,:ReceiptNo,:chargeVolume,:chargeMoney)"

        # print(json_dict_list)
        # 数据处理
        for i in json_dict_list:

            # print(i)

            # 这里要解析的json时间是符合格式的
            chargeTime_timestampStr = i['chargeTime']
            datetime_ok = timestamp_to_date(chargeTime_timestampStr)  # str类型的日期转换为时间戳，时间戳转date
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

        print('输出影响行数:' + str(len(data)))
        print('export_icr_to_oracle ok')


# 定义类-MySQLServer
class MySQLServer:

    # host    数据库服务器名称或IP
    # user      用户名
    # password  密码
    # database  数据库名称

    def __init__(self, host='Server\SQLEXPRESS', user='sa', password='lmt123',
                 database='HTGasMeterSystemLMT_GaoTang'):  # 注意host###里改为自己所需要的ip
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    # 连接数据库-返回conn
    def get_con(self):
        if not self.database:
            raise (NameError, "没有设置数据库信息")
        try:
            conn = pymssql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                   charset="utf8")
            if not conn.cursor():
                raise (NameError, "连接数据库失败")  # 将DBC信息赋值给cur
            else:
                return conn
        except Exception as e:
            print("Exception Error:{error_msg}".format(error_msg=e))  # 使用format
        finally:
            pass

    # 从SQLServer导出CustomerInfo至json文件
    def export_ci_to_json(self):
        conn = self.get_con()
        with conn.cursor(as_dict=True) as cursor:
            cursor.execute('SELECT * FROM CustomerInfo')
            row_all = cursor.fetchall()
            # print(row_all)
            for row in row_all:
                # print(row)
                pass
            print('总操作数据:' + str(len(row_all)))
        # 查询完毕关闭数据库连接
        conn.close()
        cursor.close()
        # 封装成json数据格式，为导出做准备
        json_row_all = json.dumps(row_all, ensure_ascii=False, cls=MyDateTimeAndDecimalEncoder, indent=4)  # json串格式化输出
        # print(json_row_all)
        # 导出至###.json文件中
        with open("CustomerInfo.json", "w", encoding="utf-8") as f_w:
            f_w.write(json_row_all)
            print('已导出CustomerInfo.json文件！')

    # 从SQLServer导出MeterInfo至json文件
    def export_mi_to_json(self):
        conn = self.get_con()
        with conn.cursor(as_dict=True) as cursor:
            cursor.execute('SELECT * FROM MeterInfo')
            row_all = cursor.fetchall()
            # print(row_all)
            for row in row_all:
                # print(row)
                pass
            print('总操作数据:' + str(len(row_all)))
        # 查询完毕关闭数据库连接
        conn.close()
        cursor.close()
        # 封装成json数据格式，为导出做准备
        json_row_all = json.dumps(row_all, ensure_ascii=False, cls=MyDateTimeAndDecimalEncoder, indent=4)  # json串格式化输出
        # print(json_row_all)
        # 导出至###.json文件中
        with open("MeterInfo.json", "w", encoding="utf-8") as f_w:
            f_w.write(json_row_all)
            print('已导出MeterInfo.json文件！')

    # 从SQLServer导出ICChargeRecord至json文件
    def export_icr_to_json(self):
        conn = self.get_con()
        with conn.cursor(as_dict=True) as cursor:
            cursor.execute('SELECT * FROM ICChargeRecord')
            row_all = cursor.fetchall()
            # print(row_all)
            for row in row_all:
                # print(row)
                pass
            print('总操作数据:' + str(len(row_all)))
        # 查询完毕关闭数据库连接
        conn.close()
        cursor.close()
        # 封装成json数据格式，为导出做准备
        json_row_all = json.dumps(row_all, ensure_ascii=False, cls=MyDateTimeAndDecimalEncoder, indent=4)  # json串格式化输出
        # print(json_row_all)
        # 导出至###.json文件中
        with open("ICChargeRecord.json", "w", encoding="utf-8") as f_w:
            f_w.write(json_row_all)
            print('已导出ICChargeRecord.json文件！')


# 公共对象
# 时间与Decimal转换对象-MyDateTimeAndDecimalEncoder
class MyDateTimeAndDecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        # if isinstance(obj, datetime.datetime):
        #     return int(mktime(obj.timetuple()))
        if isinstance(obj, datetime):  # datetime转换
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, decimal.Decimal):  # Decimal转换
            return float(obj)
        else:
            return json.JSONEncoder.default(self, obj)
        super(DecimalEncoder, self).default(obj)


# 公共方法
#  str类型的日期转换为时间戳，时间戳转date方法工具
def timestamp_to_date(timestamp_str):
    # # 原始时间数据格式-'/Date(1510639156973+0800)/'
    # # timestamp_str='/Date(1510639156973+0800)/';
    # jie_qu_timestamp_str=timestamp_str[6:16]  # 这种截取下来就是时间戳

    # 这里是这种
    # 原始时间数据格式-'2017-11-14 13:59:16'
    # timestampStr='2017-11-14 13:59:16';
    timeArray = time.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
    timestamp_int_ok = int(time.mktime(timeArray))  # 此日期格式正常,将其转为时间戳
    # print(timestamp_int_ok)

    datetimes = datetime.fromtimestamp(timestamp_int_ok)
    # print(datetimes)
    return datetimes


# 命令行操作
# 操作说明usage
def usage():
    print(
        """
        Author:LC
        Version:1.0
        Description:SQLServer数据库数据迁移至Oracle数据库-万能小工具-包含从SQLServer导出数据至json与从json中解析并向oracle导入数据
        DateTime:2019年2月25日12:18:13
        
        Usage:sys.args[0] [option]
        -h or --help：显示帮助信息
        -imp or --import：导入(解析json文件，导入，写入Oracle数据库) 参数[all,ci,mi,icr]   
             all:导入所有(ci,mi,icr) 备注:默认为all,如果-imp后 无参数，则默认导入所有
             ci:导入客户信息CustomerInfo
             mi:导入表计信息MeterInfo
             icr:导入IC卡充值记录ICChargeRecord
             例如1：python SQLServerToOracleAppKing.py -imp ci 
             例如2：python SQLServerToOracleAppKing.py -imp mi 
             例如3：python SQLServerToOracleAppKing.py --import icr
        -exp or --export 参数：导出(从SQLServer数据库查询出来，导出到json文件) 参数[all,ci,mi,icr] 
             all:导出所有(ci,mi,icr) 备注:默认为all,如果-exp后 无参数，则默认输出所有
             ci:导出客户信息CustomerInfo
             mi:导出表计信息MeterInfo
             icr:导出IC卡充值记录ICChargeRecord
             例如1：python SQLServerToOracleAppKing.py -exp ci 
             例如2：python SQLServerToOracleAppKing.py -exp mi 
             例如3：python SQLServerToOracleAppKing.py --export icr
        -v or --version：显示版本
        
        Example:
        > python SQLServerToOracleAppKing.py -h
        > python SQLServerToOracleAppKing.py --help
        """
    )


# 命令行cmd方法
def cmd_app():
    if len(sys.argv) == 1:
        print('请输入执行参数-参数参考usage:')
        usage()
        sys.exit()
    else:
        # print(sys.argv[0])  # 第一个参数(它是脚本名称，不是参数的一部分)
        # print(sys.argv[1])
        cmd = sys.argv[1].lower()  # lower() 方法转换字符串中所有大写字符为小写
        print("参数1:" + cmd)
        if cmd not in ("-h", "--help", "-imp", "--import", "-exp", "--export", "-v", "--version"):
            print('执行参数1输入不正确:请参考usage:')
            usage()
        else:
            if cmd in ("-h", "--help"):
                print("help Docs:")
                usage()
                sys.exit()
            elif cmd in ("-imp", "--import"):
                sys.argv.append("")  # 首先 append 一个空字符串，防止命令行-exp无任何参数时，sys.argv[2]的IndexError: list index out of range，数组越界
                cmd2 = sys.argv[2].lower()  # lower() 方法转换字符串中所有大写字符为小写
                print("参数2:" + cmd2)
                if (cmd2.strip() == "" or cmd2.strip() == "all"):
                    print("-imp all todo待完成")
                    pass
                elif (cmd2.strip() == "ci"):
                    print("-imp ci todo待完成")
                    pass
                elif (cmd2.strip() == "mi"):
                    print("-imp mi todo待完成")
                    pass
                elif (cmd2.strip() == "icr"):
                    print("-imp icr todo待完成 已完成")
                    my_oracle = MyOracle()
                    my_oracle.export_icr_to_oracle()
                    pass
                else:
                    print('执行参数2输入不正确:请参考usage:')
                    usage()
            elif cmd in ("-exp", "--export"):
                sys.argv.append("")  # 首先 append 一个空字符串，防止命令行-exp无任何参数时，sys.argv[2]的IndexError: list index out of range，数组越界
                cmd2 = sys.argv[2].lower()  # lower() 方法转换字符串中所有大写字符为小写
                print("参数2:"+cmd2)
                if (cmd2.strip() == "" or cmd2.strip() == "all"):
                    print("-exp all")
                    print("从SQLServer导出CustomerInfo,MeterInfo,ICChargeRecord至json文件:")
                    # 从SQLServer导出CustomerInfo,MeterInfo,ICChargeRecord至json文件
                    my_sql_server = MySQLServer()
                    my_sql_server.export_ci_to_json()
                    my_sql_server.export_mi_to_json()
                    my_sql_server.export_icr_to_json()
                    pass
                elif (cmd2.strip() == "ci"):
                    print("-exp ci")
                    print("从SQLServer导出CustomerInfo至json文件:")
                    # mySQLServer数据导出CustomerInfo至json文件
                    my_sql_server = MySQLServer()
                    my_sql_server.export_ci_to_json()
                    pass
                elif (cmd2.strip() == "mi"):
                    print("-exp mi")
                    print("从SQLServer导出MeterInfo至json文件:")
                    # mySQLServer数据导出MeterInfo至json文件
                    my_sql_server = MySQLServer()
                    my_sql_server.export_mi_to_json()
                    pass
                elif (cmd2.strip() == "icr"):
                    print("-exp icr")
                    print("从SQLServer导出ICChargeRecord至json文件:")
                    # mySQLServer数据导出ICChargeRecord至json文件
                    my_sql_server = MySQLServer()
                    my_sql_server.export_icr_to_json()
                    pass
                else:
                    print('执行参数2输入不正确:请参考usage:')
                    usage()
            elif cmd in ("-v", "--version"):
                print("{pyName} version 1.0".format(pyName=sys.argv[0]))  # 第一个参数(它是脚本名称，不是参数的一部分)
            else:
                pass


# main方法
if __name__ == '__main__':
    cmd_app()

    # mySQLServer对象执行方法
    # mySQLServer数据导出CustomerInfo至json文件
    # my_sql_server = MySQLServer()
    # my_sql_server.export_ci_to_json()

    # MyOracle对象执行方法
    # 解析ICChargeRecord.json写入oracle
    # my_oracle = MyOracle()
    # my_oracle.export_icr_to_oracle()

    pass

# 操作输出样例:
# > python SQLServerToOracleAppKing.py -exp
# 参数1:-exp
# 参数2:
# -exp all
# 从SQLServer导出CustomerInfo,MeterInfo,ICChargeRecord至json文件:
# 总操作数据:7952
# 已导出CustomerInfo.json文件！
# 总操作数据:7974
# 已导出MeterInfo.json文件！
# 总操作数据:14558
# 已导出ICChargeRecord.json文件！

# 操作输出样例1:
# python SQLServerToOracleAppKing.py -exp ci
# 参数1:-exp
# 参数2:ci
# -exp ci
# 从SQLServer导出CustomerInfo至json文件:
# 总操作数据:7952
# 已导出CustomerInfo.json文件！

# 操作输出样例2:
# > python SQLServerToOracleAppKing.py --HELP
# 参数1:-help
# 执行参数1输入不正确:请参考usage:
#
#         Author:LC
#         Version:1.0
#         Description:SQLServer数据库数据迁移至Oracle数据库-万能小工具-包含从SQLServer导出数据至json与从json中解析并向oracle导入数据
#         DateTime:2019年2月25日12:18:13
#
#         Usage:sys.args[0] [option]
#         -h or --help：显示帮助信息
#         -imp or --import：导入(解析json文件，导入，写入Oracle数据库) 参数[all,ci,mi,icr]
#              all:导入所有(ci,mi,icr) 备注:默认为all,如果-imp后 无参数，则默认导入所有
#              ci:导入客户信息CustomerInfo
#              mi:导入表计信息MeterInfo
#              icr:导入IC卡充值记录ICChargeRecord
#              例如1：python SQLServerToOracleAppKing.py -imp ci
#              例如2：python SQLServerToOracleAppKing.py -imp mi
#              例如3：python SQLServerToOracleAppKing.py --import icr
#         -exp or --export 参数：导出(从SQLServer数据库查询出来，导出到json文件) 参数[all,ci,mi,icr]
#              all:导出所有(ci,mi,icr) 备注:默认为all,如果-exp后 无参数，则默认输出所有
#              ci:导出客户信息CustomerInfo
#              mi:导出表计信息MeterInfo
#              icr:导出IC卡充值记录ICChargeRecord
#              例如1：python SQLServerToOracleAppKing.py -exp ci
#              例如2：python SQLServerToOracleAppKing.py -exp mi
#              例如3：python SQLServerToOracleAppKing.py --export icr
#         -v or --version：显示版本
#
#         Example:
#         > python SQLServerToOracleAppKing.py -h
#         > python SQLServerToOracleAppKing.py --help


# 操作输出样例3:
# > python SQLServerToOracleAppKing.py -v
# 参数1:-v
# SQLServerToOracleAppKing.py version 1.0

# 操作输出样例4:
# > python SQLServerToOracleAppKing.py -imp all
# 参数1:-imp
# 参数2:all
# -imp all todo待完成

# 操作输出样例4:
# > python SQLServerToOracleAppKing.py -imp ci
# 参数1:-imp
# 参数2:ci
# -imp ci todo待完成
