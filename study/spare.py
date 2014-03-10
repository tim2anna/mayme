#!/usr/bin/env python
#-*- coding:utf-8 -*-

import wx


class Frame(wx.Frame):  # 创建自己的框架类
    pass


class App(wx.App):

    def OnInit(self):
        self.frame = Frame(parent=None, title='Spare')  # 框架的实例作为应用程序的一个属性
        self.frame.Show()
        self.SetTopWindow(self.frame)  # 一个应用程序可以多个框架，设置顶级窗口
        return True


if __name__ == '__main__':  # 独立运行程序入口
    app = App()
    app.MainLoop()