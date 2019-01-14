#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2019/1/14 9:19
# Author: sxd
# File: aiohttp20190114.py
# Pycharm: PyCharm
# Contact: 3360048@163.com

# requests是同步请求，aiohttp用来发送异步请求
import asyncio
import aiohttp


tasks = []
url = 'http://www.baidu.com/{}'


# async def 定义异步函数
async def get_baidu(url, semaphore):
    # url = "http://www.baidu.com/"
    # 创建Session对象，用session发送请求
    async with semaphore:
        async with aiohttp.ClientSession() as session:
        #async 关键字加在异步操作的前面
            async with session.get(url=url) as response:
            # await 关键字加在需要等待的操作前面
                resp = await response.text()
                print(resp)


# 多个url请求怎么办?将多个请求将get_baidu()包装在asyncio的Future对象中，然后将Future对象列表作为任务传递给事件循环。
# 并发数过大会导致异常ValueError: too many file descriptors in select()，
# linux对打开文件限制数是1024，windows对打开文件限制数是509，超过这个值就会报错，有3种解决办法
# 1、限制并发数量
# 2、使用回调方式
# 3、修改操作系统打开文件数的最大限制，在系统里有个配置文件可以修改默认值
def mutiple_request():
    # 限制并发量500
    semaphore = asyncio.Semaphore(500)
    for i in range(0, 510):
        task = asyncio.ensure_future(get_baidu(url.format(i), semaphore))
        tasks.append(task)
    result = loop.run_until_complete(asyncio.gather(*tasks))


if __name__ == '__main__':
    # 创建轮询器
    loop = asyncio.get_event_loop()
    # 将任务添加到轮询器
    mutiple_request()
    # loop.run_until_complete(asyncio.wait(tasks))