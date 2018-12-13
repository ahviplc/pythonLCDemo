#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import psutil

"""
用Python来编写脚本简化日常的运维工作是Python的一个重要用途。
在Linux下，有许多系统命令可以让我们时刻监控系统运行的状态，如ps，top，free等等。
要获取这些系统信息，Python可以通过subprocess模块调用并获取结果。但这样做显得很麻烦，尤其是要写很多解析代码。

在Python中获取系统信息的另一个好办法是使用psutil这个第三方模块。
顾名思义，psutil = process and system utilities，它不仅可以通过一两行代码实现系统监控，还可以跨平台使用，
支持Linux／UNIX／OSX／Windows等，是系统管理员和运维小伙伴不可或缺的必备模块。
"""

# 获取CPU信息
# 我们先来获取CPU的信息：

print(psutil.cpu_count())  # CPU逻辑数量

print(psutil.cpu_count(logical=False))  # CPU物理核心

# 2说明是双核超线程, 4则是4核非超线程
# 统计CPU的用户／系统／空闲时间：

print(psutil.cpu_times())
# scputimes(user=10963.31, nice=0.0, system=5138.67, idle=356102.45)
# 再实现类似top命令的CPU使用率，每秒刷新一次，累计10次：

for x in range(10):
    print(psutil.cpu_percent(interval=1, percpu=True))

# [14.0, 4.0, 4.0, 4.0]
# [12.0, 3.0, 4.0, 3.0]
# [8.0, 4.0, 3.0, 4.0]
# [12.0, 3.0, 3.0, 3.0]
# [18.8, 5.1, 5.9, 5.0]
# [10.9, 5.0, 4.0, 3.0]
# [12.0, 5.0, 4.0, 5.0]
# [15.0, 5.0, 4.0, 4.0]
# [19.0, 5.0, 5.0, 4.0]
# [9.0, 3.0, 2.0, 3.0]

# 获取内存信息
# 使用psutil获取物理内存和交换内存信息，分别使用：

print(psutil.virtual_memory())
# svmem(total=8589934592, available=2866520064, percent=66.6, used=7201386496, free=216178688, active=3342192640, inactive=2650341376, wired=1208852480)
print(psutil.swap_memory())

# sswap(total=1073741824, used=150732800, free=923009024, percent=14.0, sin=10705981440, sout=40353792)
# 返回的是字节为单位的整数，可以看到，总内存大小是8589934592 = 8 GB，已用7201386496 = 6.7 GB，使用了66.6%。
#
# 而交换区大小是1073741824 = 1 GB。

# 获取磁盘信息
# 可以通过psutil获取磁盘分区、磁盘使用率和磁盘IO信息：

print(psutil.disk_partitions())  # 磁盘分区信息
# [sdiskpart(device='/dev/disk1', mountpoint='/', fstype='hfs', opts='rw,local,rootfs,dovolfs,journaled,multilabel')]
print(psutil.disk_usage('/'))  # 磁盘使用情况
# sdiskusage(total=998982549504, used=390880133120, free=607840272384, percent=39.1)
print(psutil.disk_io_counters())  # 磁盘IO
# sdiskio(read_count=988513, write_count=274457, read_bytes=14856830464, write_bytes=17509420032, read_time=2228966, write_time=1618405)
# 可以看到，磁盘'/'的总容量是998982549504 = 930 GB，使用了39.1%。文件格式是HFS，opts中包含rw表示可读写，journaled表示支持日志。

# 获取网络信息
# psutil可以获取网络接口和网络连接信息：

print(psutil.net_io_counters())  # 获取网络读写字节／包的个数
# snetio(bytes_sent=3885744870, bytes_recv=10357676702, packets_sent=10613069, packets_recv=10423357, errin=0, errout=0, dropin=0, dropout=0)
print(psutil.net_if_addrs())  # 获取网络接口信息
# {
#   'lo0': [snic(family=<AddressFamily.AF_INET: 2>, address='127.0.0.1', netmask='255.0.0.0'), ...],
#   'en1': [snic(family=<AddressFamily.AF_INET: 2>, address='10.0.1.80', netmask='255.255.255.0'), ...],
#   'en0': [...],
#   'en2': [...],
#   'bridge0': [...]
# }
print(psutil.net_if_stats())  # 获取网络接口状态
# {
#   'lo0': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>, speed=0, mtu=16384),
#   'en0': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>, speed=0, mtu=1500),
#   'en1': snicstats(...),
#   'en2': snicstats(...),
#   'bridge0': snicstats(...)
# }
# 要获取当前网络连接信息，使用net_connections()：

