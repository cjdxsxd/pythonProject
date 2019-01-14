#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2019/1/14 11:45
# Author: sxd
# File: MutipleRequest.py
# Pycharm: PyCharm
# Contact: 3360048@163.com

# 如果我们需要请求多个URL该怎么办呢，同步的做法访问多个URL只需要加个for循环就可以了。
# 但异步的实现方式并没那么容易，在之前的基础上需要将hello()包装在asyncio的Future对象中，
# 然后将Future对象列表作为任务传递给事件循环。

import asyncio
import aiohttp


tasks = []
url = 'http://www.baidu.com/{}'
# 异步函数
async def hello(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            await response.text()


def run():
    for i in range(5):
        task = asyncio.ensure_future(hello(url.format(i)))
        tasks.append(task)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    run()
    loop.run_until_complete(asyncio.wait(tasks))


