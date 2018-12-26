from __future__ import print_function
import argparse

"""
argparse_test.py

Version: 1.0
Author: LC
DateTime: 2018年12月26日11:31:20
UpdateTime: None
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""


def _argparse():
    parser = argparse.ArgumentParser(description='A Python-MySQL client')
    parser.add_argument('--host', action='store', dest='host',
                        required=True, help='connect to host')
    parser.add_argument('-u', '--user', action='store', dest='user',
                        required=True, help='user for login')
    parser.add_argument('-p', '--password', action='store',
                        dest='password', required=True, help='password to use when connecting to server')
    parser.add_argument('-P', '--port', action='store', dest='port',
                        default=3306, type=int, help='port number to use for connection or 3306 for default')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')
    return parser.parse_args()


def main():
    parser = _argparse()
    conn_args = dict(host=parser.host, user=parser.user,
                     password=parser.password, port=parser.port)
    print(conn_args)


if __name__ == '__main__':
    main()

# 执行命令：
# python argparse_test.py --help
# python argparse_test.py -h

# usage: argparse_test.py [-h] --host HOST -u USER -p PASSWORD [-P PORT] [-v]
#
# A Python-MySQL client
#
# optional arguments:
#   -h, --help            show this help message and exit
#   --host HOST           connect to host
#   -u USER, --user USER  user for login
#   -p PASSWORD, --password PASSWORD
#                         password to use when connecting to server
#   -P PORT, --port PORT  port number to use for connection or 3306 for default
#   -v, --version         show program's version number and exit

# 执行命令:
# python argparse_test.py --host HOST="localhostLC" -u USER="LC" -p PORT="LCPass"
# {'host': 'HOST=localhostLC', 'user': 'USER=LC', 'password': 'PORT=LCPass', 'port': 3306}

# python argparse_test.py
# usage: argparse_test.py [-h] --host HOST -u USER -p PASSWORD [-P PORT] [-v]
# argparse_test.py: error: the following arguments are required: --host, -u/--user, -p/--password


# 执行命令:
# python argparse_test.py -v
# argparse_test.py 0.1
