# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# models 类的集中地
# 集中管理所有的model
# 生成pony orm db对象 并提供暴露db给外面的方法
import datetime
from pony.orm import *  # 引入pony

from utils.util import make_db_config_oracle_better

# 导出数据库配置信息 mysql 生产环境
# from config.config import mysql_db_config as db_config_mysql
# 导出数据库配置信息 mysql local 测试环境 本地数据库
from config.config import mysql_db_config_local as db_config_mysql

# 导出数据库配置信息 oracle
from config.config import oracle_db_config as db_config_oracle

# 原生db================================================================
# 生成数据库引擎 mysql
db_mysql = Database(**db_config_mysql)

# 生成数据库引擎 oracle
db_config_oracle = make_db_config_oracle_better(db_config_oracle)
db_oracle = Database(**db_config_oracle)


# 备注:
# 要是使用单例版db 请去【MySQLToOracle\core\pony_orm_singleton_db.py】 查看使用方法

# 暴露db给外面
def get_dbs():
    return db_mysql, db_oracle


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
