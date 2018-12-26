# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

"""
prompt_toolkit_suggest.py

Version: 1.0
Author: LC
DateTime: 2018年12月26日11:36:45
UpdateTime: None
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""

while True:
    user_input = prompt('>',
                        history=FileHistory('prompt_toolkit_suggest_history.txt'),
                        auto_suggest=AutoSuggestFromHistory(),
                        )
    print(user_input)

#  注意：要在控制台cmd中执行
