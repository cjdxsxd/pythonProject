#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/11/15 14:59
# Author: sxd
# File: test_Base64Decode.py
# Pycharm: PyCharm
# Contact: 3360048@163.com
import wx
import base64
from Devetool import Base64CodecFrame


class Base64_Decode_Demo(Base64CodecFrame.Base64CodecFrame):
    """继承wxFormBuilder的框架，实现交互函数即可"""

    def Encode_Str(self, event):
        """点击字符串加密按钮"""
        try:
            import base64
        except Exception:
            self.m_textCtrl1.SetValue("ERROR: Could not load module 'base64'")
            return
        _ysstr = self.m_textCtrl1.GetValue()
        byte_ysstr = _ysstr.encode('utf-8')
        _jgstr = None
        try:
            _jgstr = base64.b64encode(byte_ysstr)
        except Exception:
            self.m_textCtrl2.SetValue("ERROR: Could not decode string %s" %_ysstr)
        self.m_textCtrl2.SetValue(_jgstr.strip())
        event.Skip()
        return

    def Decode_Str(self, event):
        """base64 解密"""
        _ysstr2 = self.m_textCtrl1.GetValue()
        # byte_ysstr2 = _ysstr2.encode('utf-8')
        try:
            _jgstr2 = base64.b64decode(_ysstr2)
        except Exception:
            self.m_textCtrl2.SetValue("ERROR: Could not decode string %s" %_ysstr2)
            return

        self.m_textCtrl2.SetValue(_jgstr2.strip())
        event.Skip()
        return

    def Encode_File(self, event):
        """读取文件并加密"""
        filepath = self.m_filePicker1.GetPath()

        with open(filepath, 'r') as f:
            filecontent = f.read()
        byte_filecontent = filecontent.encode('utf-8')
        try:
            encode_content = base64.b64encode(byte_filecontent)
        except Exception:
            self.m_filePicker2.SetLabelText("base64加密失败")

        filepath2 = self.m_filePicker2.GetPath()
        with open(filepath2, 'w') as w:
            str_content = str(encode_content, encoding='utf-8')
            w.write(str_content)
        wx.MessageDialog(None, u"base64加密成功", 'MessageDialog', wx.YES_NO or wx.ICON_QUESTION)
        return

    def Decode_File(self, event):
        """解密文件"""
        filepath3 = self.m_filePicker1.GetPath()
        with open(filepath3, 'r') as f:
            filecontent4 = f.read()
        try:
            encode_content2 = base64.b64decode(filecontent4)
        except Exception:
            self.m_filePicker2.SetLabelText("base64解密失败")
        filepath5 = self.m_filePicker2.GetPath()
        with open(filepath5, 'w') as w:
            str_content2 = str(encode_content2, encoding='utf-8')
            w.write(str_content2)
        wx.MessageDialog(None, u"base64解密成功", 'MessageDialog', wx.YES_NO or wx.ICON_QUESTION)
        return


if __name__ == '__main__':
    app = wx.App(False)
    frame = Base64_Decode_Demo(None)
    frame.Show()
    app.MainLoop()
