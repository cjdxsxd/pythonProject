#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/8/22 15:07
# Author: sxd
# File: tusharetest.py
# Pycharm: PyCharm
# Contact: 3360048@163.com

import tushare as ts

# print(ts.get_hs300s())
# print(type(ts.get_sz50s()))

df = ts.get_hs300s()
code, name = df['code'], df['name']
print(code,name)