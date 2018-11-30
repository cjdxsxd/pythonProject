#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/8/20 18:48
# Author: sxd
# File: runAPP.py
# Pycharm: PyCharm
# Contact: 3360048@163.com

import threading
from threading import Thread
# 这个只是导入Stock.py模块
from StockMonitor import Stock
from StockMonitor.cfg import read_config
import datetime
import queue
import logging
from StockMonitor.sxdmail import sxd_mail
from apscheduler.schedulers.blocking import BlockingScheduler



logging_level = read_config.read_config()
get_info_level = logging_level.get_value('logging_level', 'info')
print(get_info_level)
logging.basicConfig(level=get_info_level, format='%(asctime)s-%(levelname)s-%(message)s')

q = queue.Queue()
# 使用Stock.py里面的类
stock = Stock.Stock(q)
logging.info("开始运行start_run")


scheduler = BlockingScheduler()


@scheduler.scheduled_job('cron', day_of_week='mon-fri', hour='9-15', minute='*/1')
def exec_send_mail():
    result = stock.start_run()
    sxd_mail.send_mail(result)

scheduler.start()
# q = stock.q
# t = Thread(target=stock.stock_num, args=())
# t.start()
# print("开始打印-------------")
# start_dt = datetime(datetime.date.year,datetime.date.month,datetime.date.day,hour=9, minute=30,second=0)
# stop_dt = datetime(datetime.date.year,datetime.date.month,datetime.date.day,hour=15, minute=00,second=0)
#
# while True:
#     now_dt = datetime.now()
#     if now_dt<start_dt or now_dt>stop_dt:
#         print("stop trade")
#         stock.stop_run()
#         break
#     if not q.empty():
#         print("-------------------------------")
#         cur_price = q.get()
#         high_price = read_config('stock_price','high_price')
#         low_price = read_config('stock_price','low_price')
#         if cur_price>high_price or cur_price<low_price:
#             print(cur_price)
#         elif low_price<cur_price<high_price:
#             print("再15-21之间，当前是：",cur_price)
# t.join()
