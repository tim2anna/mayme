#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os

PROJECT_PATH = os.path.dirname(__file__)


DATABASE_URL = 'sqlite:///%s/resource/foo.db3' % PROJECT_PATH
DATABASE_SETTINGS = {
    'encoding': 'utf-8',
    'echo': False
}

PROJECT_NAME = 'MayMe'
VERSION_STRING = '0.1.0'


import models.auth
import models.baseinfo
import models.customer
import models.purchase
import models.sale

try:
    from local_settings import *
except Exception:
    pass

from sqlalchemy import create_engine
import models
engine = create_engine(DATABASE_URL, **DATABASE_SETTINGS)
session = models.DBSession()
models.init_model(engine)