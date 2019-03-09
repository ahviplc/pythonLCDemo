#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
python_report_daily_model.py
日报表 封装类
Version: 1.0
Author: LC
DateTime: 2019年3月8日18:19:09
UpdateTime: 2019年3月9日23:39:10
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""


class ReportDailyModel:
    # 机构号
    srd_org_id = ""
    # 记录ID-取自动递增流水号
    srd_id = ""
    # RTU编号
    rtu_no = ""
    # 流量计编号
    flmeter_no = ""
    # 客户编号
    customer_no = ""

    # 报表时间 年 月 日 时
    report_time = ""
    year = ""
    month = ""
    day = ""
    hour = ""

    # 标况总量（期末数）
    std_sum = ""
    # 工况总量（期末数）
    work_sum = ""
    # 标况流量（周期内平均值）
    std_flow = ""
    # 工况流量（周期内平均值）
    work_flow = ""
    # 温度（周期内平均值）
    temperature = ""

    # 压力（周期内平均值）
    pressure = ""
    # 单价（期末数）
    price = ""
    # 周期内工况使用量（周期内期末数-期初数）
    use_volume_work = ""
    # 周期内标况使用量（周期内期末数 - 期初数）
    use_volume_std = ""
    # 周期内使用额（单价（期末数）* 周期内标况使用量）结果四舍五入
    use_money = ""

    # 总累积使用量（期末数）
    sum_total_volume = ""
    # 累购气量（期末数）
    total_buy_volume = ""
    # 累购金额（期末数）
    total_buy_money = ""
    # 剩余金额（期末数）
    remain_money = ""
    # 总累计使用金额（期末累购金额-期末剩余金额）
    sum_total_money = ""

    # 剩余数量（期末数）
    remain_volume = ""
    # 流量计状态（期末数）
    fm_state = ""
    # RTU状态（期末数）
    rtu_state = ""
    # 阀门控制器状态（期末数）
    valve_state = ""
    # 供电电压（周期内平均值）
    power_voltage = ""

    # 电池电压（期末数）
    battery_voltage = ""
    # 电池电量（期末数）
    battery_level = ""
    # 入口压力（周期内平均值）
    press_in = ""
    # 出口压力（周期内平均值）
    press_out = ""
    # 入口温度（周期内平均值）
    temp_in = ""

    # 出口温度（周期内平均值）
    temp_out = ""
    # 信号强度（平均值）
    rssi = ""
    # 删除标识符 1正常，9不正常已删除 默认置为1
    srd_status = "1"

    def __init__(self, srd_org_id=srd_org_id,
                 srd_id=srd_id,
                 rtu_no=rtu_no,
                 flmeter_no=flmeter_no,
                 customer_no=customer_no,
                 report_time=report_time,
                 year=year,
                 month=month,
                 day=day,
                 hour=hour,
                 std_sum=std_sum,
                 work_sum=work_sum,
                 std_flow=std_flow,
                 work_flow=work_flow,
                 temperature=temperature,
                 pressure=pressure,
                 price=price,
                 use_volume_work=use_volume_work,
                 use_volume_std=use_volume_std,
                 use_money=use_money,
                 sum_total_volume=sum_total_volume,
                 total_buy_volume=total_buy_volume,
                 total_buy_money=total_buy_money,
                 remain_money=remain_money,
                 sum_total_money=sum_total_money,
                 remain_volume=remain_volume,
                 fm_state=fm_state,
                 rtu_state=rtu_state,
                 valve_state=valve_state,
                 power_voltage=power_voltage,
                 battery_voltage=battery_voltage,
                 battery_level=battery_level,
                 press_in=press_in,
                 press_out=press_out,
                 temp_in=temp_in,
                 temp_out=temp_out,
                 rssi=rssi,
                 srd_status=srd_status):
        # 机构号
        self.srd_org_id = srd_org_id
        # 记录ID-取自动递增流水号
        self.srd_id = srd_id
        # RTU编号
        self.rtu_no = rtu_no
        # 流量计编号
        self.flmeter_no = flmeter_no
        # 客户编号
        self.customer_no = customer_no

        # 报表时间 年 月 日 时
        self.report_time = report_time
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour

        # 标况总量（期末数）
        self.std_sum = std_sum
        # 工况总量（期末数）
        self.work_sum = work_sum
        # 标况流量（周期内平均值）
        self.std_flow = std_flow
        # 工况流量（周期内平均值）
        self.work_flow = work_flow
        # 温度（周期内平均值）
        self.temperature = temperature

        # 压力（周期内平均值）
        self.pressure = pressure
        # 单价（期末数）
        self.price = price
        # 周期内工况使用量（周期内期末数-期初数）
        self.use_volume_work = use_volume_work
        # 周期内标况使用量（周期内期末数 - 期初数）
        self.use_volume_std = use_volume_std
        # 周期内使用额（单价（期末数）* 周期内标况使用量）结果四舍五入
        self.use_money = use_money

        # 总累积使用量（期末数）
        self.sum_total_volume = sum_total_volume
        # 累购气量（期末数）
        self.total_buy_volume = total_buy_volume
        # 累购金额（期末数）
        self.total_buy_money = total_buy_money
        # 剩余金额（期末数）
        self.remain_money = remain_money
        # 总累计使用金额（期末累购金额-期末剩余金额）
        self.sum_total_money = sum_total_money

        # 剩余数量（期末数）
        self.remain_volume = remain_volume
        # 流量计状态（期末数）
        self.fm_state = fm_state
        # RTU状态（期末数）
        self.rtu_state = rtu_state
        # 阀门控制器状态（期末数）
        self.valve_state = valve_state
        # 供电电压（周期内平均值）
        self.power_voltage = power_voltage

        # 电池电压（期末数）
        self.battery_voltage = battery_voltage
        # 电池电量（期末数）
        self.battery_level = battery_level
        # 入口压力（周期内平均值）
        self.press_in = press_in
        # 出口压力（周期内平均值）
        self.press_out = press_out
        # 入口温度（周期内平均值）
        self.temp_in = temp_in

        # 出口温度（周期内平均值）
        self.temp_out = temp_out
        # 信号强度（平均值）
        self.rssi = rssi
        # 删除标识符 1正常，9不正常已删除 默认置为1
        self.srd_status = srd_status


# 行为:可以做的事
def can_do(self):
    print("i can do")
