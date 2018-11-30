#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/10/29 14:20
# Author: sxd
# File: testForWhileDoWhile.py
# Pycharm: PyCharm
# Contact: 3360048@163.com


# 熟悉for,while,do..while循环


for x in range(1, 10):
    x+=x
    # print(x)

sums = 0
for x in [1, 2, 3]:
    sums = sums + x

# print(sums)


count = 0
sum2 = 0
while count < 10:
    if count == 7:
        continue
    sum2 += count
    count += 1
    print(sum2)

