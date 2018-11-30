#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/11/19 17:40
# Author: sxd
# File: AsrDemo2.py
# Pycharm: PyCharm
# Contact: 3360048@163.com
import os
import requests
import time
import json
# 判断时间


def get_res_token():
    path = os.getcwd()
    file_path = os.path.join(path, "Asr_Access_Token")
    # print(file_path)
    with open(file_path, 'r') as r:
        file_content = r.read()
    # print(file_content)
    file_to_dic = json.loads(file_content)
    token_time = file_to_dic['expires_in']
    dn = time.time()
    if dn > token_time:
        """再调用一次获取token"""
        pass
    else:
        return file_to_dic['access_token']


if __name__ == '__main__':
    t = get_res_token()
    print(t)

