"""
MySQLToOracle
app2.py - 程序主执行文件 - 数据清洗
Desc:作用:oracle数据 从数据库 SCADA_REPORT_XN_MID 清洗数据 到 SCADA_REPORT_XN_WEEK
Author:LC
DateTime: 20210425
"""

import sys
# 打印日志专用
from utils.print_msg_to_log_model import PrintLogger
# 耗时工具类专用
from utils.start_to_end_time_consuming import start_and_end
# 导入公共方法 util 导入全部 使用 util.x()调用即可
from utils import util
# 其他 单独导入utils.util的方法 get_now_time
from utils.util import get_now_time
# 导入执行公共配置
from config.config import common_config_for_app2 as ccfa

# 使用全局变量
# global 关键字可以定义一个变量为全局变量，但是这个仅限于在一个模块（py文件）中调用全局变量
# 1.定义
# global val
# 2.使用时再次声明-即全局变量在使用之前就要声明，声明全局变量使用关键字 global，然后在使用该全局变量之前，需要再次声明(若没有再次声明全局变量 则 val 是局部变量)

# 全局变量
# 在使用前初次声明
global org_id  # 机构号
global that_week_min  # 某周二 日期时间最小值 不单单指上周的 承载着任何一周【that_week】
global that_week_max  # 某周一 日期时间最大值 不单单指上周的 承载着任何一周【that_week】
# 给全局变量赋值
org_id = None
that_week_min = None
that_week_max = None


# run_lmt
def run_lmt():
    # 引入lmt逻辑服务类
    # from services import pony_orm_lmt_service as pols
    print('进行罗美特业务逻辑-数据清洗')
    # 打印一条直线 95个'-' 如果传0 则counts使用默认值 95
    util.print_a_line(0)
    if before_run():
        if run():
            after_run()
        else:
            print('run 跳出,当前时间=>', get_now_time())
    else:
        print('before_run 跳出,当前时间=>', get_now_time())
    pass


# run之前 执行
def before_run():
    try:
        # 使用时 再次声明全局变量 表示在这里使用的是全局变量，而不是局部变量
        global org_id
        global that_week_min # 周二-某日期的最小时间
        global that_week_max # 周一-某日期7天之后的最大时间
        print('before_run,当前时间=>', get_now_time())
        print('目前for_app2通用配置如下=>【', ccfa, '】')
        org_id = ccfa['org_id']
        run_type = ccfa['run_type']
        that_week_min, that_week_max = util.get_run_which_datetime_max_min_week()
        if run_type == 0:
            print('命令执行', '机构', org_id, '处理数据周二到周一日期时间范围', that_week_min, ' to ', that_week_max)
            print('---开始命令执行操作---')
            return True
        elif run_type == 1:
            print('手动执行-时间范围版', '机构', org_id, '处理数据日期时间范围', that_week_min, ' to ', that_week_max, '确定执行输入y,不执行输入n 请输入:')
            is_del_flag = input('确定要执行此手动执行-时间范围版吗？确定执行输入y,不执行输入n 请输入: ')
            if is_del_flag.lower() == 'y':
                print('---开始手动执行-时间范围版操作---')
                return True
            else:
                print('---你选择了不执行此操作,取消---')
                return False
            return True
        else:
            print('...before_run...run_type 为', run_type, '不存在', '不执行此操作,取消---')
            return False
    except Exception as e:
        print("before_run Exception Error:%s" % e)
        return False
    finally:
        pass
        # 打印一条直线 95个'-'
        util.print_a_line(95)
    # 走到这里的话 那就代表公共参数不合法不对 跳出 before_run 返回 False
    return False


# run
def run():
    try:
        print('run,当前时间=>', get_now_time())
        # 使用时 再次声明，表示在这里使用的是全局变量，而不是局部变量
        global org_id
        global that_week_min
        global that_week_max
        print(org_id, that_week_min, that_week_max)
        # 开始lmt实际逻辑
        # 引入罗美特逻辑服务类
        from services import pony_orm_lmt_service as pols
        from db import db
        print('...机构号:', org_id, '进行罗美特业务逻辑-数据清洗')
        # 从通用配置里拿出以下三个配置
        is_show_sql, is_mysql_create_tables, is_oracle_create_tables = ccfa['is_show_sql'], ccfa['is_mysql_create_tables'], ccfa['is_oracle_create_tables']
        # pony db 数据库引擎初始化
        db.init_db(is_show_sql, is_mysql_create_tables, is_oracle_create_tables)
        # 开始吧
        # 首先根据周二日期that_week_min 去查询SCADA_REPORT_XN_MID【ScadaReportXNMid】表
        srxm_list_that_week_min, srxm_qr = pols.deal_with_data_for_oracle_srxm_select_where_with_org_id(org_id, that_week_min)
        # Mysql数据处理 和 MySQLToOracle入库
        if len(srxm_list_that_week_min) >= 1:
            # 查询出数据 去执行数据转移代码
            print('...机构号:', org_id, '...Oracle...srxm_list...len...查询ScadaReportXNMid总条数: ' + str(len(srxm_list_that_week_min)), ' 时间: ', that_week_min, '去执行数据清洗')
            # 打印一条直线 95个'-'
            util.print_a_line(95)
            pols.datas_from_mid_to_week_wash_data_oracle(org_id, srxm_list_that_week_min, srxm_qr, that_week_min, that_week_max)
        else:
            # 未查询出数据 输出提示即可
            print('...机构号:', org_id, '...Oracle...srxm_list...len...查询ScadaReportXNMid总条数: ' + str(len(srxm_list_that_week_min)), ' 时间: ', that_week_min, '无需执行数据清洗 跳出程序')
        return True
    except Exception as e:
        print("run Exception Error:%s" % e)
        return False
    finally:
        pass
        # 打印一条直线 95个'-'
        util.print_a_line(95)
    # 走到这里的话 那就代表run执行完毕
    return True


# run之后 执行
def after_run():
    try:
        print('after_run,当前时间=>', get_now_time())
        pass
        return True
    except Exception as e:
        print("after_run Exception Error:%s" % e)
        return False
    finally:
        pass
    # 走到这里的话 那就代表after_run执行完毕
    return True


if __name__ == '__main__':
    start_and_end(True, 1)
    # 是否开启日志
    is_open_log = ccfa['is_open_log']
    if is_open_log:
        print('...MySQLToOracle...log日志...app2...开启了...')
        sys.stdout = PrintLogger('MySQLToOracle.app2.log')  # 监听所有的print到log日志 封装类 如不需要打印所有输出print的log日志，隐掉这段即可
    else:
        print('...MySQLToOracle...log日志...未开启...')
    # 打印一条直线 95个'-'
    util.print_a_line(95)
    # ------------------------------------------
    run_lmt()
    # ------------------------------------------
    start_and_end(False, 1)
