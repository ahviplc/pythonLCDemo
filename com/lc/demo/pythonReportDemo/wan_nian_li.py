#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
wannianli.py
万年历
Version: 1.0
Author: LC
DateTime: 2019年3月7日14:33:01
UpdateTime: None
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

import os, io, sys, re, time, datetime, base64

__version__ = "1.0 "
__all__ = ['LunarDate']

solar_year = 1900
solar_month = 1
solar_day = 31
solar_weekday = 0

lunar_year = 0
lunar_month = 0
lunar_day = 0
lunar_isLeapMonth = False


class LunarDate(object):
    _startDate = datetime.date(1900, 1, 31)

    def __init__(self, year, month, day, isLeapMonth=False):
        global lunar_year
        global lunar_month
        global lunar_day
        global lunar_isLeapMonth

        lunar_year = int(year)
        lunar_month = int(month)
        lunar_day = int(day)
        lunar_isLeapMonth = bool(isLeapMonth)

        self.year = year
        self.month = month
        self.day = day
        self.isLeapMonth = bool(isLeapMonth)

    def __str__(self):
        return 'LunarDate(%d, %d, %d, %d)' % (self.year, self.month, self.day, self.isLeapMonth)

    __repr__ = __str__

    @staticmethod
    def fromSolarDate(year, month, day):
        solarDate = datetime.date(year, month, day)
        offset = (solarDate - LunarDate._startDate).days
        return LunarDate._fromOffset(offset)

    def toSolarDate(self):
        def _calcDays(yearInfo, month, day, isLeapMonth):
            isLeapMonth = int(isLeapMonth)
            res = 0
            ok = False
            for _month, _days, _isLeapMonth in self._enumMonth(yearInfo):
                if (_month, _isLeapMonth) == (month, isLeapMonth):
                    if 1 <= day <= _days:
                        res += day - 1
                        return res
                    else:
                        raise ValueError("day out of range")
                res += _days

            raise ValueError("month out of range")

        offset = 0
        if self.year < 1900 or self.year >= 2050:
            raise ValueError('year out of range [1900, 2050)')
        yearIdx = self.year - 1900
        for i in range(yearIdx):
            offset += yearDays[i]

        offset += _calcDays(yearInfos[yearIdx], self.month, self.day, self.isLeapMonth)
        return self._startDate + datetime.timedelta(days=offset)

    def __sub__(self, other):
        if isinstance(other, LunarDate):
            return self.toSolarDate() - other.toSolarDate()
        elif isinstance(other, datetime.date):
            return self.toSolarDate() - other
        elif isinstance(other, datetime.timedelta):
            res = self.toSolarDate() - other
            return LunarDate.fromSolarDate(res.year, res.month, res.day)
        raise TypeError

    def __rsub__(self, other):
        if isinstance(other, datetime.date):
            return other - self.toSolarDate()

    def __add__(self, other):
        if isinstance(other, datetime.timedelta):
            res = self.toSolarDate() + other
            return LunarDate.fromSolarDate(res.year, res.month, res.day)
        raise TypeError

    def __radd__(self, other):
        return self + other

    def __lt__(self, other):
        return self - other < datetime.timedelta(0)

    def __le__(self, other):
        return self - other <= datetime.timedelta(0)

    @classmethod
    def today(cls):
        res = datetime.date.today()
        return cls.fromSolarDate(res.year, res.month, res.day)

    @staticmethod
    def _enumMonth(yearInfo):
        months = [(i, 0) for i in range(1, 13)]
        leapMonth = yearInfo % 16
        if leapMonth == 0:
            pass
        elif leapMonth <= 12:
            months.insert(leapMonth, (leapMonth, 1))
        else:
            raise ValueError("yearInfo %r mod 16 should in [0, 12]" % yearInfo)

        for month, isLeapMonth in months:
            if isLeapMonth:
                days = (yearInfo >> 16) % 2 + 29
            else:
                days = (yearInfo >> (16 - month)) % 2 + 29
            yield month, days, isLeapMonth

    @classmethod
    def _fromOffset(cls, offset):
        def _calcMonthDay(yearInfo, offset):
            for month, days, isLeapMonth in cls._enumMonth(yearInfo):
                if offset < days:
                    break
                offset -= days
            return (month, offset + 1, isLeapMonth)

        offset = int(offset)

        for idx, yearDay in enumerate(Info.yearDays()):
            if offset < yearDay:
                break
            offset -= yearDay
        year = 1900 + idx

        yearInfo = Info.yearInfos[idx]
        month, day, isLeapMonth = _calcMonthDay(yearInfo, offset)
        return LunarDate(year, month, day, isLeapMonth)


class ChineseWord():
    def weekday_str(tm):
        a = '星期日 星期一 星期二 星期三 星期四 星期五 星期六'.split()
        return a[tm]

    def solarTerm(year, month, day):
        a = '小寒 大寒 立春 雨水 惊蛰 春分\
             清明 谷雨 立夏 小满 芒种 夏至\
             小暑 大暑 立秋 处暑 白露 秋分\
             寒露 霜降 立冬 小雪 大雪 冬至'.split()
        return

    def day_lunar(ld):
        a = '初一 初二 初三 初四 初五 初六 初七 初八 初九 初十\
             十一 十二 十三 十四 十五 十六 十七 十八 十九 廿十\
             廿一 廿二 廿三 廿四 廿五 廿六 廿七 廿八 廿九 三十'.split()
        return a[ld - 1]

    def month_lunar(le, lm):
        a = '正月 二月 三月 四月 五月 六月 七月 八月 九月 十月 十一月 十二月'.split()
        if le:
            return "闰" + a[lm - 1]
        else:
            return a[lm - 1]

    def year_lunar(ly):
        y = ly
        tg = '甲 乙 丙 丁 戊 己 庚 辛 壬 癸'.split()
        dz = '子 丑 寅 卯 辰 巳 午 未 申 酉 戌 亥'.split()
        sx = '鼠 牛 虎 兔 龙 蛇 马 羊 猴 鸡 狗 猪'.split()
        return tg[(y - 4) % 10] + dz[(y - 4) % 12] + '[' + sx[(y - 4) % 12] + ']' + '年'


