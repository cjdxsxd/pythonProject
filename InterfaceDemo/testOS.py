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