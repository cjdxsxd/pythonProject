#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2019/1/14 14:39
# Author: sxd
# File: gatherresult.py
# Pycharm: PyCharm
# Contact: 3360048@163.com


import asyncio
import aiohttp


url = 'http://wwwbaidu.com/{}'
tasks = []


# 测试收集结果
async def hello(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            resp = await response.text()
            return resp


def run():
    for i in range(5):
        task = asyncio.ensure_future(hello(url.format(i)))
        tasks.append(task)
    result = loop.run_until_complete(asyncio.gather(*tasks))
    print(result)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    run()