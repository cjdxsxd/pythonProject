#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/8/20 17:00
# Author: sxd
# File: read_config.py
# Pycharm: PyCharm
# Contact: 3360048@163.com
import os
import configparser

# 我们需要一个配置文件去控制一些，环境信息，开关，配置文件可以是txt/xml/yaml/properties/ini，
# 一般.properties使用较多在JAVA里，本文是Python系列，我可能会选择ini文件
class read_config():
    '''读取配置文件'''
    def __init__(self):
        self.parser = configparser.ConfigParser()
        file_path =os.path.join(os.path.split(os.path.realpath(__file__))[0], 'config.ini')
        self.parser.read(file_path)

    def get_value(self, section_name, key):
        return self.parser.get(section_name, key)