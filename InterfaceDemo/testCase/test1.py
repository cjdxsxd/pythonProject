#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time   :2018/5/30 14:40
# @author :shangxudong
# @File   : test1.py
# @Software: PyCharm Community Edition

import unittest
import requests

import os
import sys

# print(sys.path)


class TestRequests(unittest.TestCase):
    """测试百度get请求"""

    def setUp(self):
        print("初始化操作")

    def test_get_sou_ye(self):
        self.url = "http://www.baidu.com/"
        self.r = requests.get(self.url)
        self.assertEqual(200, self.r.status_code)
        print(self.r.headers)
        return self.r.status_code

    def test_get_text(self):
        self.url = "http://www.baidu.com/"
        r = requests.get(self.url)
        r.encoding = "utf-8"
        print(r.text)

    def tearDown(self):
        print("测试完成清理工作")

if __name__ == "__main__":
    unittest.main()