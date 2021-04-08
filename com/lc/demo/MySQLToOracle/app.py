"""
MySQLToOracle
app.py - 程序主执行文件
Desc:作用:mysql数据转到oracle数据
Author:LC
DateTime: 20210331
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
from config.config import common_config as cc

# 使用全局变量
# global 关键字可以定义一个变量为全局变量，但是这个仅限于在一个模块（py文件）中调用全局变量
# 1.定义
# global val
# 2.使用时再次声明-即全局变量在使用之前就要声明，声明全局变量使用关键字 global，然后在使用该全局变量之前，需要再次声明(若没有再次声明全局变量 则 val 是局部变量)

# 全局变量
# 在使用前初次声明
global org_id  # 机构号
global that_day_min  # 日期时间最小值 不单单指昨天的 承载着任何一天【that_day】
global that_day_max  # 日期时间最大值 不单单指昨天的 承载着任何一天【that_day】
# 给全局变量赋值
org_id = None
that_day_min = None
that_day_max = None


# run_lmt
def run_lmt():
    # 引入lmt逻辑服务类
    from services import pony_orm_lmt_service as pols
    print('进行罗美特业务逻辑')
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
        global that_day_min
        global that_day_max
        print('before_run,当前时间=>', get_now_time())
        print('目前通用配置如下=>【', cc, '】')
        org_id = cc['org_id']
        run_type = cc['run_type']
        # 通过run_type判断 得出不同的that_day_min, that_day_max
        # 具体见方法 util.get_run_which_datetime_max_min_time()
        that_day_min, that_day_max = util.get_run_which_datetime_max_min_time()
        if run_type == 0:
            print('命令执行', '机构', org_id, '处理数据日期时间范围', that_day_min, ' to ', that_day_max)
            print('---开始命令执行操作---')
            return True
        elif run_type == 1:
            print('手动执行', '机构', org_id, '处理数据日期时间范围', that_day_min, ' to ', that_day_max)
            is_del_flag = input('确定要执行此手动执行吗？确定执行输入y,不执行输入n 请输入: ')
            if is_del_flag.lower() == 'y':
                print('---开始手动执行操作---')
                return True
            else:
                print('---你选择了不执行此操作,取消---')
                return False
            return True
        elif run_type == 2:
            print('手动执行-时间范围版', '机构', org_id, '处理数据日期时间范围', that_day_min, ' to ', that_day_max)
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
        global that_day_min
        global that_day_max
        print(org_id, that_day_min, that_day_max)
        # 开始lmt实际逻辑
        # 引入罗美特逻辑服务类
        from services import pony_orm_lmt_service as pols
        from db import db
        print('...机构号:', org_id, '进行罗美特业务逻辑')
        # 从通用配置里拿出以下三个配置
        is_show_sql, is_mysql_create_tables, is_oracle_create_tables = cc['is_show_sql'],cc['is_mysql_create_tables'],cc['is_oracle_create_tables']
        # pony db 数据库引擎初始化
        db.init_db(is_show_sql, is_mysql_create_tables, is_oracle_create_tables)
        # 方法1
        # # 首先 通过日期查询当前日期是否已经写入lmt Oracle数据库
        # srxm_list, srxm_qr = pols.deal_with_data_for_oracle_srxm_select_where(that_day_min)
        # # 有的话 先删除
        # if len(srxm_list) >= 1:
        #     # 删除
        #     pols.deal_with_data_for_oracle_srxm_del_all(srxm_qr)
        # 方法2 直接查询和删除 一体化 按道理 第二种性能更好 一块提交事务
        # 通过that_day_min和that_day_max 拿出所有的对应日 肯定不会跨年 跨月 所以不用理会
        this_year, this_month, days_list = util.get_days_list_from_day_min_to_day_max(that_day_min, that_day_max)
        # pols.deal_with_data_for_oracle_srxm_del_all_with_where(org_id, that_day_min)
        # 使用更改版 - 循环日期进行删除
        print('...机构号:', org_id, '...循环删除...共需删除天份数为：', str(len(days_list)), '天数对应日期范围:', that_day_min, that_day_max)
        for this_day in days_list:
            pols.deal_with_data_for_oracle_srxm_del_all_with_where2(org_id, this_year, this_month, this_day)
        # 删除之后 在从MySQL数据库查询出来当前日期数据 经过数据再次处理之后 写入lmt Oracle数据库
        # 查询所有 不用这个
        # pols.deal_with_data_for_mysql_mrm_select_all()
        # 条件查询 使用
        mrm_list, mrm_qr = pols.deal_with_data_for_mysql_mrm_select_where(that_day_min, that_day_max)
        # Mysql数据处理 和 MySQLToOracle入库
        if len(mrm_list) >= 1:
            # 查询出数据 去执行数据转移代码
            print('...机构号:', org_id, '...MySQL...mrm_list...len...查询MeterReportMonth总条数: ' + str(len(mrm_list)), ' 时间范围: ', that_day_min, ' to ', that_day_max,'去执行数据转移')
            pols.datas_from_mysql_to_oracle(org_id, mrm_list, mrm_qr)
        else:
            # 未查询出数据 输出提示即可
            print('...机构号:', org_id, '...MySQL...mrm_list...len...查询MeterReportMonth总条数: ' + str(len(mrm_list)), ' 时间范围: ', that_day_min, ' to ', that_day_max,'无需执行数据转移')
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
    is_open_log = cc['is_open_log']
    if is_open_log:
        print('...MySQLToOracle...log日志...开启了...')
        sys.stdout = PrintLogger('MySQLToOracle.app.log')  # 监听所有的print到log日志 封装类 如不需要打印所有输出print的log日志，隐掉这段即可
    else:
        print('...MySQLToOracle...log日志...未开启...')
    # 打印一条直线 95个'-'
    util.print_a_line(95)
    # ------------------------------------------
    run_lmt()
    # ------------------------------------------
    start_and_end(False, 1)
