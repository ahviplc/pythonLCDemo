# -*- coding: utf-8 -*-
"""
pymysql_DBHelper.py
这是 pymysql db 操作类
"""
import pymysql
import logging
import sys

# print(os.path.dirname(os.path.realpath(__file__)))  # 【C:\_developSoftKu\ideaIU-2019.1.3.win\#CodeKu\pythonKu\MySQLToOracle\utils】
# print(os.path.abspath('..'))  # 【C:\_developSoftKu\ideaIU-2019.1.3.win\#CodeKu\pythonKu\MySQLToOracle】
# print(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))  # 【C:\_developSoftKu\ideaIU-2019.1.3.win\#CodeKu\pythonKu\MySQLToOracle】

# 导出数据库配置信息
from config.config import mysql_db_config_for_pymysql as db_config

# 加入日志
# 获取logger实例
logger = logging.getLogger("baseSpider")
# 指定输出格式
formatter = logging.Formatter('%(asctime)s\
               %(levelname)-8s:%(message)s')
# 文件日志
file_handler = logging.FileHandler("MySQLToOracle.operation_database.log")
file_handler.setFormatter(formatter)
# 控制台日志
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

# 为logge添加具体的日志处理器
logger.addHandler(file_handler)
logger.addHandler(console_handler)
# 设置日志级别
logger.setLevel(logging.INFO)


class DBHelper:
    # 构造函数,初始化数据库连接
    def __init__(self, sql, params=None):
        print('============================================================================================')
        print('...pymysql...db_config...=> ', db_config['host'], db_config['username'], db_config['password'],
              db_config['database'],
              db_config['charset'])
        print('============================================================================================')
        self.sql = sql
        self.params = params
        self.conn = None
        self.cur = None

    def connectiondatabase(self):
        try:
            self.conn = pymysql.connect(host=db_config['host'], user=db_config['username'],
                                        password=db_config['password'], db=db_config['database'],
                                        port=db_config['port'],
                                        charset=db_config['charset'])
        except Exception as e:
            logger.error("pymysql_DBHelper.py connectDatabase failed")
            logger.error("pymysql_DBHelper.py connectDatabase Exception " + str(e))
            print("pymysql_DBHelper.py connectDatabase failed")
            print("pymysql_DBHelper.py connectDatabase Exception " + str(e))
            return False
        self.cur = self.conn.cursor()
        return True

    # 关闭数据库
    def closedatabase(self):
        # 如果数据打开，则关闭；否则没有操作
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()
        return True

    # 执行数据库的sq语句,主要用来做插入操作
    def execute(self):
        self.connectiondatabase()
        try:
            if self.conn and self.cur:
                # 正常逻辑，执行sql，提交操作
                self.cur.execute(self.sql, self.params)
                self.conn.commit()
        except Exception as e:
            logger.error("pymysql_DBHelper.py execute failed: " + self.sql)
            logger.error("pymysql_DBHelper.py params: " + self.params)
            logger.error("pymysql_DBHelper.py Exception " + str(e))
            print("pymysql_DBHelper.py execute failed: " + self.sql)
            print("pymysql_DBHelper.py params: " + self.params)
            print("pymysql_DBHelper.py Exception " + str(e))
            self.closedatabase()
            return False
        return True

    # 执行数据库的sq语句,主要用来做插入操作 关闭数据库连接版本方法 最好使用这个
    # 在 execute 上添加
    def execute_finally_close_db(self):
        self.connectiondatabase()
        try:
            if self.conn and self.cur:
                # 正常逻辑，执行sql，提交操作
                self.cur.execute(self.sql, self.params)
                self.conn.commit()
        except Exception as e:
            logger.error("pymysql_DBHelper.py execute_finally_close_db failed: " + self.sql)
            logger.error("pymysql_DBHelper.py params: " + self.params)
            logger.error("pymysql_DBHelper.py Exception " + str(e))
            print("pymysql_DBHelper.py execute_finally_close_db failed: " + self.sql)
            print("pymysql_DBHelper.py params: " + self.params)
            print("pymysql_DBHelper.py Exception " + str(e))
            self.closedatabase()
            return False
        finally:
            self.closedatabase()
        return True

    # 用来查询表数据
    def select(self):
        self.connectiondatabase()
        self.cur.execute(self.sql, self.params)
        result = self.cur.fetchall()
        print(result)
        return result

    # 用来查询表数据 关闭数据库连接版本方法 最好使用这个
    # 在 select 上添加
    def select_finally_close_db(self):
        try:
            self.connectiondatabase()
            self.cur.execute(self.sql, self.params)
            result = self.cur.fetchall()
        except Exception as e:
            logger.error("pymysql_DBHelper.py select_finally_close_db failed: " + self.sql)
            logger.error("pymysql_DBHelper.py params: " + self.params)
            logger.error("pymysql_DBHelper.py Exception " + str(e))
            print("pymysql_DBHelper.py select_finally_close_db failed: " + self.sql)
            print("pymysql_DBHelper.py params: " + self.params)
            print("pymysql_DBHelper.py Exception " + str(e))
            self.closedatabase()
        finally:
            self.closedatabase()
        print(result)
        return result

    # 用来查询表数据 - 字典显示
    def selectDict(self):
        self.connectiondatabase()
        self.cur.execute(self.sql, self.params)
        result = self.cur.fetchall()
        index_dict = self.get_index_dict(self.cur)
        res = []
        for datai in result:
            resi = dict()
            for indexi in index_dict:
                resi[indexi] = datai[index_dict[indexi]]
            res.append(resi)
        print(res)
        return res

    # 用来查询表数据 - 字典显示 关闭数据库连接版本方法 最好使用这个
    # 在 selectDict 上添加
    # 运行sql语句，获取结果，并根据表中字段名，转化成dict格式（默认是tuple格式）
    def selectDict_finally_close_db(self):
        try:
            self.connectiondatabase()
            self.cur.execute(self.sql, self.params)
            result = self.cur.fetchall()
            index_dict = self.get_index_dict(self.cur)
            res = []
            for datai in result:
                resi = dict()
                for indexi in index_dict:
                    resi[indexi] = datai[index_dict[indexi]]
                res.append(resi)
        except Exception as e:
            logger.error("pymysql_DBHelper.py selectDict_finally_close_db failed: " + self.sql)
            logger.error("pymysql_DBHelper.py params: " + self.params)
            logger.error("pymysql_DBHelper.py Exception " + str(e))
            print("pymysql_DBHelper.py selectDict_finally_close_db failed: " + self.sql)
            print("pymysql_DBHelper.py params: " + self.params)
            print("pymysql_DBHelper.py Exception " + str(e))
            self.closedatabase()
        finally:
            self.closedatabase()
        print(res)
        return res

    # 获取数据库对应表中的字段名
    def get_index_dict(self, cursor):
        index_dict = dict()
        index = 0
        for desc in cursor.description:
            index_dict[desc[0]] = index
            index = index + 1
        return index_dict
