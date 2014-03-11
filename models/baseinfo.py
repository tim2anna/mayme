#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
基础信息

Product产品
    style_id 款号
    color 颜色
    retail_price 零售价
    wholesale_price 批发价
    catetory 分类：针织、裤子、连衣裙、衬衫、外套、针织外套

ProductAttr产品属性 动态
    name 名称
    value 值
    pro_id 所属产品
    category 分类：common普通/cost成本

Material原料
    name 名称
    unit_cost 单价
    unit 单位
    catetory 分类：主料、辅料

Distribution产品配料
    pro_id 相关产品
    mat 所用原料
    qty 数量

单件成本 = 所用原料1单价 * 所用原料1数量 + 所用原料2单价 * 所用原料2数量 + ... + Attr Cost
"""
