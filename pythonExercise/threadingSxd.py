#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time   :2018/6/20 9:30
# @author :shangxudong
# @File   : threading.py
# @Software: PyCharm Community Edition
import threading
from threading import Thread
import logging
import time

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')


def subthreadsxd():
    logging.info('subthread name is %s' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        logging.info('subthread count is %s' % n)
        time.sleep(1)


logging.info('thread %s is running' % threading.current_thread().name)
t = threading.Thread(target=subthreadsxd, name='subthreadsxd')
t.start()
t.join()
logging.info('thread %s is ended' % threading.current_thread().name)