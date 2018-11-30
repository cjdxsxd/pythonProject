#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/11/12 10:14
# Author: sxd
# File: testMockDemo.py
# Pycharm: PyCharm
# Contact: 3360048@163.com

from unittest import mock
import unittest
from testCase import test1


class  Mock_Demo(unittest.TestCase):

    def test_count(self):
        get_baidu = test1.TestRequests()
        # 　当side_effect为设置时（默认default），return_value设置的值会返回当作count.add方法的返回值，当side_effect被设置值时，return_value不起作用（side_effect参数和return_value是相反的，它给mock分配了可替换的结果，覆盖了return_value。简单的说，side_effect存在时一个模拟工厂调用将返回side_effect值，而不是return_value）
        # 　　上面代码，将side_effect的值设为count.add，此时count.add并未调用。
        get_baidu.test_get_sou_ye = mock.Mock(return_value="200 ok")
        result = get_baidu.test_get_sou_ye() #调用真实方法
        print(result)
        self.assertEqual(result, "200 ok")


if __name__ == '__main__':
     unittest.main()