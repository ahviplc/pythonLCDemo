#!/usr/local/bin/python
# -*- coding:utf-8 -*-

"""
default_logging2.py

Version: 1.0
Author: LC
DateTime: 2018年12月26日11:42:26
UpdateTime: None
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客
"""

import logging

logging.basicConfig(filename='default_logging2_app.log', level=logging.INFO)  # level=logging.INFO 可以设置输出的级别

logging.debug('debug message')
logging.info('info message')
# logging.warn('warn message')
logging.warning('warn message')
logging.error('error message')
logging.critical('critical message')
