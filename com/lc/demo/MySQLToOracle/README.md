# MySQLToOracle

> 一款mysql向oracle的数据转移app.

## 安装驱动

> pip install pony  
> pip install PyMySQL  
> pip install cx-Oracle

```markdown
mysql

PyMySQL · PyPI
https://pypi.org/project/PyMySQL/

GitHub - PyMySQL/PyMySQL: Pure Python MySQL Client
https://github.com/PyMySQL/PyMySQL

Welcome to PyMySQL’s documentation! — PyMySQL 0.7.2 documentation
https://pymysql.readthedocs.io/en/latest/

oracle

cx-Oracle · PyPI
https://pypi.org/project/cx-Oracle/

GitHub - oracle/python-cx_Oracle: Python interface to Oracle Database conforming to the Python DB API 2.0 specification.
https://github.com/oracle/python-cx_Oracle

cx_Oracle - Python Interface for Oracle Database
https://oracle.github.io/python-cx_Oracle/
```

## orm框架

```markdown
Getting Started with Pony — Pony ORM documentation
https://docs.ponyorm.org/firststeps.html

API Reference — Pony ORM documentation
https://docs.ponyorm.org/api_reference.html#oracle

Getting Started with Pony — Pony ORM documentation
https://docs.ponyorm.org/firststeps.html#pony-examples

pony/pony/orm/examples at orm · ponyorm/pony · GitHub
https://github.com/ponyorm/pony/tree/orm/pony/orm/examples

ponyorm/pony - GitHub1s - 在1s的vscode编辑器中打开
https://github1s.com/ponyorm/pony/blob/orm/pony/orm/examples/demo.py
```

## 其他链接

```markdown
python3对MySQL数据库操作进行封装_统哥哥的博客-CSDN博客-基于pymysql
https://blog.csdn.net/weixin_43935187/article/details/85763356

Python的魔法ORM --《PonyORM教程》 1.连接,声明和查询 - 简书
https://www.jianshu.com/p/11b9cdace3b2

PonyORM教程1 连接,声明和查询_justonlyyo的博客-CSDN博客-这个包含教程5-更全-其他和上面一样.
https://blog.csdn.net/justonlyyo/article/details/102523401

PonyORM教程 5 钩子函数和实体方法扩展_justonlyyo的博客-CSDN博客
https://blog.csdn.net/justonlyyo/article/details/102523602

随笔之pymysql查询结果转字典dict_家住海边，见过大风大浪-CSDN博客
https://blog.csdn.net/u014487025/article/details/88684541

只有Python魔法少女才知道的PonyORM
https://farer.org/2018/07/09/ponyorm/

Python 线程安全（同步锁Lock）详解 - 说的不错 - 【utils/cx_Oracle_db_utils.py:26】
http://c.biancheng.net/view/2617.html

详解python的ORM中Pony用法_python_脚本之家 对应源码【https://github.com/flowpig/daily_demos】
https://www.jb51.net/article/134781.htm
pony学习 - 【https://github.com/flowpig/daily_demos/tree/master/Pony%E5%AD%A6%E4%B9%A0】

py 全局变量_paulkg12的博客-CSDN博客_py全局变量
https://blog.csdn.net/paulkg12/article/details/88660994

Python random() 函数 | 菜鸟教程
https://www.runoob.com/python/func-number-random.html

Python练习题-判断某一个字符串是否是小数_oito_菜鸟-CSDN博客_python 判断字符串是小数 这个很不错
https://blog.csdn.net/wls666/article/details/96038402

Python range() 函数 | 菜鸟教程
https://www.runoob.com/python/python-func-range.html

Python 3 实现定义跨模块的全局变量和使用 - _Suwings - 博客园
https://www.cnblogs.com/suwings/p/6358061.html

Python __all__变量用法
http://c.biancheng.net/view/2401.html
```

## 两个核心SQL脚本

> 一个MySQL(数据提供者),一个Oracle(数据接收者).下面数据库脚本,对应数据域执行,即可建表.

### MySQL

`docs/sql/MySQL-meter_report_month_202104.sql`

### Oracle

`docs/sql/Oracle-SCADA_REPORT_XN_MID和SCADA_REPORT_XN_WEEK和SCADA_REPORT_XN_MONTH.sql`

