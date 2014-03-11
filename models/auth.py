#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
认证模块模型：用户、角色(组)、权限
"""

import os
from datetime import datetime
from hashlib import sha1

from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode, Boolean, DateTime
from sqlalchemy.orm import synonym, relationship

import models

__all__ = ['User', 'Group', 'Permission']


group_permission_table = Table('auth_group_permissions', models.metadata,
    Column('group_id', Integer, ForeignKey('auth_group.id',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True),
    Column('permission_id', Integer, ForeignKey('auth_permission.id',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
)


user_group_table = Table('auth_user_groups', models.metadata,
    Column('user_id', Integer, ForeignKey('auth_user.id',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True),
    Column('group_id', Integer, ForeignKey('auth_group.id',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
)


class Group(models.Base):
    """角色"""
    __tablename__ = 'auth_group'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(Unicode(80), unique=True, nullable=False)

    users = relationship('User', secondary=user_group_table, backref='groups')

    def __repr__(self):
        return ('<Group: name=%s>' % self.name).encode('utf-8')

    def __unicode__(self):
        return self.name


class User(models.Base):
    """用户"""
    __tablename__ = 'auth_user'

    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(Unicode(30), unique=True, nullable=False)
    first_name = Column(Unicode(30))
    last_name = Column(Unicode(30))
    email = Column(Unicode(75), unique=True, nullable=False, info={'rum': {'field':'Email'}})
    _password = Column('password', Unicode(80), info={'rum': {'field':'Password'}})
    is_staff = Column(Boolean())
    is_active = Column(Boolean())
    is_superuser = Column(Boolean())
    last_login = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    date_joined = Column(DateTime(), default=datetime.now)

    def __repr__(self):
        return ('<User: name=%r, email=%r>' % (self.user_name, self.email)).encode('utf-8')

    def __unicode__(self):
        return self.username

    @property
    def permissions(self):
        """Return a set with all permissions granted to the user."""
        perms = set()
        for g in self.groups:
            perms = perms | set(g.permissions)
        return perms

    @classmethod
    def by_email_address(cls, email):
        """Return the user object whose email address is ``email``."""
        return models.DBSession.query(cls).filter_by(email=email).first()

    @classmethod
    def by_user_name(cls, username):
        """Return the user object whose user name is ``username``."""
        return models.DBSession.query(cls).filter_by(username=username).first()

    def _set_password(self, password):
        """Hash ``password`` on the fly and store its hashed version."""
        # Make sure password is a str because we cannot hash unicode objects
        if isinstance(password, unicode):
            password = password.encode('utf-8')
        salt = sha1()
        salt.update(os.urandom(60))
        hash = sha1()
        hash.update(password + salt.hexdigest())
        password = salt.hexdigest() + hash.hexdigest()
        # Make sure the hashed password is a unicode object at the end of the
        # process because SQLAlchemy _wants_ unicode objects for Unicode cols
        if not isinstance(password, unicode):
            password = password.decode('utf-8')
        self._password = password

    def _get_password(self):
        """Return the hashed version of the password."""
        return self._password

    password = synonym('_password', descriptor=property(_get_password, _set_password))

    def validate_password(self, password):
        hash = sha1()
        if isinstance(password, unicode):
            password = password.encode('utf-8')
        hash.update(password + str(self.password[:40]))
        return self.password[40:] == hash.hexdigest()


class Permission(models.Base):
    """权限"""
    __tablename__ = 'auth_permission'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(Unicode(50), unique=True, nullable=False)
    codename = Column(Unicode(100))

    groups = relationship(Group, secondary=group_permission_table, backref='permissions')

    def __repr__(self):
        return ('<Permission: name=%r>' % self.name).encode('utf-8')

    def __unicode__(self):
        return self.name