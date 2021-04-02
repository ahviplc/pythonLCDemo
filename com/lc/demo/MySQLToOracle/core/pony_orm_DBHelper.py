# -*- coding: utf-8 -*-
"""
pony_orm_DBHelper.py
这是 pony db 操作类
内含测试代码
"""

import datetime
from pony.orm import *  # 引入
from utils.util import make_db_config_oracle_better

# 导出数据库配置信息 mysql 生产环境
# from config.config import mysql_db_config as db_config_mysql

# 导出数据库配置信息 mysql local 测试环境 本地数据库
from config.config import mysql_db_config_local as db_config_mysql

# 导出数据库配置信息 oracle
from config.config import oracle_db_config as db_config_oracle

# 生成数据库引擎 mysql
db_mysql = Database(**db_config_mysql)

# 生成数据库引擎 oracle
db_config_oracle = make_db_config_oracle_better(db_config_oracle)
db_oracle = Database(**db_config_oracle)


# 员工类 db_mysql
class Employee(db_mysql.Entity):
    """员工类"""
    _table_ = "employee"
    name = Required(str, max_len=40, unique=False, nullable=False, default="无名氏")  # 姓名
    age = Optional(int, size=8, nullable=True, default=None)  # 年龄
    born = Required(datetime.date, nullable=False, column="born_date", default=datetime.date.today)  # 🏠出生年月日


# 员工类2 db_oracle
class Employee2(db_oracle.Entity):
    """员工类"""
    _table_ = "employee2"
    name = Required(str, max_len=40, unique=False, nullable=False, default="无名氏")  # 姓名
    age = Optional(int, size=8, nullable=True, default=None)  # 年龄
    born = Required(datetime.date, nullable=False, column="born_date", default=datetime.date.today)  # 🏠出生年月日


# 员工类3 db_oracle
class Employee3(db_oracle.Entity):
    """员工类"""
    _table_ = "EMPLOYEE3"
    name = Required(str, max_len=40, unique=False, nullable=False, default="无名氏")  # 姓名
    age = Optional(int, size=8, nullable=True, default=None)  # 年龄
    born = Required(datetime.datetime, nullable=False, column="born_date", default=datetime.datetime.today)  # 🏠出生年月日


# 删除表
# 生成实体
def run_pony():
    # db_mysql.drop_table(table_name="employee", if_exists=True, with_all_data=True)  # 删除表，演示实体声明时用于快速清除旧表
    db_mysql.generate_mapping(create_tables=False)  # 生成实体，表和映射关系
    db_oracle.generate_mapping(create_tables=False)  # 生成实体，表和映射关系
    pass


# 增删改查
# 使用上下文 with db_session:
def run_db_session():
    with db_session:
        # 这就是新增
        # emp = Employee(name="张三", age=12)  # 创建一个实例
        # emp = Employee(name="张三2", age=13)  # 创建一个实例
        # emp = Employee(name="张三3", age=15)  # 创建一个实例
        # emp = Employee(name="张三4", age=15)  # 创建一个实例
        # emp = Employee(name="张三5", age=12)  # 创建一个实例
        # emp = Employee(name="john", age=15)  # 创建一个实例
        # emp_dict = emp.to_dict()  # 实例转字典
        # print(emp_dict)
        # # 修改
        # emp.set(age=14)  # 修改字段
        # emp = Employee.select(name="张三")[:]  # 查找名字叫张三的员工
        # emp.show()
        # el = emp.to_list()
        # print(el)
        # # 删除
        # # emp.delete()  # 删除实例
        # # 一系列查询
        # emp = Employee.get(name="张三", age=15)  # 查找名字叫张三的员工
        # print(emp)
        # print(emp.to_dict())
        # list = select(p for p in Employee if p.age > 13)[:]
        # list2 = list.to_list()
        # x = 11
        # res = db_mysql.select('* FROM employee p WHERE p.age < $x')
        #
        # res2 = Employee.select_by_sql('SELECT * FROM employee WHERE age < $x')
        # print(list, res, res2)
        # print(res2[0].name)  # employee 对象
        #
        # # 查询全部 下面均可用
        # # Employee.select().show()
        # es = Employee.select()
        # print(es)
        # # es.show()
        # # show(es) 可以这样用 和 es.show() 效果一样
        # print(es[:])
        # for e_s in es[:]:
        #     # 这一步就是把所有的mysql查询出来的转移到新增到oracle
        #     # 新建对象就是向oracle数据库插入数据 新增数据 添加数据
        #     Employee2(name=e_s.name, age=e_s.age, born=e_s.born)
        #     Employee3(name=e_s.name, age=e_s.age,
        #               born=datetime.datetime.combine(e_s.born, datetime.datetime.today().time()))
        #
        # # print(es[:].show())
        # # print(es[:].to_list())
        #
        # # 返回 a list of tuples
        # listX = select((p, p.age) for p in Employee if p.age > 13)[0:3]
        # print('---------------------------------------------------------------')
        # print(listX.show())
        # print('---------------------------------------------------------------')
        # print(listX.to_list())
        #
        # # 带日期的
        # list_born = select(p for p in Employee if p.age > 13 and p.born == datetime.date(1993, 2, 21))[:]
        # print('---------------------------------------------------------------')
        # list_born.show()
        # print('---------------------------------------------------------------')

        # res_settings = db_mysql.select('* FROM settings')
        # print(res_settings)

        # res2 = db_mysql.select('* FROM meter_report_month_202104')
        # print(res2)

        res = db_mysql.select('* FROM employee')
        print(res)

        res2 = db_oracle.select('* FROM BRANCH_INFO where rownum <= 3')
        print(res2)


# 使用装饰器db_session
@db_session
def add_one():
    # emp = Employee(name="LC", age=12, born=datetime.date(1993, 2, 21))  # 创建一个实例 这就完成了 新增操作
    # emp = Employee2(name="LC-ORACLE", age=12, born=datetime.date.today())  # 创建一个实例 这就完成了 新增操作
    # emp = Employee3(name="LC-ORACLE", age=12, born=datetime.datetime.today())  # 创建一个实例 这就完成了 新增操作
    pass


'''
您会注意到我们需要使用一个装饰器db_session来处理数据库。
它负责打开连接，提交数据并关闭连接。 你也可以把它作为一个上
下文管理器，with db_session
'''
