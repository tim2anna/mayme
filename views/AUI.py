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

ArtIDs = [ "wx.ART_ADD_BOOKMARK",
           "wx.ART_DEL_BOOKMARK",
           "wx.ART_HELP_SIDE_PANEL",
           "wx.ART_HELP_SETTINGS",
           "wx.ART_HELP_BOOK",
           "wx.ART_HELP_FOLDER",
           "wx.ART_HELP_PAGE",
           "wx.ART_GO_BACK",
           "wx.ART_GO_FORWARD",
           "wx.ART_GO_UP",
           "wx.ART_GO_DOWN",
           "wx.ART_GO_TO_PARENT",
           "wx.ART_GO_HOME",
           "wx.ART_FILE_OPEN",
           "wx.ART_PRINT",
           "wx.ART_HELP",
           "wx.ART_TIP",
           "wx.ART_REPORT_VIEW",
           "wx.ART_LIST_VIEW",
           "wx.ART_NEW_DIR",
           "wx.ART_HARDDISK",
           "wx.ART_FLOPPY",
           "wx.ART_CDROM",
           "wx.ART_REMOVABLE",
           "wx.ART_FOLDER",
           "wx.ART_FOLDER_OPEN",
           "wx.ART_GO_DIR_UP",
           "wx.ART_EXECUTABLE_FILE",
           "wx.ART_NORMAL_FILE",
           "wx.ART_TICK_MARK",
           "wx.ART_CROSS_MARK",
           "wx.ART_ERROR",
           "wx.ART_QUESTION",
           "wx.ART_WARNING",
           "wx.ART_INFORMATION",
           "wx.ART_MISSING_IMAGE",
           ]
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


ID_CreateTree = wx.ID_HIGHEST + 1
ID_CreateGrid = ID_CreateTree + 1
ID_CreateText = ID_CreateTree + 2
ID_CreateHTML = ID_CreateTree + 3
ID_CreateNotebook = ID_CreateTree + 4
ID_CreateSizeReport = ID_CreateTree + 5
ID_GridContent = ID_CreateTree + 6
ID_TextContent = ID_CreateTree + 7
ID_TreeContent = ID_CreateTree + 8
ID_HTMLContent = ID_CreateTree + 9
ID_NotebookContent = ID_CreateTree + 10
ID_SizeReportContent = ID_CreateTree + 11
ID_SwitchPane = ID_CreateTree + 12
ID_CreatePerspective = ID_CreateTree + 13
ID_CopyPerspectiveCode = ID_CreateTree + 14
ID_CreateNBPerspective = ID_CreateTree + 15
ID_CopyNBPerspectiveCode = ID_CreateTree + 16
ID_AllowFloating = ID_CreateTree + 17
ID_AllowActivePane = ID_CreateTree + 18
ID_TransparentHint = ID_CreateTree + 19
ID_VenetianBlindsHint = ID_CreateTree + 20
ID_RectangleHint = ID_CreateTree + 21
ID_NoHint = ID_CreateTree + 22
ID_HintFade = ID_CreateTree + 23
ID_NoVenetianFade = ID_CreateTree + 24
ID_TransparentDrag = ID_CreateTree + 25
ID_NoGradient = ID_CreateTree + 26
ID_VerticalGradient = ID_CreateTree + 27
ID_HorizontalGradient = ID_CreateTree + 28
ID_LiveUpdate = ID_CreateTree + 29
ID_AnimateFrames = ID_CreateTree + 30
ID_PaneIcons = ID_CreateTree + 31
ID_TransparentPane = ID_CreateTree + 32
ID_DefaultDockArt = ID_CreateTree + 33
ID_ModernDockArt = ID_CreateTree + 34
ID_SnapToScreen = ID_CreateTree + 35
ID_SnapPanes = ID_CreateTree + 36
ID_FlyOut = ID_CreateTree + 37
ID_CustomPaneButtons = ID_CreateTree + 38
ID_Settings = ID_CreateTree + 39
ID_MinimizePosSmart = ID_CreateTree + 42
ID_MinimizePosTop = ID_CreateTree + 43
ID_MinimizePosLeft = ID_CreateTree + 44
ID_MinimizePosRight = ID_CreateTree + 45
ID_MinimizePosBottom = ID_CreateTree + 46
ID_MinimizeCaptSmart = ID_CreateTree + 47
ID_MinimizeCaptHorz = ID_CreateTree + 48
ID_MinimizeCaptHide = ID_CreateTree + 49

