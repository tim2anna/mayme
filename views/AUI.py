#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import sys

import wx
import wx.html
import wx.grid

try:
    dirName = os.path.dirname(os.path.abspath(__file__))
except:
    dirName = os.path.dirname(os.path.abspath(sys.argv[0]))

sys.path.append(os.path.split(dirName)[0])

try:
    from agw import aui
    from agw.aui import aui_switcherdialog as ASD
except ImportError: # if it's not there locally, try the wxPython lib.
    import wx.lib.agw.aui as aui
    from wx.lib.agw.aui import aui_switcherdialog as ASD

import images

from views.py_images import *
#----------------------------------------------------------------------

# Custom pane bitmaps reference
#                      bitmap  button id       active  maximize
CUSTOM_PANE_BITMAPS = [(close, aui.AUI_BUTTON_CLOSE, True, False),
                       (close_inactive, aui.AUI_BUTTON_CLOSE, False, False),
                       (minimize, aui.AUI_BUTTON_MINIMIZE, True, False),
                       (minimize_inactive, aui.AUI_BUTTON_MINIMIZE, False, False),
                       (maximize, aui.AUI_BUTTON_MAXIMIZE_RESTORE, True, True),
                       (maximize_inactive, aui.AUI_BUTTON_MAXIMIZE_RESTORE, False, True),
                       (restore, aui.AUI_BUTTON_MAXIMIZE_RESTORE, True, False),
                       (restore_inactive, aui.AUI_BUTTON_MAXIMIZE_RESTORE, False, False)]

#----------------------------------------------------------------------
# Custom buttons in tab area
#
CUSTOM_TAB_BUTTONS = {"Left": [(sort, aui.AUI_BUTTON_CUSTOM1),
                               (superscript, aui.AUI_BUTTON_CUSTOM2)],
                      "Right": [(fullscreen, aui.AUI_BUTTON_CUSTOM3),
                                (remove, aui.AUI_BUTTON_CUSTOM4),
                                (reload, aui.AUI_BUTTON_CUSTOM5)]
                      }

#----------------------------------------------------------------------

# Define a translation function
_ = wx.GetTranslation


ID_CREATE_CUSTOMER_PANEL = wx.NewId()
ID_CUSTOMER_PANEL = wx.NewId()
ID_CUSTOMER_IMPORT = wx.NewId()
ID_CUSTOMER_EXPORT = wx.NewId()

ID_CREATE_PRODUCT_PANEL = wx.NewId()
ID_PRODUCT_PANEL = wx.NewId()
ID_PRODUCT_IMPORT = wx.NewId()
ID_PRODUCT_EXPORT = wx.NewId()

ID_CREATE_MATERIAL_PANEL = wx.NewId()
ID_MATERIAL_PANEL = wx.NewId()
ID_MATERIAL_IMPORT = wx.NewId()
ID_MATERIAL_EXPORT = wx.NewId()

ID_CREATE_ORDER_PANEL = wx.NewId()
ID_ORDER_PANEL = wx.NewId()
ID_ORDER_IMPORT = wx.NewId()
ID_ORDER_EXPORT = wx.NewId()


# -- SizeReportCtrl --
# (a utility control that always reports it's client size)
class SizeReportCtrl(wx.PyControl):
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition,
                size=wx.DefaultSize, mgr=None):
        wx.PyControl.__init__(self, parent, id, pos, size, style=wx.NO_BORDER)
        self._mgr = mgr

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_SIZE, self.OnSize)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        size = self.GetClientSize()

        s = "Size: %d x %d"%(size.x, size.y)

        dc.SetFont(wx.NORMAL_FONT)
        w, height = dc.GetTextExtent(s)
        height += 3
        dc.SetBrush(wx.WHITE_BRUSH)
        dc.SetPen(wx.WHITE_PEN)
        dc.DrawRectangle(0, 0, size.x, size.y)
        dc.SetPen(wx.LIGHT_GREY_PEN)
        dc.DrawLine(0, 0, size.x, size.y)
        dc.DrawLine(0, size.y, size.x, 0)
        dc.DrawText(s, (size.x-w)/2, (size.y-height*5)/2)

        if self._mgr:
            pi = self._mgr.GetPane(self)

            s = "Layer: %d"%pi.dock_layer
            w, h = dc.GetTextExtent(s)
            dc.DrawText(s, (size.x-w)/2, ((size.y-(height*5))/2)+(height*1))

            s = "Dock: %d Row: %d"%(pi.dock_direction, pi.dock_row)
            w, h = dc.GetTextExtent(s)
            dc.DrawText(s, (size.x-w)/2, ((size.y-(height*5))/2)+(height*2))

            s = "Position: %d"%pi.dock_pos
            w, h = dc.GetTextExtent(s)
            dc.DrawText(s, (size.x-w)/2, ((size.y-(height*5))/2)+(height*3))

            s = "Proportion: %d"%pi.dock_proportion
            w, h = dc.GetTextExtent(s)
            dc.DrawText(s, (size.x-w)/2, ((size.y-(height*5))/2)+(height*4))

    def OnEraseBackground(self, event):
        pass

    def OnSize(self, event):
        self.Refresh()


