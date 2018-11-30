#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/8/27 14:49
# Author: sxd
# File: utc.py
# Pycharm: PyCharm
# Contact: 3360048@163.com


# -*- coding: gb2312 -*-
# UTC时间转换，最终得到的都是UTC时间：
# 时间戳（timestamp）   转换->  UTC显示时间（datetime）
# 显示时间（datetime）  转换->  UTC时间戳（timestamp）
# UTC，协调世界时，又称世界统一时间，可以认为是时区为0的时间。

import time
import datetime
import calendar

aDatetime = datetime.datetime(1970, 1, 1, 0, 0, 1)
aTimestamp = 1

# 获取时区时差
print("time.timezone: ", time.timezone)

# 根据自定义时间，获取显示时间（datetime）。
print("datetime: ", aDatetime)
print("timetuple: ", aDatetime.timetuple())
print("time.strptime: ", time.strptime("1970-1-1 0:1:1", "%Y-%m-%d %H:%M:%S"))


# 根据显示时间（datetime），获取UTC时间戳（timestamp）。即：显示时间（datetime） 转换-> 时间戳（timestamp）。
print("calendar.timegm: datetime(%s)->timestamp(%s)" % (aDatetime.timetuple(), calendar.timegm(aDatetime.timetuple())))
dt = time.gmtime(aTimestamp - time.timezone)  # time.mktime转换时间是带时区的，所以需要减掉时区时差
print("time.mktime: datetime(%s)->timestamp(%s)" % (dt, time.mktime(dt)))
