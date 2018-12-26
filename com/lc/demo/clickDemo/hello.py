# -*- coding: utf-8 -*-
import click

"""
hello.py

Version: 1.0
Author: LC
DateTime: 2018年12月26日11:33:54
UpdateTime: None
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""


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
