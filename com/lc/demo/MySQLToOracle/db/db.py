"""
db.py 生成数据库引擎 初始化db 公共db类
# 生成pony orm db对象 并提供暴露db给外面的方法
"""

from pony.orm import *  # 引入pony

# 导入 make_db_config_oracle_better 方法
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

# 暴露db的数据库引擎给外面
def get_dbs():
    return db_mysql, db_oracle


# 初始化db
# is_show_sql 是否显示sql
# is_mysql_create_tables 其MySQL引擎是否创建表
# is_oracle_create_tables 其Oracle引擎是否创建表
# 注意点【core/pony_orm_DBHelper.py:78】有【删除表，实体声明时用于快速清除旧表】的数据库引擎初始化配置,可具体使用,具体参考.
def init_db(is_show_sql, is_mysql_create_tables, is_oracle_create_tables):
    sql_debug(is_show_sql)  # 显示debug信息(sql语句)  turn on debug mode
    db_mysql.generate_mapping(create_tables=is_mysql_create_tables)
    db_oracle.generate_mapping(create_tables=is_oracle_create_tables)
