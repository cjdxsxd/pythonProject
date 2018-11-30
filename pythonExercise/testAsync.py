#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/11/6 9:37
# Author: sxd
# File: testAsync.py
# Pycharm: PyCharm
# Contact: 3360048@163.com

import asyncio
import threading


async def hello():
    print("hello, thread is %s" % threading.current_thread())
    await asyncio.sleep(1)
    print("hello,again %s" % threading.current_thread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
