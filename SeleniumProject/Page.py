#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/8/21 11:11
# Author: sxd
# File: Page.py
# Pycharm: PyCharm
# Contact: 3360048@163.com
import selenium


class BasePage():
    '''浏览器驱动基类'''

    def __init__(self, driver):
        self.driver = driver