ID_SampleItem = ID_CreateTree + 77
ID_StandardGuides = ID_CreateTree + 78
ID_AeroGuides = ID_CreateTree + 79
ID_WhidbeyGuides = ID_CreateTree + 80
ID_NotebookPreview = ID_CreateTree + 81
ID_PreviewMinimized = ID_CreateTree + 82

ID_SmoothDocking = ID_CreateTree + 83
ID_NativeMiniframes = ID_CreateTree + 84

ID_FirstPerspective = ID_CreatePerspective + 1000
ID_FirstNBPerspective = ID_CreateNBPerspective + 10000

ID_PaneBorderSize = ID_SampleItem + 100
ID_SashSize = ID_PaneBorderSize + 2
ID_CaptionSize = ID_PaneBorderSize + 3
ID_BackgroundColour = ID_PaneBorderSize + 4
ID_SashColour = ID_PaneBorderSize + 5
ID_InactiveCaptionColour = ID_PaneBorderSize + 6
ID_InactiveCaptionGradientColour = ID_PaneBorderSize + 7
ID_InactiveCaptionTextColour = ID_PaneBorderSize + 8
ID_ActiveCaptionColour = ID_PaneBorderSize + 9
ID_ActiveCaptionGradientColour = ID_PaneBorderSize + 10
ID_ActiveCaptionTextColour = ID_PaneBorderSize + 11
ID_BorderColour = ID_PaneBorderSize + 12
ID_GripperColour = ID_PaneBorderSize + 13
ID_SashGrip = ID_PaneBorderSize + 14
ID_HintColour = ID_PaneBorderSize + 15

