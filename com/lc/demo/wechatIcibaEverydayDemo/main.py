#!/usr/bin/python3
# coding=utf-8
# 每日一句
import Iciba

if __name__ == '__main__':
    # 微信配置
    wechat_config = {
        'appid': 'wx288fdb15f260ce59',  # (No.1)此处填写公众号的appid
        'appsecret': '###',  # (No.2)此处填写公众号的appsecret
        'template_id': 'GPb6ipprPuD1ylES5_tPCh88MlsAKitkMkd_SMrRBU4'  # (No.3)此处填写公众号的模板消息ID
    }

    # 用户列表
    openids = [
        'ovKgCv3r_WvaMDpVzUnrG0fjS5js',  # (No.4)此处填写你的微信号（微信公众平台上的微信号）
        'ovKgCvzZJX03ErPvviCPpKtCJfXE',
        # 'xxxxx',#如果有多个用户也可以
    ]

    # 执行
    icb = Iciba.iciba(wechat_config)

    '''
    run()方法可以传入openids列表，也可不传参数
    不传参数则对微信公众号的所有用户进行群发
    '''
    icb.run()
