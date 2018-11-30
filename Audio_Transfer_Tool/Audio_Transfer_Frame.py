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
## Class Audio_Transfer_Frame
###########################################################################

class Audio_Transfer_Frame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"音频格式转换小工具", pos=wx.DefaultPosition,
                          size=wx.Size(793, 473), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(wx.Font(16, 70, 90, 90, False, "宋体"))

        gSizer2 = wx.GridSizer(0, 0, 0, 0)

        fgSizer1 = wx.FlexGridSizer(4, 0, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"需要转换的文件：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        bSizer2.Add(self.m_staticText6, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        m_choice1Choices = [u"PCM", u"WAV", u"AMR", u"MP3"]
        self.m_choice1 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0)
        self.m_choice1.SetSelection(2)
        bSizer2.Add(self.m_choice1, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_filePicker2 = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*",
                                               wx.DefaultPosition, wx.Size(600, 30), wx.FLP_DEFAULT_STYLE)
        bSizer2.Add(self.m_filePicker2, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        fgSizer1.Add(bSizer2, 1, wx.EXPAND, 5)

        bSizer1 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"需要转换成格式：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        bSizer1.Add(self.m_staticText5, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_radioBtn5 = wx.RadioButton(self, wx.ID_ANY, u"PCM", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_radioBtn5, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_radioBtn6 = wx.RadioButton(self, wx.ID_ANY, u"MP3", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_radioBtn6, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_radioBtn7 = wx.RadioButton(self, wx.ID_ANY, u"WAV", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_radioBtn7, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_radioBtn8 = wx.RadioButton(self, wx.ID_ANY, u"AWR", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_radioBtn8, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        fgSizer1.Add(bSizer1, 1, wx.EXPAND, 5)

        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"新文件目录：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        bSizer3.Add(self.m_staticText7, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_dirPicker1 = wx.DirPickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition,
                                             wx.Size(630, -1), wx.DIRP_DEFAULT_STYLE)
        bSizer3.Add(self.m_dirPicker1, 0, wx.ALL, 5)

        fgSizer1.Add(bSizer3, 1, 0, 5)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"转换", wx.DefaultPosition, wx.Size(-1, 50), 0)
        self.m_button4.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))

        bSizer4.Add(self.m_button4, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        fgSizer1.Add(bSizer4, 1, 0, 5)

        gSizer2.Add(fgSizer1, 1, wx.EXPAND, 5)

        self.SetSizer(gSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_filePicker2.Bind(wx.EVT_FILEPICKER_CHANGED, self.get_old_file)
        self.m_radioBtn5.Bind(wx.EVT_RADIOBUTTON, self.choice_pcm)
        self.m_radioBtn6.Bind(wx.EVT_RADIOBUTTON, self.choice_mp3)
        self.m_radioBtn7.Bind(wx.EVT_RADIOBUTTON, self.choice_wav)
        self.m_radioBtn8.Bind(wx.EVT_RADIOBUTTON, self.choice_awr)
        self.m_dirPicker1.Bind(wx.EVT_DIRPICKER_CHANGED, self.get_new_file)
        self.m_button4.Bind(wx.EVT_BUTTON, self.transfer_format)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def get_old_file(self, event):
        event.Skip()

    def choice_pcm(self, event):
        event.Skip()

    def choice_mp3(self, event):
        event.Skip()

    def choice_wav(self, event):
        event.Skip()

    def choice_awr(self, event):
        event.Skip()

    def get_new_file(self, event):
        event.Skip()

    def transfer_format(self, event):
        event.Skip()


