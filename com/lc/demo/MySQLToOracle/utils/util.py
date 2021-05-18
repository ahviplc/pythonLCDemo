import datetime
import random
import string
import re
import decimal
from cx_Oracle import makedsn

# 导入执行公共配置
from config.config import common_config as cc


# get_now_time
# @return 当前日期时间
def get_now_time():
    return datetime.datetime.now()


# 处理db_config_oracle
# 使其可用
# @param  db_config_oracle 原先的字典Dict类型配置项
# @return 可用的db_config_oracle
def make_db_config_oracle_better(db_config_oracle):
    # print(db_config_oracle)
    db_config_oracle_dict = db_config_oracle
    db_config_oracle_dict_new = {}
    db_config_oracle_dict_new['provider'] = db_config_oracle_dict['provider']
    db_config_oracle_dict_new['user'] = db_config_oracle_dict['user']
    db_config_oracle_dict_new['password'] = db_config_oracle_dict['password']
    dsn_tns = makedsn(db_config_oracle_dict['host'], db_config_oracle_dict['port'], db_config_oracle_dict['sid'])
    # 如果是Oracle 12c 数据库需要替换sid 为service_name
    dsn_tns = dsn_tns.replace('SID', 'SERVICE_NAME')
    db_config_oracle_dict_new['dsn'] = dsn_tns
    # print('...美化后...db_config_oracle...',db_config_oracle_dict_new)
    return db_config_oracle_dict_new


# 获取间隔n天时间的最小时间(0点)和最大时间(23点59分59秒)-datetime.timedelta(days=1)可以处理天，datetime.timedelta(weeks=1)也可以处理周等
# @param  n,type,isFormat; n代表几天，可以正值(n天后)，可以负值(n天前),0代表今天 ;
#                          type取值有max和min,max代表输出当前时间最大时间，min代表输出当前时间最小时间;
#                          isFormat是否格式化输出，布尔值为True,格式化输出str类型时间,为False,不格式化输出，直接返回datetime类型时间。
# @return 符合要求的datetime格式日期
# 使用示例:
# print(to_n_datetime_max_min_time(2,"max", False))-2019-03-09 23:59:59.999999
# print(to_n_datetime_max_min_time(0,"min", False))-2019-03-07 00:00:00
# print(to_n_datetime_max_min_time(-1,"min", False))-2019-03-06 00:00:00
# print(to_n_datetime_max_min_time(-5, "max", True))-2019-03-02 23:59:59
def to_n_datetime_max_min_time(n, type, is_format):
    if type == "max":
        return_time = datetime.datetime.combine(datetime.date.today() + datetime.timedelta(days=n), datetime.time.max)
    elif type == "min":
        return_time = datetime.datetime.combine(datetime.date.today() + datetime.timedelta(days=n), datetime.time.min)
    if (is_format):
        return_time = return_time.strftime('%Y-%m-%d %H:%M:%S')
    return return_time


# 获取指定日期的时间的最小时间(0点)和最大时间(23点59分59秒)-datetime.timedelta(days=1)可以处理天，datetime.timedelta(weeks=1)也可以处理周等
# @param  diy_date,type,isFormat; diy_date代表指定的日期 ;
#                          type取值有max和min,max代表输出当前时间最大时间，min代表输出当前时间最小时间;
#                          isFormat是否格式化输出，布尔值为True,格式化输出str类型时间,为False,不格式化输出，直接返回datetime类型时间。
# @return 符合要求的datetime格式日期
# 使用示例:
# print(to_diy_date_datetime_max_min_time('20190309',"max", False))-2019-03-09 23:59:59.999999
# print(to_diy_date_datetime_max_min_time('20190307',"min", False))-2019-03-07 00:00:00
# print(to_diy_date_datetime_max_min_time('20190306',"min", False))-2019-03-06 00:00:00
# print(to_diy_date_datetime_max_min_time('20190302', "max", True))-2019-03-02 23:59:59
def to_diy_date_datetime_max_min_time(diy_date, type, is_format):
    this_datetime_date = datetime.date(year=int(diy_date[0:4]), month=int(diy_date[4:6]), day=int(diy_date[6:8]))
    if type == "max":
        return_time = datetime.datetime.combine(this_datetime_date, datetime.time.max)
    elif type == "min":
        return_time = datetime.datetime.combine(this_datetime_date, datetime.time.min)
    if (is_format):
        return_time = return_time.strftime('%Y-%m-%d %H:%M:%S')
    return return_time