print(psutil.net_connections())
# Traceback (most recent call last):
#   ...
# PermissionError: [Errno 1] Operation not permitted
#
# During handling of the above exception, another exception occurred:
#
# Traceback (most recent call last):
#   ...
# psutil.AccessDenied: psutil.AccessDenied (pid=3847)
# 你可能会得到一个AccessDenied错误，原因是psutil获取信息也是要走系统接口，而获取网络连接信息需要root权限，这种情况下，可以退出Python交互环境，用sudo重新启动：


print(psutil.net_connections())
# [
#     sconn(fd=83, family=<AddressFamily.AF_INET6: 30>, type=1, laddr=addr(ip='::127.0.0.1', port=62911), raddr=addr(ip='::127.0.0.1', port=3306), status='ESTABLISHED', pid=3725),
#     sconn(fd=84, family=<AddressFamily.AF_INET6: 30>, type=1, laddr=addr(ip='::127.0.0.1', port=62905), raddr=addr(ip='::127.0.0.1', port=3306), status='ESTABLISHED', pid=3725),
#     sconn(fd=93, family=<AddressFamily.AF_INET6: 30>, type=1, laddr=addr(ip='::', port=8080), raddr=(), status='LISTEN', pid=3725),
#     sconn(fd=103, family=<AddressFamily.AF_INET6: 30>, type=1, laddr=addr(ip='::127.0.0.1', port=62918), raddr=addr(ip='::127.0.0.1', port=3306), status='ESTABLISHED', pid=3725),
#     sconn(fd=105, family=<AddressFamily.AF_INET6: 30>, type=1, ..., pid=3725),
#     sconn(fd=106, family=<AddressFamily.AF_INET6: 30>, type=1, ..., pid=3725),
#     sconn(fd=107, family=<AddressFamily.AF_INET6: 30>, type=1, ..., pid=3725),
#     ...
#     sconn(fd=27, family=<AddressFamily.AF_INET: 2>, type=2, ..., pid=1)
# ]

# 获取进程信息
# 通过psutil可以获取到所有进程的详细信息：
print(
    '----------------------------------------------------------------------------------------------------------------------------------------------')
print(psutil.pids())  # 所有进程ID
# [3865, 3864, 3863, 3856, 3855, 3853, 3776, ..., 45, 44, 1, 0]
p = psutil.Process(11304)  # 获取指定进程ID=4980，其实就是当前Python交互环境
print(p.name())  # 进程名称
# 'python3.6'
print(p.exe())  # 进程exe路径
# '/Users/michael/anaconda3/bin/python3.6'
print(p.cwd())  # 进程工作目录
# '/Users/michael'
print(p.cmdline())  # 进程启动的命令行
# ['python3']
print(p.ppid())  # 父进程ID
# 3765
print(p.parent())  # 父进程
# <psutil.Process(pid=3765, name='bash') at 4503144040>
print(p.children())  # 子进程列表
# []
print(p.status())  # 进程状态
# 'running'
print(p.username())  # 进程用户名
# 'michael'
print(p.create_time())  # 进程创建时间
# 1511052731.120333
# print(p.terminal()) # 进程终端
# '/dev/ttys002'
print(p.cpu_times())  # 进程使用的CPU时间
# pcputimes(user=0.081150144, system=0.053269812, children_user=0.0, children_system=0.0)
print(p.memory_info())  # 进程使用的内存
# pmem(rss=8310784, vms=2481725440, pfaults=3207, pageins=18)
print(p.open_files())  # 进程打开的文件
# []
print(p.connections())  # 进程相关网络连接
# []
print(p.num_threads())  # 进程的线程数量
# 1
print(p.threads())  # 所有线程信息
# [pthread(id=1, user_time=0.090318, system_time=0.062736)]
print(p.environ())  # 进程环境变量
# {'SHELL': '/bin/bash', 'PATH': '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:...', 'PWD': '/Users/michael', 'LANG': 'zh_CN.UTF-8', ...}
p.terminate()  # 结束进程
# Terminated: 15 <-- 自己把自己结束了
# 和获取网络连接类似，获取一个root用户的进程需要root权限，启动Python交互环境或者.py文件时，需要sudo权限。

# psutil还提供了一个test()函数，可以模拟出ps命令的效果：
print(psutil.test())
