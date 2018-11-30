#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/9/7 10:56
# Author: sxd
# File: testMongodb.py
# Pycharm: PyCharm
# Contact: 3360048@163.com

from pymongo import MongoClient

# 1、连接到mongodb
client = MongoClient("192.168.220.130", 27017)
# 2、创建一个数据库，数据库名称test
db_name = 'test'
db = client[db_name]
# 3、数据库下面创建一个集合文档
collection_set01 = db['set01']
# 4、向这个文档中添加数据
post = {"_id":100, "author":"sxd"}
# collection_set01.save(post)
# 5、获取所有文档名称
col = db.collection_names()
print(col)
#获取第一个文档对象
col_01 = db.get_collection(col[0])
print(col_01)
# 获取文档对象内容
document = col_01.find_one()
print(document)