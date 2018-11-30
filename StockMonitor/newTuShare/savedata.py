#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/10/24 10:33
# Author: sxd
# File: savedata.py
# Pycharm: PyCharm
# Contact: 3360048@163.com
from  StockMonitor.newTuShare.ListStock import tushare
import pandas as pd
from sqlalchemy import create_engine
data = tushare().get_list_stock()
print(type(data))

# 第一个参数thedataframe是需要导入的pd dataframe,
#
# 第二个参数tablename是将导入的数据库中的表名
#
# 第三个参数yconnect是启动数据库的接口，pd 1.9以后的版本，除了sqllite，均需要通过sqlalchemy来设置
#
# 第四个参数databasename是将导入的数据库名字
#
# 第五个参数if_exists='append'的意思是，如果表tablename存在，则将数据添加到这个表的后面

yconnect = create_engine('mysql+mysqldb://root@localhost:3306/mysql?charset=utf8')
# mysql是要用的数据库
#
# mysqldb是需要用的接口程序
#
# root是数据库账户
#
# password是数据库密码
#
# localhost是数据库所在服务器的地址，这里是本机
#
# 3306是mysql占用的端口
#
# elonuse是数据库的名字
#
# charset=utf8是设置数据库的编码方式，这样可以防止latin字符不识别而报错
pd.io.sql.to_sql(data,'tushare', yconnect, schema='mysql', if_exists='append')