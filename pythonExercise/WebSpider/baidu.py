#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/8/2 14:33
# Author: sxd
# File: baidu.py
# Pycharm: PyCharm
# Contact: 3360048@163.com

import requests
from bs4 import BeautifulSoup
import re

baidu_url = "http://www.58pic.com/newpic/28929979.html"
headers = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"

r = requests.get(baidu_url, headers)
r.encoding = 'utf-8'
# print(r.text)
# print(r.encoding)

soup = BeautifulSoup(r.text, 'lxml')
a_list = soup.find_all('img', "origin_image zh-lightbox-thumb",src=re.compile(r'.jpg$'))
href = ''
for a in a_list:
    print(a)
    print(a.get("href"))
    print(a.string)
    if a.get("href").startswith("http:"):
        href += a.get("href")
        href += '\n'

with open("D:\\href.txt", 'w') as f:
    f.write(href)