#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/11/27 9:48
# Author: sxd
# File: test_post.py
# Pycharm: PyCharm
# Contact: 3360048@163.com
import requests
import json
# 1、字典data----存在form中
# "form": {
#     "key1": "value1",
#     "key2": "value2"
# }
data = {'key1':"value1", 'key2': "value2"}
# r = requests.post("http://httpbin.org/post", data=data)
# print(r.text)
# 2、元组data----存在form中
# "form": {
#     "key1": [
#         "value1",
#         "value2"
#     ],
#     "key2": "value3"
# }
data1 = (('key1', 'value1'),('key1', 'value2'),('key2', 'value3'))
# r = requests.post("http://httpbin.org/post", data=data1)
# print(r.text)

# 3、参数不是表单而是字符串形式------存在data中
payload = {'key1': 'value1'}
print(type(payload))
data = json.dumps(payload)
print(type(data))
# r = requests.post('http://httpbin.org/post', data=data)
try:
    # timeout设置3的倍数，tcp重传是3s
    r = requests.post('http://httpbin.org/post', json=payload, timeout=3)
    print(r.headers)
except TimeoutError as e:
    print("连接超时", e.strerror)
except ConnectionError:
    print("连接异常")
except Exception as e :
    print("所有异常的终极异常",e.__traceback__, e.__str__())