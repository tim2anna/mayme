#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest


class TestCreateTable(unittest.TestCase):

    def test_create_table(self):
        """创建数据库表"""
        import models
        from main import engine
        models.metadata.create_all(engine)


if __name__ == '__main__':
    unittest.main()
