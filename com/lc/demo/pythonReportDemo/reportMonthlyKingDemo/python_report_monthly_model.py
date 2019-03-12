#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
python_report_monthly_model.py
月报表 封装类
Version: 1.0
Author: LC
DateTime: 2019年3月12日10:45:43
UpdateTime:
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""


class ReportMonthlyModel:
    # 机构号
    srm_org_id = ""
    # 记录ID-取自动递增流水号
    srm_id = ""
    # RTU编号
    rtu_no = ""
    # 流量计编号
    flmeter_no = ""
    # 客户编号
    customer_no = ""

    # 报表时间 年 月 日
    report_time = ""
    year = ""
    month = ""
    day = ""
    # 标况总量（期末数）
    std_sum = ""

    # 工况总量（期末数）
    work_sum = ""
    # 标况流量（周期内最大值）
    max_std_flow = ""
    # 标况流量（周期内最小值）
    min_std_flow = ""
    # 标况流量（周期内平均值）
    avg_std_flow = ""
    # 最大标况流量时间
    max_std_flow_time = ""

    # 最小标况流量时间
    min_std_flow_time = ""
    # 工况流量（周期内最大值）
    max_work_flow = ""
    # 工况流量（周期内最小值）
    min_work_flow = ""
    # 工况流量（周期内平均值）
    avg_work_flow = ""
    # 最大工况流量时间
    max_work_flow_time = ""

    # 最小工况流量时间
    min_work_flow_time = ""
    # 温度（周期内最大值）
    max_temperature = ""
    # 温度（周期内最小值）
    min_temperature = ""
    # 温度（周期内平均值）
    avg_temperature = ""
    # 最高温度时间
    max_temp_time = ""

    # 最低温度时间
    min_temp_time = ""
    # 压力（周期内最高值）
    max_press = ""
    # 压力（周期内最低值）
    min_press = ""
    # 压力（周期内平均值）
    avg_press = ""
    # 最高压力时间
    max_press_time = ""

    # 最低压力时间
    min_press_time = ""
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
    # 总累计使用金额（期末累购金额-期末剩余金额）
    sum_total_money = ""
    # 累购气量（期末数）
    total_buy_volume = ""
    # 累购金额（期末数）
    total_buy_money = ""
    # 剩余金额（期末数）
    remain_money = ""

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
    srm_status = "1"

    def __init__(self, srm_org_id=srm_org_id,
                 srm_id=srm_id,
                 rtu_no=rtu_no,
                 flmeter_no=flmeter_no,
                 customer_no=customer_no,

                 report_time=report_time,
                 year=year,
                 month=month,
                 day=day,
                 std_sum=std_sum,

                 work_sum=work_sum,
                 max_std_flow=max_std_flow,
                 min_std_flow=min_std_flow,
                 avg_std_flow=avg_std_flow,
                 max_std_flow_time=max_std_flow_time,

                 min_std_flow_time=min_std_flow_time,
                 max_work_flow=max_work_flow,
                 min_work_flow=min_work_flow,
                 avg_work_flow=avg_work_flow,
                 max_work_flow_time=max_work_flow_time,

                 min_work_flow_time=min_work_flow_time,
                 max_temperature=max_temperature,
                 min_temperature=min_temperature,
                 avg_temperature=avg_temperature,
                 max_temp_time=max_temp_time,

                 min_temp_time=min_temp_time,
                 max_press=max_press,
                 min_press=min_press,
                 avg_press=avg_press,
                 max_press_time=max_press_time,

                 min_press_time=min_press_time,
                 price=price,
                 use_volume_work=use_volume_work,
                 use_volume_std=use_volume_std,
                 use_money=use_money,

                 sum_total_volume=sum_total_volume,
                 sum_total_money=sum_total_money,
                 total_buy_volume=total_buy_volume,
                 total_buy_money=total_buy_money,
                 remain_money=remain_money,

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
                 srm_status=srm_status):
        self.srm_org_id = srm_org_id
        self.srm_id = srm_id
        self.rtu_no = rtu_no
        self.flmeter_no = flmeter_no
        self.customer_no = customer_no

        self.report_time = report_time
        self.year = year
        self.month = month
        self.day = day
        self.std_sum = std_sum

        self.work_sum = work_sum
        self.max_std_flow = max_std_flow
        self.min_std_flow = min_std_flow
        self.avg_std_flow = avg_std_flow
        self.max_std_flow_time = max_std_flow_time

        self.min_std_flow_time = min_std_flow_time
        self.max_work_flow = max_work_flow
        self.min_work_flow = min_work_flow
        self.avg_work_flow = avg_work_flow
        self.max_work_flow_time = max_work_flow_time

        self.min_work_flow_time = min_work_flow_time
        self.max_temperature = max_temperature
        self.min_temperature = min_temperature
        self.avg_temperature = avg_temperature
        self.max_temp_time = max_temp_time

        self.min_temp_time = min_temp_time
        self.max_press = max_press
        self.min_press = min_press
        self.avg_press = avg_press
        self.max_press_time = max_press_time

        self.min_press_time = min_press_time
        self.price = price
        self.use_volume_work = use_volume_work
        self.use_volume_std = use_volume_std
        self.use_money = use_money

        self.sum_total_volume = sum_total_volume
        self.sum_total_money = sum_total_money
        self.total_buy_volume = total_buy_volume
        self.total_buy_money = total_buy_money
        self.remain_money = remain_money

        self.remain_volume = remain_volume
        self.fm_state = fm_state
        self.rtu_state = rtu_state
        self.valve_state = valve_state
        self.power_voltage = power_voltage

        self.battery_voltage = battery_voltage
        self.battery_level = battery_level
        self.press_in = press_in
        self.press_out = press_out
        self.temp_in = temp_in

        self.temp_out = temp_out
        self.rssi = rssi
        self.srm_status = srm_status


# 行为:可以做的事
def can_do(self):
    print("i can do")
