#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""写入Excel文件"""

import os
import xlwt


def write_excel(cols, data, file_path, sheet_name='sheet'):
    book = xlwt.Workbook()
    sheet_size = 60000  # 每个sheet页只能写入6万行记录，多于6万行，新建sheet
    sheet_total = len(data)/sheet_size if len(data) % sheet_size == 0 else len(data)/sheet_size + 1
    for i in range(sheet_total):
        sheet_data = data[i*sheet_size:(i+1)*sheet_size]
        sheet = book.add_sheet(sheet_name if i is 0 else sheet_name+str(i+1))
        for m, col_name in enumerate(cols):
            sheet.row(0).write(m, col_name)
        for row, row_values in enumerate(sheet_data):
            for m, value in enumerate(row_values):
                sheet.row(row+1).write(m, value)
    book.save(file_path)


def write_sheet(book, sheet_name, cols, data):
    sheet_size = 60000  # 每个sheet页只能写入6万行记录，多于6万行，新建sheet
    sheet_total = len(data)/sheet_size if len(data) % sheet_size == 0 else len(data)/sheet_size + 1
    for i in range(sheet_total):
        sheet_data = data[i*sheet_size:(i+1)*sheet_size]
        sheet = book.add_sheet(sheet_name if i is 0 else sheet_name+str(i+1))
        for m, col_name in enumerate(cols):
            sheet.row(0).write(m, col_name)
        for row, row_values in enumerate(sheet_data):
            for m, value in enumerate(row_values):
                sheet.row(row+1).write(m, value)
    return book


def gen_all_order_excel(order_data, output_dir):
    """ 生成所有订单的Excel """
    cols = [
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
    ]

    all_dict, mode_dict = {}, {}
    for item in order_data:
        if item['style'] not in all_dict: all_dict[item['style']] = {}
        if item['color'] not in all_dict[item['style']]: all_dict[item['style']][item['color']] = {
            's_size': 0, 'm_size': 0, 'l_size': 0, 'xl_size': 0, '2xl_size': 0, '3xl_size': 0, '4xl_size': 0, '5xl_size': 0
        }
        all_dict[item['style']][item['color']]['s_size'] += item['s_size'] if item['s_size'] else 0
        all_dict[item['style']][item['color']]['m_size'] += item['m_size'] if item['m_size'] else 0
        all_dict[item['style']][item['color']]['l_size'] += item['l_size'] if item['l_size'] else 0
        all_dict[item['style']][item['color']]['xl_size'] += item['xl_size'] if item['xl_size'] else 0
        all_dict[item['style']][item['color']]['2xl_size'] += item['2xl_size'] if item['2xl_size'] else 0
        all_dict[item['style']][item['color']]['3xl_size'] += item['3xl_size'] if item['3xl_size'] else 0
        all_dict[item['style']][item['color']]['4xl_size'] += item['4xl_size'] if item['4xl_size'] else 0
        all_dict[item['style']][item['color']]['5xl_size'] += item['5xl_size'] if item['5xl_size'] else 0

        if item['mode'] not in mode_dict: mode_dict[item['mode']] = {}
        if item['style'] not in mode_dict[item['mode']]: mode_dict[item['mode']][item['style']] = {}
        if item['color'] not in mode_dict[item['mode']][item['style']]: mode_dict[item['mode']][item['style']][item['color']] = {
            's_size': 0, 'm_size': 0, 'l_size': 0, 'xl_size': 0, '2xl_size': 0, '3xl_size': 0, '4xl_size': 0, '5xl_size': 0
        }
        mode_dict[item['mode']][item['style']][item['color']]['s_size'] += item['s_size'] if item['s_size'] else 0
        mode_dict[item['mode']][item['style']][item['color']]['m_size'] += item['m_size'] if item['m_size'] else 0
        mode_dict[item['mode']][item['style']][item['color']]['l_size'] += item['l_size'] if item['l_size'] else 0
        mode_dict[item['mode']][item['style']][item['color']]['xl_size'] += item['xl_size'] if item['xl_size'] else 0
        mode_dict[item['mode']][item['style']][item['color']]['2xl_size'] += item['2xl_size'] if item['2xl_size'] else 0
        mode_dict[item['mode']][item['style']][item['color']]['3xl_size'] += item['3xl_size'] if item['3xl_size'] else 0
        mode_dict[item['mode']][item['style']][item['color']]['4xl_size'] += item['4xl_size'] if item['4xl_size'] else 0
        mode_dict[item['mode']][item['style']][item['color']]['5xl_size'] += item['5xl_size'] if item['5xl_size'] else 0

    book = xlwt.Workbook()
    # 总订单汇总
    all_datas = []
    for style, color_dict in all_dict.items():
        for color, size_dict in color_dict.items():
            all_datas.append([style, color, size_dict['s_size'], size_dict['m_size'], size_dict['l_size'],
                              size_dict['xl_size'], size_dict['2xl_size'], size_dict['3xl_size'],
                              size_dict['4xl_size'], size_dict['5xl_size']])
    book = write_sheet(book, u'所有订单', [name for name, name_en in cols], all_datas)
    # 不同模式(批发、零售、商场)的订单汇总，每种模式单独一个sheet
    for mode, mode_dict in mode_dict.items():
        mode_datas = []
        for style, color_dict in all_dict.items():
            for color, size_dict in color_dict.items():
                mode_datas.append([style, color, size_dict['s_size'], size_dict['m_size'], size_dict['l_size'],
                                  size_dict['xl_size'], size_dict['2xl_size'], size_dict['3xl_size'],
                                  size_dict['4xl_size'], size_dict['5xl_size']])
        book = write_sheet(book, mode, [name for name, name_en in cols], mode_datas)
    book.save(os.path.join(output_dir, u'汇总订单.xls'))

    return u'已生成文件：' + os.path.join(output_dir, u'汇总订单.xls')