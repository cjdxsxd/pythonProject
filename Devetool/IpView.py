#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/11/13 10:08
# Author: sxd
# File: IpView.py
# Pycharm: PyCharm
# Contact: 3360048@163.com
import wx

# 创建一个应用对象
app = wx.App()
# 创建顶层框架窗口，并给出标题和尺寸
frame = wx.Frame(parent=None, title="查看本机ip", size=(600, 800))
# 其他控件也可以加入到frame但是无法管理，因此需要使用pannel,放到frame
pannel = wx.Panel(parent=frame)
# 添加文本对象控件到pannel
label = wx.StaticText(parent=pannel, label="第一个文本对象", pos=(100, 100))
# 通过show方法激活窗口
frame.Show()
# 输入应用对象主事件循环
app.MainLoop()