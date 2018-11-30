#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/8/20 16:26
# Author: sxd
# File: Stock.py
# Pycharm: PyCharm
# Contact: 3360048@163.com
import time
import tushare as ts
import datetime
from StockMonitor.sxdmail import sxd_mail


class Stock():
    '''获取股票实时信息'''
    def __init__(self, q, stock_num='603712'):
        self.q = q
        self.stock_num = stock_num
        self._terminal = True

    def query_stock_real_price(self):
        df = ts.get_realtime_quotes(self.stock_num)
        # print(df)
        df = df[['price','time']]
        price = df['price'].values[0]
        time = df['time'].values[0]
        return price,time

    def get_kline_date(self, ktype='ma5'):
        today = datetime.now().strftime('%Y-%m-%d')
        df = ts.get_hist_data(self.stock_num, start='2018-08-17', end='2018-08-21')
        return (df[[ktype]])


    def start_run(self):
        while self._terminal:
            p, t = self.query_stock_real_price()
            subject = '当前时间：{}, 七一二价格：{}'.format(t,p)
            # print('-----------------------------')
            # print('当前时间：{}:七一二价格：{}'.format(t,p))

            real_price = float(p)
            self.q.put(real_price)
            time.sleep(3)
            return subject


    def stop_run(self):
        self._terminal = False




