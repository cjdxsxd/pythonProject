#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/10/31 10:11
# Author: sxd
# File: test_pipe_thread.py
# Pycharm: PyCharm
# Contact: 3360048@163.com

# 进程间通信-Pipe,双向通信
from multiprocessing import Process, Pipe
# pipe同时收和发，是双向操作

def conn1(pipe):
    pipe.send(['123']+['4', '5'])
    rece1 = pipe.recv()
    print(rece1)


def conn2(pipe):
    pipe.send("woshishangxudong")
    rece2 = pipe.recv()
    print(rece2)


if __name__ == '__main__':
    con1, con2 = Pipe()
    p1 = Process(target=conn1, args=(con1,))
    p2 = Process(target=conn2, args=(con2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

