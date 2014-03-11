#!/usr/bin/env python
#-*- coding:utf-8 -*-


DATABASE_URL = 'sqlite:///resource/foo.db3'
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