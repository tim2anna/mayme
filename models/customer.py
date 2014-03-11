#!/usr/bin/env python
#-*- coding:utf-8 -*-

from sqlalchemy import Column
from sqlalchemy.types import Integer, Unicode

import models


class Customer(models.Base):
    """客户"""
    __tablename__ = 'customer_customer'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(Unicode(30), unique=True, nullable=False)  # 客户名
    phone = Column(Unicode(30))  # 电话
    region = Column(Unicode(30))  # 地区

    def __unicode__(self):
        return self.name
