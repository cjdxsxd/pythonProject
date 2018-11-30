#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/8/2 11:15
# Author: sxd
# File: webSpider.py
# Pycharm: PyCharm
# Contact: 3360048@163.com
import requests
from bs4 import BeautifulSoup
# 学爬虫重要的是爬取数据的逻辑，逻辑掌握了网站怎么变都不重要啦。
# 静态用request库，动态用PhantomJS
# 1、获取数据
url = "https://unsplash.com"
r = requests.get(url)
# print(r.text)

# 2、生命BeautifulSoup对象,lxml HTML 解析器
soap = BeautifulSoup(r.text, 'lxml')
# 3、find方法查找tag
find = soap.find('img')
print(type(find))
print(find)
# tag name
print(find.name)
# tag ['attribute']
print(find['src'])
# tag.string
print(find.string)

# 4、点号获取tag
print(soap.header)
print(soap.img)
# find_all()
# 搜索当前tag的所有tag子节点，并判断是否符合过滤器的条件。返回值类型是bs4.element.ResultSet。
# 完整的语法：
# find_all( name , attrs , recursive , string , **kwargs )
# find()
# 与find_all()类似，只不过只返回找到的第一个值。返回值类型是bs4.element.Tag。
# 完整语法：
# find( name , attrs , recursive , string , **kwargs )