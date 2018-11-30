#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/10/30 14:17
# Author: sxd
# File: testDecorator.py
# Pycharm: PyCharm
# Contact: 3360048@163.com

# test decorator装饰器,作用是扩展函数方法，将函数转换成属性


class Student(object):
    def __init__(self, score):
        self.__score = score

    # 自定义property只具备只读属性
    @property
    def get_score(self):
        return self.__score

    # 定义这个属性的setter才是可写属性
    @get_score.setter
    def set_score(self, score):
        if not isinstance(score, int):
            print("输入不是分数")
        if score < 0 or score > 1000:
            print("值不对")
        self.__score = score


# a = Student(123)
# a.set_score(345)
# print(a.get_score())
a = Student(123)
a.set_score = 456
print(a.get_score)
