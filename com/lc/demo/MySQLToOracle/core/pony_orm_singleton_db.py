#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 将pony的Database改为单例
# pony_orm_singleton_db.py
# 已测试 可用 但是我这里目前lmt的需求 不适合这个 因为需要同时连接MySQL和Oracle,进行管理和操作.
# 这个适合单库操作时使用

from functools import wraps
from pony.orm import Database


# singleton
def singleton(cls):
    instances = {}

    @wraps(cls)
    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return getinstance


# PonySingletonDB
@singleton
class PonySingletonDB(Database):
    """
    将pony的Database改为单例
    """

    def __init__(self, *args, **kwargs):
        Database.__init__(self, *args, **kwargs)


"""
使用步骤说明：
1.导入数据库配置文件,所需类和所需工具
# 导出数据库配置信息 mysql 生产环境
# from config.config import mysql_db_config as db_config_mysql

# 导出数据库配置信息 mysql local 测试环境 本地数据库
from config.config import mysql_db_config_local as db_config_mysql

# 导出数据库配置信息 oracle
from config.config import oracle_db_config as db_config_oracle

# 引入自加工过的 单例 pony orm db
# 类 PonySingletonDB
from core.pony_orm_singleton_db import PonySingletonDB

2. 使用即可
# 单例 pony orm db
# 类 PonySingletonDB
db_mysql = PonySingletonDB(**db_config_mysql)
db_config_oracle = make_db_config_oracle_better(db_config_oracle)
db_oracle = PonySingletonDB(**db_config_oracle)

3.要是使用原生 直接按照下面写法使用即可.
# 原生db================================================================
# # 生成数据库引擎 mysql
# db_mysql = Database(**db_config_mysql)
#
# # 生成数据库引擎 oracle
# db_config_oracle = make_db_config_oracle_better(db_config_oracle)
# db_oracle = Database(**db_config_oracle)
# 原生db================================================================

注意：别忘引入 
from pony.orm import *  # 引入pony

# 引入自加工过的 单例 pony orm db
# 类 PonySingletonDB
from core.pony_orm_singleton_db import PonySingletonDB
"""
