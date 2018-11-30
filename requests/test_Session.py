#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/11/27 10:53
# Author: sxd
# File: test_Session.py
# Pycharm: PyCharm
# Contact: 3360048@163.com

import requests

url = ''
# 1、夸请求保持cookie,方法级cookie不会垮请求保持
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)

# 2、为请求方法提供缺省数据,通过会话对象属性实现的
# s= requests.Session()
# s.auth = ('usr', 'pass')
# s.headers.update({'key1': 'value1'})
# r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
# print(r.text)

# 3、为会话添加cookie
# s = requests.Session()
# jar = requests.cookies.RequestsCookieJar()
# jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
# jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
# s.cookies = jar
# r = s.get('http://httpbin.org/cookies')
# print(r.text)

# jar = requests.cookies.RequestsCookieJar()
# cook_dict = {'cookie1': 'value1', 'cookie2': 'value2'}
# # s.cookies = requests.utils.add_dict_to_cookiejar(jar, cook_dict)
# s.cookies = requests.utils.cookiejar_from_dict(cook_dict, cookiejar=None, overwrite=True)
# r = s.get('http://httpbin.org/cookies')
# r2 = s.get('http://httpbin.org/headers')
# print(r2.text)
# s.close()

# 4、会话对象做上下文管理器,response对象包含服务器返回所有信息，和request对象
with requests.Session() as s:
    r = s.get('http://www.baidu.com/')
    print(r.request.headers)