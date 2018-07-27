#!/user/bin/env
# _*_ coding: utf-8 _*_

import requests
import unittest
import json
import base64


class BaiDuAiGetString(unittest.TestCase):

    def setUp(self):
        # 百度高精度版url接口
        self.url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic'

    def test_string(self):
        self.url2 = "https://aip.baidubce.com/oauth/2.0/token"
        self.data2 = {
            "grant_type": "client_credentials",
            "client_id": "QK5Y35TTCM4f3Cm83D4R4VMg",
            "client_secret": "RN9cVdZ2GIY4foEueqE8DOPqZHhr719X"
        }
        self.token = requests.post(self.url2, data=self.data2)
        self.content = self.token.text
        self.dic = json.loads(self.content)
        self.tokenvalue = self.dic['access_token']
        print(self.tokenvalue)

        file = open("D:\\02python\\youchu.jpg", 'rb')
        self.base64value = base64.b64encode(file.read())
        file.close()

        self.data = {"access_token": self.tokenvalue, "image": self.base64value }

        self.headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        r = requests.post(self.url, headers=self.headers, data=self.data)
        dict = json.loads(r.text)
        print(type(dict))
        print(type(dict['words_result']))
        for x in dict['words_result']:
            for key, value in x.items():
                f = open("D:\\baiduAI789.txt", 'a+')
                f.writelines(value)
                # f.write(value)
                f.close()


if __name__ == '__main__':
    unittest.main()