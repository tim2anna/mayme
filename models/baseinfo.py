#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
基础信息

Product产品
    style_id 款号
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
    mat_id 所用原料
    qty 数量

单件成本 = 所用原料1单价 * 所用原料1数量 + 所用原料2单价 * 所用原料2数量 + ... + Attr Cost
"""


from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, Unicode, Float
from sqlalchemy.orm import relationship

import models


class Distribution(models.Base):
    """  产品配料 """
    __tablename__ = 'distribution'

    pro_id = Column(Integer, ForeignKey('product.id'), primary_key=True)
    mat_id = Column(Integer, ForeignKey('material.id'), primary_key=True)
    qty = Column(Float)  # 数量

    materials = relationship('Material', backref='product_dists')


class Product(models.Base):
    """ 产品 """
    __tablename__ = 'product'

    id = Column(Integer, autoincrement=True, primary_key=True)
    style_id = Column(Unicode(30), unique=True, nullable=False)  # 款号
    retail_price = Column(Unicode(30))  # 零售价
    wholesale_price = Column(Unicode(30))  # 批发价
    catetory = Column(Unicode(30))  # 分类：针织、裤子、连衣裙、衬衫、外套、针织外套

    materials = relationship('Distribution', backref='products')
    so_items = relationship('SaleOrderItem', backref='product')

    # TODO: 一件产品的尺码，应该是和产品绑定的，不同产品的可选尺码是不同的
    # TODO: 产品的颜色也同上


# TODO: 动态扩展产品属性
# class ProductAttr:
#     pass


class Material(models.Base):
    """ 原料 """
    __tablename__ = 'material'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(Unicode(30), unique=True, nullable=False)  # 名称
    unit = Column(Unicode(30))  # 单位
    unit_cost = Column(Float)  # 单价
    catetory = Column(Unicode(30))  # 分类：主料、辅料
