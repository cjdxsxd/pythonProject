#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/10/24 8:58
# Author: sxd
# File: ListStock.py
# Pycharm: PyCharm
# Contact: 3360048@163.com
# 股票列表接口
import tushare as ts


class tushare:

    def __init__(self):
        pass


    def get_list_stock(self):

         # 注册网站https://tushare.pro，个人中心有token
        self.pro = ts.pro_api('359b2c1b3b9f2855816953fd109ad9635ba55db78515bc2f8ca4951f')
# 接口说明https://tushare.pro/document/2?doc_id=25
        data = self.pro.query('stock_basic', exchange_id='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
        print(data)
        return data



if __name__ == '__main__':
    tushare().get_list_stock()
