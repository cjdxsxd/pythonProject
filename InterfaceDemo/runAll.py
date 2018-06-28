#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time   :2018/5/30 14:40
# @author :shangxudong
# @File   : runAll.py
# @Software: PyCharm Community Edition
import unittest
from test1 import TestRequests
import os
import sys
import datetime, time
from HTMLTestRunner import HTMLTestRunner
import sendemail

def test_single_test():
    suit1 = unittest.TestSuite()
    # suit1.addTest(TestRequests("test_get_sou_ye"))
    suit1.addTests([TestRequests("test_get_sou_ye"), TestRequests("test_get_text")])

    # 创建目录
    test_reult = os.path.join(os.getcwd(), "Results")
    # 创建文件
    now = time.strftime('%Y-%m-%d %H-%M-%S')
    file_name = test_reult+"\\"+now+"result.html"


    with open(file_name, 'wb') as f:
        runner = HTMLTestRunner(stream=f, title="标题描述", description="1.使用了那个接口 2.接口注意事项")
        runner.run(suit1)


def test_loader():
    print(os.getcwd())
    test_dir = os.getcwd()+"/testCase"
    print(test_dir)
    driver = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
    runner2 = unittest.TextTestRunner()
    runner2.run(driver)


if __name__ == "__main__":
    test_single_test()
    sendemail.send_email()