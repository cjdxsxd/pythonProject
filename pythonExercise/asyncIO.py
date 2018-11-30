#!/usr/bin/env
# _*_ coding: utf-8 _*_

import asyncio
import time
import aiohttp

now = time.time()


async def wget(host):
    print('wget %s' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = 'get / http1.1 host:%s '% host
    print(header)
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
        writer.close()


loop = asyncio.get_event_loop()
task = [wget(host) for host in ['www.baidu.com','www.sohu.com']]
loop.run_until_complete(asyncio.wait(task))
loop.close()