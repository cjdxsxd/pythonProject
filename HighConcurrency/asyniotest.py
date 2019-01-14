#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2019/1/10 16:50
# Author: sxd
# File: asyniotest.py
# Pycharm: PyCharm
# Contact: 3360048@163.com
# python 异步非阻塞框架asynio


import requests
import time
import asyncio


# 创建异步函数
async def task_func():
    await asyncio.sleep(1)
    resp = requests.get("http://www.baidu.com/")
    print("2222222222222", time.time(), resp.text)


async def main(loop):
    #  获取全局轮询器
    loop = asyncio.get_event_loop()
    #  在全局轮询器中加入任务
    task = loop.create_task(task_func())
    #  等待2s
    await asyncio.sleep(2)


event_loop = asyncio.get_event_loop()

try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()

