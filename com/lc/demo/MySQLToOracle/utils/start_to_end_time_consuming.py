"""
start_to_end_ time_consuming.py 开始到结束 耗时工具类
Author:LC
"""
import time
import datetime

# 使用全局变量
# global 关键字可以定义一个变量为全局变量，但是这个仅限于在一个模块（py文件）中调用全局变量
# 1.定义
# global val
# 2.使用时再次声明-即全局变量在使用之前就要声明，声明全局变量使用关键字 global，然后在使用该全局变量之前，需要再次声明(若没有再次声明全局变量 则 val 是局部变量)

# 全局变量
# 在使用前初次声明
global begin_time_clock  # 接收程序运行开始时间
global end_time_clock  # 接收程序运行结束时间
global begin_time  # 接收程序运行开始时间
global end_time  # 接收程序运行结束时间
# 给全局变量赋值
begin_time_clock = None
end_time_clock = None
begin_time = None
end_time = None


# start_and_end
# is_start 是否是开始 True 是代表开始 False 代表结束
# which_type 1为time.perf_counter()版本 2为datetime.datetime.now()版本
def start_and_end(is_start, which_type):
    # 使用时再次声明 全局变量 表示在这里使用的是全局变量，而不是局部变量
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
