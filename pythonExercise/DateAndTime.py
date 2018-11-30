#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/8/22 9:08
# Author: sxd
# File: DateAndTime.py
# Pycharm: PyCharm
# Contact: 3360048@163.com
import  time
import datetime
# 时间戳
start = time.time()
print("start:", start)
# 时间格式化
print(time.strftime('%Y-%m-%d %H:%M:%S'))
time.sleep(1)
# 当前时间
print("datetime：", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
end = time.time()
print("end:", end)
print(end-start)