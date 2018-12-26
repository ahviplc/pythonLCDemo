from __future__ import print_function
import argparse

"""
test_argparse.py

Version: 1.0
Author: LC
DateTime: 2018年12月26日11:32:02
UpdateTime: None
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""

def _argparse():
    parser = argparse.ArgumentParser(description="This is description")
    parser.add_argument('--host', action='store',
                        dest='server', default="localhost", help='connect to host')
    parser.add_argument('-t', action='store_true',
                        default=False, dest='boolean_switch', help='Set a switch to true')
    return parser.parse_args()


def main():
    parser = _argparse()
    print(parser)
    print('host =', parser.server)
    print('boolean_switch=', parser.boolean_switch)


if __name__ == '__main__':
    main()

# 执行命令:
# python test_argparse.py -h

# usage: test_argparse.py [-h] [--host SERVER] [-t]
#
# This is description
#
# optional arguments:
#   -h, --help     show this help message and exit
#   --host SERVER  connect to host
#   -t             Set a switch to true


# 执行命令:
# python test_argparse.py --host="localhostLC2"

# Namespace(boolean_switch=False, server='localhostLC2')
# host = localhostLC2
# boolean_switch= False

# 执行命令:
# python test_argparse.py -t  --host="localhostLC2"

# Namespace(boolean_switch=True, server='localhostLC2')
# host = localhostLC2
# boolean_switch= True
