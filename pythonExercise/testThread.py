#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/10/31 8:53
# Author: sxd
# File: testThread.py
# Pycharm: PyCharm
# Contact: 3360048@163.com
# multiprocessin模块，导入Process类
from multiprocessing import Process
import os

# 1、结构是什么？multiProcess模块-》引入Process->创建进程对象Process(target=函数名子进程函数,args=())->p.start()启动子进程->p.join()等待子进程解释。
# 2、这个例子还能怎么拓展？

# 多进程

# 子进程代码


def run_proc(name):
    print("run child process %s  (%s)" % (name, os.getpid()))


if __name__ == '__main__':
    print("parent process is %s" % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print("child process will start")
    p.start()
    # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    p.join()
    print('child process end')
