#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/7/28 17:29
# Author: sxd
# File: ParserXml2.py
# Pycharm: PyCharm
# Contact: 3360048@163.com

# 解析xml第二种方法cElementTree，C语言快一点
import os, sys
try:
    import xml.etree.cElementTree as ET
except:
    import xml.etree.ElementTree as ET

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

# 遍历xml
def traverseXml(element):
    if (len(element)) > 0:
        for child in element:
            print("child tag", "------", child)
            traverseXml(child)


if __name__ == '__main__':
    try:
        tree = ET.parse(xmlrealpath)
        print("tree type:", type(tree))
        # 获取根节点
        root = tree.getroot()
        # print("根节点:", root, root.attrib)
        # for child in root:
            # print("child tag", "------", type(child.attrib), child.attrib)
        # print(traverseXml(root))
        for child in root:
            print(child)
            for children in child:
                print(children.tag, children.attrib)

        childlist = root[0].findall("personDebtPayingAbilityEvaluate")
        print(childlist)


        for childs in root.iter("personDebtPayingAbilityEvaluate"):
            print(childs)
            print(childs[0].text)

    except Exception as e:
        print("parser xml fail")
        sys.exit()
