#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/7/19 9:00
# Author: sxd
# File: BaiDuOCR.py
# Pycharm: PyCharm
# Contact: 3360048@163.com

# 首选要安装baidu-aip ,ocr:Optical Character Recognition

from aip import AipOcr
import json


APP_ID = '11488774'  # 百度AI上的ID和KEY，下同
API_KEY = 'QK5Y35TTCM4f3Cm83D4R4VMg'
SECRECT_KEY = 'RN9cVdZ2GIY4foEueqE8DOPqZHhr719X'

# 创建客户端
client = AipOcr(APP_ID, API_KEY, SECRECT_KEY)

"""读取图片"""
def get_image_content(filepath):
    with open(filepath, 'rb') as f:
        return f.read()


image = get_image_content("D:\\154108134050658621.jpg")


def get_basic_general():
    # 可选参数
    options = {}
    options['language_type']='CHN_ENG'
    # options['detect_language']='true'

    """调用通用文字识别，照片为本地图片"""
    r = client.basicGeneral(image, options)
    print(type(r))
    print(r['words_result'])
    with open("D:\\image\\youchu123.txt", 'a+') as w:
        for text in r['words_result']:
            w.writelines(text.get('words')+'\n')


def get_basic_accurate():
    """调用通用文字识别精确版，照片为本地图片"""
    options = {}
    options['language_type']='CHN_ENG'
    r = client.basicAccurate(image)
    print(r)
    with open("D:\\image\\youchu456.txt", 'a+') as w:
        for text in r['words_result']:
            w.writelines(text.get('words')+'\n')


def get_id_card():
    """读取身份证正面"""
    idCardSide = "front"
    r = client.idcard(image, idCardSide)
    print(r)
    print(r['words_result'])
    for key, value in r['words_result'].items():
        print(key, value)
        with open("D:\\image\\sfz.txt", 'a+') as w:
                w.writelines(value.get('words')+'\n')


def get_bank_card():
    """获取银行卡信息"""
    r = client.bankcard(image)
    print(r.get('result'))
    print(type(r.get('result')))
    str = json.dumps(r.get('result'))
    with open("D:\\image\\card456.txt", 'a+') as w:
        w.write(str)


def get_drive_lisence():
    """获取驾驶证照片信息"""
    r = client.drivingLicense(image)
    print(r)
    for key, value in r['words_result'].items():
        print(key, value)
        with open("D:\\image\\driver.txt", 'a+') as w:
                w.writelines(key+":"+value.get('words')+'\n')


if __name__ == '__main__':
    # get_basic_general()
    get_basic_accurate()
    # get_id_card()
    # get_bank_card()
    # get_drive_lisence()