#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
读取原始资料数据

包括：
    1. 各个客户订单excel
    2. 产品用料成本excel

输出：
    1. 所有客户的订单合计excel
    2. 所有订单的用料合计excel
    3. 所有订单的成本合计excel
"""

import os
import xlrd

order_cols = [
    (u'款号', 'style'),
    (u'颜色', 'color'),
    (u'S', 's_size'),
    (u'M', 'm_size'),
    (u'L', 'l_size'),
    (u'XL', 'xl_size'),
    (u'2XL', '2xl_size'),
    (u'3XL', '3xl_size'),
    (u'4XL', '4xl_size'),
    (u'5XL', '5xl_size'),
    (u'模式', 'mode'),
]

material_cols = [
    (u'款号', 'style'),
    (u'颜色', 'color'),
    (u'原料', 'material'),
    (u'用量', 'cnt'),
    (u'单价', 'unit_price'),
    (u'单位', 'unit'),
]


def is_using_sheet(sheet, cols):
    if sheet.nrows == 0: return False
    row = [value.strip() if isinstance(value, basestring) else value for value in sheet.row_values(0)]  # 去除单元格前后空格
    for name, name_en in cols:
        if name not in row:
            return False
    return True

def read(source_dir):
    """
    读取源数据文件夹里的数据文件
    """
    logs =[]
    order_sheet, material_sheet = [], []
    # 读取文件，根据列头信息判断是否是所需sheet
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if os.path.splitext(file)[1] != '.xls': continue
            xls_file = os.path.join(root, file)
            book = xlrd.open_workbook(xls_file)
            for i in range(book.nsheets):
                sheet = book.sheet_by_index(i)
                if is_using_sheet(sheet, order_cols):
                    order_sheet.append(sheet)
                elif is_using_sheet(sheet, material_cols):
                    material_cols.append(sheet)

    # 数据文件缺失不能处理
    if not order_sheet:
        logs.append(u'缺失订单Excel文件，请检查订单Excel的列头信息')
        return
    if not order_sheet:
        logs.append(u'缺失产品用料成本Excel文件，请检查产品用料成本Excel的列头信息')
        return

    order_data = []
    for sheet in order_sheet:
        data = process_order_sheet(sheet)
        order_data.append(data)

    material_data = []
    for sheet in material_sheet:
        data = process_material_sheet(sheet)
        material_data.append(data)


def process_order_sheet(sheet):
    print sheet


def process_material_sheet(sheet):
    pass


if __name__ == '__main__':
    read(os.path.dirname(__file__))


