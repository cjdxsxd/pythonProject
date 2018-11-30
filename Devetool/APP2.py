#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/9/26 9:50
# Author: sxd
# File: APP2.py
# Pycharm: PyCharm
# Contact: 3360048@163.com

import wx
import os

class MyFrame(wx.Frame):
    """we simple drive a new calls of Frame"""
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title)
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        # 创建底部菜单
        self.statusBar = wx.StatusBar()
        # 创建菜单
        filemenu = wx.Menu()
        # 添加关于项
        menuAbout = filemenu.Append(wx.ID_ABOUT, "About", "Information about this program")
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        # 添加退出项
        menuExit = filemenu.Append(wx.ID_EXIT, "Exit", "Terminate the program")
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        # 添加打开文件项
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open", "Open a file")
        self.Bind(wx.EVT_MENU, self.menuOpenFile, menuOpen)
        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.buttons = []
        for i in range(0, 6):
            self.buttons.append(wx.Button(self, -1, "Button &" +str(i)))
            self.sizer2.Add(self.buttons[i], 1, wx.EXPAND)
        # 把菜单添加到菜单栏
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "File")
        self.SetMenuBar(menuBar)
        self.Show(True)

    def OnAbout(self, e):
        dig = wx.MessageDialog(self, "A small test")
        dig.ShowModal()
        dig.Destroy()

    def OnExit(self, e):
        self.Close(True)

    def menuOpenFile(self, e):
        """open a file"""
        self.dirname = ""
        dlg = wx.FileDialog(self, "choose a file", self.dirname, "", "*.*", wx.ID_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'rb')
            self.control.SetValue(f.read().decode('utf-8'))
            f.close()
        dlg.Destroy()


app = wx.App(False)
frame = MyFrame(None, 'Small Editor')
app.MainLoop()
