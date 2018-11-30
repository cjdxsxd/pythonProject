#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/11/1 15:25
# Author: sxd
# File: test_yield.py
# Pycharm: PyCharm
# Contact: 3360048@163.com

# //单独yield将函数变成一个生成器对象
# 每次执行到yield，就返回一个值
# def gen():
#     for x in['1', '2', '3']:
#         yield x
#         print('123')


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)
