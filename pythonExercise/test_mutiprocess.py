#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/10/31 9:15
# Author: sxd
# File: test_mutiprocess.py
# Pycharm: PyCharm
# Contact: 3360048@163.com

# 多进程
import os
# 批量进程引入进程池概念
from multiprocessing import Pool
# 1、结构是什么？multiprocessing 模块-》引入Pool进程池-》创建进程池大小Pool(4)->创建for循环来并发进程，p.apply_async(函数名，args=)
# 2、怎么应用到项目中？

def multi_process(name):
    print("task name is %s %s" % (name, os.getpid()))


if __name__ == '__main__':
    p = Pool(4)
    for i in range(1,5):
        p.apply_async(func=multi_process, args=(i,))

    print("等待所有进程完成")
    # 禁止添加新进程
    p.close()
    # 等待子进程执行完成
    p.join()
    print("所有进程完成")