#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/10/31 9:54
# Author: sxd
# File: test_commun_thread.py
# Pycharm: PyCharm
# Contact: 3360048@163.com
# 进程间通信

from multiprocessing import Process, Queue
# 进程间数据共享，主要是Queue的作用，一个函数写数据，一个函数读数据

def write(q):
    for i in ['a', 'b', 'c']:
        q.put(i)


def read(q):
    while True:
        value = q.get(True)
        print(value)


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()