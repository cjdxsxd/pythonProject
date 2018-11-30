#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 09:37:38 2018
利用百度api实现图片文本识别
@author: XnCSD
"""

import glob
from os import path
import os
from aip import AipOcr
from PIL import Image

# def convertimg(picfile, outdir):
#     '''调整图片大小，对于过大的图片进行压缩
#     picfile:    图片路径
#     outdir：    图片输出路径
#     '''
#     img = Image.open(picfile)
#     width, height = img.size
#     while(width*height > 4000000):  # 该数值压缩后的图片大约 两百多k
#         width = width // 2
#         height = height // 2
#     new_img=img.resize((width//odd,height//odd),Image.BILINEAR)
#     new_img.save(path.join(outdir,os.path.basename(picfile)))


def baiduOCR(picfile, outfile):
    """利用百度api识别文本，并保存提取的文字
    picfile:    图片文件名
    outfile:    输出文件
    """
    # filename = path.basename(picfile)

    APP_ID = '11488774' # 刚才获取的 ID，下同
    API_KEY = 'QK5Y35TTCM4f3Cm83D4R4VMg'
    SECRECT_KEY = 'RN9cVdZ2GIY4foEueqE8DOPqZHhr719X'
    client = AipOcr(APP_ID, API_KEY, SECRECT_KEY)
    # client.setConnectionTimeoutInMillis()

    i = open(picfile, 'rb')
    img = i.read()
    options = {}
    options["language_type"] = "ENG"
    # print("正在识别图片：\t" + filename)
    # message = client.basicGeneral(img)   # 通用文字识别，每天 50 000 次免费
    message = client.basicAccurate(img, options)   # 通用文字高精度识别，每天 800 次免费

    print("识别成功！")
    i.close();

    with open(outfile, 'a+') as fo:
        fo.writelines("+" * 60 + '\n')
        # fo.writelines("识别图片：\t" + filename + "\n" * 2)
        # fo.writelines("文本内容：\n")
        # 输出文本内容
        for text in message.get('words_result'):
            fo.writelines(text.get('words') + '\n')
        fo.writelines('\n'*2)
    print("文本导出成功！")



if __name__ == "__main__":

    outfile = 'D:\\exports123.txt'
    # if path.exists(outfile):
    #     os.remove(outfile)
    # 首先对过大的图片进行压缩，以提高识别速度，将压缩的图片保存与临时文件夹中
    # for picfile in glob.glob("picture/*"):
    #     convertimg(picfile, outdir)
    # print("图片识别...")
    for pic in glob.glob("D:\\154108134050658621.jpg"):
    # picfile = 'D:\\02python\\youzhengimage.jpg'
        print(pic)
        baiduOCR(pic, outfile)
