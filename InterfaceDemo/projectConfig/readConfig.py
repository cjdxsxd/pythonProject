#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time   :2018/6/26 16:41
# @author :shangxudong
# @File   : readConfig.py
# @Software: PyCharm Community Edition
import configparser
import os


def get_item(sections, keys):
    cfg_path = os.path.join(os.getcwd(),"mainconfig.ini")
    conf = configparser.ConfigParser()
    conf.read(cfg_path,encoding='utf-8')
    return conf.get(sections, keys)


if __name__ == "__main__":
    s = get_item("mail_163", "To")
    str = s[1:-1]
    print(str)