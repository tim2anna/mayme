#!/usr/bin/env python
#-*- coding:utf-8 -*-

import wx
import os
from datetime import datetime
import wx.lib.filebrowsebutton as filebrowse
import wx.lib.mixins.inspection
from wx.lib.embeddedimage import PyEmbeddedImage

from xls.read import read


class MyPanel(wx.Panel):
    def __init__(self, parent, ID):
        wx.Panel.__init__(self, parent, ID)

        current_path = os.getcwd()
        self.source_path = current_path
        self.output_path = current_path


        source = filebrowse.DirBrowseButton(
            self, -1, size=(450, -1), changeCallback = self.sourceCallback,
            labelText=u'源文件夹   ', buttonText=u'浏览', dialogTitle=u'选择源文件夹',
            startDirectory=current_path
        )
        source.SetValue(self.source_path)

        output = filebrowse.DirBrowseButton(
            self, -1, size=(450, -1), changeCallback = self.outputCallback,
            labelText=u'输出文件夹', buttonText=u'浏览', dialogTitle=u'选择输出文件夹',
            startDirectory=current_path
        )
        output.SetValue(self.output_path)

        self.ok_btn = ok_btn = wx.Button(self, -1, u"确定")

        log_panel = wx.Panel(self, -1)
        log_txt = wx.StaticText(log_panel, -1, u"日志", pos=(0, 10))
        self.log_ctrl = log_ctrl = wx.TextCtrl(log_panel, -1, "", pos=(65, 10), size=(360, 250), style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(source, 0, wx.ALL, 5)
        sizer.Add(output, 0, wx.ALL, 5)
        sizer.Add(ok_btn, 0, wx.ALL, 5)
        sizer.Add(log_panel, 0, wx.ALL, 5)
        box = wx.BoxSizer()
        box.Add(sizer, 0, wx.ALL, 20)
        self.SetSizer(box)

        self.Bind(wx.EVT_BUTTON, self.OnClick, ok_btn)

    def sourceCallback(self, evt):
        self.source_path = evt.GetString()


    def outputCallback(self, evt):
        self.output_path = evt.GetString()


    def OnClick(self, evt):
        self.ok_btn.Enable(False)
        now = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        output_dir = os.path.join(self.output_path, now)
        os.mkdir(output_dir)
        logs = read(self.source_path, output_dir)
        for t, log in logs:
            self.log_ctrl.AppendText(t + '\t' + log + '\n')
        self.ok_btn.Enable(True)


def opj(path):
    """Convert paths to the platform-specific separator"""
    st = apply(os.path.join, tuple(path.split('/')))
    # HACK: on Linux, a leading / gets lost...
    if path.startswith('/'):
        st = '/' + st
    return st


WXPdemo = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAWlJ"
    "REFUWIW1V1sSwjAIBMebeBU9db2KZ8EPmxbCI4TUnXGskWaXDQktwhjErjERP4XRhER08iPi"
    "5SKiyQR5JyI7xxB3j7wn5GI6V2hFxM0gJtjYANFBiIjQu7L/1lYlwR0QxLDZhE0II1+CtwRC"
    "RI8riBva7DL7CC9VAwDbbxwKtdDXwBi7K+1zCP99T1vDFedd8FBwYd6BCAUXuACEF7QsbET/"
    "FaHs+gDQw4vOLNHkMojAnTw8nlNipIiwmR0DCXJbjCXkFCAL23BnpQgRWt1EMbyujCK9AZzZ"
    "f+b3sX0oSqJQ6EorFeT4NiL6Wtj0+LXnQAzThYoAAsN6ehqR3sHExmcEqGeFApQLcTvm5Kt9"
    "wkHGgb+RZwSkyc1dwOcpCtCoNKSz6FRCUQ3o7Nn+5Y+Lg+y5CIXlcyAk99ziiQS32+svz/UY"
    "vClJoLpIC8gi+VwwfDecEiEtT/WZTJDf94uk1Ru8vbz0cvoF7S2DnpeVL9UAAAAASUVORK5C"
    "YII=")

class MySplashScreen(wx.SplashScreen):
    def __init__(self):
        bmp = wx.Image(opj("resource/splash.png")).ConvertToBitmap()
        wx.SplashScreen.__init__(self, bmp,
                                 wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT,
                                 1000, None, -1)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.fc = wx.FutureCall(1000, self.ShowMain)


    def OnClose(self, evt):
        evt.Skip()
        self.Hide()
        if self.fc.IsRunning():
            self.fc.Stop()
            self.ShowMain()


    def ShowMain(self):
        self.frame = wx.Frame(parent=None, id=-1, size=(500, 500), title='MayMe')  # 框架的实例作为应用程序的一个属性
        self.panel = MyPanel(self.frame, -1)
        self.frame.Center()
        self.frame.Show()
        icon = WXPdemo.GetIcon()
        self.frame.SetIcon(icon)
        if self.fc.IsRunning():
            self.Raise()


class App(wx.App, wx.lib.mixins.inspection.InspectionMixin):

    def OnInit(self):
        self.InitInspection()
        wx.SystemOptions.SetOptionInt("mac.window-plain-transition", 1)
        self.SetAppName("MayMe")
        splash = MySplashScreen()
        splash.Show()
        return True


if __name__ == '__main__':  # 独立运行程序入口
    app = App()
    app.MainLoop()