#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/11/27 13:59
# Author: sxd
# File: test_SSL.py
# Pycharm: PyCharm
# Contact: 3360048@163.com
import requests
import traceback
from urllib3.connectionpool import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# D:\02python\python3.6.5Install\lib\site-packages\urllib3\connectionpool.py:858: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
#   InsecureRequestWarning)

try:
    # verify验证服务器端证书False关闭验证，一般是pem格式，cert是客户端证书
    r = requests.get('https://github.com', verify=False, cert='')
    print(r.text)
except requests.exceptions.SSLError as e:
# 1、返回字符串类型，只给出异常信息，不包括异常信息的类型，如1/0的异常信息
#     print('ssl异常', str(e))
#   2、给出较全的异常信息，包括异常信息的类型，如1/0的异常信息
    print('sslyichang', repr(e))
except Exception as e:
    print('yichang', traceback.print_exc())
    # print('yichang',traceback.format_exc())