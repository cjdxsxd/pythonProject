#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/11/13 13:57
# Author: sxd
# File: testcmd.py
# Pycharm: PyCharm
# Contact: 3360048@163.com
import wx
import os
cmd_str = "ping www.baidu.com"
cmd_str2 = "telnet www.baidu.com 180"
res = os.popen(cmd_str2)
# result = os.popen("telnet www.baidu.com",mode='w')
# print("telnet返回结果", res.read())


print(help(wx))