#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/11/29 9:18
# Author: sxd
# File: test_non_blocking.py
# Pycharm: PyCharm
# Contact: 3360048@163.com

import grequests

# 非阻塞式请求

urls = ['http://www.heroku.com', 'http://python-tablib.org', 'http://httpbin.org']
rs = (grequests.get(u) for u in urls)
rsp = grequests.map(rs)
print(rsp)