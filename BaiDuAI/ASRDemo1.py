#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/11/19 16:15
# Author: sxd
# File: ASRDemo1.py
# Pycharm: PyCharm
# Contact: 3360048@163.com
# 百度ASR语音识别
import requests
import time
import json
import os


def get_token():
    print(time.time())
    # application/x-www-form-urlencoded
    API_Key = "eyyPk3i1QaqCgYSgrMGZIff5"
    Secret_Key = "H0w2BKKoM8UkL9ZtWPhlC3vAoz9Z3Apa"
    url = "https://aip.baidubce.com/oauth/2.0/token"
    payload = {"grant_type": "client_credentials", "client_id": API_Key, "client_secret": Secret_Key}
    # 返回string
    # headers = {"Content-Type": "application/x-www-form-urlencoded"}
    # 返回json
    headers = {"Content-Type": "application/json"}
    asr_token = requests.post(url, data=payload, headers=headers)
    print(asr_token.text)
    print(type(asr_token.text))
    # 将返回str转化成json，字典
    str_to_json = json.loads(asr_token.text)
    expires_in = str_to_json['expires_in']
    expires_in2 = time.time()+expires_in
    str_to_json['expires_in'] = expires_in2
    json_to_str = json.dumps(str_to_json)
    print(json_to_str)
    path = os.getcwd()
    token_file = os.path.join(path, "Asr_Access_Token")
    with open(token_file, 'w') as w:
        w.write(json_to_str)
