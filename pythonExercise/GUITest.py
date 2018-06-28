#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time   :2018/6/6 10:42
# @author :shangxudong
# @File   : GUITest.py
# @Software: PyCharm Community Edition
from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
         Frame.__init__(self, master)
         self.pack()
         self.createWidgets()

    def createWidgets(self):
        self.lable = Entry(self)
        self.lable.pack()
        self.quitButton = Button(self, text="quit", command=self.hello)
        self.quitButton.pack()

    def hello(self):
         name = self.lable.get() or 'world'
         messagebox.showinfo('Message','Hello,%s' %name)


app = Application()
app.master.title= "test"
app.mainloop()