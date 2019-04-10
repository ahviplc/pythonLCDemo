#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
python_fi_balance_bill_monthly_model.py
月账单 封装类
Version: 1.0
Author: LC
DateTime: 2019年4月9日15:21:25
UpdateTime: 2019年4月9日15:28:58
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
LC博客url: http://oneplusone.vip/index.html
一加壹.SNS LC - 又一个SNS社区: http://sns.oneplusone.vip
赞助一加壹博客最Top-LC万能收款码支持-支付宝、微信、QQ
http://lc.oneplusone.vip/donateMeByLC.html

"""


class FiBalanceBillMonthlyModel:
    # 机构号
    fbb_org_id = ""
    # 单据ID 记录ID-取自动递增流水号
    fbb_id = ""
    # 会计月 YYYYMM
    account_month = ""
    # 流量计编号 表记号
    meter_no = ""
    # 客户编号
    customer_no = ""

    # 上次抄见数 总累计量
    last_read = ""
    # 本次抄见数 总累计量
    this_read = ""
    # 本次用量（控制器总累积量） 本次 - 上次 sumTotal
    this_use_volume = ""
    # 抄表时间
    read_time = ""
    # 抄表员
    read_operator = ""

    # 价格本号
    price_no = ""
    # 价格
    price = ""
    # 应缴金额
    payable_money = ""
    # 应缴日期（最后付款日期）
    payable_date = ""
    # 是否计算滞纳金
    late_fee_enable = ""

    # 滞纳金率
    late_fee_rate = ""
    # 滞纳天数
    late_days = ""
    # 滞纳金
    late_fee_money = ""
    # 合计金额
    payable_money_total = ""
    # 结算操作员
    balance_operator = ""

    # 结算时间
    balance_time = ""
    # 收款操作员
    receipt_operator = ""
    # 收款时间
    receipt_time = ""
    # 营业厅号
    receipt_branch_no = ""
    # 收款单号
    receipt_no = ""

    # 备注
    remark = ""
    # 单据状态0未确认，1未收款，2已收款，9已作废
    fbb_status = ""
    # 付款方式 idbooks6
    fbb_pay_way = ""
    # 实收金额
    receipt_money_total = ""
    # 账单生成时间
    create_time = ""

    def __init__(self, fbb_org_id=fbb_org_id,
                 fbb_id=fbb_id,
                 account_month=account_month,
                 meter_no=meter_no,
                 customer_no=customer_no,

                 last_read=last_read,
                 this_read=this_read,
                 this_use_volume=this_use_volume,
                 read_time=read_time,
                 read_operator=read_operator,

                 price_no=price_no,
                 price=price,
                 payable_money=payable_money,
                 payable_date=payable_date,
                 late_fee_enable=late_fee_enable,

                 late_fee_rate=late_fee_rate,
                 late_days=late_days,
                 late_fee_money=late_fee_money,
                 payable_money_total=payable_money_total,
                 balance_operator=balance_operator,

                 balance_time=balance_time,
                 receipt_operator=receipt_operator,
                 receipt_time=receipt_time,
                 receipt_branch_no=receipt_branch_no,
                 receipt_no=receipt_no,

                 remark=remark,
                 fbb_status=fbb_status,
                 fbb_pay_way=fbb_pay_way,
                 receipt_money_total=receipt_money_total,
                 create_time=create_time):
        self.fbb_org_id = fbb_org_id
        self.fbb_id = fbb_id
        self.account_month = account_month
        self.meter_no = meter_no
        self.customer_no = customer_no

        self.last_read = last_read
        self.this_read = this_read
        self.this_use_volume = this_use_volume
        self.read_time = read_time
        self.read_operator = read_operator

        self.price_no = price_no
        self.price = price
        self.payable_money = payable_money
        self.payable_date = payable_date
        self.late_fee_enable = late_fee_enable

        self.late_fee_rate = late_fee_rate
        self.late_days = late_days
        self.late_fee_money = late_fee_money
        self.payable_money_total = payable_money_total
        self.balance_operator = balance_operator

        self.balance_time = balance_time
        self.receipt_operator = receipt_operator
        self.receipt_time = receipt_time
        self.receipt_branch_no = receipt_branch_no
        self.receipt_no = receipt_no

        self.remark = remark
        self.fbb_status = fbb_status
        self.fbb_pay_way = fbb_pay_way
        self.receipt_money_total = receipt_money_total
        self.create_time = create_time


# 行为:可以做的事
def can_do(self):
    print("i can do")
