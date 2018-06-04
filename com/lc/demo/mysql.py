#!/usr/bin/python3
import pymysql


# 打开数据库连接
db = pymysql.connect("localhost","root","root","ceshi" )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
cursor1 = db.cursor()

# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")
cursor1.execute("SELECT * from lc")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
data1 = cursor1.fetchone()
print ("Database version : %s " % data)
print (data1)
# 关闭数据库连接
db.close()