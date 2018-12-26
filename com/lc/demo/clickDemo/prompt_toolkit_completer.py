# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter

# from prompt_toolkit.contrib.completers import WordCompleter # 废弃，prompt_toolkit目录结构已改
# WordCompleter函数最新导入:from prompt_toolkit.completion import WordCompleter

"""
prompt_toolkit_completer.py

Version: 1.0
Author: LC
DateTime: 2018年12月26日11:34:31
UpdateTime: None
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""

SQLCompleter = WordCompleter(['select', 'from', 'insert', 'update', 'delete',
                              'drop', 'LC', 'I Love LC'], ignore_case=True)

while True:
    user_input = prompt('SQL>',
                        history=FileHistory('prompt_toolkit_completer_history.txt'),
                        auto_suggest=AutoSuggestFromHistory(),
                        completer=SQLCompleter,
                        )
    print(user_input)

#  注意：要在控制台cmd中执行
