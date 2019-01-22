#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2019/1/21 17:22
# Author: sxd
# File: BaiduOcrClass.py
# Pycharm: PyCharm
# Contact: 3360048@163.com
from BaiduOcrForImage import BaiduOcrForImageMyFrame
import os
from aip import AipOcr
import wx
import logging
# logging.basicConfig(level=logging.DEBUG)


# 继承框架类
class BaiduOcrClass(BaiduOcrForImageMyFrame.MyFrame):

    def update_app_id(self, event):
        event.Skip()
        x = self.m_textCtrl4.GetValue()
        print(x)
        return x

    def update_app_key(self, event):
        event.Skip()
        y = self.m_textCtrl5.GetValue()
        return y

    def update_secret_key(self, event):
        event.Skip()
        z = self.m_textCtrl6.GetValue()
        return z

    def clear_app_id(self, event):
        event.Skip()
        self.m_textCtrl4.Clear()

    def clear_app_key(self, event):
        event.Skip()
        self.m_textCtrl5.Clear()

    def clear_secret_key(self, event):
        event.Skip()
        self.m_textCtrl6.Clear()
    # 重写框架类方法，获取文件夹路径
    def get_result_from_baiduocr(self, event):
        event.Skip()
        APP_ID = ('15462878' if self.update_app_id(event) == '' else self.update_app_id(event) )
        print(APP_ID)
        APP_KEY = ('RLnaHWt4RTMcKnp0TeyyCRkB' if self.update_app_key(event) == '' else self.update_app_key(event))
        SECRET_KEY = ('LtwGlxYVSR3v99fiBlZLZWXYISa4yzWC' if self.update_secret_key(event) == '' else self.update_secret_key(event))
        client = AipOcr(APP_ID, APP_KEY, SECRET_KEY)
        options = {}
        imagefile = self.m_dirPicker3.GetPath()
        file = os.listdir(imagefile)
        for files in file:
            filename = os.path.join(imagefile, files)
            with open(filename, 'rb') as rb:
                result = client.basicAccurate(rb.read(), options)
                self.m_textCtrl2.AppendText(str(result))
                # print(result)


if __name__ == '__main__':
    app = wx.App(False)
    frame = BaiduOcrClass(None)
    frame.Show()
    app.MainLoop()