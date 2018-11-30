#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/8/21 17:16
# Author: sxd
# File: LoginPage.py
# Pycharm: PyCharm
# Contact: 3360048@163.com
# 采用页面设计思想
from SeleniumProject import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage(Page.BasePage):
    '''登录页面：1、元素定位 2、操作'''
    username = (By.ID, 'username')
    passwrod = (By.ID, 'password')

    dialogTitle = (By.XPATH, "//")
    cancelButton = (By.XPATH, '//')
    okButton = (By.XPATH, '')

    # def set_username(self,username):
