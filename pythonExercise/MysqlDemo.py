#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time   :2018/6/27 15:28
# @author :shangxudong
# @File   : MysqlDemo.py
# @Software: PyCharm Community Edition
import MySQLdb

try:
    conn = MySQLdb.connect(
        user="root",
        password="",
        port=3306,
        host="127.0.0.1",
        db="MYSQL",
        charset="utf8"
    )
    cursor = conn.cursor()
    # 当前数据库
    # cursor.execute("select database()")
    # 所有数据库
    # cursor.execute("show databases")
    # 所有表
    # cursor.execute("show tables")
    # sql = "select * from user"
    # cursor.execute(sql)

    cursor.execute("desc user")
    row1 = cursor.fetchall()
    print(row1)
    cursor.execute("select * from user")
    row2 = cursor.fetchall()
    print(row2)
    sql = "insert into user values('localhost', 'shangxd123', '',"\
          " 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y',"\
          " 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y',"\
          " 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', '',"\
          " b'', b'', b'', 0, 0, 0, 0, '', '')"
    cursor.execute(sql)
    cursor.execute("select * from user")
    row3 = cursor.fetchall()
    print(row3)
except MySQLdb.Error:
    print("")
finally:
    conn.close()