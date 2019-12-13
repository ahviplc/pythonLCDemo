import base64
import json

"""

base64_demo.py
base64工具类
备注：base64工具类的使用说明和使用示例以及SS/SSR相关的base64原理
Version: 1.0
Author: LC
DateTime: 2019年12月13日14:52:31
UpdateTime:
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
LC博客url: http://oneplusone.vip/index.html
一加壹.SNS LC - 又一个SNS社区: http://sns.oneplusone.vip
赞助一加壹博客最Top-LC万能收款码支持-支付宝、微信、QQ
http://lc.oneplusone.vip/donateMeByLC.html

"""


# 初始化数据
def row_data():
    content = {
        "buyer_nick": "家有亲亲",
        "payment": "109.40",
        "status": "ok",
        "iid": 0,
        "oid": 76491699395733780,
        "tid": "654561321213",
        "type": "guarantee_trade",
        "post_fee": "0.00",
        "seller_nick": "测试店铺"
    }
    context_str = json.dumps(content, ensure_ascii=False)
    d = {
        "TmcId": 654561321213,
        "Topic": "taobao_trade_TradeBuyerPay",
        "UserId": "123456789",
        "UserNick": "测试店铺",
        "PubAppKey": "12345678",
        "PubTime": "2017-10-18T16:32:39.033",
        "OutgoingTime": "2017-10-18T16:32:39.237",
        "Content": context_str
    }
    return d


# 新建Base64Handler类
class Base64Handler:
    @classmethod
    def base64_encode(cls, json_data: dict, is_json_flag):  # json_data参数:要操作的数据 is_json_flag参数:要操作的参数是不是json
        if is_json_flag:
            data_to_str = json.dumps(json_data, ensure_ascii=False)
        else:
            data_to_str = json_data
        r = base64.b64encode(bytes(data_to_str, "utf-8"))
        return str(r, encoding="utf-8")

    @classmethod
    def base64_decode(cls, s):
        if len(s) % 4 != 0:  # 如果s的长度可以被4整除 无余数 不操作
            missing_padding = 4 - len(s) % 4  # s的长度不可以被4整除 4-(减去)(s的长度除以4的余数)的值 值是多少 在s后面加几个=
            if missing_padding:
                s += '=' * missing_padding
        decode_data = base64.b64decode(s).decode()
        return decode_data


