#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time   :2018/6/4 9:47
# @author :shangxudong
# @File   : testDict.py
# @Software: PyCharm Community Edition
import sys
import os
import psutil

d = {"a":1,"b":2,"c":3}


# for key in d:
#     print(key)

# for value in d.values():
#     print(value)

# for key,value in d.items():
#     print(key,value)
#
# print(dir(sys))
# print(sys.__doc__)

# print(os.name)
# print(os.environ)
# print(os.getenv)
# print(os.path.abspath("."))
# print(os.path.join(os.getcwd(),"sxd"))
# print()
# url = os.path.split(os.getcwd())
# print(url[0])
# filepath1 = os.path.join(url[0], 'interfaceDemo')
# filepath = os.path.join(filepath1, 'testCase')
# print(filepath)

print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))
print(psutil.virtual_memory())