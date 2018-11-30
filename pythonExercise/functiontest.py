#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time   :2018/6/1 11:06
# @author :shangxudong
# @File   : functiontest.py
# @Software: PyCharm Community Edition

# 位置参数
def powers(x):
    return x*x

# print(powers(2))

#默认参数
def powerm(x,n=2):
    s = 1
    while n > 0:
        n = n-1
        s = s*x
    return s

# print(powerm(5))

# 可变参数*
def kebiancanshu(*argus):
    s = 0
    for i in argus:
        s = s+i
    return s
list = [1,2,3]
lists = (1,2,3,4,5)
# print(kebiancanshu(*lists))


# 关键字参数
def keywordcanshu(name, age, **kwa):

    print("name:", name, "age:", age, "other:", kwa)

# keywordcanshu("sxd","11",city="beijing")
dict = {"city":"beijing","sex":"F"}
# keywordcanshu("sxd",11,**dict)


def products(x, y, *argus):
    s = 1
    for i in argus:
        print(i)
        s = s*i
    return s


print(products(*(1, 2, 3)))