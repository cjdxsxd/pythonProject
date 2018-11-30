#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/11/28 13:52
# Author: sxd
# File: test_Cookie.py
# Pycharm: PyCharm
# Contact: 3360048@163.com
import requests

# 1、响应cookie
# url = 'http://example.com/some/cookie/setting/url'
# r = requests.get(url=url)
# # 字典与RequestsCookieJar之间的转换
# c = requests.utils.dict_from_cookiejar(r.cookies)
# print(c, type(c))

# 2、请求cookie,cookies是字典类型
# url = 'http://httpbin.org/cookies'
# cookies = {'cookie1': 'value1'}
# r = requests.get(url, cookies=cookies)
# print(r.text)

# 3、请求cookie，以RequestsCookieJar组织
jar = requests.cookies.RequestsCookieJar()
jar.set('cookie1', 'value1', domain='www.httpbin.org', path='/cookies')
jar.set('cookie2', 'value2', domain='www.baidu.com', path='/cookies')
url = 'http://www.httpbin.org/cookies'
r = requests.get(url, cookies=jar)
print(r.text)

