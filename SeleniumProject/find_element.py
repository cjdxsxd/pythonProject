#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/10/29 15:52
# Author: sxd
# File: find_element.py
# Pycharm: PyCharm
# Contact: 3360048@163.com

from selenium import webdriver

url = 'http://www.baidu.com'
driver = webdriver.Chrome()
driver.get(url=url)
