#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/8/28 15:19
# Author: sxd
# File: testString.py
# Pycharm: PyCharm
# Contact: 3360048@163.com
import codecs
import sys
import json
import datetime
import re
file_path = "D:\\sxd.txt"

# f = open(file_path, 'r', encoding='gbk')
# print(f)
# s=f.read()
# print(s)


# print('中文'.encode('gbk'))
# print('中文'.encode('utf-8'))

# d = {'a': 1, 'b': 2}
# fp = open('D:\\dump.txt','w')
# dump = json.dump(d, fp)
# dumps = json.dumps(d)
# print(dumps, type(dumps))


#
# rp = open('D:\\dump.txt', 'r')
# dumpr = json.load(rp)
# print(dumpr,type(dumpr))

# str = 'format字符串{},{}'.format('a','b')
# print(str)
#
# try:
#     f = open("D:\\1212123.txt", 'r')
#     f.read()
# except Exception as e:
#     tb = None
#     raise e.with_traceback(tb)

print(datetime.datetime.month)
print(datetime.time.hour)