# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class MyFrame
###########################################################################

class MyFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"提取照片文字（照片小于4M）", pos=wx.DefaultPosition,
                          size=wx.Size(879, 580), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        bSizer7.SetMinSize(wx.Size(879, 580))
        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer9.SetMinSize(wx.Size(879, 50))
        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"原始照片路径：", wx.Point(-1, 10), wx.Size(150, 30), 0)
        self.m_staticText4.Wrap(-1)
        self.m_staticText4.SetFont(wx.Font(14, 70, 90, 90, False, wx.EmptyString))

        bSizer9.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.m_dirPicker3 = wx.DirPickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.Point(-1, 20),
                                             wx.Size(500, -1), wx.DIRP_DEFAULT_STYLE)
        bSizer9.Add(self.m_dirPicker3, 0, wx.ALL, 5)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"提取照片文字", wx.Point(-1, 30), wx.DefaultSize, 0)
        bSizer9.Add(self.m_button2, 0, wx.ALL, 5)

        bSizer7.Add(bSizer9, 1, wx.EXPAND, 5)

        self.m_textCtrl2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(879, 370),
                                       0 | wx.HSCROLL | wx.VSCROLL)
        bSizer7.Add(self.m_textCtrl2, 0, wx.ALL, 5)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"APP_ID：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        bSizer11.Add(self.m_staticText7, 0, wx.ALL, 5)

        self.m_textCtrl4 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer11.Add(self.m_textCtrl4, 0, wx.ALL, 5)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"更新", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer11.Add(self.m_button3, 0, wx.ALL, 5)

        self.m_button51 = wx.Button(self, wx.ID_ANY, u"清空", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer11.Add(self.m_button51, 0, wx.ALL, 5)

        bSizer10.Add(bSizer11, 1, wx.EXPAND, 5)

        bSizer12 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, u"APP_KEY：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)
        bSizer12.Add(self.m_staticText8, 0, wx.ALL, 5)

        self.m_textCtrl5 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.m_textCtrl5, 0, wx.ALL, 5)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"更新", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.m_button4, 0, wx.ALL, 5)

        self.m_button6 = wx.Button(self, wx.ID_ANY, u"清空", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.m_button6, 0, wx.ALL, 5)

        bSizer10.Add(bSizer12, 1, wx.EXPAND, 5)

        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText9 = wx.StaticText(self, wx.ID_ANY, u"SECRET_KEY：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)
        bSizer13.Add(self.m_staticText9, 0, wx.ALL, 5)

        self.m_textCtrl6 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer13.Add(self.m_textCtrl6, 0, wx.ALL, 5)

        self.m_button5 = wx.Button(self, wx.ID_ANY, u"更新", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer13.Add(self.m_button5, 0, wx.ALL, 5)

        self.m_button7 = wx.Button(self, wx.ID_ANY, u"清空", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer13.Add(self.m_button7, 0, wx.ALL, 5)

        bSizer10.Add(bSizer13, 1, wx.EXPAND, 5)

        bSizer7.Add(bSizer10, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer7)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button2.Bind(wx.EVT_BUTTON, self.get_result_from_baiduocr)
        self.m_textCtrl2.Bind(wx.EVT_TEXT, self.get_result)
        self.m_button3.Bind(wx.EVT_BUTTON, self.update_app_id)
        self.m_button51.Bind(wx.EVT_BUTTON, self.clear_app_id)
        self.m_button4.Bind(wx.EVT_BUTTON, self.update_app_key)
        self.m_button6.Bind(wx.EVT_BUTTON, self.clear_app_key)
        self.m_textCtrl6.Bind(wx.EVT_TEXT, self.update_secret_key)
        self.m_button7.Bind(wx.EVT_BUTTON, self.clear_secret_key)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def get_result_from_baiduocr(self, event):
        event.Skip()

    def get_result(self, event):
        event.Skip()

    def update_app_id(self, event):
        event.Skip()

    def clear_app_id(self, event):
        event.Skip()

    def update_app_key(self, event):
        event.Skip()

    def clear_app_key(self, event):
        event.Skip()

    def update_secret_key(self, event):
        event.Skip()

    def clear_secret_key(self, event):
        event.Skip()


