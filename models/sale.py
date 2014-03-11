#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
销售

销售订单 SaleOrder
    customer_id客户
    order_time下单时间

销售订单明细 SaleOrderItem

    so_id 所属订单
    qty 数量
    size 尺码
    color 颜色
    product_id 订购的产品
    unit_cost 单价

销售额 = 单价 * 数量
成本 = 单件成本 * 数量
利润 = 销售额 - 成本
"""
