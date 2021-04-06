# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# models 类的集中地
# 集中管理所有的model
import datetime
from pony.orm import *  # 引入pony
# 引入db
# 暴露db的数据库引擎给外面 get_dbs
from db.db import get_dbs

# 获取在db包 生成的 双db
db_mysql, db_oracle = get_dbs()


########################################################################
# MySQL
# pony_orm_test_service.py 测试使用
class Artist(db_mysql.Entity):
    """
    Pony ORM model of the Artist table
    """
    # set是被外键关联
    name = Required(unicode)
    albums = Set("Album")


########################################################################
# pony_orm_test_service.py 测试使用
class Album(db_mysql.Entity):
    """
    Pony ORM model of album table
    """
    # 创建外键时两个表都要写，外键默认index=True
    artist = Required(Artist)
    title = Required(unicode)
    release_date = Required(datetime.date)
    publisher = Required(unicode)
    media_type = Required(unicode)


# Oracle
# pony_orm_test_service.py 测试使用
class Artist2(db_oracle.Entity):
    """
    Pony ORM model of the Artist table
    """
    # set是被外键关联
    name = Required(unicode)
