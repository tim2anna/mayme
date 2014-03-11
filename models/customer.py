#!/usr/bin/env python
#-*- coding:utf-8 -*-

from sqlalchemy import Column
from sqlalchemy.types import Integer, Unicode
from sqlalchemy.orm import relationship

import models


class Customer(models.Base):
    """客户"""
    __tablename__ = 'customer'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(Unicode(30), unique=True, nullable=False)  # 客户名
    phone = Column(Unicode(30))  # 电话
    region = Column(Unicode(30))  # 地区

    sale_orders = relationship('SaleOrder', backref='customer')

    def __unicode__(self):
        return self.name