# main方法
def main():
    encode_data = Base64Handler.base64_encode(row_data(), True)

    print("encode data:\n{}".format(encode_data))

    decode_data = Base64Handler.base64_decode(encode_data)
    print("decode data:\n{}".format(decode_data))

    # base64在线加解密网站: https://www.sojson.com/base64.html
    # Base64在线解码、编码 Base64 UTF8 GB2312 二进制 十六进制 加密、解密 - The X 在线工具: https://the-x.cn/base64
    """
    encode data:
    eyJUbWNJZCI6IDY1NDU2MTMyMTIxMywgIlRvcGljIjogInRhb2Jhb190cmFkZV9UcmFkZUJ1eWVyUGF5IiwgIlVzZXJJZCI6ICIxMjM0NTY3ODkiLCAiVXNlck5pY2siOiAi5rWL6K+V5bqX6ZO6IiwgIlB1YkFwcEtleSI6ICIxMjM0NTY3OCIsICJQdWJUaW1lIjogIjIwMTctMTAtMThUMTY6MzI6MzkuMDMzIiwgIk91dGdvaW5nVGltZSI6ICIyMDE3LTEwLTE4VDE2OjMyOjM5LjIzNyIsICJDb250ZW50IjogIntcImJ1eWVyX25pY2tcIjogXCLlrrbmnInkurLkurJcIiwgXCJwYXltZW50XCI6IFwiMTA5LjQwXCIsIFwic3RhdHVzXCI6IFwib2tcIiwgXCJpaWRcIjogMCwgXCJvaWRcIjogNzY0OTE2OTkzOTU3MzM3ODAsIFwidGlkXCI6IFwiNjU0NTYxMzIxMjEzXCIsIFwidHlwZVwiOiBcImd1YXJhbnRlZV90cmFkZVwiLCBcInBvc3RfZmVlXCI6IFwiMC4wMFwiLCBcInNlbGxlcl9uaWNrXCI6IFwi5rWL6K+V5bqX6ZO6XCJ9In0=
    decode data:
    {"TmcId": 654561321213, "Topic": "taobao_trade_TradeBuyerPay", "UserId": "123456789", "UserNick": "测试店铺", "PubAppKey": "12345678", "PubTime": "2017-10-18T16:32:39.033", "OutgoingTime": "2017-10-18T16:32:39.237", "Content": "{\"buyer_nick\": \"家有亲亲\", \"payment\": \"109.40\", \"status\": \"ok\", \"iid\": 0, \"oid\": 76491699395733780, \"tid\": \"654561321213\", \"type\": \"guarantee_trade\", \"post_fee\": \"0.00\", \"seller_nick\": \"测试店铺\"}"}
    """

    # SSR SS 的解析
    print(Base64Handler.base64_decode("MTM5LjE2Mi41Ni4xMjU6MTc3MzE6b3JpZ2luOmFlcy0yNTYtY2ZiOnBsYWluOlpqVTFMbVoxYmkweE1EQTFPVEF3TVEvP29iZnNwYXJhbT1iMkptYzNCaGNtRnQmcHJvdG9wYXJhbT1jSEp2ZEc5amIyeHdZWEpoYlEmcmVtYXJrcz1jbVZ0WVhKcmN3Jmdyb3VwPVJuSmxaVk5UVWkxd2RXSnNhV00"))  # SSR ssr://MTM5LjE2Mi41Ni4xMjU6MTc3MzE6b3JpZ2luOmFlcy0yNTYtY2ZiOnBsYWluOlpqVTFMbVoxYmkweE1EQTFPVEF3TVEvP29iZnNwYXJhbT1iMkptYzNCaGNtRnQmcHJvdG9wYXJhbT1jSEp2ZEc5amIyeHdZWEpoYlEmcmVtYXJrcz1jbVZ0WVhKcmN3Jmdyb3VwPVJuSmxaVk5UVWkxd2RXSnNhV00
    print(Base64Handler.base64_decode("MTcyLjEwNC4xMDUuMTY4OjMwNzA3Om9yaWdpbjphZXMtMjU2LWNmYjpwbGFpbjpaalV5V0dsVWRYVjJNbk54Lz9vYmZzcGFyYW09JnJlbWFya3M9UUhOemNnJmdyb3VwPVFITnpjZw"))  # SSR ssr://MTcyLjEwNC4xMDUuMTY4OjMwNzA3Om9yaWdpbjphZXMtMjU2LWNmYjpwbGFpbjpaalV5V0dsVWRYVjJNbk54Lz9vYmZzcGFyYW09JnJlbWFya3M9UUhOemNnJmdyb3VwPVFITnpjZw

    print(Base64Handler.base64_decode("cmM0LW1kNTpsbmNuLm9yZyB2NjZAODkuMzEuMTI1LjIzNjoyMDE1"))  # SS ss://cmM0LW1kNTpsbmNuLm9yZyB2NjZAODkuMzEuMTI1LjIzNjoyMDE1

    print(Base64Handler.base64_decode("QHNzcg"))
    print("")

    # encode data:
    # eyJUbWNJZCI6IDY1NDU2MTMyMTIxMywgIlRvcGljIjogInRhb2Jhb190cmFkZV9UcmFkZUJ1eWVyUGF5IiwgIlVzZXJJZCI6ICIxMjM0NTY3ODkiLCAiVXNlck5pY2siOiAi5rWL6K+V5bqX6ZO6IiwgIlB1YkFwcEtleSI6ICIxMjM0NTY3OCIsICJQdWJUaW1lIjogIjIwMTctMTAtMThUMTY6MzI6MzkuMDMzIiwgIk91dGdvaW5nVGltZSI6ICIyMDE3LTEwLTE4VDE2OjMyOjM5LjIzNyIsICJDb250ZW50IjogIntcImJ1eWVyX25pY2tcIjogXCLlrrbmnInkurLkurJcIiwgXCJwYXltZW50XCI6IFwiMTA5LjQwXCIsIFwic3RhdHVzXCI6IFwib2tcIiwgXCJpaWRcIjogMCwgXCJvaWRcIjogNzY0OTE2OTkzOTU3MzM3ODAsIFwidGlkXCI6IFwiNjU0NTYxMzIxMjEzXCIsIFwidHlwZVwiOiBcImd1YXJhbnRlZV90cmFkZVwiLCBcInBvc3RfZmVlXCI6IFwiMC4wMFwiLCBcInNlbGxlcl9uaWNrXCI6IFwi5rWL6K+V5bqX6ZO6XCJ9In0=
    # decode data:
    # {"TmcId": 654561321213, "Topic": "taobao_trade_TradeBuyerPay", "UserId": "123456789", "UserNick": "测试店铺", "PubAppKey": "12345678", "PubTime": "2017-10-18T16:32:39.033", "OutgoingTime": "2017-10-18T16:32:39.237", "Content": "{\"buyer_nick\": \"家有亲亲\", \"payment\": \"109.40\", \"status\": \"ok\", \"iid\": 0, \"oid\": 76491699395733780, \"tid\": \"654561321213\", \"type\": \"guarantee_trade\", \"post_fee\": \"0.00\", \"seller_nick\": \"测试店铺\"}"}
    # 139.162.56.125:17731:origin:aes-256-cfb:plain:ZjU1LmZ1bi0xMDA1OTAwMQ/?obfsparam=b2Jmc3BhcmFt&protoparam=cHJvdG9jb2xwYXJhbQ&remarks=cmVtYXJrcw&group=RnJlZVNTUi1wdWJsaWM
    # 172.104.105.168:30707:origin:aes-256-cfb:plain:ZjUyWGlUdXV2MnNx/?obfsparam=&remarks=QHNzcg&group=QHNzcg
    # rc4-md5:lncn.org v66@89.31.125.236:2015
    # @ssr

    print(Base64Handler.base64_encode("@ssr", False))
    print(Base64Handler.base64_decode("ZjUyWGlUdXV2MnNx"))
    print("")
    sss_temp = Base64Handler.base64_encode("172.104.105.168:30707:origin:aes-256-cfb:plain:ZjUyWGlUdXV2MnNx/?obfsparam=&remarks=QHNzcg&group=QHNzcg", False)
    print(sss_temp)
    print("实际的SSS链接是: " + "ssr://" + sss_temp)
    print("")
    ss_temp = Base64Handler.base64_encode("rc4-md5:lncn.org v66@89.31.125.236:2015", False)
    print(ss_temp)
    print("实际的SS链接是: " + "ss://" + ss_temp)

    # QHNzcg==
    # f52XiTuuv2sq
    #
    # MTcyLjEwNC4xMDUuMTY4OjMwNzA3Om9yaWdpbjphZXMtMjU2LWNmYjpwbGFpbjpaalV5V0dsVWRYVjJNbk54Lz9vYmZzcGFyYW09JnJlbWFya3M9UUhOemNnJmdyb3VwPVFITnpjZw==
    # 实际的SSS链接是: ssr://MTcyLjEwNC4xMDUuMTY4OjMwNzA3Om9yaWdpbjphZXMtMjU2LWNmYjpwbGFpbjpaalV5V0dsVWRYVjJNbk54Lz9vYmZzcGFyYW09JnJlbWFya3M9UUhOemNnJmdyb3VwPVFITnpjZw==
    #
    # cmM0LW1kNTpsbmNuLm9yZyB2NjZAODkuMzEuMTI1LjIzNjoyMDE1
    # 实际的SS链接是: ss://cmM0LW1kNTpsbmNuLm9yZyB2NjZAODkuMzEuMTI1LjIzNjoyMDE1


if __name__ == '__main__':
    main()
