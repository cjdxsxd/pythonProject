#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/11/20 10:22
# Author: sxd
# File: Asr_Start.py
# Pycharm: PyCharm
# Contact: 3360048@163.com

import requests
import base64
from BaiDuAI import AsrDemo2
import json
import numpy as np


url = "http://vop.baidu.com/server_api"
headers = {"Content-Type": "application/json"}
tokens = AsrDemo2.get_res_token()
# print(tokens)
with open('D:\\baiduAsrAudio\\16k.pcm', 'rb') as rb:
    file_content = rb.read()
print("读取文件后", file_content)
speechs = base64.b64encode(file_content)
print("解码后", speechs)
str_speechs = str(speechs, 'utf-8')
print(str_speechs)

datas = {
     "format": "amr",
     "rate": 16000,
     "channel": 1,
     "token": tokens,
     "len": 15000,
     "cuid": "fe80::6d6b:6115:62c1:ea26",
     "speech": str_speechs}
json_datas = json.dumps(datas)
print(type(json_datas))
res = requests.post(url, data=json_datas, headers=headers)
print(res.text)