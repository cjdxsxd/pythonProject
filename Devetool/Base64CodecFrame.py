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
## Class Base64CodecFrame
###########################################################################

class Base64CodecFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Base64CodecFrame", pos=wx.DefaultPosition,
                          size=wx.Size(579, 362), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        gSizer1 = wx.GridSizer(2, 1, 0, 0)

        gSizer2 = wx.GridSizer(2, 1, 0, 0)

        fgSizer1 = wx.FlexGridSizer(2, 2, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"原始字符串", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        self.m_staticText1.SetFont(wx.Font(12, 70, 90, 90, False, "宋体"))

        fgSizer1.Add(self.m_staticText1, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400, 30), 0)
        self.m_textCtrl1.SetFont(wx.Font(14, 70, 90, 90, False, "宋体"))

        fgSizer1.Add(self.m_textCtrl1, 0, wx.ALIGN_LEFT | wx.ALL, 2)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"加解密后", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        self.m_staticText2.SetFont(wx.Font(12, 70, 90, 90, False, "宋体"))

        fgSizer1.Add(self.m_staticText2, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.m_textCtrl2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400, 30), 0)
        fgSizer1.Add(self.m_textCtrl2, 0, wx.ALIGN_LEFT | wx.ALL, 2)

        gSizer2.Add(fgSizer1, 1, wx.SHAPED, 5)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"Base64加密", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_button4, 1, wx.ALIGN_CENTER | wx.ALIGN_LEFT | wx.ALIGN_RIGHT | wx.ALL, 5)

        self.m_button5 = wx.Button(self, wx.ID_ANY, u"Base64解密", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_button5, 0, wx.ALIGN_CENTER | wx.ALIGN_RIGHT, 5)

        gSizer2.Add(bSizer2, 1, wx.ALIGN_CENTER, 2)

        gSizer1.Add(gSizer2, 1, wx.EXPAND, 5)

        gSizer3 = wx.GridSizer(2, 1, 0, 0)

        fgSizer3 = wx.FlexGridSizer(2, 2, 0, 0)
        fgSizer3.SetFlexibleDirection(wx.BOTH)
        fgSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"原始文件", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        self.m_staticText5.SetFont(wx.Font(12, 70, 90, 90, False, "宋体"))

        fgSizer3.Add(self.m_staticText5, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.m_filePicker1 = wx.FilePickerCtrl(self, wx.ID_ANY, u"", u"Select a file", u"*.*",
                                               wx.DefaultPosition, wx.Size(400, -1), wx.FLP_DEFAULT_STYLE)
        fgSizer3.Add(self.m_filePicker1, 0, wx.ALL, 5)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"加解密后文件", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        self.m_staticText6.SetFont(wx.Font(12, 70, 90, 90, False, "宋体"))

        fgSizer3.Add(self.m_staticText6, 0, wx.ALL, 5)

        self.m_filePicker2 = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*",
                                               wx.DefaultPosition, wx.Size(400, -1), wx.FLP_DEFAULT_STYLE)
        fgSizer3.Add(self.m_filePicker2, 0, wx.ALL, 5)

        gSizer3.Add(fgSizer3, 1, wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button8 = wx.Button(self, wx.ID_ANY, u"Base64加密", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_button8, 0, wx.ALIGN_CENTER | wx.ALIGN_RIGHT | wx.ALL, 5)

        self.m_button9 = wx.Button(self, wx.ID_ANY, u"Base64解密", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_button9, 0, wx.ALIGN_CENTER | wx.ALIGN_RIGHT | wx.ALL, 5)

        gSizer3.Add(bSizer4, 1, wx.ALIGN_CENTER, 5)

        gSizer1.Add(gSizer3, 1, wx.EXPAND, 5)

        self.SetSizer(gSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button4.Bind(wx.EVT_BUTTON, self.Encode_Str)
        self.m_button5.Bind(wx.EVT_BUTTON, self.Decode_Str)
        self.m_button8.Bind(wx.EVT_BUTTON, self.Encode_File)
        self.m_button9.Bind(wx.EVT_BUTTON, self.Decode_File)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def Encode_Str(self, event):
        event.Skip()

    def Decode_Str(self, event):
        event.Skip()

    def Encode_File(self, event):
        event.Skip()

    def Decode_File(self, event):
        event.Skip()


