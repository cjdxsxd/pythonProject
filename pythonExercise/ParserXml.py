#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/7/28 16:07
# Author: sxd
# File: ParserXml.py
# Pycharm: PyCharm
# Contact: 3360048@163.com

# 解析xml练习
# 一个 DOM 的解析器在解析一个XML文档时，一次性读取整个文档，把文档中所有元素保存在内存中的一个树结构里，之后你可以利用DOM 提供的不同的函数来读取或修改文档的内容和结构，
# 也可以把修改过的内容写入xml文件。python中用xml.dom.minidom来解析xml文件。

import xml.dom.minidom as xmldom
import os
from xml.dom.minidom import Element

# 当前文件路径(\)
xmlpath = os.path.abspath(__file__)
print(xmlpath)
# 当前目录路径（/）
xmldir = os.path.dirname(__file__)
print(xmldir)
# 分解url目录和文件(\)
xmlsplit = os.path.split(xmlpath)
print(xmlsplit[0])
# 添加文件到目录路径
xmlrealpath = os.path.join(xmlsplit[0], "changzhainengli.xml")
print(xmlrealpath)


# 1、解析xml文件，得到document对象
domobj = xmldom.parse(xmlrealpath)
print("获得document对象：", domobj, type(domobj))

# 2、得到元素对象根节点
elementobj = domobj.documentElement
print("根节点元素对象：", elementobj, type(elementobj))

batNo = elementobj.getAttribute("batNo")
print("根节点属性：", batNo)

# 3、获取第一个子标签
subElementObj = elementobj.getElementsByTagName("cisReport")
print("子节点元素对象：", subElementObj, type(subElementObj))
print("子标签个数：", len(subElementObj))

# 4、获取标签属性
hasSystemError = subElementObj[0].getAttribute("hasSystemError")
print(hasSystemError)

# 5、获取第一个子标签的节点列表
childList = subElementObj[0].childNodes
# print(childList)
childList2 = []
for i in childList:
    """instance函数第一个参数是变量，第二个参数是类型"""
    if isinstance(i, Element):
        print("第一个子节点下的节点是：", i)
        childList2.append(i)


queryConditions = subElementObj[0].getElementsByTagName("queryConditions")
print(queryConditions)

personDebtPayingAbilityEvaluate = childList2[1]
print("treatResult是：", personDebtPayingAbilityEvaluate.getAttribute("treatResult"))