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
## Class TestFrame
###########################################################################

class TestFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"测试网络连通性", pos=wx.DefaultPosition, size=wx.Size(691, 670),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        # self.SetSizeHints()

        self.m_menubar2 = wx.MenuBar(0)
        self.m_menu3 = wx.Menu()
        self.m_menubar2.Append(self.m_menu3, u"菜单")

        self.m_menu4 = wx.Menu()
        self.m_menubar2.Append(self.m_menu4, u"菜单2")

        self.m_menu6 = wx.Menu()
        self.m_menubar2.Append(self.m_menu6, u"菜单3")

        self.SetMenuBar(self.m_menubar2)

        self.m_statusBar1 = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)
        gSizer1 = wx.GridSizer(5, 3, 0, 0)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"测试鹏元生产网络连通性", wx.Point(20, 20), wx.Size(200, 20), 0)
        self.m_staticText3.Wrap(-1)
        self.m_staticText3.SetFont(wx.Font(12, 70, 90, 90, False, "宋体"))

        gSizer1.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"测试", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_button3, 0, wx.ALL, 5)

        self.m_textCtrl7 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TE_MULTILINE)
        gSizer1.Add(self.m_textCtrl7, 0, wx.ALL, 5)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"测试鹏元测试环境连通性", wx.DefaultPosition, wx.Size(200, 20), 0)
        self.m_staticText4.Wrap(-1)
        self.m_staticText4.SetFont(wx.Font(12, 70, 90, 90, False, "宋体"))

        gSizer1.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"测试", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_button4, 0, wx.ALL, 5)

        self.m_textCtrl6 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TE_MULTILINE)
        gSizer1.Add(self.m_textCtrl6, 0, wx.ALL, 5)

        self.SetSizer(gSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button3.Bind(wx.EVT_BUTTON, self.produc_env)
        self.m_button4.Bind(wx.EVT_BUTTON, self.test_env)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def produc_env(self, event):
        event.Skip()

    def test_env(self, event):
        event.Skip()


