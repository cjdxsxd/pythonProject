# _*_ coding: utf-8 _*_
# DATE: 2019/1/11 14:58
# Author: sxd
# File: aiohttptest.py
# Pycharm: PyCharm
# Contact: 3360048@163.com
import aiohttp
import asyncio
# It is a SyntaxError to use async with outside of an async def function.


async def client_session():
    async with aiohttp.ClientSession() as session:
        # async with session.get("http://httpbin.org/get") as resp:
        #     print(resp.status)
        #     print(await resp.text())
        # 传递参数字典dict
        # params = {"key1": "value1", "key2": "value2"}
        # 为同一个key增加多个值,列表list和tuple
        parms = [("key1", "value1"), ("key1", "value2")]
        async with session.get('http://httpbin.org/get') as resp:
            # expect = "http://httpbin.org/get?key1=value1&key2=value2"
            print(resp.url)
            # assert str(resp.url) == expect
            print(await resp.content.read(100))

# 轮询器
loop = asyncio.get_event_loop()
#知道方法运行完
loop.run_until_complete(client_session())