class Festival():
    # 国历节日 *表示放假日
    def solar_Fstv(solar_month, solar_day):
        sFtv = [
            "0101#元旦节#",
            "0202#世界湿地日#",
            "0210#国际气象节#",
            "0214#情人节#",
            "0301#国际海豹日#",
            "0303#全国爱耳日#",
            "0305#学雷锋纪念日#",
            "0308#妇女节#",
            "0312#植树节# #孙中山逝世纪念日#",
            "0314#国际警察日#",
            "0315#消费者权益日#",
            "0317#中国国医节# #国际航海日#",
            "0321#世界森林日# #消除种族歧视国际日# #世界儿歌日#",
            "0322#世界水日#",
            "0323#世界气象日#",
            "0324#世界防治结核病日#",
            "0325#全国中小学生安全教育日#",
            "0330#巴勒斯坦国土日#",
            "0401#愚人节# #全国爱国卫生运动月(四月)# #税收宣传月(四月)#",
            "0407#世界卫生日#",
            "0422#世界地球日#",
            "0423#世界图书和版权日#",
            "0424#亚非新闻工作者日#",
            "0501#劳动节#",
            "0504#青年节#",
            "0505#碘缺乏病防治日#",
            "0508#世界红十字日#",
            "0512#国际护士节#",
            "0515#国际家庭日#",
            "0517#国际电信日#",
            "0518#国际博物馆日#",
            "0520#全国学生营养日#",
            "0523#国际牛奶日#",
            "0531#世界无烟日#",
            "0601#国际儿童节#",
            "0605#世界环境保护日#",
            "0606#全国爱眼日#",
            "0617#防治荒漠化和干旱日#",
            "0623#国际奥林匹克日#",
            "0625#全国土地日#",
            "0626#国际禁毒日#",
            "0701#中国共·产党诞辰# #香港回归纪念日# #世界建筑日#",
            "0702#国际体育记者日#",
            "0707#抗日战争纪念日#",
            "0711#世界人口日#",
            "0730#非洲妇女日#",
            "0801#建军节#",
            "0808#中国男子节(爸爸节)#",
            "0815#抗日战争胜利纪念#",
            "0908#国际扫盲日# #国际新闻工作者日#",
            "0909#毛·泽东逝世纪念#",
            "0910#中国教师节#",
            "0914#世界清洁地球日#",
            "0916#国际臭氧层保护日#",
            "0918#九·一八事变纪念日#",
            "0920#国际爱牙日#",
            "0927#世界旅游日#",
            "0928#孔子诞辰#",
            "1001#国庆节# #世界音乐日# #国际老人节#",
            "1002#国庆节假日# #国际和平与民主自由斗争日#",
            "1003#国庆节假日#",
            "1004#世界动物日#",
            "1006#老人节#",
            "1008#全国高血压日# #世界视觉日#",
            "1009#世界邮政日# #万国邮联日#",
            "1010#辛亥革命纪念日# #世界精神卫生日#",
            "1013#世界保健日# #国际教师节#",
            "1014#世界标准日#",
            "1015#国际盲人节(白手杖节)#",
            "1016#世界粮食日#",
            "1017#世界消除贫困日#",
            "1022#世界传统医药日#",
            "1024#联合国日#",
            "1031#世界勤俭日#",
            "1107#十月社会主义革命纪念日#",
            "1108#中国记者日#",
            "1109#全国消防安全宣传教育日#",
            "1110#世界青年节#",
            "1111#国际科学与和平周(本日所属的一周)#",
            "1112#孙中山诞辰纪念日#",
            "1114#世界糖尿病日#",
            "1116#国际宽容日#",
            "1117#国际大学生节# #世界学生节#",
            "1120#彝族年#",
            "1121#彝族年# #世界问候日# #世界电视日#",
            "1122#彝族年#",
            "1129#国际声援巴勒斯坦人民国际日#",
            "1201#世界艾滋病日#",
            "1203#世界残疾人日#",
            "1205#国际经济和社会发展志愿人员日#",
            "1208#国际儿童电视日#",
            "1209#世界足球日#",
            "1210#世界人权日#",
            "1212#西安事变纪念日#",
            "1213#南京大屠杀(1937年)纪念日#",
            "1220#澳门回归纪念#",
            "1221#国际篮球日#",
            "1224#平安夜#",
            "1225#圣诞节#",
            "1226#毛·泽东诞辰纪念日#"
        ]
        solar_month_str = str(solar_month) if solar_month > 9 else "0" + str(solar_month)
        solar_day_str = str(solar_day) if solar_day > 9 else "0" + str(solar_day)
        pattern = "(" + solar_month_str + solar_day_str + ")([\w+?\#???\d+\s?·?]*)"
        for solar_fstv_item in sFtv:
            result = re.search(pattern, solar_fstv_item)
            if result is not None:
                return result.group(2)

    def lunar_Fstv(lunar_month, lunar_day):
        # 农历节日 *表示放假日
        # 每年单独来算
        lFtv = [
            "0101#春节#",
            "0115#元宵节#",
            "0202#春龙节",
            # "0314#清明节#", #每年不一样，此为2012年，事实上为公历节日
            "0505#端午节#",
            "0707#七夕情人节#",
            "0715#中元节#",
            "0815#中秋节#",
            "0909#重阳节#",
            "1208#腊八节#",
            "1223#小年#",
            "1229#除夕#"  # 每年不一样，此为2011年
        ]
        lunar_month_str = str(lunar_month) if lunar_month > 9 else "0" + str(lunar_month)
        lunar_day_str = str(lunar_day) if lunar_day > 9 else "0" + str(lunar_day)
        pattern = "(" + lunar_month_str + lunar_day_str + ")([\w+?\#?\s?]*)"
        for lunar_fstv_item in lFtv:
            result = re.search(pattern, lunar_fstv_item)
            if result is not None:
                return result.group(2)

    # 国历节日 *表示放假日
    def weekday_Fstv(solar_month, solar_day, solar_weekday):
        # 某月的第几个星期几
        wFtv = [
            "0150#世界防治麻风病日#",  # 一月的最后一个星期日（月倒数第一个星期日）
            "0520#国际母亲节#",
            "0530#全国助残日#",
            "0630#父亲节#",
            "0730#被奴役国家周#",
            "0932#国际和平日#",
            "0940#国际聋人节# #世界儿童日#",
            "0950#世界海事日#",
            "1011#国际住房日#",
            "1013#国际减轻自然灾害日(减灾日)#",
            "1144#感恩节#"]

        # 7，14等应该属于1, 2周，能整除的那天实际属于上一周，做个偏移
        offset = -1 if solar_day % 7 == 0 else 0
        # 计算当前日属于第几周，得出来从0开始计周，再向后偏移1
        weekday_ordinal = solar_day // 7 + offset + 1

        solar_month_str = str(solar_month) if solar_month > 9 else "0" + str(solar_month)
        solar_weekday_str = str(weekday_ordinal) + str(solar_weekday)

        pattern = "(" + solar_month_str + solar_weekday_str + ")([\w+?\#?\s?]*)"
        for weekday_fstv_item in wFtv:
            result = re.search(pattern, weekday_fstv_item)
            if result is not None:
                return result.group(2)

        # 如何计算某些最后一个星期几的情况，..........

    # 24节气
    def solar_Term(solar_month, solar_day):
        # 每年数据不一样，此为2012年内的数据
        stFtv = [
            "0106#小寒#",
            "0120#大寒#",
            "0204#立春#",
            "0219#雨水#",
            "0305#惊蛰#",
            "0320#春分#",
            "0404#清明#",
            "0420#谷雨#",
            "0505#立夏#",
            "0521#小满#",
            "0605#芒种#",
            "0621#夏至#",
            "0707#小暑#",
            "0722#大暑#",
            "0807#立秋#",
            "0823#处暑#",
            "0907#白露#",
            "0922#秋分#",
            "1008#寒露#",
            "1023#霜降#",
            "1107#立冬#",
            "1122#小雪#",
            "1206#大雪#",
            "1221#冬至#",
        ]
        solar_month_str = str(solar_month) if solar_month > 9 else "0" + str(solar_month)
        solar_day_str = str(solar_day) if solar_day > 9 else "0" + str(solar_day)
        pattern = "(" + solar_month_str + solar_day_str + ")([\w+?\#?]*)"
        for solarTerm_fstv_item in stFtv:
            result = re.search(pattern, solarTerm_fstv_item)
            if result is not None:
                return result.group(2)


