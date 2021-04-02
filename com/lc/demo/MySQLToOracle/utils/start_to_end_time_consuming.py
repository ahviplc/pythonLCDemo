"""
start_to_end_ time_consuming.py 开始到结束 耗时工具类
Author:LC
"""
import time
import datetime


# start_and_end
# is_start 是否是开始 True 是代表开始 False 代表结束
# which_type 1为time.perf_counter()版本 2为datetime.datetime.now()版本
def start_and_end(is_start, which_type):
    global begin_time_clock  # 接收程序运行开始时间
    global end_time_clock  # 接收程序运行结束时间
    global begin_time  # 接收程序运行开始时间
    global end_time  # 接收程序运行结束时间
    if is_start:
        print("============================================================================================分隔符")
        print('开始执行....')
        if which_type == 1:
            begin_time_clock = time.perf_counter()
            begin_time = datetime.datetime.now()
            print("程序运行开始time.perf_counter():", begin_time_clock, " 程序运行开始时间:", begin_time)
            print("----------------------------------------------------------------------------------------")
        else:
            begin_time = datetime.datetime.now()
            print("程序运行开始时间:", begin_time)
            print("----------------------------------------------------------------------------------------")
    else:
        if which_type == 1:
            end_time_clock = time.perf_counter()
            end_time = datetime.datetime.now()
            print("----------------------------------------------------------------------------------------")
            print("程序运行结束time.perf_counter():", end_time_clock, " 程序运行结束时间:", end_time)
            print("----------------------------------------------------------------------------------------")
            print("程序运行开始time.perf_counter():", begin_time_clock, " 程序运行开始时间:", begin_time)
            print("程序运行结束time.perf_counter():", end_time_clock, " 程序运行结束时间:", end_time)
            print("整个程序运行总时间time.perf_counter()差:", (end_time_clock - begin_time_clock), "秒")
            print("----------------------------------------------------------------------------------------")
        else:
            end_time = datetime.datetime.now()
            print("----------------------------------------------------------------------------------------")
            print("程序运行结束时间:", end_time)
            print("----------------------------------------------------------------------------------------")
            print("程序运行开始时间", begin_time)
            print("程序运行结束时间:", end_time)
            print("整个程序运行总时间:", (end_time - begin_time).seconds, "秒")  # (end_time - begin_time).microseconds, "微秒 "1秒 = 10的6次方微秒
            print("----------------------------------------------------------------------------------------")
        print("============================================================================================分隔符")
