#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/7/27 15:58
# Author: sxd
# File: EncodingDemo.py
# Pycharm: PyCharm
# Contact: 3360048@163.com

import sys
import chardet

# 打开py文件过程：读取文件到内存，解释执行内容
# 1、有一点需要清楚的是，当python要做编码转换的时候，会借助于内部的编码，转换过程是这样的：
# 原有编码 -> 内部编码 -> 目的编码
# 2、如果输出的值为65535, 那么就是UCS - 2, 如果输出是1114111就是UCS - 4编码
# 3、我们要认识到一点：当一个字符串转换为内部编码后，它就不是str类型了！它是unicode类型：
print(sys.maxunicode)
print(sys.getdefaultencoding())
# 1114111
# 65536

name = '张三'
# print("字符串编码是：", type(name))
uni_name = name.encode()
gbk_name = uni_name.decode('utf-8')
# print("字符串encode后变成字节",type(uni_name))
# print("字节解码后变成字符串", type(gbk_name))



name2 = u'李四'
print(type(name2))
s = name2.encode('utf-8')
print("encode字符串", type(s), s)
s2 = s.decode("utf-8")
print(s2)

isinstance(name2, str)