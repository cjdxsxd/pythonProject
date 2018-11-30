#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/9/27 17:32
# Author: sxd
# File: APP3.py
# Pycharm: PyCharm
# Contact: 3360048@163.com
import wx

class Simple_Frame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title="测试Label")
        panel = wx.Panel(self)
        self.quote = wx.StaticText(panel, label="your quote", pos=(20, 30))
        self.Show()

app = wx.App()
frame = Simple_Frame(None)
nb = wx.Notebook(frame)

nb.AddPage()

