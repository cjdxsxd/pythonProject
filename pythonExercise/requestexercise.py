#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/7/23 20:40
# Author: sxd
# File: requestexercise.py
# Pycharm: PyCharm
# Contact: 3360048@163.com

import requests, json

urlg = 'https://api.github.com/events'
urlg2 = "http://httpbin.org/get"
urlg3 = "https://api.github.com/some/endpoint"
urlp = 'http://httpbin.org/post'
urlc = "http://httpbin.org/cookies"
urls = "https://github.com"
data = {"key":"value"}
# multipart-Encoded
files = {"file": open("D:\\baiduAI.txt", 'rb')}
# 设置文件名，头等
files2 = {"file": ('baiduAI.txt', open("D:\\baiduAI.txt", 'rb'))}

payload = {"key1":"value1", "key2":"value2"}
payload1 = {"key1": "value1", "key2":["value2", "value3"]}
cookies = dict(cookies_are="working")
# 元组
payload2 = (("key1", "value1"),("key2", "value2"))
# 定制请求头
headers = {'user-agent': 'my-app/0.0.1'
           # "Host":"shangxudong"
           }
rg = requests.get(url=urlg)
rp = requests.post(url=urlp, data=data)
rpp = requests.head(url=urlp)
rg2 = requests.get(url=urlg2, params=payload)
rg3 = requests.get(url=urlg2, headers=headers)
rg4 = requests.get(url=urlc, cookies=cookies)
rg5 = requests.get(url=urls)

rp1 = requests.post(url=urlp, data= payload1)
rp2 = requests.post(url=urlp, data=payload2)
rp3 = requests.post(url=urlp, json=payload2)
rp4 = requests.post(url=urlp, files=files2)
# print(rp.text)
# print(type(rp.text))
#返回响应头
print(rp.headers)
print(rpp.text)
# print(rp.headers.get("Content-Type"))
# print(rp.headers["Content-Type"])
# print(rp.request.headers)
# print(type(rg2.text), rg2.text)
# print(rg2.url)
# print(rg2.encoding)
# print(rg2.content)
# 定制请求头
# print(rg3.text)
# print(rp4.text)
# print(rg4.text)
# print(rg4.cookies)
# print(requests.utils.dict_from_cookiejar(rg4.cookies))
# for i in rg4.cookies.iteritems():
#      print(i)
#
# print(rg4.history)

# print(rg5.text)