#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/10/18 15:43
# Author: sxd
# File: loopTest.py
# Pycharm: PyCharm
# Contact: 3360048@163.com

# for循环逻辑
# (1) for：
# for (循环控制变量初始化; 循环终止条件; 循环控制变量增量)
# {
# 循环体
# }
# 循环执行步骤：
# 第一，先进行循环控制变量初始化；
# 第二，执行循环终止条件，如果判断结果为真，则进入第三步；如果为假则循环终止并退出；
# 第三，执行循环体；
# 第四，执行循环控制变量增量，转入第二步；

# for x in([1,2,3]):
#     print(x)
#
#
# n = 0
# while n<9:
#     n +=1
#     print(n)


d = {'a': 123, 'b': 456}
v = d.get('a')
v2 = d['a']
print(v)
print(v2)