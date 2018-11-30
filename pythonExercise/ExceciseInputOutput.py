#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/8/15 10:13
# Author: sxd
# File: ExceciseInputOutput.py
# Pycharm: PyCharm
# Contact: 3360048@163.com

from collections import Iterable

print("sxd", "123")

# name = input("请输入你的姓名：")
# print('hello,', name)


def f(n):
    if n == 1:
        return 1
    return n*f(n-1)


L=[1,2,3,4]
# print(L[-2])
# print(L[-2:])
# print(L[-2:-1])

dict = {'a':1, 'b':2}
for key in dict:
    print(key)

for values in dict.values():
    print(values)

for k,v in dict.items():
    print(k,v)

print(isinstance(dict,Iterable))

lst = [1,2,3,4]
# lst.sort()
# print(list)
enum = enumerate(lst)
print(enum,isinstance(enum, Iterable))
for i in lst:
    print(i)


def findMaxAndMin(L):
    if (len(L) == 0):
        return (None, None)
    else:
        maxv = L[0]
        minv = L[0]
        for v in L:
            if v > maxv:
                maxv = v
            if v < minv:
                minv = v
        return (maxv, minv)

print(findMaxAndMin(lst))