class AuiFrame(wx.Frame):

    def __init__(self, parent, id=wx.ID_ANY, title="", pos= wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE|wx.SUNKEN_BORDER, log=None):

        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        # 使用AuiManager管理框架
        self._mgr = aui.AuiManager()
        self._mgr.SetManagedWindow(self)
        # 设置框架图标
        self.SetIcon(images.Mondrian.GetIcon())

        # set up default notebook style
        self._notebook_style = aui.AUI_NB_DEFAULT_STYLE | aui.AUI_NB_TAB_EXTERNAL_MOVE | wx.NO_BORDER
        self._notebook_theme = 0
        # Attributes
        self._textCount = 1
        self._transparency = 255
        self._snapped = False
        self._custom_pane_buttons = False
        self._custom_tab_buttons = False
        self._pane_icons = False
        self._veto_tree = self._veto_text = False

        self.BuildPanes()  # 创建面板
        self.CreateMenuBar()  # 创建菜单栏
        self.BindEvents()  # 绑定事件

    def CreateMenuBar(self):
        # 创建菜单栏
        mb = wx.MenuBar()
        # 创建文件菜单
        file_menu = wx.Menu()
        file_menu.Append(wx.ID_EXIT, u"退出")
        mb.Append(file_menu, u"&文件")
        # 创建窗口菜单
        win_menu = wx.Menu()
        win_menu.Append(ID_CREATE_CUSTOMER_PANEL, u"客户")
        win_menu.Append(ID_CREATE_MATERIAL_PANEL, u"原料")
        win_menu.Append(ID_CREATE_PRODUCT_PANEL, u"产品")
        win_menu.Append(ID_CREATE_ORDER_PANEL, u"订单")
        mb.Append(win_menu, u"&窗口")
        # 创建数据导入菜单
        import_menu = wx.Menu()
        import_menu.Append(ID_CUSTOMER_IMPORT, u"客户")
        import_menu.Append(ID_MATERIAL_IMPORT, u"原料")
        import_menu.Append(ID_PRODUCT_IMPORT, u"产品")
        import_menu.Append(ID_ORDER_IMPORT, u"订单")
        mb.Append(import_menu, u"&数据导入")
        # 创建数据导出菜单
        export_menu = wx.Menu()
        export_menu.Append(ID_CUSTOMER_EXPORT, u"客户")
        export_menu.Append(ID_MATERIAL_EXPORT, u"原料")
        export_menu.Append(ID_PRODUCT_EXPORT, u"产品")
        export_menu.Append(ID_ORDER_EXPORT, u"订单")
        mb.Append(export_menu, u"&数据导出")

        help_menu = wx.Menu()
        help_menu.Append(wx.ID_ABOUT, "About...")
        mb.Append(help_menu, "&Help")

        self.SetMenuBar(mb)

    def BuildPanes(self):
        self.SetMinSize(wx.Size(800, 600))  # 设置最小的尺寸

        # add a bunch of panes
        self._mgr.AddPane(self.CreateTreeCtrl(), aui.AuiPaneInfo().
                          Name("autonotebook").Caption(u"原料").
                          Bottom().Layer(1).Position(1).MinimizeButton(True).MaximizeButton(True).CloseButton(False))

        self._mgr.AddPane(self.CreateCutomerPanel(), aui.AuiPaneInfo().
                          Name("cutomer_panel").Caption(u"客户").
                          Bottom().MinimizeButton(True).MaximizeButton(True).CloseButton(False),
                          target=self._mgr.GetPane("autonotebook"))

        self._mgr.AddPane(self.CreateCutomerPanel(), aui.AuiPaneInfo().
                          Name("cutomer_panel2").Caption(u"产品").
                          Bottom().MinimizeButton(True).MaximizeButton(True).CloseButton(False),
                          target=self._mgr.GetPane("autonotebook"))

        self._mgr.AddPane(self.CreateTreeCtrl(), aui.AuiPaneInfo().
                          Name("thirdauto").Caption(u"订单").
                          Bottom().MinimizeButton(True).MaximizeButton(True).CloseButton(False),
                          target=self._mgr.GetPane("autonotebook"))

        # 创建中间面板
        self._mgr.AddPane(self.CreateHTMLCtrl(), aui.AuiPaneInfo().Name("html_content").CenterPane())

        self._mgr.Update()

    def BindEvents(self):

        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(aui.EVT_AUI_PANE_CLOSE, self.OnPaneClose)
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        self.Bind(wx.EVT_MENU, self.OnCreateCutomerPanel, id=ID_CREATE_CUSTOMER_PANEL)

        self.timer = wx.Timer(self)
        self.timer.Start(100)

    def __del__(self):
        """ 对象销毁时调用 """
        self.timer.Stop()

    def OnClose(self, event):
        """ 窗口关闭事件 """
        self.timer.Stop()
        self._mgr.UnInit()
        event.Skip()


    def OnEraseBackground(self, event):
        event.Skip()


    def OnSize(self, event):
        event.Skip()


    def OnUpdateUI(self, event):

        evId = event.GetId()
        for ids in self._requestPanes:
            if evId == ids:
                paneName = self._requestPanes[ids]
                pane = self._mgr.GetPane(paneName)
                event.Enable(pane.IsShown())


    def OnPaneClose(self, event):
        msg = u"你是否想要"
        if event.GetEventType() == aui.wxEVT_AUI_PANE_MINIMIZE:
            msg += u"最小化 "
        else:
            msg += u"关闭"

        res = wx.MessageBox(msg + u"此窗口?", u'提示', wx.YES_NO, self)
        if res != wx.YES:
            event.Veto()


    def OnExit(self, event):

        self.Close(True)


    def CreateCutomerPanel(self):
        from views.customer_views import CustomerPanel
        ctrl = CustomerPanel(parent=self, data=[])
        return ctrl


    def CreateGrid(self):

        grid = wx.grid.Grid(self, -1, wx.Point(0, 0), wx.Size(150, 250),
                            wx.NO_BORDER | wx.WANTS_CHARS)
        grid.CreateGrid(50, 20)
        return grid


    def CreateTreeCtrl(self):

        tree = wx.TreeCtrl(self, -1, wx.Point(0, 0), wx.Size(160, 250),
                           wx.TR_DEFAULT_STYLE | wx.NO_BORDER)

        imglist = wx.ImageList(16, 16, True, 2)
        imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, wx.Size(16, 16)))
        imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, wx.Size(16, 16)))
        tree.AssignImageList(imglist)

        root = tree.AddRoot("AUI Project", 0)
        items = []

        items.append(tree.AppendItem(root, "Item 1", 0))
        items.append(tree.AppendItem(root, "Item 2", 0))
        items.append(tree.AppendItem(root, "Item 3", 0))
        items.append(tree.AppendItem(root, "Item 4", 0))
        items.append(tree.AppendItem(root, "Item 5", 0))

        for item in items:
            tree.AppendItem(item, "Subitem 1", 1)
            tree.AppendItem(item, "Subitem 2", 1)
            tree.AppendItem(item, "Subitem 3", 1)
            tree.AppendItem(item, "Subitem 4", 1)
            tree.AppendItem(item, "Subitem 5", 1)

        tree.Expand(root)

        return tree


    def CreateSizeReportCtrl(self, width=80, height=80):

        ctrl = SizeReportCtrl(self, -1, wx.DefaultPosition, wx.Size(width, height), self._mgr)
        return ctrl


    def CreateHTMLCtrl(self, parent=None):
        from views.customer_views import CustomerPanel
        if not parent:
            parent = self
        ctrl = CustomerPanel(parent=parent, data=[])
        return ctrl


    def OnCreateCutomerPanel(self, event):
        self._mgr.AddPane(self.CreateCutomerPanel(), aui.AuiPaneInfo().
                          Caption(u"客户").
                          Float().FloatingPosition(self.GetStartPosition()).
                          FloatingSize(wx.Size(150, 300)).MinimizeButton(True))
        self._mgr.Update()

    def GetStartPosition(self):
        """ 获取新建面板的开始位置 """
        x = 20
        pt = self.ClientToScreen(wx.Point(0, 0))
        return wx.Point(pt.x + x, pt.y + x)


#----------------------------------------------------------------------
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = AuiFrame(None, -1, "MayMe", size=(800, 600))
    frame.CenterOnScreen()  # 框架屏幕居中
    frame.Show()
    app.MainLoop()