# 获取当前脚本执行 要处理对应数据日期时间的年月
# 从config里 通用配置 可算出 拿到
# 使用示例:
# print(get_run_which_day_year_month()-202104
# 为了拼接到MySQL表名后 具体找到对应表
# 'meter_report_month_' + '202104'
# meter_report_month_202104
# @return 对应的年月拼接
def get_run_which_datetime_year_month():
    that_day_min, that_day_max = get_run_which_datetime_max_min_time()
    # 从that_day_min或者that_day_max均可取出
    this_year = that_day_min.year
    this_month = that_day_max.month
    # 处理年
    this_year = get_real_year_month_day(this_year)
    # 处理月
    # print(len(str(this_month)))
    # 如果月份小于10 补零 让9变为09月
    this_month = get_real_year_month_day(this_month)
    return this_year + this_month


# 获取当前脚本执行 要处理对应数据日期时间 某日期最大时间和某日期最小时间
# 从config里 通用配置 可算出 拿到
# @return 通过run_type判断 得出不同的that_day_min, that_day_max
def get_run_which_datetime_max_min_time():
    that_day_min = None
    that_day_max = None
    run_type = cc['run_type']
    if run_type == 0:
        days = cc['days']
        that_day_min = to_n_datetime_max_min_time(days, "min", False)
        that_day_max = to_n_datetime_max_min_time(days, "max", False)
    elif run_type == 1:
        diy_date = cc['diy_date']
        that_day_min = to_diy_date_datetime_max_min_time(diy_date, "min", False)
        that_day_max = to_diy_date_datetime_max_min_time(diy_date, "max", False)
    elif run_type == 2:
        diy_range_date = cc['diy_range_date']
        diy_range_date_list = diy_range_date.split('#')
        diy_date_min = diy_range_date_list[0]
        diy_date_max = diy_range_date_list[1]
        that_day_min = to_diy_date_datetime_max_min_time(diy_date_min, "min", False)
        that_day_max = to_diy_date_datetime_max_min_time(diy_date_max, "max", False)
    else:
        # 当天日期
        today_datetime_date = datetime.date.today()
        # 格式化年月日
        this_year, this_month, this_day = get_year_month_day_from_datetime(today_datetime_date)
        today_date = this_year + this_month + this_day
        that_day_min = to_diy_date_datetime_max_min_time(today_date, "min", False)
        that_day_max = to_diy_date_datetime_max_min_time(today_date, "max", False)
        print('...get_run_which_datetime_max_min_time...run_type 为', run_type, '不存在', 'that_day_min，that_day_max 取今天', today_date)
    return that_day_min, that_day_max


# 传入一个datetime 获取其 年月日
# @param 传入的datetime
# @return 输出格式为 2021,04,06
# 输出均是字符串
def get_year_month_day_from_datetime(in_datetime):
    this_year = in_datetime.year
    this_month = in_datetime.month
    this_day = in_datetime.day
    # 处理年
    this_year = get_real_year_month_day(this_year)
    # 处理月
    # print(len(str(this_month)))
    # 如果月份小于10 补零 让9变为09月
    this_month = get_real_year_month_day(this_month)
    # 处理日
    # print(len(this_day))
    # 如果日小于10 补零 让9变为09日
    this_day = get_real_year_month_day(this_day)
    return this_year, this_month, this_day


# 从a-zA-Z0-9生成指定数量的随机字符
# 生成指定数量的随机字符
# @param counts 生成的数量
# @return 结果字符串
def get_random_str_with_counts(counts):
    return ''.join(random.sample(string.ascii_letters + string.digits, counts))


# 返回符合要求的 年月日 格式
# @param in_ymd 进来的可能是 int 类型的 年 2021 月 4 日 6
# @return 返回出去的会是 字符串类型的 年 2021 月 04 日 06
def get_real_year_month_day(in_ymd):
    # 处理年月日
    # print(len(str(in_ymd)))
    # 如果月份小于10 补零 让9变为09月
    if len(str(in_ymd)) < 2:
        in_ymd = "0" + str(in_ymd)
    else:
        in_ymd = str(in_ymd)
    return in_ymd


# @param in_num 输入的字符或者数字或者 float
# @return 如果是浮点数 float 则直接返回其字符串格式
# 如果不是 float 则返回 None
def get_float_str(in_num):
    if is_float(in_num):
        return str(in_num)
    else:
        return None


# 判断"字符串"是否为数字
# @param s 要检测的字符串
# @return 处理结果 True是数字 False不是数字
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False


