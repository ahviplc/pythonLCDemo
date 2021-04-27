import datetime

"""
Python获取周几日期 工具类
"""


class DayOfWeek:
    # 以下都是当前日期时间的周几
    # 周一
    Monday = ""
    # 周二
    Tuesday = ""
    # 周三
    Wednesday = ""
    # 周四
    Thursday = ""
    # 周五
    Friday = ""
    # 周六
    Saturday = ""
    # 周天
    Sunday = ""
    # 其他时间
    # 那个周二
    that_Tuesday = ""
    # 那个周二对应的七天后
    that_Tuesday_after_seven_day = ""

    # week_num 其为int类型 为0代表这周 为1代表下周 为 -1 代表上周二日期 -2为上上周二日期 自己推断下去
    def __init__(self, week_num):
        now = datetime.datetime.now()
        self.Monday = (now - datetime.timedelta(days=now.weekday())).strftime('%Y%m%d')
        self.Tuesday = (now + datetime.timedelta(days=1 - now.weekday())).strftime('%Y%m%d')
        self.Wednesday = (now + datetime.timedelta(days=2 - now.weekday())).strftime('%Y%m%d')
        self.Thursday = (now + datetime.timedelta(days=3 - now.weekday())).strftime('%Y%m%d')
        self.Friday = (now + datetime.timedelta(days=4 - now.weekday())).strftime('%Y%m%d')
        self.Saturday = (now + datetime.timedelta(days=5 - now.weekday())).strftime('%Y%m%d')
        self.Sunday = (now + datetime.timedelta(days=6 - now.weekday())).strftime('%Y%m%d')
        self.that_Tuesday = (now + datetime.timedelta(days=1 - now.weekday() + 7 * week_num)).strftime('%Y%m%d')
        # that_Tuesday_after_seven_day是that_Tuesday的七天之后 也就是下周一 （+7-1） 可到下周一
        self.that_Tuesday_after_seven_day = (now + datetime.timedelta(days=1 - now.weekday() + 7 * week_num + 7 - 1)).strftime('%Y%m%d')
