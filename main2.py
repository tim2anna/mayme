#!/usr/bin/env python
#-*- coding:utf-8 -*-

import wx
import os
import wx.lib.filebrowsebutton as filebrowse


class MyPanel(wx.Panel):
    def __init__(self, parent, ID):
        wx.Panel.__init__(self, parent, ID)

        current_path = os.path.dirname(__file__)
        self.source_path = current_path
        self.output_path = current_path


        source = filebrowse.DirBrowseButton(
            self, -1, size=(450, -1), changeCallback = self.sourceCallback,
            labelText=u'源文件夹   ', buttonText=u'浏览', dialogTitle=u'选择源文件夹',
            startDirectory=current_path
        )
        output = filebrowse.DirBrowseButton(
            self, -1, size=(450, -1), changeCallback = self.outputCallback,
            labelText=u'输出文件夹', buttonText=u'浏览', dialogTitle=u'选择输出文件夹',
            startDirectory=current_path
        )

        ok_btn = wx.Button(self, -1, u"确定")

        log_panel = wx.Panel(self, -1)
        log_txt = wx.StaticText(log_panel, -1, u"日志", pos=(0, 10))
        log_ctrl = wx.TextCtrl(log_panel, -1, "", pos=(65, 10), size=(300, 250), style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(source, 0, wx.ALL, 5)
        sizer.Add(output, 0, wx.ALL, 5)
        sizer.Add(ok_btn, 0, wx.ALL, 5)
        sizer.Add(log_panel, 0, wx.ALL, 5)
        box = wx.BoxSizer()
        box.Add(sizer, 0, wx.ALL, 20)
        self.SetSizer(box)

    def sourceCallback(self, evt):
        self.source_path = evt.GetString()


    def outputCallback(self, evt):
        self.output_path = evt.GetString()


class App(wx.App):

    def OnInit(self):
        self.frame = wx.Frame(parent=None, id=-1, size=(500, 500), title='MayMe')  # 框架的实例作为应用程序的一个属性
        self.panel = MyPanel(self.frame, -1)
        self.frame.Center()
        self.frame.Show()
        self.SetTopWindow(self.frame)  # 一个应用程序可以多个框架，设置顶级窗口
        return True


if __name__ == '__main__':  # 独立运行程序入口
    app = App()
    app.MainLoop()