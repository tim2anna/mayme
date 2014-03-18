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


def write_cell(book, sheet_name, cols, data):
    # TODO: 65535行的限制
    sheet = book.add_sheet(sheet_name)
    for m, col_name in enumerate(cols):
        sheet.row(0).write(m, col_name)
    for cell in data:
        if cell['r1'] == cell['r2'] and cell['c1'] == cell['c2']:
            sheet.row(cell['r1']).write(cell['c1'], cell['value'])
        else:
            sheet.write_merge(cell['r1'], cell['r2'], cell['c1'], cell['c2'], cell['value'])
    return book

def gen_all_order_excel(order_data, output_dir):
    """ 生成所有订单的Excel """
    cols = [
        (u'款号', 'style'),
        (u'总量', 'total'),
        (u'颜色', 'color'),
        (u'S', 's_size'),
        (u'M', 'm_size'),
        (u'L', 'l_size'),
        (u'XL', 'xl_size'),
        (u'2XL', '2xl_size'),
        (u'3XL', '3xl_size'),
        (u'4XL', '4xl_size'),
        (u'5XL', '5xl_size'),
        (u'合计', 'color_total'),
    ]

    all_dict = {}
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

    book = xlwt.Workbook()
    # 总订单汇总
    all_datas = []
    r = 1
    for style, color_dict in all_dict.items():
        c = 0
        # 款式
        all_datas.append({'value': style, 'r1': r, 'r2': r+len(color_dict)-1, 'c1': c, 'c2': c})
        c += 1
        # 预留给总量
        style_total_cnt = {'value': 0, 'r1': r, 'r2': r+len(color_dict)-1, 'c1': c, 'c2': c}
        c += 1

        temp_c = c
        for color, size_dict in color_dict.items():
            # 颜色
            all_datas.append({'value': color, 'r1': r, 'r2': r, 'c1': c, 'c2': c})
            c += 1
            # S尺码
            all_datas.append({'value': size_dict['s_size'], 'r1': r, 'r2': r, 'c1': c, 'c2': c})
            c += 1
            # M尺码
            all_datas.append({'value': size_dict['m_size'], 'r1': r, 'r2': r, 'c1': c, 'c2': c})
            c += 1
            # L尺码
            all_datas.append({'value': size_dict['l_size'], 'r1': r, 'r2': r, 'c1': c, 'c2': c})
            c += 1
            # XL尺码
            all_datas.append({'value': size_dict['xl_size'], 'r1': r, 'r2': r, 'c1': c, 'c2': c})
            c += 1
            # 2XL尺码
            all_datas.append({'value': size_dict['2xl_size'], 'r1': r, 'r2': r, 'c1': c, 'c2': c})
            c += 1
            # 3XL尺码
            all_datas.append({'value': size_dict['3xl_size'], 'r1': r, 'r2': r, 'c1': c, 'c2': c})
            c += 1
            # 4XL尺码
            all_datas.append({'value': size_dict['4xl_size'], 'r1': r, 'r2': r, 'c1': c, 'c2': c})
            c += 1
            # 5XL尺码
            all_datas.append({'value': size_dict['5xl_size'], 'r1': r, 'r2': r, 'c1': c, 'c2': c})
            c += 1
            # 合计
            color_total = size_dict['s_size'] + size_dict['m_size'] + size_dict['l_size'] + size_dict['xl_size'] + size_dict['2xl_size'] + size_dict['3xl_size'] + size_dict['4xl_size'] + size_dict['5xl_size']
            all_datas.append({'value': color_total, 'r1': r, 'r2': r, 'c1': c, 'c2': c})
            style_total_cnt['value'] += color_total
            # 列复位
            c = temp_c
            r += 1
        all_datas.append(style_total_cnt)


    book = write_cell(book, u'所有订单', [name for name, name_en in cols], all_datas)

    book.save(os.path.join(output_dir, u'汇总订单.xls'))

    return u'已生成文件：' + os.path.join(output_dir, u'汇总订单.xls')


