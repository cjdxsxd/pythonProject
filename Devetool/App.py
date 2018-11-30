#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/9/20 10:42
# Author: sxd
# File: App.py
# Pycharm: PyCharm
# Contact: 3360048@163.com

import  wx
# 定义应用程序对象
app = wx.App()
# 创建顶层窗口wx.Frame对象，给出标题和尺寸
window = wx.Frame(None, title="小工具", size=(600, 800))
# 其他空间对象可以在Frame对象上加入，但是无法管理，所以创建Panel对象
panel = wx.Panel(window)
# 创建静态文本对象
label = wx.StaticText(panel, label="工具", pos=(100, 200))
# 创建菜单栏对象
menubar = wx.MenuBar()
# 创建菜单对象
filemenu = wx.Menu()
#菜单项
fileItem = filemenu.Append(wx.ID_EXIT, '退出', '退出应用程序')
menubar.Append(filemenu, '&File')

# show方法激活窗口对象
window.Show(True)
# 输入应用程序主循环事件
app.MainLoop()