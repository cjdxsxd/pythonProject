# /usr/bin/env
# _*_ coding: utf-8 _*_

import unittest
import requests


class Interface001(unittest.TestCase):
    """001接口测试案例 """

    def setUp(self):
        pass

    def test_get_noparam(self):
        self.url = "http://baidu.com/"
        r = requests.get(self.url)
        print(r.headers)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
