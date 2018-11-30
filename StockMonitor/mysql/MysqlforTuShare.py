#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/10/24 9:10
# Author: sxd
# File: MysqlforTuShare.py
# Pycharm: PyCharm
# Contact: 3360048@163.com

import MySQLdb


try:
    # 连接数据库
    conn = MySQLdb.connect(
        user='root',
        password='',
        port=3306,
        host='127.0.0.1',
        db='MYSQL',
        charset='utf8'
    )
    # 获取游标
    cursor = conn.cursor()

#    创建一个表
    sql1 = 'create table tushare(tu_id int not null AUTO_INCREMENT, \
          ts_code varchar(100),\
          symbol varchar(100), \
          name varchar(100), \
          area varchar(100),\
          industry varchar(100),\
          list_date DATE,\
           PRIMARY KEY (tu_id));'
    print("1")
    # cursor.execute(sql1)
    # data2 = cursor.fetchall()
    # 执行显示所有表
    # sql = 'show tables'
    # sql = 'desc tushare'
    print("12")
    # sql = 'alter table tushare add COLUMN `index` varchar(20)'
    # sql = 'select * from tushare'
    # sql = 'truncate table tushare'
    # sql = 'alter table tushare DEFAULT CHARACTER SET utf8 ,\
    #       modify `name` varchar(100) CHARACTER SET utf8,\
    #       modify `area`  varchar(100) CHARACTER SET utf8,\
    #       modify `industry`  varchar(100) CHARACTER SET utf8'
    sql = 'select * from tushare'
    cursor.execute(sql)

    #     查看结果
    # data = cursor.fetchone()
    data = cursor.fetchmany(20)
    print(data)

except MySQLdb.Error:
    print("exception")
finally:
    conn.close()
