#!/usr/bin/env python
#-*- coding:utf-8 -*-

import wx
import wx.aui

from views.customer_views import CustomerPanel


ID_GridContent = wx.NewId()
ID_TextContent = wx.NewId()

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'MayMe', size=(640, 480),
                          style=wx.DEFAULT_FRAME_STYLE | wx.NO_FULL_REPAINT_ON_RESIZE)
        self.SetMinSize((640, 480))

        self._mgr = wx.aui.AuiManager()
        self._mgr.SetManagedWindow(self)

        panel = wx.Panel(self, -1)
        wx.StaticText(panel, -1, "Welcome to MayMe", pos=(0, 100), size=(640, 480), style=wx.ALIGN_CENTER)

        self._mgr.AddPane(CustomerPanel(self, data=[]))
        self._mgr.AddPane(panel)

        # 添加菜单工具栏
        menuBar = wx.MenuBar()

        menu_customer = wx.Menu()
        menu_item_customer_view = menu_customer.Append(ID_GridContent, u"查看", u"查看所有客户信息")
        menu_item_customer_view2 = menu_customer.Append(ID_TextContent, u"查看2", u"查看所有客户信息")
        self.Bind(wx.EVT_MENU, self.OnChangeContentPane, menu_item_customer_view)
        self.Bind(wx.EVT_MENU, self.OnChangeContentPane, menu_item_customer_view2)
        menuBar.Append(menu_customer, u"客户信息")

        self.SetMenuBar(menuBar)

    def OnChangeContentPane(self, event):
        self._mgr.GetPane("grid_content").Show(event.GetId() == ID_GridContent)
        self._mgr.GetPane("text_content").Show(event.GetId() == ID_TextContent)
        self._mgr.Update()

    def OnViewCustomer(self, event):
        self.panel.Destroy()
        self.customer_panel = CustomerPanel(self, data=[])


if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()