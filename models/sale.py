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

from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, Unicode, Float, DateTime
from sqlalchemy.orm import relationship

import models


class SaleOrder(models.Base):
    """  销售订单 """
    __tablename__ = 'sale_order'

    id = Column(Integer, autoincrement=True, primary_key=True)
    order_id = Column(Unicode(30))  # 订单号
    order_time = Column(DateTime)  # 下单时间

    customer_id = Column(Integer, ForeignKey('customer.id'))  # 客户
    sale_orders = relationship('SaleOrderItem', backref='items')


class SaleOrderItem(models.Base):
    """ 销售订单明细 """
    __tablename__ = 'sale_order_item'

    id = Column(Integer, autoincrement=True, primary_key=True)
    qty = Column(Float)  # 数量
    size = Column(Unicode(30))  # 尺码
    color = Column(Unicode(30))  # 颜色
    unit_cost = Column(Float)  # 单价

    so_id = Column(Integer, ForeignKey('sale_order.id'))
    pro_id = Column(Integer, ForeignKey('product.id'))