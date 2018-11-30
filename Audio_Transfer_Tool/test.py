#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/11/21 19:27
# Author: sxd
# File: test.py
# Pycharm: PyCharm
# Contact: 3360048@163.com

import ffmpeg
from ffmpeg import audio
import os,sys

import uuid

uuid_str = uuid.uuid4().hex()
tmp_file_name = 'tmpfile_%s.txt' % uuid_str
print (tmp_file_name)