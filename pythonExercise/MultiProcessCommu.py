#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time   :2018/6/19 9:46
# @author :shangxudong
# @File   : MultiProcessCommu.py
# @Software: PyCharm Community Edition

from multiprocessing import Process
from multiprocessing import Queue
import os,time,random
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')


def write(q):
    logging.info('Process to wirte:%s' % os.getpid())
    for value in ['K', 'T', 'V']:
        logging.info('put %s to queue' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    logging.info('Process to read:%s' % os.getpid())
    while True:
        value = q.get(True)
        logging.info('get %s from queue' % value)


if __name__ == '__main__':
    logging.info('Process will begin')
    q = Queue()
    w = Process(target=write, args=(q,))
    r = Process(target=read, args=(q,))
    w.start()
    r.start()
    w.join()
    r.terminate()