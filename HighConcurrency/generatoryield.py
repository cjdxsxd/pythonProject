#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2019/1/10 14:13
# Author: sxd
# File: generatortest.py
# Pycharm: PyCharm
# Contact: 3360048@163.com


# 高并发模型离不开生成器
# yield将函数变成了生成器generator对象,可以通过for循环取值
def func():
    yield 1
    yield 2
    yield 3


# for循环获取generator值
# if __name__ == '__main__':
#     gen = func()
#     print(type(gen))
#     for i in gen:
#         print(i)


# next获取generator值,可以当成暂停，需要的时候，就可以next一次
# if __name__ == '__main__':
#     gen = func()
#     print(next(gen))
#     print(next(gen))
#     print(next(gen))


#除了返回值，还能接收值
def fun2():
    a = yield 1
    print("a:", a)
    b = yield 2
    print("b:", b)
    c = yield 3
    print("c:", c)


if __name__ == '__main__':
    gen = fun2()
    for i in range(4):
        if i == 0:
            print(gen.send(None))
        else:
            try:
                print(gen.send(i))
            except StopIteration as e:
                print("e:", e)
