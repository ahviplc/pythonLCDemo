# -*- coding: utf-8 -*-

"""
click · PyPI
https://pypi.org/project/click/

Python Click 学习笔记 | I sudo X
https://isudox.com/2016/09/03/learning-python-package-click/

click

Version: 1.0
Author: LC
DateTime: 2018年12月26日10:16:13
UpdateTime: None
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""

import click


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)


if __name__ == '__main__':
    hello()


# python clickDemoByLC.py --count=6

# 执行输出
# Your name: LC
# Hello LC!
# Hello LC!
# Hello LC!
# Hello LC!
# Hello LC!
# Hello LC!


# 输出demo样例2：
# python clickDemoByLC.py --count=6 --name='LC2'
# Hello 'LC2'!
# Hello 'LC2'!
# Hello 'LC2'!
# Hello 'LC2'!
# Hello 'LC2'!
# Hello 'LC2'!


# 难猜到控制台的输出结果。除此之外，Click 还悄悄地做了其他的工作，比如帮助选项：
# python clickDemoByLC.py --help

# Usage: clickDemoByLC.py [OPTIONS]
#
#   Simple program that greets NAME for a total of COUNT times.
#
# Options:
#   --count INTEGER  Number of greetings.
#   --name TEXT      The person to greet.
#   --help           Show this message and exit.

# 与hello.py是同一个代码文件