# 判断字符串是否为 float
# @param num 要检测的num或者字符串num
# @return 如果包含两个（或以上）小数点，return False
# 否则（只剩一个或者没有小数点），去掉字符串中的小数点，然后判断是否全是由数字组成，是，return True，否，return False
# 返回True 代表为 float 返回False 代表不为 float
def is_float(num):
    string1 = str(num)
    if string1.count('.') > 1:  # 检测字符串小数点的个数
        # 如果小数点个数大于 1 肯定不是float
        return False
    elif string1.isdigit():  # 检测字符串是否只由数字组成，如果字符串只包含数字则返回 True 否则返回 False
        # 只是包含数字的话 就不是float
        return False
    else:
        new_string = string1.split(".")  # 按小数点分割字符
        first_num = new_string[0]  # 取分割完之后这个list的第一个元素
        # 判断负号的个数和first_num第一个元素是不是"-"，如果负号个数等于1并且firs_num第一个元素是"-"，则合法
        if first_num.count('-') == 1 and first_num[0] == '-':
            first_num = first_num.replace('-', '')
        if first_num.isdigit() and new_string[1].isdigit():
            return True
        else:
            return False


# 通过that_day_min和that_day_max 拿出所有的对应日 肯定不会跨年 跨月 所以不用理会
# @param that_day_min,that_day_max
# @return 返回 年 月 日的list集合
def get_days_list_from_day_min_to_day_max(that_day_min, that_day_max):
    min_this_year, min_this_month, min_this_day = get_year_month_day_from_datetime(that_day_min)
    max_this_year, max_this_month, max_this_day = get_year_month_day_from_datetime(that_day_max)
    days_list = []
    for i in range(int(min_this_day), int(max_this_day) + 1, 1):
        # print(i)
        days_list.append(get_real_year_month_day(i))
    return min_this_year, max_this_month, days_list


# 打印一条直线 用于分割日志 是log日志更加直观
# @param counts_tuple '-'的数量 传来的可变元组（Tuple） 如果不传或者传0 则使用默认值 95 如果传多值 则取第一个值
# @return 返回 加工好的直线
def print_a_line(*counts_tuple):
    counts = None
    # 不传
    if len(counts_tuple) == 0:
        counts = 95
    # 传1值 并且值是0
    elif len(counts_tuple) == 1 and counts_tuple[0] == 0:
        counts = 95
    # 传其他 多值的话 取第一个值
    else:
        counts = counts_tuple[0]
    a_line = '-' * counts
    print(a_line)
    return a_line


# 获取当前脚本执行 要处理对应数据周二日期时间 和七天之后 周一
# 从config里 通用配置 可算出 拿到
# @return 通过run_type判断 得出不同的that_week_min, that_week_max
def get_run_which_datetime_max_min_week():
    # 导入执行公共配置
    from config.config import common_config_for_app2 as ccfa
    from utils.day_of_week_model import DayOfWeek
    that_week_min = None
    that_week_max = None
    run_type = ccfa['run_type']
    if run_type == 0:
        week_num = ccfa['week_num']
        # 类DayOfWeek的实例化
        dow = DayOfWeek(week_num)
        # 周二-那个周二日期的最小时间 - 周二的日期
        that_Tuesday = dow.that_Tuesday
        # 周一-那个周二日期7天之后的最大时间 也就是周一 - 上面周二日期时间的七天后
        that_Tuesday_after_seven_day = dow.that_Tuesday_after_seven_day
        # 某周二 日期时间最小值 不单单指上周的 承载着任何一周【that_week】
        that_week_min = to_diy_date_datetime_max_min_time(that_Tuesday, "min", False)
        # 某周一 日期时间最大值 不单单指上周的 承载着任何一周【that_week】
        that_week_max = to_diy_date_datetime_max_min_time(that_Tuesday_after_seven_day, "max", False)
    elif run_type == 1:
        diy_range_date = ccfa['diy_range_date']
        diy_range_date_list = diy_range_date.split('#')
        diy_date_min = diy_range_date_list[0]
        diy_date_max = diy_range_date_list[1]
        that_week_min = to_diy_date_datetime_max_min_time(diy_date_min, "min", False)
        that_week_max = to_diy_date_datetime_max_min_time(diy_date_max, "max", False)
    else:
        # 类DayOfWeek的实例化
        dow = DayOfWeek(-1)
        # 周二-那个周二日期的最小时间 - 上周二
        that_Tuesday = dow.that_Tuesday
        # 周一-那个周二日期7天之后的最大时间 也就是周一 上周二日期时间的七天后
        that_Tuesday_after_seven_day = dow.that_Tuesday_after_seven_day
        that_week_min = to_diy_date_datetime_max_min_time(that_Tuesday, "min", False)
        that_week_max = to_diy_date_datetime_max_min_time(that_Tuesday_after_seven_day, "max", False)
        print('...get_run_which_datetime_max_min_time...run_type 为', run_type, '不存在', 'that_day_min，that_day_max 取上周', that_week_min, that_week_max)
    return that_week_min, that_week_max


