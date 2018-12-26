#!/usr/local/bin/python
# -*- coding:utf-8 -*-

"""
use_logging_config.py

Version: 1.0
Author: LC
DateTime: 2018年12月26日11:43:07
UpdateTime: None
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客
"""

import logging
import logging.config

logging.config.fileConfig('use_logging_config_logging.cnf')

logging.debug('debug message')
logging.info('info message')
# logging.warn('warn message')
logging.warning('warn message')
logging.error('error message')
logging.critical('critical message')
