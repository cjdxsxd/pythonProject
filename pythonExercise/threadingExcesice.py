# /user/bin/env
# _*_ coding: utf-8
# @author: shangxudong
# @date:20180704
import threading,os


# def get_threading():
#     print("sub_thread:%s" % threading.current_thread().name)
#
#
# print("main_thread: %s" % threading.current_thread().name)
# t = threading.Thread(target=get_threading, name='get_threading')
# t.start()
# t.join()

balance = 0
lock = threading.Lock()


def chang_it(n):
    global balance

    balance = balance + n
    balance = balance - n
    print(balance)


def run_thread(i):
    for i in range(1, 10):
        lock.acquire()
        try:
            chang_it(i)
        finally:
            lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
