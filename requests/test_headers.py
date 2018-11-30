#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/11/28 17:53
# Author: sxd
# File: test_headers.py
# Pycharm: PyCharm
# Contact: 3360048@163.com
import collections
import requests
from collections import OrderedDict
import json

url = 'http://www.baidu.com/'
# 1、提交的数据data按照 key1=value1&key2=value2 组织，2、key和value都进行了URL转码
# headers = {'Content-Type': 'application/x-www-form-urlencoded'}
# payload = {'key1': 'value1', 'key2': 'value2'}
# res = requests.post(url, headers=headers, data=payload)
# print(res.text)

# 2、用来告诉服务端消息主体是序列化后的 JSON 字符串
# post有两种参数，data和json,json参数会自动将字典类型的对象转换为json格式,data默认是字典类型
headers = {'Content-Type': 'application/json'}
payload = {'key1': 'value1', 'key2': 'value2'}
print(type(json.dumps(payload)))
# re = requests.post(url, data=json.dumps(payload), headers=headers)
re = requests.post(url, json=payload, headers=headers)
print(re.request.headers)