ID_VetoTree = ID_PaneBorderSize + 16
ID_VetoText = ID_PaneBorderSize + 17
ID_NotebookMultiLine = ID_PaneBorderSize + 18


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
        # 创建视图菜单
        view_menu = wx.Menu()
        view_menu.Append(ID_CreateText, "Create Text Control")
        view_menu.Append(ID_CreateHTML, "Create HTML Control")
        view_menu.Append(ID_CreateTree, "Create Tree")
        view_menu.Append(ID_CreateGrid, "Create Grid")
        view_menu.Append(ID_CreateSizeReport, "Create Size Reporter")
        view_menu.AppendSeparator()
        view_menu.Append(ID_GridContent, "Use a Grid for the Content Pane")
        view_menu.Append(ID_TextContent, "Use a Text Control for the Content Pane")
        view_menu.Append(ID_HTMLContent, "Use an HTML Control for the Content Pane")
        view_menu.Append(ID_TreeContent, "Use a Tree Control for the Content Pane")
        view_menu.Append(ID_SizeReportContent, "Use a Size Reporter for the Content Pane")
        view_menu.AppendSeparator()
        mb.Append(view_menu, u"&视图")

        help_menu = wx.Menu()
        help_menu.Append(wx.ID_ABOUT, "About...")
        mb.Append(help_menu, "&Help")

        self.SetMenuBar(mb)

    def BuildPanes(self):
        self.SetMinSize(wx.Size(800, 600))  # 设置最小的尺寸

        # add a bunch of panes
        self._mgr.AddPane(self.CreateSizeReportCtrl(), aui.AuiPaneInfo().
                          Name("test1").Caption("Pane Caption").Top().MinimizeButton(True))

        self._mgr.AddPane(self.CreateSizeReportCtrl(), aui.AuiPaneInfo().
                          Name("test2").Caption("Client Size Reporter").
                          Bottom().Position(1).CloseButton(True).MaximizeButton(True).
                          MinimizeButton(True).CaptionVisible(True, left=True))

        self._mgr.AddPane(self.CreateSizeReportCtrl(), aui.AuiPaneInfo().
                          Name("test3").Caption("Client Size Reporter").
                          Bottom().CloseButton(True).MaximizeButton(True).MinimizeButton(True).
                          CaptionVisible(True, left=True))

        self._mgr.AddPane(self.CreateSizeReportCtrl(), aui.AuiPaneInfo().
                          Name("test4").Caption("Pane Caption").Left())

        self._mgr.AddPane(self.CreateSizeReportCtrl(), aui.AuiPaneInfo().
                          Name("test5").Caption("No Close Button").Right().CloseButton(False))

        self._mgr.AddPane(self.CreateSizeReportCtrl(), aui.AuiPaneInfo().
                          Name("test6").Caption("Client Size Reporter").Right().Row(1).
                          CloseButton(True).MaximizeButton(True).MinimizeButton(True))

        self._mgr.AddPane(self.CreateSizeReportCtrl(), aui.AuiPaneInfo().
                          Name("test7").Caption("Client Size Reporter").Left().Layer(1).
                          CloseButton(True).MaximizeButton(True).MinimizeButton(True))

        self._mgr.AddPane(self.CreateTreeCtrl(), aui.AuiPaneInfo().Name("test8").Caption("Tree Pane").
                          Left().Layer(1).Position(1).CloseButton(True).MaximizeButton(True).
                          MinimizeButton(True))

        self._mgr.AddPane(self.CreateSizeReportCtrl(), aui.AuiPaneInfo().
                          Name("test9").Caption("Min Size 200x100").
                          BestSize(wx.Size(200,100)).MinSize(wx.Size(200,100)).Bottom().Layer(1).
                          CloseButton(True).MaximizeButton(True).MinimizeButton(True))

        self._mgr.AddPane(self.CreateTreeCtrl(), aui.AuiPaneInfo().
                          Name("autonotebook").Caption("Auto NB").
                          Bottom().Layer(1).Position(1).MinimizeButton(True))

        wnd10 = self.CreateTextCtrl("This pane will prompt the user before hiding.")
        self._mgr.AddPane(wnd10, aui.AuiPaneInfo().
                          Name("test10").Caption("Text Pane with Hide Prompt").
                          Bottom().MinimizeButton(True), target=self._mgr.GetPane("autonotebook"))

        self._mgr.AddPane(self.CreateTreeCtrl(), aui.AuiPaneInfo().
                          Name("thirdauto").Caption("A Third Auto-NB Pane").
                          Bottom().MinimizeButton(True), target=self._mgr.GetPane("autonotebook"))

        self._mgr.AddPane(self.CreateSizeReportCtrl(), aui.AuiPaneInfo().
                          Name("test11").Caption("Fixed Pane").
                          Bottom().Layer(1).Position(2).Fixed().MinimizeButton(True))

        # create some center panes

        self._mgr.AddPane(self.CreateGrid(), aui.AuiPaneInfo().Name("grid_content").
                          CenterPane().Hide().MinimizeButton(True))

        self._mgr.AddPane(self.CreateTreeCtrl(), aui.AuiPaneInfo().Name("tree_content").
                          CenterPane().Hide().MinimizeButton(True))

        self._mgr.AddPane(self.CreateSizeReportCtrl(), aui.AuiPaneInfo().Name("sizereport_content").
                          CenterPane().Hide().MinimizeButton(True))

        self._mgr.AddPane(self.CreateTextCtrl(), aui.AuiPaneInfo().Name("text_content").
                          CenterPane().Hide().MinimizeButton(True))

        self._mgr.AddPane(self.CreateHTMLCtrl(), aui.AuiPaneInfo().Name("html_content").
                          CenterPane().Hide().PaneBorder(False))

        self._mgr.AddPane(self.CreateNotebook(), aui.AuiPaneInfo().Name("notebook_content").
                          CenterPane().Hide().MinimizeButton(True))

        self._mgr.AddPane(wx.Button(self, -1, "Test Button"),
                          aui.AuiPaneInfo().Name("tb7").ToolbarPane().Top().Row(2).Position(1))

        # Show how to add a control inside a tab
        html = self._mgr.GetPane("html_content").window
        self._main_notebook = html

        # make some default perspectives
        perspective_all = self._mgr.SavePerspective()

        all_panes = self._mgr.GetAllPanes()
        for pane in all_panes:
            if not pane.IsToolbar():
                pane.Hide()

        self._mgr.GetPane("tb1").Hide()
        self._mgr.GetPane("tb7").Hide()

        self._mgr.GetPane("test8").Show().Left().Layer(0).Row(0).Position(0)
        self._mgr.GetPane("__notebook_%d"%self._mgr.GetPane("test10").notebook_id).Show().Bottom().Layer(0).Row(0).Position(0)
        self._mgr.GetPane("autonotebook").Show()
        self._mgr.GetPane("thirdauto").Show()
        self._mgr.GetPane("test10").Show()
        self._mgr.GetPane("html_content").Show()

        perspective_default = self._mgr.SavePerspective()

        self._perspectives = []
        self._perspectives.append(perspective_default)
        self._perspectives.append(perspective_all)

        self._mgr.LoadPerspective(perspective_default)

        self._mgr.Update()  # "commit" all changes made to AuiManager

    def BindEvents(self):

        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_SIZE, self.OnSize)

        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_AllowFloating)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_TransparentHint)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_HintFade)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_TransparentDrag)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NoGradient)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_VerticalGradient)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_HorizontalGradient)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_VenetianBlindsHint)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_RectangleHint)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NoHint)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NoVenetianFade)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_LiveUpdate)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_PaneIcons)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_AnimateFrames)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_DefaultDockArt)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_ModernDockArt)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_SnapPanes)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_FlyOut)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_CustomPaneButtons)

        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_VetoTree)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_VetoText)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_StandardGuides)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_AeroGuides)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_WhidbeyGuides)

        self.Bind(aui.EVT_AUI_PANE_CLOSE, self.OnPaneClose)

        self.Bind(aui.EVT_AUI_PANE_FLOATING, self.OnFloatDock)
        self.Bind(aui.EVT_AUI_PANE_FLOATED, self.OnFloatDock)
        self.Bind(aui.EVT_AUI_PANE_DOCKING, self.OnFloatDock)
        self.Bind(aui.EVT_AUI_PANE_DOCKED, self.OnFloatDock)

        self.Bind(wx.EVT_CLOSE, self.OnClose)

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


    def GetDockArt(self):

        return self._mgr.GetArtProvider()


    def DoUpdate(self):

        self._mgr.Update()
        self.Refresh()


    def OnEraseBackground(self, event):

        event.Skip()


    def OnSize(self, event):

        event.Skip()


    def OnUpdateUI(self, event):

        agwFlags = self._mgr.GetAGWFlags()
        evId = event.GetId()

        if evId == ID_NoGradient:
            event.Check(self._mgr.GetArtProvider().GetMetric(aui.AUI_DOCKART_GRADIENT_TYPE) == aui.AUI_GRADIENT_NONE)

        elif evId == ID_VerticalGradient:
            event.Check(self._mgr.GetArtProvider().GetMetric(aui.AUI_DOCKART_GRADIENT_TYPE) == aui.AUI_GRADIENT_VERTICAL)

        elif evId == ID_HorizontalGradient:
            event.Check(self._mgr.GetArtProvider().GetMetric(aui.AUI_DOCKART_GRADIENT_TYPE) == aui.AUI_GRADIENT_HORIZONTAL)

        elif evId == ID_AllowFloating:
            event.Check((agwFlags & aui.AUI_MGR_ALLOW_FLOATING) != 0)

        elif evId == ID_TransparentDrag:
            event.Check((agwFlags & aui.AUI_MGR_TRANSPARENT_DRAG) != 0)

        elif evId == ID_TransparentHint:
            event.Check((agwFlags & aui.AUI_MGR_TRANSPARENT_HINT) != 0)

        elif evId == ID_LiveUpdate:
            event.Check(aui.AuiManager_HasLiveResize(self._mgr))

        elif evId == ID_VenetianBlindsHint:
            event.Check((agwFlags & aui.AUI_MGR_VENETIAN_BLINDS_HINT) != 0)

        elif evId == ID_RectangleHint:
            event.Check((agwFlags & aui.AUI_MGR_RECTANGLE_HINT) != 0)

        elif evId == ID_NoHint:
            event.Check(((aui.AUI_MGR_TRANSPARENT_HINT |
                              aui.AUI_MGR_VENETIAN_BLINDS_HINT |
                              aui.AUI_MGR_RECTANGLE_HINT) & agwFlags) == 0)

        elif evId == ID_HintFade:
            event.Check((agwFlags & aui.AUI_MGR_HINT_FADE) != 0)

        elif evId == ID_NoVenetianFade:
            event.Check((agwFlags & aui.AUI_MGR_NO_VENETIAN_BLINDS_FADE) != 0)

        elif evId == ID_NativeMiniframes:
            event.Check(aui.AuiManager_UseNativeMiniframes(self._mgr))

        elif evId == ID_PaneIcons:
            event.Check(self._pane_icons)

        elif evId == ID_SmoothDocking:
            event.Check((agwFlags & aui.AUI_MGR_SMOOTH_DOCKING) != 0)

        elif evId == ID_AnimateFrames:
            event.Check((agwFlags & aui.AUI_MGR_ANIMATE_FRAMES) != 0)

        elif evId == ID_DefaultDockArt:
            event.Check(isinstance(self._mgr.GetArtProvider(), aui.AuiDefaultDockArt))

        elif evId == ID_ModernDockArt:
            event.Check(isinstance(self._mgr.GetArtProvider(), aui.ModernDockArt))

        elif evId == ID_SnapPanes:
            event.Check(self._snapped)

        elif evId == ID_FlyOut:
            pane = self._mgr.GetPane("test8")
            event.Check(pane.IsFlyOut())

        elif evId == ID_AeroGuides:
            event.Check(agwFlags & aui.AUI_MGR_AERO_DOCKING_GUIDES != 0)

        elif evId == ID_WhidbeyGuides:
            event.Check(agwFlags & aui.AUI_MGR_WHIDBEY_DOCKING_GUIDES != 0)

        elif evId == ID_StandardGuides:
            event.Check((agwFlags & aui.AUI_MGR_AERO_DOCKING_GUIDES == 0) and (agwFlags & aui.AUI_MGR_WHIDBEY_DOCKING_GUIDES == 0))

        elif evId == ID_CustomPaneButtons:
            event.Check(self._custom_pane_buttons)

        elif evId == ID_PreviewMinimized:
            event.Check(agwFlags & aui.AUI_MGR_PREVIEW_MINIMIZED_PANES)

        elif evId == ID_VetoTree:
            event.Check(self._veto_tree)

        elif evId == ID_VetoText:
            event.Check(self._veto_text)

        else:
            for ids in self._requestPanes:
                if evId == ids:
                    paneName = self._requestPanes[ids]
                    pane = self._mgr.GetPane(paneName)
                    event.Enable(pane.IsShown())


    def OnPaneClose(self, event):

        if event.pane.name == "test10":

            msg = "Are you sure you want to "
            if event.GetEventType() == aui.wxEVT_AUI_PANE_MINIMIZE:
                msg += "minimize "
            else:
                msg += "close/hide "

            res = wx.MessageBox(msg + "this pane?", "AUI", wx.YES_NO, self)
            if res != wx.YES:
                event.Veto()


    def GetStartPosition(self):

        x = 20
        pt = self.ClientToScreen(wx.Point(0, 0))
        return wx.Point(pt.x + x, pt.y + x)



    def OnPreview(self, event):

        auibook = self._mgr.GetPane("notebook_content").window
        auibook.NotebookPreview()


    def OnAddMultiLine(self, event):

        auibook = self._mgr.GetPane("notebook_content").window

        auibook.InsertPage(1, wx.TextCtrl(auibook, -1, "Some more text", wx.DefaultPosition, wx.DefaultSize,
                                          wx.TE_MULTILINE|wx.NO_BORDER), "Multi-Line\nTab Labels", True)

        auibook.SetPageTextColour(1, wx.BLUE)


    def OnFloatDock(self, event):

        paneLabel = event.pane.caption
        etype = event.GetEventType()

        strs = "Pane %s "%paneLabel
        if etype == aui.wxEVT_AUI_PANE_FLOATING:
            strs += "is about to be floated"

            if event.pane.name == "test8" and self._veto_tree:
                event.Veto()
                strs += "... Event vetoed by user selection!"
                self.log.write(strs + "\n")
                return

        elif etype == aui.wxEVT_AUI_PANE_FLOATED:
            strs += "has been floated"
        elif etype == aui.wxEVT_AUI_PANE_DOCKING:
            strs += "is about to be docked"

            if event.pane.name == "test11" and self._veto_text:
                event.Veto()
                strs += "... Event vetoed by user selection!"
                self.log.write(strs + "\n")
                return

        elif etype == aui.wxEVT_AUI_PANE_DOCKED:
            strs += "has been docked"


    def OnExit(self, event):

        self.Close(True)


    def CreateTextCtrl(self, ctrl_text=""):

        if ctrl_text.strip():
            text = ctrl_text
        else:
            text = "This is text box %d"%self._textCount
            self._textCount += 1

        return wx.TextCtrl(self,-1, text, wx.Point(0, 0), wx.Size(150, 90),
                           wx.NO_BORDER | wx.TE_MULTILINE)


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

        if not parent:
            parent = self

        ctrl = wx.html.HtmlWindow(parent, -1, wx.DefaultPosition, wx.Size(400, 300))
        ctrl.SetPage('Welcome to MayMe')
        return ctrl


    def CreateNotebook(self):

        # create the notebook off-window to avoid flicker
        client_size = self.GetClientSize()
        ctrl = aui.AuiNotebook(self, -1, wx.Point(client_size.x, client_size.y),
                              wx.Size(430, 200), agwStyle=self._notebook_style)

        arts = [aui.AuiDefaultTabArt, aui.AuiSimpleTabArt, aui.VC71TabArt, aui.FF2TabArt,
                aui.VC8TabArt, aui.ChromeTabArt]

        art = arts[self._notebook_theme]()
        ctrl.SetArtProvider(art)

        page_bmp = wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, wx.Size(16, 16))
        ctrl.AddPage(self.CreateHTMLCtrl(ctrl), "Welcome to AUI", False, page_bmp)

        panel = wx.Panel(ctrl, -1)
        flex = wx.FlexGridSizer(0, 2)
        flex.Add((5, 5))
        flex.Add((5, 5))
        flex.Add(wx.StaticText(panel, -1, "wxTextCtrl:"), 0, wx.ALL|wx.ALIGN_CENTRE, 5)
        flex.Add(wx.TextCtrl(panel, -1, "", wx.DefaultPosition, wx.Size(100, -1)),
                 1, wx.ALL|wx.ALIGN_CENTRE, 5)
        flex.Add(wx.StaticText(panel, -1, "wxSpinCtrl:"), 0, wx.ALL|wx.ALIGN_CENTRE, 5)
        flex.Add(wx.SpinCtrl(panel, -1, "5", wx.DefaultPosition, wx.Size(100, -1),
                             wx.SP_ARROW_KEYS, 5, 50, 5), 0, wx.ALL|wx.ALIGN_CENTRE, 5)
        flex.Add((5, 5))
        flex.Add((5, 5))
        flex.AddGrowableRow(0)
        flex.AddGrowableRow(3)
        flex.AddGrowableCol(1)
        panel.SetSizer(flex)
        ctrl.AddPage(panel, "Disabled", False, page_bmp)

        ctrl.AddPage(wx.TextCtrl(ctrl, -1, "Some text", wx.DefaultPosition, wx.DefaultSize,
                                 wx.TE_MULTILINE|wx.NO_BORDER), "DClick Edit!", False, page_bmp)

        ctrl.AddPage(wx.TextCtrl(ctrl, -1, "Some more text", wx.DefaultPosition, wx.DefaultSize,
                                 wx.TE_MULTILINE|wx.NO_BORDER), "Blue Tab")

        ctrl.AddPage(wx.TextCtrl(ctrl, -1, "Some more text", wx.DefaultPosition, wx.DefaultSize,
                                 wx.TE_MULTILINE|wx.NO_BORDER), "A Control")

        ctrl.AddPage(wx.TextCtrl(ctrl, -1, "Some more text", wx.DefaultPosition, wx.DefaultSize,
                                 wx.TE_MULTILINE|wx.NO_BORDER), "wxTextCtrl 4")

        ctrl.AddPage(wx.TextCtrl(ctrl, -1, "Some more text", wx.DefaultPosition, wx.DefaultSize,
                                 wx.TE_MULTILINE|wx.NO_BORDER), "wxTextCtrl 5")

        ctrl.AddPage(wx.TextCtrl(ctrl, -1, "Some more text", wx.DefaultPosition, wx.DefaultSize,
                                 wx.TE_MULTILINE|wx.NO_BORDER), "wxTextCtrl 6")

        ctrl.AddPage(wx.TextCtrl(ctrl, -1, "Some more text", wx.DefaultPosition, wx.DefaultSize,
                                 wx.TE_MULTILINE|wx.NO_BORDER), "wxTextCtrl 7 (longer title)")

        ctrl.AddPage(wx.TextCtrl(ctrl, -1, "Some more text", wx.DefaultPosition, wx.DefaultSize,
                                 wx.TE_MULTILINE|wx.NO_BORDER), "wxTextCtrl 8")

        # Demonstrate how to disable a tab
        ctrl.EnableTab(1, False)

        ctrl.SetPageTextColour(2, wx.RED)
        ctrl.SetPageTextColour(3, wx.BLUE)
        ctrl.SetRenamable(2, True)

        return ctrl


    def OnSwitchPane(self, event):

        items = ASD.SwitcherItems()
        items.SetRowCount(12)

        # Add the main windows and toolbars, in two separate columns
        # We'll use the item 'id' to store the notebook selection, or -1 if not a page

        for k in xrange(2):
            if k == 0:
                items.AddGroup(_("Main Windows"), "mainwindows")
            else:
                items.AddGroup(_("Toolbars"), "toolbars").BreakColumn()

            for pane in self._mgr.GetAllPanes():
                name = pane.name
                caption = pane.caption
                if not caption:
                    continue

                toolBar = isinstance(pane.window, wx.ToolBar) or isinstance(pane.window, aui.AuiToolBar)
                bitmap = (pane.icon.IsOk() and [pane.icon] or [wx.NullBitmap])[0]

                if (toolBar and k == 1) or (not toolBar and k == 0):
                    items.AddItem(caption, name, -1, bitmap).SetWindow(pane.window)

        # Now add the wxAuiNotebook pages
        items.AddGroup(_("Notebook Pages"), "pages").BreakColumn()

        for pane in self._mgr.GetAllPanes():
            nb = pane.window
            if isinstance(nb, aui.AuiNotebook):
                for j in xrange(nb.GetPageCount()):

                    name = nb.GetPageText(j)
                    win = nb.GetPage(j)

                    items.AddItem(name, name, j, nb.GetPageBitmap(j)).SetWindow(win)

        # Select the focused window

        idx = items.GetIndexForFocus()
        if idx != wx.NOT_FOUND:
            items.SetSelection(idx)

        if wx.Platform == "__WXMAC__":
            items.SetBackgroundColour(wx.WHITE)

        # Show the switcher dialog

        dlg = ASD.SwitcherDialog(items, self, self._mgr)

        # In GTK+ we can't use Ctrl+Tab; we use Ctrl+/ instead and tell the switcher
        # to treat / in the same was as tab (i.e. cycle through the names)

        if wx.Platform == "__WXGTK__":
            dlg.SetExtraNavigationKey('/')

        if wx.Platform == "__WXMAC__":
            dlg.SetBackgroundColour(wx.WHITE)
            dlg.SetModifierKey(wx.WXK_ALT)

        ans = dlg.ShowModal()

        if ans == wx.ID_OK and dlg.GetSelection() != -1:
            item = items.GetItem(dlg.GetSelection())

            if item.GetId() == -1:
                info = self._mgr.GetPane(item.GetName())
                info.Show()
                self._mgr.Update()
                info.window.SetFocus()

            else:
                nb = item.GetWindow().GetParent()
                win = item.GetWindow()
                if isinstance(nb, aui.AuiNotebook):
                    nb.SetSelection(item.GetId())
                    win.SetFocus()


#----------------------------------------------------------------------
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = AuiFrame(None, -1, "MayMe", size=(800, 600))
    frame.CenterOnScreen()  # 框架屏幕居中
    frame.Show()
    app.MainLoop()