# grade3_price_volume
# 当阶梯价格处理 函数处理，
# 把END_THIS_CYCLE_SUM当成使用量参数USE_VOLUME_STD调用GRADE3_PRICE_VOLUME（）函数算出结果集END（）。
# 把BEGIN_THIS_CYCLE_SUM当成使用量参数USE_VOLUME_STD调用GRADE3_PRICE_VOLUME（）函数算出结果集BEGIN（）。
# price1_volume, price1_money, price2_volume, price2_money,price3_volume,price3_money,use_money
# =
# grade3_price_volume(use_volume_std,gp1,gv1,gp2,gv2,gp3)
def grade3_price_volume(use_volume_std, gp1, gv1, gp2, gv2, gp3):
    if decimal.Decimal(use_volume_std) <= decimal.Decimal(gv1):
        price1_volume = decimal.Decimal(use_volume_std)
        price1_money = decimal.Decimal(gp1) * decimal.Decimal(use_volume_std)
        # 其他均为0
        price2_volume, price2_money, price3_volume, price3_money = 0, 0, 0, 0
        # 三阶梯 金额 加一起 就是 use_money
        use_money = decimal.Decimal(price1_money) + decimal.Decimal(price2_money) + decimal.Decimal(price3_money)
        return price1_volume, price1_money, price2_volume, price2_money, price3_volume, price3_money, use_money
    elif decimal.Decimal(gv1) < decimal.Decimal(use_volume_std) <= decimal.Decimal(gv2):
        price1_volume = gv1
        price1_money = decimal.Decimal(gp1) * decimal.Decimal(gv1)
        price2_volume = decimal.Decimal(use_volume_std) - decimal.Decimal(price1_volume)
        price2_money = decimal.Decimal(gp2) * price2_volume
        # 其他均为0
        price3_volume, price3_money = 0, 0
        # 三阶梯 金额 加一起 就是 use_money
        use_money = decimal.Decimal(price1_money) + decimal.Decimal(price2_money) + decimal.Decimal(price3_money)
        return price1_volume, price1_money, price2_volume, price2_money, price3_volume, price3_money, use_money
    elif decimal.Decimal(use_volume_std) > decimal.Decimal(gv2):
        price1_volume = gv1
        price1_money = decimal.Decimal(gp1) * decimal.Decimal(gv1)
        price2_volume = gv2
        price2_money = decimal.Decimal(gp2) * decimal.Decimal(gv2)
        price3_volume = decimal.Decimal(use_volume_std) - decimal.Decimal(price2_volume)
        price3_money = decimal.Decimal(gp3) * price3_volume
        # 三阶梯 金额 加一起 就是 use_money
        use_money = decimal.Decimal(price1_money) + decimal.Decimal(price2_money) + decimal.Decimal(price3_money)
        return price1_volume, price1_money, price2_volume, price2_money, price3_volume, price3_money, use_money
    else:
        print("...grade3_price_volume... if均没有命中")
    pass


# 获取当前脚本执行 要处理对应数据某月1号 日期时间最小值 和 某月最后一天 日期时间最大值
# 从config里 通用配置 可算出 拿到
# @return 通过run_type判断 得出不同的that_month_min, that_month_max
def get_run_which_datetime_max_min_month():
    # 导入执行公共配置
    from config.config import common_config_for_app3 as ccfa
    from utils.day_of_week_model import DayOfWeek
    that_month_min = None
    that_month_max = None
    run_type = ccfa['run_type']
    if run_type == 0:
        month_num = ccfa['month_num']
        that_month_min = to_get_month_first_last_day_datetime_max_min_time(month_num, "first", "min", False)  # 方法:获取间隔n月的第一天的最小时间和最后一天的最大时间
        that_month_max = to_get_month_first_last_day_datetime_max_min_time(month_num, "last", "max", False)
    elif run_type == 1:
        diy_range_date = ccfa['diy_range_date']
        diy_range_date_list = diy_range_date.split('#')
        diy_date_min = diy_range_date_list[0]
        diy_date_max = diy_range_date_list[1]
        that_month_min = to_diy_date_datetime_max_min_time(diy_date_min, "min", False)
        that_month_max = to_diy_date_datetime_max_min_time(diy_date_max, "max", False)
    else:
        that_month_min = to_get_month_first_last_day_datetime_max_min_time(-1, "first", "min", False)  # 方法:获取间隔n月的第一天的最小时间和最后一天的最大时间
        that_month_max = to_get_month_first_last_day_datetime_max_min_time(-1, "last", "max", False)
        print('...get_run_which_datetime_max_min_month...run_type 为', run_type, '不存在', 'that_day_min，that_day_max 取上月', that_month_min, that_month_max)
    return that_month_min, that_month_max


