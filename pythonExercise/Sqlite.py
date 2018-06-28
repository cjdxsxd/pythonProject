#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time   :2018/6/7 16:38
# @author :shangxudong
# @File   : Sqlite.py
# @Software: PyCharm Community Edition
import sqlite3


conn = sqlite3.connect("test.db")
cursor = conn.cursor()
# cursor.execute("create table sxd(id varchar(20) primary key,name varchar(20))")
cursor.execute('insert into sxd(id,name) values (\'1\',\'sxd\')')
# cursor.close()
# conn.commit()
# conn.close()
cursor.execute('select * from sxd')
values = cursor.fetchone()
print(values)