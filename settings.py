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

try:
    from local_settings import *
except Exception:
    pass