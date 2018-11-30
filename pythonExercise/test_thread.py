#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/10/31 10:45
# Author: sxd
# File: test_thread.py
# Pycharm: PyCharm
# Contact: 3360048@163.com

# 多线程
import  threading
from threading import Thread


def sub_thread():
    print("thread name is %s" % threading.current_thread().name)


if __name__ == '__main__':
    t = Thread(target=sub_thread, name='sub_thread')
    t.start()
    t.join()
