#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time   :2018/6/20 14:22
# @author :shangxudong
# @File   : xiecheng.py
# @Software: PyCharm Community Edition

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(levelname)s-%(message)s')


def consumer():
    r = ''
    while True:
        m = yield r
        print(r)
        if not m:
            return
        logging.info('consumer is %s' % m)
        r = '200 ok'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n+1
        logging.info('produce is %s'% n)
        s = c.send(n)
        logging.info('produce receive consumer returnvalue is %s'% s)
    c.close()


c = consumer()
logging.info("调用consumer()")
produce(c)