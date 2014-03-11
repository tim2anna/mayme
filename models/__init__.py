#!/usr/bin/env python
#-*- coding:utf-8 -*-

from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

maker = sessionmaker(autoflush=True, autocommit=False)
DBSession = scoped_session(maker)
Base = declarative_base()
metadata = Base.metadata


def init_model(engine):
    DBSession.configure(bind=engine)
    metadata.bind = engine
