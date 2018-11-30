#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/11/13 11:31
# Author: sxd
# File: test_network.py
# Pycharm: PyCharm
# Contact: 3360048@163.com


from Devetool import testone
import wx
import os

class MainWin(testone.TestFrame):

    def produc_env(self, event):
        """执行telnet命令"""
        result = os.popen("ping www.baidu.com")
        # respon = result.read()
        # self.m_textCtrl5.clear()
        self.m_textCtrl7.SetValue(result.read())
        result.close()

    def test_env(self, event):
        pass


if __name__ == '__main__':
    app = wx.App()
    main_win = MainWin(None)
    main_win.Show()

    app.MainLoop()