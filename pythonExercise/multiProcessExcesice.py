# /user/bin/env
# _*_ coding: utf-8 _*_
# @date:20180703
# @author:shangxudong

from multiprocessing import Process, Queue
from multiprocessing import Pool
import os,time,random


def subprocess(i):
    print("子进程id", os.getpid())
    print("父进程id", os.getppid())
    print(i)


def write(q):
    print("Process to write: %s" % os.getpid())
    for value in ['A','B', 'C']:
        print("write %s" % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    print("Process to read: %s" % os.getpid())
    while True:
        value = q.get(True)
        print("read %s" % value)


if __name__ == '__main__':

    # print("当前进程id", os.getpid())
    # p = Process(target=subprocess)
    # print("开启进程")
    # p.start()
    # print("等待进程执行完成")
    # p.join()
    # print("进程执行完成。。。。")
    print("pool ..")
    p = Pool(4)
    for i in range(5):
        p.apply_async(subprocess, args=(i,))
    # p.close()
    p.join()
    print("end")
    # q = Queue()
    # pw = Process(target=write, args=(q,))
    # pr = Process(target=read, args=(q,))
    # pw.start()
    # pr.start()
    # pw.join()
    # pr.terminate()
