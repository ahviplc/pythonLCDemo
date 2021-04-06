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
# 其他
from utils.util import get_now_time


def run_lmt():
    # 引入lmt逻辑服务类
    from services import pony_orm_lmt_service as pols
    print('进行罗美特业务逻辑')
    # todo
    pass


if __name__ == '__main__':
    # sys.stdout = PrintLogger('MySQLToOracle.app.log')  # 监听所有的print到log日志 封装类 如不需要打印所有输出print的log日志，隐掉这段即可
    start_and_end(True, 1)
    # ------------------------------------------
    run_lmt()
    # ------------------------------------------
    start_and_end(False, 1)
