#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time   :2018/6/25 14:25
# @author :shangxudong
# @File   : testOS.py
# @Software: PyCharm Community Edition

import os
import time
import datetime
import sys
import random
from functools import reduce
import json


test = os.getcwd()
# print(test)
# print(os.path.join(test,"testResult"))
# print(os.times())
# print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+".html")
# now = time.strftime('%Y-%m-%d_%H-%M-%S')
# file_name = "D:\\"+'test'+now + ".html"
# with open(file_name,'wb'):
#     print('sxd')
#
#
msg_to = ["469820049@qq.com", "cjdxsxd@gmail.com"]
reports = os.path.join(os.getcwd(),"Results")
lists = os.listdir(reports)
lists.sort(key=lambda fn: os.path.getmtime(reports+"\\"+fn))
file_new = os.path.join(reports, lists[-1])
print(file_new)
print(','.join(msg_to))
print(type(msg_to))

str = b'sxd'
print(type(str))


print(random.randint(10, 15))


print(os.path.abspath(__file__))
print(os.path.split(os.path.abspath(__file__))[0])
print(os.getcwd())


list_sxd = ['s', 'x', 'd']
tuple_sxd = ['s', 'x', 'd']
list_sxd.append('sxd')
list_sxd.insert(0, 'sxdinsert')
list_sxd.pop()
list_sxd.pop(0)
list_sxd[0]='sxd'
print(list_sxd)
print(tuple_sxd[-1])
print(list_sxd[0:2])
print(list_sxd[-2:])
print(list_sxd[-2:-1])

print(random.random())

#1个参数
g = lambda x: x+3
print(g(3))
#2个参数
g2 = lambda x, y: x+y
print(g2(2, 3))
#0个参数
g3 = lambda: 2
print(g3())

print(list(range(6)))

print(reduce(lambda x,y: x+y, list(range(1,6))))


def action(x):
    return lambda y: x+y


f = action(2)
print(f(3))


print(os.path.basename("D:\\02python\\youzhengimage.jpg"))

dicts = {"name": "123", "age": "12"}
print(type(dicts))
dicts2str = json.dumps(dicts, indent=4)
print(dicts2str)
print(type(dicts2str))

str2dicts = json.loads(dicts2str)
print(type(str2dicts))
print(str2dicts)


lists = [1,2,3,4,5]
list2json = json.dumps(lists)
print(type(list2json))

x, y =[1,2]
print(x)