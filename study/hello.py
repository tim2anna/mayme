#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""Hello, wxPython! program."""

import wx


class Frame(wx.Frame):
    """显示一幅图片"""

    def __init__(self, image, parent=None, id=-1, pos=wx.DefaultPosition, title='Hello, wxPython!'):
        temp = image.ConvertToBitmap()
        size = temp.GetWidth(), temp.GetHeight()
        wx.Frame.__init__(self, parent, id, title, pos, size)
        self.bmp = wx.StaticBitmap(parent=self, bitmap=temp)


class App(wx.App):

    def OnInit(self):
        image = wx.Image('wxPython.png', wx.BITMAP_TYPE_PNG)
        self.frame = Frame(image)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True


def main():
    app = App()
    app.MainLoop()


if __name__ == '__main__':
    main()