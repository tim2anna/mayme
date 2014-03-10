#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""最小的空的wxPython程序"""

import wx  # 导入wxPython包


class App(wx.App):  # 继承wxPython应用程序类

    def OnInit(self):  # 定义应用程序类的初始化方法
        frame = wx.Frame(parent=None, title='Bare')
        frame.Show()  # 使框架可见
        return True


app = App()  # 创建一个应用程序类的实例
app.MainLoop()  # 进入这个应用程序的主事件循环