class Info():
    yearInfos = [
        #    /* encoding:
        #               b bbbbbbbbbbbb bbbb
        #       bit#    1 111111000000 0000
        #               6 543210987654 3210
        #               . ............ ....
        #       month#    000000000111
        #               M 123456789012   L
        #
        #    b_j = 1 for long month, b_j = 0 for short month
        #    L is the leap month of the year if 1<=L<=12; NO leap month if L = 0.
        #    The leap month (if exists) is long one iff M = 1.
        #    */
        0x04bd8,  # /* 1900 */
        0x04ae0, 0x0a570, 0x054d5, 0x0d260, 0x0d950,  # /* 1905 */
        0x16554, 0x056a0, 0x09ad0, 0x055d2, 0x04ae0,  # /* 1910 */
        0x0a5b6, 0x0a4d0, 0x0d250, 0x1d255, 0x0b540,  # /* 1915 */
        0x0d6a0, 0x0ada2, 0x095b0, 0x14977, 0x04970,  # /* 1920 */
        0x0a4b0, 0x0b4b5, 0x06a50, 0x06d40, 0x1ab54,  # /* 1925 */
        0x02b60, 0x09570, 0x052f2, 0x04970, 0x06566,  # /* 1930 */
        0x0d4a0, 0x0ea50, 0x06e95, 0x05ad0, 0x02b60,  # /* 1935 */
        0x186e3, 0x092e0, 0x1c8d7, 0x0c950, 0x0d4a0,  # /* 1940 */
        0x1d8a6, 0x0b550, 0x056a0, 0x1a5b4, 0x025d0,  # /* 1945 */
        0x092d0, 0x0d2b2, 0x0a950, 0x0b557, 0x06ca0,  # /* 1950 */
        0x0b550, 0x15355, 0x04da0, 0x0a5d0, 0x14573,  # /* 1955 */
        0x052d0, 0x0a9a8, 0x0e950, 0x06aa0, 0x0aea6,  # /* 1960 */
        0x0ab50, 0x04b60, 0x0aae4, 0x0a570, 0x05260,  # /* 1965 */
        0x0f263, 0x0d950, 0x05b57, 0x056a0, 0x096d0,  # /* 1970 */
        0x04dd5, 0x04ad0, 0x0a4d0, 0x0d4d4, 0x0d250,  # /* 1975 */
        0x0d558, 0x0b540, 0x0b5a0, 0x195a6, 0x095b0,  # /* 1980 */
        0x049b0, 0x0a974, 0x0a4b0, 0x0b27a, 0x06a50,  # /* 1985 */
        0x06d40, 0x0af46, 0x0ab60, 0x09570, 0x04af5,  # /* 1990 */
        0x04970, 0x064b0, 0x074a3, 0x0ea50, 0x06b58,  # /* 1995 */
        0x05ac0, 0x0ab60, 0x096d5, 0x092e0, 0x0c960,  # /* 2000 */
        0x0d954, 0x0d4a0, 0x0da50, 0x07552, 0x056a0,  # /* 2005 */
        0x0abb7, 0x025d0, 0x092d0, 0x0cab5, 0x0a950,  # /* 2010 */
        0x0b4a0, 0x0baa4, 0x0ad50, 0x055d9, 0x04ba0,  # /* 2015 */
        0x0a5b0, 0x15176, 0x052b0, 0x0a930, 0x07954,  # /* 2020 */
        0x06aa0, 0x0ad50, 0x05b52, 0x04b60, 0x0a6e6,  # /* 2025 */
        0x0a4e0, 0x0d260, 0x0ea65, 0x0d530, 0x05aa0,  # /* 2030 */
        0x076a3, 0x096d0, 0x04afb, 0x04ad0, 0x0a4d0,  # /* 2035 */
        0x1d0b6, 0x0d250, 0x0d520, 0x0dd45, 0x0b5a0,  # /* 2040 */
        0x056d0, 0x055b2, 0x049b0, 0x0a577, 0x0a4b0,  # /* 2045 */
        0x0aa50, 0x1b255, 0x06d20, 0x0ada0  # /* 2049 */
    ]

    def yearInfo2yearDay(yearInfo):
        yearInfo = int(yearInfo)

        res = 29 * 12

        leap = False
        if yearInfo % 16 != 0:
            leap = True
            res += 29

        yearInfo //= 16

        for i in range(12 + leap):
            if yearInfo % 2 == 1:
                res += 1
            yearInfo //= 2
        return res

    def yearDays():
        yearDays = [Info.yearInfo2yearDay(x) for x in Info.yearInfos]
        return yearDays

    def day2LunarDate(offset):
        offset = int(offset)
        res = LunarDate()

        for idx, yearDay in enumerate(yearDays()):
            if offset < yearDay:
                break
            offset -= yearDay
        res.year = 1900 + idx


class SolarDate():

    def __init__(self):
        global solar_year
        global solar_month
        global solar_day
        global solar_weekday

        solar_year = int(time.strftime("%Y", time.localtime()))
        solar_month = int(time.strftime("%m", time.localtime()))
        solar_day = int(time.strftime("%d", time.localtime()))
        solar_weekday = int(time.strftime("%w", time.localtime()))

        self.year = solar_year
        self.month = solar_month
        self.day = solar_day
        self.weekday = solar_weekday

    def __str__(self):
        return 'LunarDate(%d, %d, %d, %d)' % (self.year, self.month, self.day, self.isLeapMonth)


def getCalendar_today():
    solar = SolarDate()
    LunarDate.fromSolarDate(solar_year, solar_month, solar_day)

    festival = ""

    if Festival.solar_Term(solar_month, solar_day):
        festival = festival + " 今日节气：" + Festival.solar_Term(solar_month, solar_day)
    if Festival.solar_Fstv(solar_month, solar_day):
        festival = festival + " 公历节日：" + Festival.solar_Fstv(solar_month, solar_day)
    if Festival.weekday_Fstv(solar_month, solar_day, solar_weekday):
        if festival.find("公历节日") == -1:
            festival = festival + " 公历节日：" + Festival.weekday_Fstv(solar_month, solar_day, solar_weekday)
        else:
            festival = festival + " " + Festival.weekday_Fstv(solar_month, solar_day, solar_weekday)
    if Festival.lunar_Fstv(lunar_month, lunar_day):
        festival = festival + " 农历节日：" + Festival.lunar_Fstv(lunar_month, lunar_day)

    twitter = \
        "今天是" + str(solar_year) + "年" + str(solar_month) + "月" + str(solar_day) + "日" + " " \
        + ChineseWord.weekday_str(solar_weekday) + " 农历" + ChineseWord.year_lunar(lunar_year) \
        + ChineseWord.month_lunar(lunar_isLeapMonth, lunar_month) \
        + ChineseWord.day_lunar(lunar_day) + festival
    print(twitter)
    return twitter


def getCalendar_all_day():
    # solar = SolarDate()
    global solar_year
    global solar_month
    global solar_day
    global solar_weekday

    #    solar_year = 2012

    solar_year = 2012

    solar_month = 1
    weekday_offset = 0  # 1月1号星期几?
    index_day = 0
    for solar_month in range(1, 13):
        if solar_month in [1, 3, 5, 7, 8, 10, 12]:
            solar_day_max = 31
        elif solar_month in [4, 6, 9, 11]:
            solar_day_max = 30
        elif solar_month == 2:
            if ((solar_year % 4 == 0) and (solar_year % 100 != 0)) or (solar_year % 400 == 0):
                solar_day_max = 29
            else:
                solar_day_max = 28
        else:
            None

        for solar_day in range(1, solar_day_max + 1):
            index_day += 1
            solar_weekday = (index_day) % 7 + - 1
            solar_weekday = 0 if solar_weekday == 7 else solar_weekday
            solar_weekday = 6 if solar_weekday == -1 else solar_weekday

            LunarDate.fromSolarDate(solar_year, solar_month, solar_day)
            festival = ""

            if Festival.solar_Term(solar_month, solar_day):
                festival = festival + " 节气：" + Festival.solar_Term(solar_month, solar_day)
            if Festival.solar_Fstv(solar_month, solar_day):
                festival = festival + " 节日：" + Festival.solar_Fstv(solar_month, solar_day)
            if Festival.weekday_Fstv(solar_month, solar_day, solar_weekday):
                if festival.find("节日") == -1:
                    festival = festival + " 节日：" + Festival.weekday_Fstv(solar_month, solar_day, solar_weekday)
                else:
                    festival = festival + " " + Festival.weekday_Fstv(solar_month, solar_day, solar_weekday)
            if Festival.lunar_Fstv(lunar_month, lunar_day):
                if festival.find("节日") == -1:
                    festival = festival + " 节日：" + Festival.lunar_Fstv(lunar_month, lunar_day)
                else:
                    festival = festival + " " + Festival.lunar_Fstv(lunar_month, lunar_day)

            index_yy = str(solar_year)
            if int(solar_month) < 10:
                index_mm = "0" + str(solar_month)
            else:
                index_mm = str(solar_month)
            if int(solar_day) < 10:
                index_dd = "0" + str(solar_day)
            else:
                index_dd = str(solar_day)

            index_yyddmm = index_yy + index_mm + index_dd

            twitter = ("message(" + str(index_yyddmm) + ') = "') + \
                      str(solar_year) + "年" + str(solar_month) + "月" + str(solar_day) + "日" + " " \
                      + ChineseWord.weekday_str(solar_weekday) + " 农历" + ChineseWord.year_lunar(lunar_year) \
                      + ChineseWord.month_lunar(lunar_isLeapMonth, lunar_month) \
                      + ChineseWord.day_lunar(lunar_day) + festival + '"'
            print(twitter)

    return twitter


