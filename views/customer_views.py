#!/usr/bin/env python
#-*- coding:utf-8 -*-

""" 客户管理 """

import wx
import wx.dataview as dv


class CustomerModel(dv.PyDataViewIndexListModel):
    def __init__(self, data):
        dv.PyDataViewIndexListModel.__init__(self, len(data))
        self.data = data

    def GetColumnType(self, col):
        """ 获取列类型 """
        return "string"

    def GetValueByRow(self, row, col):
        """ 设定特定单元格的值 """
        return self.data[row][col]

    def SetValueByRow(self, value, row, col):
        """ 用户编辑数据时调用此方法 """
        self.data[row][col] = value

    def GetColumnCount(self):
        """ 获取数据的总列数 """
        return len(self.data[0])

    def GetCount(self):
        """ 获取数据的总行数 """
        return len(self.data)

    def GetAttrByRow(self, row, col, attr):
        """ 设定特定单元格(row,col)的属性 """
        return False

    def Compare(self, item1, item2, col, ascending):
        """ 排序 """
        if not ascending: # swap sort order?
            item2, item1 = item1, item2
        row1 = self.GetRow(item1)
        row2 = self.GetRow(item2)
        if col == 0:
            return cmp(int(self.data[row1][col]), int(self.data[row2][col]))
        else:
            return cmp(self.data[row1][col], self.data[row2][col])

    def DeleteRows(self, rows):
        """ 删除数据行 """
        rows = list(rows)  # make a copy since we'll be sorting(mutating) the list
        rows.sort(reverse=True)  # use reverse order so the indexes don't change as we remove items
        for row in rows:
            del self.data[row]  # remove it from our data structure
            self.RowDeleted(row)  # notify the view(s) using this model that it has been removed

    def AddRow(self, value):
        """ 增加数据行 """
        self.data.append(value)  # update data structure
        self.RowAppended()  # notify views


class CustomerPanel(wx.Panel):
    def __init__(self, parent, model=None, data=None, size=wx.Size(100, 100)):
        wx.Panel.__init__(self, parent, -1, size=size)
        # Create a dataview control
        self.dvc = dv.DataViewCtrl(self,style=wx.BORDER_THEME | dv.DV_ROW_LINES | dv.DV_VERT_RULES | dv.DV_MULTIPLE)

        # Create an instance of our simple model...
        if model is None:
            self.model = CustomerModel(data)
        else:
            self.model = model

        self.dvc.AssociateModel(self.model)

        self.dvc.AppendTextColumn("Artist",  1, width=170, mode=dv.DATAVIEW_CELL_EDITABLE)
        self.dvc.AppendTextColumn("Title",   2, width=260, mode=dv.DATAVIEW_CELL_EDITABLE)
        self.dvc.AppendTextColumn("Genre",   3, width=80,  mode=dv.DATAVIEW_CELL_EDITABLE)

        c0 = self.dvc.PrependTextColumn("Id", 0, width=40)
        c0.Alignment = wx.ALIGN_RIGHT
        c0.Renderer.Alignment = wx.ALIGN_RIGHT
        c0.MinWidth = 40

        for c in self.dvc.Columns:
            c.Sortable = True
            c.Reorderable = True
        c0.Reorderable = False

        self.Sizer = wx.BoxSizer(wx.VERTICAL)
        self.Sizer.Add(self.dvc, 1, wx.EXPAND)

        # Bind some events so we can see what the DVC sends us
        self.Bind(dv.EVT_DATAVIEW_ITEM_EDITING_DONE, self.OnEditingDone, self.dvc)
        self.Bind(dv.EVT_DATAVIEW_ITEM_VALUE_CHANGED, self.OnValueChanged, self.dvc)

    def OnNewView(self, evt):
        """ 在新窗口中显示视图 """
        f = wx.Frame(None, title="New view, shared model", size=(600,400))
        CustomerPanel(f, self.model)
        b = f.FindWindowByName("newView")
        b.Disable()
        f.Show()

    def OnDeleteRows(self, evt):
        """ 删除数据行事件 """
        items = self.dvc.GetSelections()
        rows = [self.model.GetRow(item) for item in items]
        self.model.DeleteRows(rows)
        # TODO: 从数据库中删除

    def OnAddRow(self, evt):
        """ 添加数据行事件 """
        # Add some bogus data to a new row in the model's data
        id = len(self.model.data) + 1
        value = [str(id),
                 'new artist %d' % id,
                 'new title %d' % id,
                 'genre %d' % id]
        self.model.AddRow(value)
        # TODO: 插入数据库


    def OnEditingDone(self, evt):
        """ 编辑完成后事件 """

    def OnValueChanged(self, evt):
        """ 值改变后事件 """


class App(wx.App):

    def OnInit(self):
        self.frame = wx.Frame(parent=None, id=-1, size=(970, 720))  # 框架的实例作为应用程序的一个属性
        self.panel = CustomerPanel(parent=self.frame, data=[])
        self.frame.Show()
        self.SetTopWindow(self.frame)  # 一个应用程序可以多个框架，设置顶级窗口
        return True


if __name__ == '__main__':  # 独立运行程序入口
    app = App()
    app.MainLoop()

