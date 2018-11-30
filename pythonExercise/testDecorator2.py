#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/10/30 14:42
# Author: sxd
# File: testDecorator2.py
# Pycharm: PyCharm
# Contact: 3360048@163.com


class Screen(object):

    @property
    def width(self):
        return self._width

    # 变量前面带有1个_表示是私有变量，只用于标明，外部可以引用，如果是2个__是内置变量，外部不能调用
    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def resolution(self):
        return self._width*self._height


s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)