def main():
    "main function"
    print(base64.b64decode(b'Q29weXJpZ2h0IChjKSAyMDEyIERvdWN1YmUgSW5jLiBBbGwgcmlnaHRzIHJlc2VydmVkLg==').decode())
    getCalendar_all_day()
    getCalendar_today()


if __name__ == '__main__':
    main()

# Copyright (c) 2012 Doucube Inc. All rights reserved.
# message(20120101) = "2012年1月1日 星期日 农历辛卯[兔]年十二月初八 节日：#元旦节# #腊八节#"
# message(20120102) = "2012年1月2日 星期一 农历辛卯[兔]年十二月初九"
# message(20120103) = "2012年1月3日 星期二 农历辛卯[兔]年十二月初十"
# message(20120104) = "2012年1月4日 星期三 农历辛卯[兔]年十二月十一"
# message(20120105) = "2012年1月5日 星期四 农历辛卯[兔]年十二月十二"
# message(20120106) = "2012年1月6日 星期五 农历辛卯[兔]年十二月十三 节气：#小寒#"
# message(20120107) = "2012年1月7日 星期六 农历辛卯[兔]年十二月十四"
# message(20120108) = "2012年1月8日 星期日 农历辛卯[兔]年十二月十五"
# message(20120109) = "2012年1月9日 星期一 农历辛卯[兔]年十二月十六"
# message(20120110) = "2012年1月10日 星期二 农历辛卯[兔]年十二月十七"
# message(20120111) = "2012年1月11日 星期三 农历辛卯[兔]年十二月十八"
# message(20120112) = "2012年1月12日 星期四 农历辛卯[兔]年十二月十九"
# message(20120113) = "2012年1月13日 星期五 农历辛卯[兔]年十二月廿十"
# message(20120114) = "2012年1月14日 星期六 农历辛卯[兔]年十二月廿一"
# message(20120115) = "2012年1月15日 星期日 农历辛卯[兔]年十二月廿二"
# message(20120116) = "2012年1月16日 星期一 农历辛卯[兔]年十二月廿三 节日：#小年#"
# message(20120117) = "2012年1月17日 星期二 农历辛卯[兔]年十二月廿四"
# message(20120118) = "2012年1月18日 星期三 农历辛卯[兔]年十二月廿五"
# message(20120119) = "2012年1月19日 星期四 农历辛卯[兔]年十二月廿六"
# message(20120120) = "2012年1月20日 星期五 农历辛卯[兔]年十二月廿七 节气：#大寒#"
# message(20120121) = "2012年1月21日 星期六 农历辛卯[兔]年十二月廿八"
# message(20120122) = "2012年1月22日 星期日 农历辛卯[兔]年十二月廿九 节日：#除夕#"
# message(20120123) = "2012年1月23日 星期一 农历壬辰[龙]年正月初一 节日：#春节#"
# message(20120124) = "2012年1月24日 星期二 农历壬辰[龙]年正月初二"
# message(20120125) = "2012年1月25日 星期三 农历壬辰[龙]年正月初三"
# message(20120126) = "2012年1月26日 星期四 农历壬辰[龙]年正月初四"
# message(20120127) = "2012年1月27日 星期五 农历壬辰[龙]年正月初五"
# message(20120128) = "2012年1月28日 星期六 农历壬辰[龙]年正月初六"
# message(20120129) = "2012年1月29日 星期日 农历壬辰[龙]年正月初七 节日：#世界防治麻风病日#"
# message(20120130) = "2012年1月30日 星期一 农历壬辰[龙]年正月初八"
# message(20120131) = "2012年1月31日 星期二 农历壬辰[龙]年正月初九"
# message(20120201) = "2012年2月1日 星期三 农历壬辰[龙]年正月初十"
# message(20120202) = "2012年2月2日 星期四 农历壬辰[龙]年正月十一 节日：#世界湿地日#"
# message(20120203) = "2012年2月3日 星期五 农历壬辰[龙]年正月十二"
# message(20120204) = "2012年2月4日 星期六 农历壬辰[龙]年正月十三 节气：#立春#"
# message(20120205) = "2012年2月5日 星期日 农历壬辰[龙]年正月十四"
# message(20120206) = "2012年2月6日 星期一 农历壬辰[龙]年正月十五 节日：#元宵节#"
# message(20120207) = "2012年2月7日 星期二 农历壬辰[龙]年正月十六"
# message(20120208) = "2012年2月8日 星期三 农历壬辰[龙]年正月十七"
# message(20120209) = "2012年2月9日 星期四 农历壬辰[龙]年正月十八"
# message(20120210) = "2012年2月10日 星期五 农历壬辰[龙]年正月十九 节日：#国际气象节#"
# message(20120211) = "2012年2月11日 星期六 农历壬辰[龙]年正月廿十"
# message(20120212) = "2012年2月12日 星期日 农历壬辰[龙]年正月廿一"
# message(20120213) = "2012年2月13日 星期一 农历壬辰[龙]年正月廿二"
# message(20120214) = "2012年2月14日 星期二 农历壬辰[龙]年正月廿三 节日：#情人节#"
# message(20120215) = "2012年2月15日 星期三 农历壬辰[龙]年正月廿四"
# message(20120216) = "2012年2月16日 星期四 农历壬辰[龙]年正月廿五"
# message(20120217) = "2012年2月17日 星期五 农历壬辰[龙]年正月廿六"
# message(20120218) = "2012年2月18日 星期六 农历壬辰[龙]年正月廿七"
# message(20120219) = "2012年2月19日 星期日 农历壬辰[龙]年正月廿八 节气：#雨水#"
# message(20120220) = "2012年2月20日 星期一 农历壬辰[龙]年正月廿九"
# message(20120221) = "2012年2月21日 星期二 农历壬辰[龙]年正月三十"
# message(20120222) = "2012年2月22日 星期三 农历壬辰[龙]年二月初一"
# message(20120223) = "2012年2月23日 星期四 农历壬辰[龙]年二月初二 节日：#春龙节"
# message(20120224) = "2012年2月24日 星期五 农历壬辰[龙]年二月初三"
# message(20120225) = "2012年2月25日 星期六 农历壬辰[龙]年二月初四"
# message(20120226) = "2012年2月26日 星期日 农历壬辰[龙]年二月初五"
# message(20120227) = "2012年2月27日 星期一 农历壬辰[龙]年二月初六"
# message(20120228) = "2012年2月28日 星期二 农历壬辰[龙]年二月初七"
# message(20120229) = "2012年2月29日 星期三 农历壬辰[龙]年二月初八"
# message(20120301) = "2012年3月1日 星期四 农历壬辰[龙]年二月初九 节日：#国际海豹日#"
# message(20120302) = "2012年3月2日 星期五 农历壬辰[龙]年二月初十"
# message(20120303) = "2012年3月3日 星期六 农历壬辰[龙]年二月十一 节日：#全国爱耳日#"
# message(20120304) = "2012年3月4日 星期日 农历壬辰[龙]年二月十二"
# message(20120305) = "2012年3月5日 星期一 农历壬辰[龙]年二月十三 节气：#惊蛰# 节日：#学雷锋纪念日#"
# message(20120306) = "2012年3月6日 星期二 农历壬辰[龙]年二月十四"
# message(20120307) = "2012年3月7日 星期三 农历壬辰[龙]年二月十五"
# message(20120308) = "2012年3月8日 星期四 农历壬辰[龙]年二月十六 节日：#妇女节#"
# message(20120309) = "2012年3月9日 星期五 农历壬辰[龙]年二月十七"
# message(20120310) = "2012年3月10日 星期六 农历壬辰[龙]年二月十八"
# message(20120311) = "2012年3月11日 星期日 农历壬辰[龙]年二月十九"
# message(20120312) = "2012年3月12日 星期一 农历壬辰[龙]年二月廿十 节日：#植树节# #孙中山逝世纪念日#"
# message(20120313) = "2012年3月13日 星期二 农历壬辰[龙]年二月廿一"
# message(20120314) = "2012年3月14日 星期三 农历壬辰[龙]年二月廿二 节日：#国际警察日#"
# message(20120315) = "2012年3月15日 星期四 农历壬辰[龙]年二月廿三 节日：#消费者权益日#"
# message(20120316) = "2012年3月16日 星期五 农历壬辰[龙]年二月廿四"
# message(20120317) = "2012年3月17日 星期六 农历壬辰[龙]年二月廿五 节日：#中国国医节# #国际航海日#"
# message(20120318) = "2012年3月18日 星期日 农历壬辰[龙]年二月廿六"
# message(20120319) = "2012年3月19日 星期一 农历壬辰[龙]年二月廿七"
# message(20120320) = "2012年3月20日 星期二 农历壬辰[龙]年二月廿八 节气：#春分#"
# message(20120321) = "2012年3月21日 星期三 农历壬辰[龙]年二月廿九 节日：#世界森林日# #消除种族歧视国际日# #世界儿歌日#"
# message(20120322) = "2012年3月22日 星期四 农历壬辰[龙]年三月初一 节日：#世界水日#"
# message(20120323) = "2012年3月23日 星期五 农历壬辰[龙]年三月初二 节日：#世界气象日#"
# message(20120324) = "2012年3月24日 星期六 农历壬辰[龙]年三月初三 节日：#世界防治结核病日#"
# message(20120325) = "2012年3月25日 星期日 农历壬辰[龙]年三月初四 节日：#全国中小学生安全教育日#"
# message(20120326) = "2012年3月26日 星期一 农历壬辰[龙]年三月初五"
# message(20120327) = "2012年3月27日 星期二 农历壬辰[龙]年三月初六"
# message(20120328) = "2012年3月28日 星期三 农历壬辰[龙]年三月初七"
# message(20120329) = "2012年3月29日 星期四 农历壬辰[龙]年三月初八"
# message(20120330) = "2012年3月30日 星期五 农历壬辰[龙]年三月初九 节日：#巴勒斯坦国土日#"
# message(20120331) = "2012年3月31日 星期六 农历壬辰[龙]年三月初十"
# message(20120401) = "2012年4月1日 星期日 农历壬辰[龙]年三月十一 节日：#愚人节# #全国爱国卫生运动月"
# message(20120402) = "2012年4月2日 星期一 农历壬辰[龙]年三月十二"
# message(20120403) = "2012年4月3日 星期二 农历壬辰[龙]年三月十三"
# message(20120404) = "2012年4月4日 星期三 农历壬辰[龙]年三月十四 节气：#清明#"
# message(20120405) = "2012年4月5日 星期四 农历壬辰[龙]年三月十五"
# message(20120406) = "2012年4月6日 星期五 农历壬辰[龙]年三月十六"
# message(20120407) = "2012年4月7日 星期六 农历壬辰[龙]年三月十七 节日：#世界卫生日#"
# message(20120408) = "2012年4月8日 星期日 农历壬辰[龙]年三月十八"
# message(20120409) = "2012年4月9日 星期一 农历壬辰[龙]年三月十九"
# message(20120410) = "2012年4月10日 星期二 农历壬辰[龙]年三月廿十"
# message(20120411) = "2012年4月11日 星期三 农历壬辰[龙]年三月廿一"
# message(20120412) = "2012年4月12日 星期四 农历壬辰[龙]年三月廿二"
# message(20120413) = "2012年4月13日 星期五 农历壬辰[龙]年三月廿三"
# message(20120414) = "2012年4月14日 星期六 农历壬辰[龙]年三月廿四"
# message(20120415) = "2012年4月15日 星期日 农历壬辰[龙]年三月廿五"
# message(20120416) = "2012年4月16日 星期一 农历壬辰[龙]年三月廿六"
# message(20120417) = "2012年4月17日 星期二 农历壬辰[龙]年三月廿七"
# message(20120418) = "2012年4月18日 星期三 农历壬辰[龙]年三月廿八"
# message(20120419) = "2012年4月19日 星期四 农历壬辰[龙]年三月廿九"
# message(20120420) = "2012年4月20日 星期五 农历壬辰[龙]年三月三十 节气：#谷雨#"
# message(20120421) = "2012年4月21日 星期六 农历壬辰[龙]年四月初一"
# message(20120422) = "2012年4月22日 星期日 农历壬辰[龙]年四月初二 节日：#世界地球日#"
# message(20120423) = "2012年4月23日 星期一 农历壬辰[龙]年四月初三 节日：#世界图书和版权日#"
# message(20120424) = "2012年4月24日 星期二 农历壬辰[龙]年四月初四 节日：#亚非新闻工作者日#"
# message(20120425) = "2012年4月25日 星期三 农历壬辰[龙]年四月初五"
# message(20120426) = "2012年4月26日 星期四 农历壬辰[龙]年四月初六"
# message(20120427) = "2012年4月27日 星期五 农历壬辰[龙]年四月初七"
# message(20120428) = "2012年4月28日 星期六 农历壬辰[龙]年四月初八"
# message(20120429) = "2012年4月29日 星期日 农历壬辰[龙]年四月初九"
# message(20120430) = "2012年4月30日 星期一 农历壬辰[龙]年四月初十"
# message(20120501) = "2012年5月1日 星期二 农历壬辰[龙]年四月十一 节日：#劳动节#"
# message(20120502) = "2012年5月2日 星期三 农历壬辰[龙]年四月十二"
# message(20120503) = "2012年5月3日 星期四 农历壬辰[龙]年四月十三"
# message(20120504) = "2012年5月4日 星期五 农历壬辰[龙]年四月十四 节日：#青年节#"
# message(20120505) = "2012年5月5日 星期六 农历壬辰[龙]年四月十五 节气：#立夏# 节日：#碘缺乏病防治日#"
# message(20120506) = "2012年5月6日 星期日 农历壬辰[龙]年四月十六"
# message(20120507) = "2012年5月7日 星期一 农历壬辰[龙]年四月十七"
# message(20120508) = "2012年5月8日 星期二 农历壬辰[龙]年四月十八 节日：#世界红十字日#"
# message(20120509) = "2012年5月9日 星期三 农历壬辰[龙]年四月十九"
# message(20120510) = "2012年5月10日 星期四 农历壬辰[龙]年四月廿十"
# message(20120511) = "2012年5月11日 星期五 农历壬辰[龙]年四月廿一"
# message(20120512) = "2012年5月12日 星期六 农历壬辰[龙]年四月廿二 节日：#国际护士节#"
# message(20120513) = "2012年5月13日 星期日 农历壬辰[龙]年四月廿三 节日：#国际母亲节#"
# message(20120514) = "2012年5月14日 星期一 农历壬辰[龙]年四月廿四"
# message(20120515) = "2012年5月15日 星期二 农历壬辰[龙]年四月廿五 节日：#国际家庭日#"
# message(20120516) = "2012年5月16日 星期三 农历壬辰[龙]年四月廿六"
# message(20120517) = "2012年5月17日 星期四 农历壬辰[龙]年四月廿七 节日：#国际电信日#"
# message(20120518) = "2012年5月18日 星期五 农历壬辰[龙]年四月廿八 节日：#国际博物馆日#"
# message(20120519) = "2012年5月19日 星期六 农历壬辰[龙]年四月廿九"
# message(20120520) = "2012年5月20日 星期日 农历壬辰[龙]年四月三十 节日：#全国学生营养日# #全国助残日#"
# message(20120521) = "2012年5月21日 星期一 农历壬辰[龙]年闰四月初一 节气：#小满#"
# message(20120522) = "2012年5月22日 星期二 农历壬辰[龙]年闰四月初二"
# message(20120523) = "2012年5月23日 星期三 农历壬辰[龙]年闰四月初三 节日：#国际牛奶日#"
# message(20120524) = "2012年5月24日 星期四 农历壬辰[龙]年闰四月初四"
# message(20120525) = "2012年5月25日 星期五 农历壬辰[龙]年闰四月初五"
# message(20120526) = "2012年5月26日 星期六 农历壬辰[龙]年闰四月初六"
# message(20120527) = "2012年5月27日 星期日 农历壬辰[龙]年闰四月初七"
# message(20120528) = "2012年5月28日 星期一 农历壬辰[龙]年闰四月初八"
# message(20120529) = "2012年5月29日 星期二 农历壬辰[龙]年闰四月初九"
# message(20120530) = "2012年5月30日 星期三 农历壬辰[龙]年闰四月初十"
# message(20120531) = "2012年5月31日 星期四 农历壬辰[龙]年闰四月十一 节日：#世界无烟日#"
# message(20120601) = "2012年6月1日 星期五 农历壬辰[龙]年闰四月十二 节日：#国际儿童节#"
# message(20120602) = "2012年6月2日 星期六 农历壬辰[龙]年闰四月十三"
# message(20120603) = "2012年6月3日 星期日 农历壬辰[龙]年闰四月十四"
# message(20120604) = "2012年6月4日 星期一 农历壬辰[龙]年闰四月十五"
# message(20120605) = "2012年6月5日 星期二 农历壬辰[龙]年闰四月十六 节气：#芒种# 节日：#世界环境保护日#"
# message(20120606) = "2012年6月6日 星期三 农历壬辰[龙]年闰四月十七 节日：#全国爱眼日#"
# message(20120607) = "2012年6月7日 星期四 农历壬辰[龙]年闰四月十八"
# message(20120608) = "2012年6月8日 星期五 农历壬辰[龙]年闰四月十九"
# message(20120609) = "2012年6月9日 星期六 农历壬辰[龙]年闰四月廿十"
# message(20120610) = "2012年6月10日 星期日 农历壬辰[龙]年闰四月廿一"
# message(20120611) = "2012年6月11日 星期一 农历壬辰[龙]年闰四月廿二"
# message(20120612) = "2012年6月12日 星期二 农历壬辰[龙]年闰四月廿三"
# message(20120613) = "2012年6月13日 星期三 农历壬辰[龙]年闰四月廿四"
# message(20120614) = "2012年6月14日 星期四 农历壬辰[龙]年闰四月廿五"
# message(20120615) = "2012年6月15日 星期五 农历壬辰[龙]年闰四月廿六"
# message(20120616) = "2012年6月16日 星期六 农历壬辰[龙]年闰四月廿七"
# message(20120617) = "2012年6月17日 星期日 农历壬辰[龙]年闰四月廿八 节日：#防治荒漠化和干旱日# #父亲节#"
# message(20120618) = "2012年6月18日 星期一 农历壬辰[龙]年闰四月廿九"
# message(20120619) = "2012年6月19日 星期二 农历壬辰[龙]年五月初一"
# message(20120620) = "2012年6月20日 星期三 农历壬辰[龙]年五月初二"
# message(20120621) = "2012年6月21日 星期四 农历壬辰[龙]年五月初三 节气：#夏至#"
# message(20120622) = "2012年6月22日 星期五 农历壬辰[龙]年五月初四"
# message(20120623) = "2012年6月23日 星期六 农历壬辰[龙]年五月初五 节日：#国际奥林匹克日# #端午节#"
# message(20120624) = "2012年6月24日 星期日 农历壬辰[龙]年五月初六"
# message(20120625) = "2012年6月25日 星期一 农历壬辰[龙]年五月初七 节日：#全国土地日#"
# message(20120626) = "2012年6月26日 星期二 农历壬辰[龙]年五月初八 节日：#国际禁毒日#"
# message(20120627) = "2012年6月27日 星期三 农历壬辰[龙]年五月初九"
# message(20120628) = "2012年6月28日 星期四 农历壬辰[龙]年五月初十"
# message(20120629) = "2012年6月29日 星期五 农历壬辰[龙]年五月十一"
# message(20120630) = "2012年6月30日 星期六 农历壬辰[龙]年五月十二"
# message(20120701) = "2012年7月1日 星期日 农历壬辰[龙]年五月十三 节日：#中国共·产党诞辰# #香港回归纪念日# #世界建筑日#"
# message(20120702) = "2012年7月2日 星期一 农历壬辰[龙]年五月十四 节日：#国际体育记者日#"
# message(20120703) = "2012年7月3日 星期二 农历壬辰[龙]年五月十五"
# message(20120704) = "2012年7月4日 星期三 农历壬辰[龙]年五月十六"
# message(20120705) = "2012年7月5日 星期四 农历壬辰[龙]年五月十七"
# message(20120706) = "2012年7月6日 星期五 农历壬辰[龙]年五月十八"
# message(20120707) = "2012年7月7日 星期六 农历壬辰[龙]年五月十九 节气：#小暑# 节日：#抗日战争纪念日#"
# message(20120708) = "2012年7月8日 星期日 农历壬辰[龙]年五月廿十"
# message(20120709) = "2012年7月9日 星期一 农历壬辰[龙]年五月廿一"
# message(20120710) = "2012年7月10日 星期二 农历壬辰[龙]年五月廿二"
# message(20120711) = "2012年7月11日 星期三 农历壬辰[龙]年五月廿三 节日：#世界人口日#"
# message(20120712) = "2012年7月12日 星期四 农历壬辰[龙]年五月廿四"
# message(20120713) = "2012年7月13日 星期五 农历壬辰[龙]年五月廿五"
# message(20120714) = "2012年7月14日 星期六 农历壬辰[龙]年五月廿六"
# message(20120715) = "2012年7月15日 星期日 农历壬辰[龙]年五月廿七 节日：#被奴役国家周#"
# message(20120716) = "2012年7月16日 星期一 农历壬辰[龙]年五月廿八"
# message(20120717) = "2012年7月17日 星期二 农历壬辰[龙]年五月廿九"
# message(20120718) = "2012年7月18日 星期三 农历壬辰[龙]年五月三十"
# message(20120719) = "2012年7月19日 星期四 农历壬辰[龙]年六月初一"
# message(20120720) = "2012年7月20日 星期五 农历壬辰[龙]年六月初二"
# message(20120721) = "2012年7月21日 星期六 农历壬辰[龙]年六月初三"
# message(20120722) = "2012年7月22日 星期日 农历壬辰[龙]年六月初四 节气：#大暑#"
# message(20120723) = "2012年7月23日 星期一 农历壬辰[龙]年六月初五"
# message(20120724) = "2012年7月24日 星期二 农历壬辰[龙]年六月初六"
# message(20120725) = "2012年7月25日 星期三 农历壬辰[龙]年六月初七"
# message(20120726) = "2012年7月26日 星期四 农历壬辰[龙]年六月初八"
# message(20120727) = "2012年7月27日 星期五 农历壬辰[龙]年六月初九"
# message(20120728) = "2012年7月28日 星期六 农历壬辰[龙]年六月初十"
# message(20120729) = "2012年7月29日 星期日 农历壬辰[龙]年六月十一"
# message(20120730) = "2012年7月30日 星期一 农历壬辰[龙]年六月十二 节日：#非洲妇女日#"
# message(20120731) = "2012年7月31日 星期二 农历壬辰[龙]年六月十三"
# message(20120801) = "2012年8月1日 星期三 农历壬辰[龙]年六月十四 节日：#建军节#"
# message(20120802) = "2012年8月2日 星期四 农历壬辰[龙]年六月十五"
# message(20120803) = "2012年8月3日 星期五 农历壬辰[龙]年六月十六"
# message(20120804) = "2012年8月4日 星期六 农历壬辰[龙]年六月十七"
# message(20120805) = "2012年8月5日 星期日 农历壬辰[龙]年六月十八"
# message(20120806) = "2012年8月6日 星期一 农历壬辰[龙]年六月十九"
# message(20120807) = "2012年8月7日 星期二 农历壬辰[龙]年六月廿十 节气：#立秋#"
# message(20120808) = "2012年8月8日 星期三 农历壬辰[龙]年六月廿一 节日：#中国男子节"
# message(20120809) = "2012年8月9日 星期四 农历壬辰[龙]年六月廿二"
# message(20120810) = "2012年8月10日 星期五 农历壬辰[龙]年六月廿三"
# message(20120811) = "2012年8月11日 星期六 农历壬辰[龙]年六月廿四"
# message(20120812) = "2012年8月12日 星期日 农历壬辰[龙]年六月廿五"
# message(20120813) = "2012年8月13日 星期一 农历壬辰[龙]年六月廿六"
# message(20120814) = "2012年8月14日 星期二 农历壬辰[龙]年六月廿七"
# message(20120815) = "2012年8月15日 星期三 农历壬辰[龙]年六月廿八 节日：#抗日战争胜利纪念#"
# message(20120816) = "2012年8月16日 星期四 农历壬辰[龙]年六月廿九"
# message(20120817) = "2012年8月17日 星期五 农历壬辰[龙]年七月初一"
# message(20120818) = "2012年8月18日 星期六 农历壬辰[龙]年七月初二"
# message(20120819) = "2012年8月19日 星期日 农历壬辰[龙]年七月初三"
# message(20120820) = "2012年8月20日 星期一 农历壬辰[龙]年七月初四"
# message(20120821) = "2012年8月21日 星期二 农历壬辰[龙]年七月初五"
# message(20120822) = "2012年8月22日 星期三 农历壬辰[龙]年七月初六"
# message(20120823) = "2012年8月23日 星期四 农历壬辰[龙]年七月初七 节气：#处暑# 节日：#七夕情人节#"
# message(20120824) = "2012年8月24日 星期五 农历壬辰[龙]年七月初八"
# message(20120825) = "2012年8月25日 星期六 农历壬辰[龙]年七月初九"
# message(20120826) = "2012年8月26日 星期日 农历壬辰[龙]年七月初十"
# message(20120827) = "2012年8月27日 星期一 农历壬辰[龙]年七月十一"
# message(20120828) = "2012年8月28日 星期二 农历壬辰[龙]年七月十二"
# message(20120829) = "2012年8月29日 星期三 农历壬辰[龙]年七月十三"
# message(20120830) = "2012年8月30日 星期四 农历壬辰[龙]年七月十四"
# message(20120831) = "2012年8月31日 星期五 农历壬辰[龙]年七月十五 节日：#中元节#"
# message(20120901) = "2012年9月1日 星期六 农历壬辰[龙]年七月十六"
# message(20120902) = "2012年9月2日 星期日 农历壬辰[龙]年七月十七"
# message(20120903) = "2012年9月3日 星期一 农历壬辰[龙]年七月十八"
# message(20120904) = "2012年9月4日 星期二 农历壬辰[龙]年七月十九"
# message(20120905) = "2012年9月5日 星期三 农历壬辰[龙]年七月廿十"
# message(20120906) = "2012年9月6日 星期四 农历壬辰[龙]年七月廿一"
# message(20120907) = "2012年9月7日 星期五 农历壬辰[龙]年七月廿二 节气：#白露#"
# message(20120908) = "2012年9月8日 星期六 农历壬辰[龙]年七月廿三 节日：#国际扫盲日# #国际新闻工作者日#"
# message(20120909) = "2012年9月9日 星期日 农历壬辰[龙]年七月廿四 节日：#毛·泽东逝世纪念#"
# message(20120910) = "2012年9月10日 星期一 农历壬辰[龙]年七月廿五 节日：#中国教师节#"
# message(20120911) = "2012年9月11日 星期二 农历壬辰[龙]年七月廿六"
# message(20120912) = "2012年9月12日 星期三 农历壬辰[龙]年七月廿七"
# message(20120913) = "2012年9月13日 星期四 农历壬辰[龙]年七月廿八"
# message(20120914) = "2012年9月14日 星期五 农历壬辰[龙]年七月廿九 节日：#世界清洁地球日#"
# message(20120915) = "2012年9月15日 星期六 农历壬辰[龙]年七月三十"
# message(20120916) = "2012年9月16日 星期日 农历壬辰[龙]年八月初一 节日：#国际臭氧层保护日#"
# message(20120917) = "2012年9月17日 星期一 农历壬辰[龙]年八月初二"
# message(20120918) = "2012年9月18日 星期二 农历壬辰[龙]年八月初三 节日：#九·一八事变纪念日# #国际和平日#"
# message(20120919) = "2012年9月19日 星期三 农历壬辰[龙]年八月初四"
# message(20120920) = "2012年9月20日 星期四 农历壬辰[龙]年八月初五 节日：#国际爱牙日#"
# message(20120921) = "2012年9月21日 星期五 农历壬辰[龙]年八月初六"
# message(20120922) = "2012年9月22日 星期六 农历壬辰[龙]年八月初七 节气：#秋分#"
# message(20120923) = "2012年9月23日 星期日 农历壬辰[龙]年八月初八 节日：#国际聋人节# #世界儿童日#"
# message(20120924) = "2012年9月24日 星期一 农历壬辰[龙]年八月初九"
# message(20120925) = "2012年9月25日 星期二 农历壬辰[龙]年八月初十"
# message(20120926) = "2012年9月26日 星期三 农历壬辰[龙]年八月十一"
# message(20120927) = "2012年9月27日 星期四 农历壬辰[龙]年八月十二 节日：#世界旅游日#"
# message(20120928) = "2012年9月28日 星期五 农历壬辰[龙]年八月十三 节日：#孔子诞辰#"
# message(20120929) = "2012年9月29日 星期六 农历壬辰[龙]年八月十四"
# message(20120930) = "2012年9月30日 星期日 农历壬辰[龙]年八月十五 节日：#世界海事日# #中秋节#"
# message(20121001) = "2012年10月1日 星期一 农历壬辰[龙]年八月十六 节日：#国庆节# #世界音乐日# #国际老人节# #国际住房日#"
# message(20121002) = "2012年10月2日 星期二 农历壬辰[龙]年八月十七 节日：#国庆节假日# #国际和平与民主自由斗争日#"
# message(20121003) = "2012年10月3日 星期三 农历壬辰[龙]年八月十八 节日：#国庆节假日# #国际减轻自然灾害日"
# message(20121004) = "2012年10月4日 星期四 农历壬辰[龙]年八月十九 节日：#世界动物日#"
# message(20121005) = "2012年10月5日 星期五 农历壬辰[龙]年八月廿十"
# message(20121006) = "2012年10月6日 星期六 农历壬辰[龙]年八月廿一 节日：#老人节#"
# message(20121007) = "2012年10月7日 星期日 农历壬辰[龙]年八月廿二"
# message(20121008) = "2012年10月8日 星期一 农历壬辰[龙]年八月廿三 节气：#寒露# 节日：#全国高血压日# #世界视觉日#"
# message(20121009) = "2012年10月9日 星期二 农历壬辰[龙]年八月廿四 节日：#世界邮政日# #万国邮联日#"
# message(20121010) = "2012年10月10日 星期三 农历壬辰[龙]年八月廿五 节日：#辛亥革命纪念日# #世界精神卫生日#"
# message(20121011) = "2012年10月11日 星期四 农历壬辰[龙]年八月廿六"
# message(20121012) = "2012年10月12日 星期五 农历壬辰[龙]年八月廿七"
# message(20121013) = "2012年10月13日 星期六 农历壬辰[龙]年八月廿八 节日：#世界保健日# #国际教师节#"
# message(20121014) = "2012年10月14日 星期日 农历壬辰[龙]年八月廿九 节日：#世界标准日#"
# message(20121015) = "2012年10月15日 星期一 农历壬辰[龙]年九月初一 节日：#国际盲人节"
# message(20121016) = "2012年10月16日 星期二 农历壬辰[龙]年九月初二 节日：#世界粮食日#"
# message(20121017) = "2012年10月17日 星期三 农历壬辰[龙]年九月初三 节日：#世界消除贫困日#"
# message(20121018) = "2012年10月18日 星期四 农历壬辰[龙]年九月初四"
# message(20121019) = "2012年10月19日 星期五 农历壬辰[龙]年九月初五"
# message(20121020) = "2012年10月20日 星期六 农历壬辰[龙]年九月初六"
# message(20121021) = "2012年10月21日 星期日 农历壬辰[龙]年九月初七"
# message(20121022) = "2012年10月22日 星期一 农历壬辰[龙]年九月初八 节日：#世界传统医药日#"
# message(20121023) = "2012年10月23日 星期二 农历壬辰[龙]年九月初九 节气：#霜降# 节日：#重阳节#"
# message(20121024) = "2012年10月24日 星期三 农历壬辰[龙]年九月初十 节日：#联合国日#"
# message(20121025) = "2012年10月25日 星期四 农历壬辰[龙]年九月十一"
# message(20121026) = "2012年10月26日 星期五 农历壬辰[龙]年九月十二"
# message(20121027) = "2012年10月27日 星期六 农历壬辰[龙]年九月十三"
# message(20121028) = "2012年10月28日 星期日 农历壬辰[龙]年九月十四"
# message(20121029) = "2012年10月29日 星期一 农历壬辰[龙]年九月十五"
# message(20121030) = "2012年10月30日 星期二 农历壬辰[龙]年九月十六"
# message(20121031) = "2012年10月31日 星期三 农历壬辰[龙]年九月十七 节日：#世界勤俭日#"
# message(20121101) = "2012年11月1日 星期四 农历壬辰[龙]年九月十八"
# message(20121102) = "2012年11月2日 星期五 农历壬辰[龙]年九月十九"
# message(20121103) = "2012年11月3日 星期六 农历壬辰[龙]年九月廿十"
# message(20121104) = "2012年11月4日 星期日 农历壬辰[龙]年九月廿一"
# message(20121105) = "2012年11月5日 星期一 农历壬辰[龙]年九月廿二"
# message(20121106) = "2012年11月6日 星期二 农历壬辰[龙]年九月廿三"
# message(20121107) = "2012年11月7日 星期三 农历壬辰[龙]年九月廿四 节气：#立冬# 节日：#十月社会主义革命纪念日#"
# message(20121108) = "2012年11月8日 星期四 农历壬辰[龙]年九月廿五 节日：#中国记者日#"
# message(20121109) = "2012年11月9日 星期五 农历壬辰[龙]年九月廿六 节日：#全国消防安全宣传教育日#"
# message(20121110) = "2012年11月10日 星期六 农历壬辰[龙]年九月廿七 节日：#世界青年节#"
# message(20121111) = "2012年11月11日 星期日 农历壬辰[龙]年九月廿八 节日：#国际科学与和平周"
# message(20121112) = "2012年11月12日 星期一 农历壬辰[龙]年九月廿九 节日：#孙中山诞辰纪念日#"
# message(20121113) = "2012年11月13日 星期二 农历壬辰[龙]年九月三十"
# message(20121114) = "2012年11月14日 星期三 农历壬辰[龙]年十月初一 节日：#世界糖尿病日#"
# message(20121115) = "2012年11月15日 星期四 农历壬辰[龙]年十月初二"
# message(20121116) = "2012年11月16日 星期五 农历壬辰[龙]年十月初三 节日：#国际宽容日#"
# message(20121117) = "2012年11月17日 星期六 农历壬辰[龙]年十月初四 节日：#国际大学生节# #世界学生节#"
# message(20121118) = "2012年11月18日 星期日 农历壬辰[龙]年十月初五"
# message(20121119) = "2012年11月19日 星期一 农历壬辰[龙]年十月初六"
# message(20121120) = "2012年11月20日 星期二 农历壬辰[龙]年十月初七 节日：#彝族年#"
# message(20121121) = "2012年11月21日 星期三 农历壬辰[龙]年十月初八 节日：#彝族年# #世界问候日# #世界电视日#"
# message(20121122) = "2012年11月22日 星期四 农历壬辰[龙]年十月初九 节气：#小雪# 节日：#彝族年# #感恩节#"
# message(20121123) = "2012年11月23日 星期五 农历壬辰[龙]年十月初十"
# message(20121124) = "2012年11月24日 星期六 农历壬辰[龙]年十月十一"
# message(20121125) = "2012年11月25日 星期日 农历壬辰[龙]年十月十二"
# message(20121126) = "2012年11月26日 星期一 农历壬辰[龙]年十月十三"
# message(20121127) = "2012年11月27日 星期二 农历壬辰[龙]年十月十四"
# message(20121128) = "2012年11月28日 星期三 农历壬辰[龙]年十月十五"
# message(20121129) = "2012年11月29日 星期四 农历壬辰[龙]年十月十六 节日：#国际声援巴勒斯坦人民国际日#"
# message(20121130) = "2012年11月30日 星期五 农历壬辰[龙]年十月十七"
# message(20121201) = "2012年12月1日 星期六 农历壬辰[龙]年十月十八 节日：#世界艾滋病日#"
# message(20121202) = "2012年12月2日 星期日 农历壬辰[龙]年十月十九"
# message(20121203) = "2012年12月3日 星期一 农历壬辰[龙]年十月廿十 节日：#世界残疾人日#"
# message(20121204) = "2012年12月4日 星期二 农历壬辰[龙]年十月廿一"
# message(20121205) = "2012年12月5日 星期三 农历壬辰[龙]年十月廿二 节日：#国际经济和社会发展志愿人员日#"
# message(20121206) = "2012年12月6日 星期四 农历壬辰[龙]年十月廿三 节气：#大雪#"
# message(20121207) = "2012年12月7日 星期五 农历壬辰[龙]年十月廿四"
# message(20121208) = "2012年12月8日 星期六 农历壬辰[龙]年十月廿五 节日：#国际儿童电视日#"
# message(20121209) = "2012年12月9日 星期日 农历壬辰[龙]年十月廿六 节日：#世界足球日#"
# message(20121210) = "2012年12月10日 星期一 农历壬辰[龙]年十月廿七 节日：#世界人权日#"
# message(20121211) = "2012年12月11日 星期二 农历壬辰[龙]年十月廿八"
# message(20121212) = "2012年12月12日 星期三 农历壬辰[龙]年十月廿九 节日：#西安事变纪念日#"
# message(20121213) = "2012年12月13日 星期四 农历壬辰[龙]年十一月初一 节日：#南京大屠杀"
# message(20121214) = "2012年12月14日 星期五 农历壬辰[龙]年十一月初二"
# message(20121215) = "2012年12月15日 星期六 农历壬辰[龙]年十一月初三"
# message(20121216) = "2012年12月16日 星期日 农历壬辰[龙]年十一月初四"
# message(20121217) = "2012年12月17日 星期一 农历壬辰[龙]年十一月初五"
# message(20121218) = "2012年12月18日 星期二 农历壬辰[龙]年十一月初六"
# message(20121219) = "2012年12月19日 星期三 农历壬辰[龙]年十一月初七"
# message(20121220) = "2012年12月20日 星期四 农历壬辰[龙]年十一月初八 节日：#澳门回归纪念#"
# message(20121221) = "2012年12月21日 星期五 农历壬辰[龙]年十一月初九 节气：#冬至# 节日：#国际篮球日#"
# message(20121222) = "2012年12月22日 星期六 农历壬辰[龙]年十一月初十"
# message(20121223) = "2012年12月23日 星期日 农历壬辰[龙]年十一月十一"
# message(20121224) = "2012年12月24日 星期一 农历壬辰[龙]年十一月十二 节日：#平安夜#"
# message(20121225) = "2012年12月25日 星期二 农历壬辰[龙]年十一月十三 节日：#圣诞节#"
# message(20121226) = "2012年12月26日 星期三 农历壬辰[龙]年十一月十四 节日：#毛·泽东诞辰纪念日#"
# message(20121227) = "2012年12月27日 星期四 农历壬辰[龙]年十一月十五"
# message(20121228) = "2012年12月28日 星期五 农历壬辰[龙]年十一月十六"
# message(20121229) = "2012年12月29日 星期六 农历壬辰[龙]年十一月十七"
# message(20121230) = "2012年12月30日 星期日 农历壬辰[龙]年十一月十八"
# message(20121231) = "2012年12月31日 星期一 农历壬辰[龙]年十一月十九"
# 今天是2019年3月7日 星期四 农历己亥[猪]年二月初一
