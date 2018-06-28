#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time   :2018/6/11 10:17
# @author :shangxudong
# @File   : MultiProcess.py
# @Software: PyCharm Community Edition

from multiprocessing import Process
from multiprocessing import Pool
import os
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s-%(filename)s[line:%(lineno)d]-%(levelname)s-%(message)s')

def run_proc(name):
    print("Run chile process %s (%s)." % (name, os.getppid()))

if __name__ == "__main__":
    print("Parent process %s." % (os.getpid()))
    p=Pool(3)
    for i in range(5):
        p.apply_async(run_proc, (i,))
    # p = Process(target=run_proc, args=('test',))
    logging.info("Waiting for all subprocesses done..")
    # print("child process will start")
    # p.start()
    p.close()
    p.join()#d等待子进程结束后，再继续运行
    print("child process end.")
