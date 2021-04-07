"""
MySQLToOracle
app_for_tests.py - 测试程序主执行文件
Desc:作用:测试一下
Author:LC
DateTime: 20210406
"""

import sys
# 打印日志专用
from utils.print_msg_to_log_model import PrintLogger
# 耗时工具类专用
from utils.start_to_end_time_consuming import start_and_end
# 其他 单独导入utils.util的方法 get_now_time
from utils.util import get_now_time


# 可用
# from config.config import mysql_db_config as conf

def run_pymysql_dbhelper():
    from core import pymysql_DBHelper as pd
    db = pd.DBHelper('select * from settings')
    # db.select()
    # db.selectDict()
    for i in [1, 3]:
        db.selectDict_finally_close_db()
    pass


def run_cx_Oracle_dbhelper():
    from core import cx_Oracle_DBHelper as cod
    db = cod.DBHelper()
    sql = "select * from BRANCH_INFO"
    # 查询所有
    # fc = db.select_all(sql)
    # 带条件查询
    # data = [{}] # 不传 代表只是sql 类似db.select_all(sql)
    # fc = db.select_by_where_many_params_dict(sql, data)

    sql2 = "select * from BRANCH_INFO where BI_ORG_ID= :bi_org_id"
    # 带条件查询 含真实条件
    bi_org_id = '0003'
    data2 = [{"bi_org_id": bi_org_id}]  # 不传 代表只是sql 类似db.select_all(sql)
    fc = db.select_by_where_many_params_dict(sql2, data2)
    print(fc)
    pass


def run():
    print(get_now_time())
    pass


def run_pony():
    from core import pony_orm_DBHelper as pod
    pod.run_pony()  # 必须要执行的
    pod.add_one()
    pod.run_db_session()


def run_test():
    # 引入测试逻辑服务类
    from services import pony_orm_test_service as pots
    from db import db
    print('进行测试业务逻辑')
    # pony db 数据库引擎初始化
    db.init_db(True, True, False)
    pots.add_data_artist_for_mysql()
    pots.add_data_artist_for_oracle()
    pass


def run_lmt():
    # 引入lmt逻辑服务类
    from services import pony_orm_lmt_service as pols
    print('进行罗美特业务逻辑')
    pass


if __name__ == '__main__':
    # sys.stdout = PrintLogger('MySQLToOracle.app_for_tests.log')  # 监听所有的print到log日志 封装类 如不需要打印所有输出print的log日志，隐掉这段即可
    start_and_end(True, 1)
    # ------------------------------------------
    # run()
    # run_pymysql_dbhelper()
    # run_cx_Oracle_dbhelper()
    # run_pony()
    run_test()
    # run_lmt()
    # ------------------------------------------
    start_and_end(False, 1)
