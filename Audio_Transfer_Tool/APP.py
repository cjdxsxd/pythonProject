#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/11/21 16:11
# Author: sxd
# File: APP.py
# Pycharm: PyCharm
# Contact: 3360048@163.com
import wx
from Audio_Transfer_Tool import Audio_Transfer_Frame
import os
import ffmpeg
import sys
from pydub import AudioSegment
import subprocess
import traceback
import time


class MainWind(Audio_Transfer_Frame.Audio_Transfer_Frame):
    """窗口中事件方法重写"""

    # Virtual event handlers, overide them in your derived class
    def get_old_file(self, event):
        """读取原始文件"""
        # 读取文件路径
        filepath = self.m_filePicker2.GetPath()
        print(filepath)
        # 获取扩展名
        file_format = os.path.splitext(filepath)[1]
        print(file_format)
    #     判断扩展名在不在4个范围内
        if file_format not in('.amr', '.mp3', '.pcm', '.wav'):
            print("只能选择MP3,AMR,PCM,WAV格式文件！")
            wx.MessageBox(u"只能选择MP3,AMR,PCM,WAV格式文件！", u"消息提示", wx.OK | wx.ICON_INFORMATION)
        # with open(filepath, 'rb')as rb:
        #     print(rb.read())
        #     return rb.read()
        return filepath

    def choice_pcm(self, event):
        event.Skip()

    def choice_mp3(self, event):
        event.Skip()

    def choice_wav(self, event):
        event.Skip()

    def choice_awr(self, event):
        event.Skip()

    def get_new_file(self, event):
        """返回文件目录"""
        print(self.m_dirPicker1.GetPath())
        return self.m_dirPicker1.GetPath()

    def transfer_format(self, event):
        """格式转换操作"""
        cmd = ""
        if self.m_radioBtn5.GetValue():
            now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            new_file = os.path.join(self.get_new_file(None), now+'x.pcm')
            try:
                error = subprocess.call(["D:\\02python\\python3.6.5Install\\Lib\\site-packages\\ffmpeg-20181121-77bf855-win64-static\\bin\\ffmpeg", "-i", self.get_old_file(None), new_file])
                print(error)
            except Exception as e:
                print("打印异常", e)

            if error:
                wx.MessageBox(u"转换PCM失败！", u"消息提示", wx.OK | wx.ICON_INFORMATION)
            else:
                wx.MessageBox(u"转换PCM成功！", u"消息提示", wx.OK | wx.ICON_INFORMATION)

        elif self.m_radioBtn6.GetValue():
            now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            new_file = os.path.join(self.get_new_file(None), now+'.mp3')
            error = subprocess.call(["D:\\02python\\python3.6.5Install\\Lib\\site-packages\\ffmpeg-20181121-77bf855-win64-static\\bin\\ffmpeg", "-i", self.get_old_file(None), new_file])
            print(error)
            if error:
                wx.MessageBox(u"转换MP3失败！", u"消息提示", wx.OK | wx.ICON_INFORMATION)
            else:
                wx.MessageBox(u"转换MP3成功！", u"消息提示", wx.OK | wx.ICON_INFORMATION)

        elif self.m_radioBtn7.GetValue():
            now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            new_file = os.path.join(self.get_new_file(None),now)
            error = subprocess.call(["D:\\02python\\python3.6.5Install\\Lib\\site-packages\\ffmpeg-20181121-77bf855-win64-static\\bin\\ffmpeg", "-i", self.get_old_file(None), new_file])
            print(error)
            # sound = AudioSegment.from_file(self.get_old_file(None), format='mp3')
            # sound.export(new_file, format='.wav')
            if error:
                wx.MessageBox(u"转换wav失败！", u"消息提示", wx.OK | wx.ICON_INFORMATION)
            else:
                wx.MessageBox(u"转换wav成功！", u"消息提示", wx.OK | wx.ICON_INFORMATION)

        elif self.m_radioBtn8.GetValue():
            new_file = os.path.join(self.get_new_file(None), 'x.amr')
            error = subprocess.call(["D:\\02python\\python3.6.5Install\\Lib\\site-packages\\ffmpeg-20181121-77bf855-win64-static\\bin\\ffmpeg", "-i", self.get_old_file(None), new_file])
            print(error)
            if error:
                wx.MessageBox(u"转换amr失败！", u"消息提示", wx.OK | wx.ICON_INFORMATION)
            else:
                wx.MessageBox(u"转换amr成功！", u"消息提示", wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox(u"请先选择需要转换的格式", u"消息提示", wx.OK | wx.ICON_INFORMATION)


if __name__ == '__main__':
    app = wx.App(False)
    frame = MainWind(None)
    frame.Show()
    app.MainLoop()