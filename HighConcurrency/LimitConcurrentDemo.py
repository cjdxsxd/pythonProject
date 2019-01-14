#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2019/1/14 11:22
# Author: sxd
# File: LimitConcurrentDemo.py
# Pycharm: PyCharm
# Contact: 3360048@163.com
import asyncio
import aiohttp


url = 'http://www.baidu.com/'


# 异步函数
async def hello(url, semaphore):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                print(response.status)
                return await response.read()


async def run():
    # 限制并发量500
    semaphore = asyncio.Semaphore(500)
    to_get = [hello(url.format(), semaphore) for _ in range(1000)]
    await asyncio.wait(to_get)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    loop.close()