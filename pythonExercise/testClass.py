#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/10/30 10:45
# Author: sxd
# File: testClass.py
# Pycharm: PyCharm
# Contact: 3360048@163.com

# 类的联系
class Student(object):
    '''student类'''
    def __init__(self, names, ages):
        # __私有变量，加双下划线，只有类内部访问
        self.__names = names
        self.__ages = ages

    def get_name(self):
        # 类的内部也是引用整个私有变量
        print(self.__names)
        return 'ok'


student = Student('sxd', '123')
name = student.get_name()
# age = student.age
print(name)


class A(Student):
    def get_name(self):
        pass

class B(Student):
    pass


a = A('A', '1')
b = B('B', '2')
a.get_name()
b.get_name()