def gen_material_sta_excel(material_data, order_data, output_dir):
    # 统计所有订单
    order_dict = {}
    for item in order_data:
        if item['style'] not in order_dict: order_dict[item['style']] = {}
        if item['color'] not in order_dict[item['style']]: order_dict[item['style']][item['color']] = {
            's_size': 0, 'm_size': 0, 'l_size': 0, 'xl_size': 0, '2xl_size': 0, '3xl_size': 0, '4xl_size': 0, '5xl_size': 0
        }
        order_dict[item['style']][item['color']]['s_size'] += item['s_size'] if item['s_size'] else 0
        order_dict[item['style']][item['color']]['m_size'] += item['m_size'] if item['m_size'] else 0
        order_dict[item['style']][item['color']]['l_size'] += item['l_size'] if item['l_size'] else 0
        order_dict[item['style']][item['color']]['xl_size'] += item['xl_size'] if item['xl_size'] else 0
        order_dict[item['style']][item['color']]['2xl_size'] += item['2xl_size'] if item['2xl_size'] else 0
        order_dict[item['style']][item['color']]['3xl_size'] += item['3xl_size'] if item['3xl_size'] else 0
        order_dict[item['style']][item['color']]['4xl_size'] += item['4xl_size'] if item['4xl_size'] else 0
        order_dict[item['style']][item['color']]['5xl_size'] += item['5xl_size'] if item['5xl_size'] else 0

    material_dict = {}
    for item in material_data:
        if item['material'] not in material_dict:
            material_dict[item['material']] = {'colors': set(), 'styles': {}}
        if item['style'] not in material_dict[item['material']]['styles']:
            material_dict[item['material']]['styles'][item['style']] = {}
        material_dict[item['material']]['styles'][item['style']][item['color']] = {
            'cnt': item['cnt'] if item['cnt'] else 0, 'unit_price': item['unit_price'], 'unit': item['unit']
        }
        material_dict[item['material']]['colors'].add(item['color'])

    book = xlwt.Workbook()

    for material, mat_dict in material_dict.items():
        cols = list(mat_dict['colors'])
        style_dict = mat_dict['styles']
        mat_data = []
        for style, color_dict in style_dict.items():
            row = [style]
            style_cnt_total = 0
            for color in cols:
                if color in color_dict:
                    try:
                        unit_cnt = float(color_dict[color]['cnt'])
                    except:
                        unit_cnt = 0
                    size_cnt_dict = order_dict.get(style, {}).get(color, {})
                    s_size_cnt = size_cnt_dict.get('s_size', 0)
                    m_size_cnt = size_cnt_dict.get('m_size', 0)
                    l_size_cnt = size_cnt_dict.get('l_size', 0)
                    xl_size_cnt = size_cnt_dict.get('xl_size', 0)
                    xl2_size_cnt = size_cnt_dict.get('2xl_size', 0)
                    xl3_size_cnt = size_cnt_dict.get('3xl_size', 0)
                    xl4_size_cnt = size_cnt_dict.get('4xl_size', 0)
                    xl5_size_cnt = size_cnt_dict.get('5xl_size', 0)
                    color_cnt_total = unit_cnt * (s_size_cnt + m_size_cnt + l_size_cnt + xl_size_cnt + xl2_size_cnt + xl3_size_cnt + xl4_size_cnt + xl5_size_cnt)
                    row.append(color_cnt_total)
                    style_cnt_total += color_cnt_total
                else:  # 该款式没有使用此颜色的布料
                    row.append('/')
            row.append(style_cnt_total)
            mat_data.append(row)
        book = write_sheet(book, material, [u'款式'] + cols + [u'合计'], mat_data)

    book.save(os.path.join(output_dir, u'原料用量汇总.xls'))
    return u'已生成文件：' + os.path.join(output_dir, u'原料用量汇总.xls')