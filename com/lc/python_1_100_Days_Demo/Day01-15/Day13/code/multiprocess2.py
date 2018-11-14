"""

实现进程间的通信

Version: 0.1
Author: LC
DateTime:2018年11月14日16:10:22
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html


"""

import multiprocessing
import os


def sub_task(queue):
	print('子进程进程号:', os.getpid())
	counter = 0
	while counter < 1000:
		queue.put('Pong')
		counter += 1


if __name__ == '__main__':
	print('当前进程号:', os.getpid())
	queue = multiprocessing.Queue()
	p = multiprocessing.Process(target=sub_task, args=(queue,))
	p.start()
	counter = 0
	while counter < 1000:
		queue.put('Ping')
		counter += 1
	p.join()
	print('子任务已经完成.')
	for _ in range(2000):
		print(queue.get(), end='')
