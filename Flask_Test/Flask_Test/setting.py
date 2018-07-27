#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/7/12 17:04
# Author: sxd
# File: setting
# Pycharm: PyCharm
# Contact: 3360048@163.com

# 开启调试模式
DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# mysql数据库连接信息,这里改为自己的账号
SQLALCHEMY_DATABASE_URI = "jdbc:mysql://localhost:3306/mysql"