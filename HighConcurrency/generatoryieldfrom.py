#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2019/1/10 15:15
# Author: sxd
# File: generatoryieldfrom.py
# Pycharm: PyCharm
# Contact: 3360048@163.com


def first_gen():
    a = yield 1
    print("a:", a)
    b = yield 2
    print("b:", b)
    c = yield 3
    print("c:", c)
    return 4


def second_gen():
    gen = first_gen()
    ret = yield from gen
    print("ret:", ret)
    return "middle Exception"


def main():
    gen2 = second_gen()
    for i in range(4):
        if i == 0:
            bb = gen2.send(None)
            print(bb)
        else:
            try:
                aa = gen2.send(i)
                print(aa)
            except StopIteration as e:
                print("e:", e)


if __name__ == '__main__':
    main()