# 获取间隔n月的第一天的最小时间和最后一天的最大时间
# @param  n,first_or_last_type,types,isFormat; n代表几月，可以正值(n月后)，可以负值(n月前),0代表当前月 ;
#                          first_or_last_type取值有first和last,first代表月的第一天,last代表月的最后一天
#                          types取值有max和min,max代表输出当前时间最大时间，min代表输出当前时间最小时间;
#                          isFormat是否格式化输出，布尔值为True,格式化输出str类型时间,为False,不格式化输出，直接返回datetime类型时间。
# @return 符合要求的datetime格式日期
def to_get_month_first_last_day_datetime_max_min_time(n, first_or_last_type, types, is_format):
    if first_or_last_type == "first":
        return_time_day = datetime.datetime(datetime.date.today().year, datetime.date.today().month + n, 1)
    elif first_or_last_type == "last":
        if datetime.date.today().month + 1 + n == 13:  # 如果这个if满足，代表当前月是12月份，取last直接下面操作即可,得到2019-12-31 00:00:00 (备注:12月不可以加1月那样操作了,因为没有月份中没有13月)
            return_time_day = datetime.datetime(datetime.date.today().year, datetime.date.today().month, 31)
        else:  # 其他情况 都是 先获得当前月份加上1月的第一天再减去1天 来得到当前月份的最后一天
            return_time_day = datetime.datetime(datetime.date.today().year, datetime.date.today().month + 1 + n, 1) - datetime.timedelta(1)

    if types == "max":
        return_time = datetime.datetime.combine(return_time_day + datetime.timedelta(days=0), datetime.time.max)
    elif types == "min":
        return_time = datetime.datetime.combine(return_time_day + datetime.timedelta(days=0), datetime.time.min)

    if (is_format):
        return_time = return_time.strftime('%Y-%m-%d %H:%M:%S')
    return return_time


# 获取间隔n月的第一天的最小时间和最后一天的最大时间
# @param  n,first_or_last_type,types,isFormat; n代表几月，可以正值(n月后)，可以负值(n月前),0代表当前月 ;
#                          first_or_last_type取值有first和last,first代表月的第一天,last代表月的最后一天
#                          types取值有max和min,max代表输出当前时间最大时间，min代表输出当前时间最小时间;
#                          isFormat是否格式化输出，布尔值为True,格式化输出str类型时间,为False,不格式化输出，直接返回datetime类型时间。
# @return 符合要求的datetime格式日期
def to_get_month_first_last_day_datetime_max_min_time(n, first_or_last_type, types, is_format):
    if first_or_last_type == "first":
        return_time_day = datetime.datetime(datetime.date.today().year, datetime.date.today().month + n, 1)
    elif first_or_last_type == "last":
        if datetime.date.today().month + 1 + n == 13:  # 如果这个if满足，代表当前月是12月份，取last直接下面操作即可,得到2019-12-31 00:00:00 (备注:12月不可以加1月那样操作了,因为没有月份中没有13月)
            return_time_day = datetime.datetime(datetime.date.today().year, datetime.date.today().month, 31)
        else:  # 其他情况 都是 先获得当前月份加上1月的第一天再减去1天 来得到当前月份的最后一天
            return_time_day = datetime.datetime(datetime.date.today().year, datetime.date.today().month + 1 + n, 1) - datetime.timedelta(1)

    if types == "max":
        return_time = datetime.datetime.combine(return_time_day + datetime.timedelta(days=0), datetime.time.max)
    elif types == "min":
        return_time = datetime.datetime.combine(return_time_day + datetime.timedelta(days=0), datetime.time.min)

    if (is_format):
        return_time = return_time.strftime('%Y-%m-%d %H:%M:%S')
    return return_time
