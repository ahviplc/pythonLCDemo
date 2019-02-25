#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
pythonSQLServerApp.py
python操作SQLServer数据库
Version: 1.0
Author: LC
DateTime: 2019年2月23日13:30:07
UpdateTime: None
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""
import pymssql


# main方法
def main():
    conn = pymssql.connect(host="Server\SQLEXPRESS", user="sa", password="lmt123", database="HTGasMeterSystemSHLMT",charset="utf8")
    cur = conn.cursor(as_dict=True)  # as_dict（bool）：是否作为字典返回，默认为元组 ------ as_dict=True
    if not cur:
        raise (NameError, "数据库连接失败")
    cur.execute("SELECT top 30 * from CustomerInfo")
    resList = cur.fetchall()  # fetchall()是接收全部的返回结果行
    conn.close()
    print(resList)


# main方法一:生成操作persons.sql示例
def main1():

    # host    数据库服务器名称或IP
    # user      用户名
    # password  密码
    # database  数据库名称
    conn = pymssql.connect(host="Server\SQLEXPRESS", user="sa", password="lmt123", database="HTGasMeterSystemSHLMT",charset="utf8")

    cursor = conn.cursor(as_dict=True)  # as_dict（bool）：是否作为字典返回，默认为元组 ------ as_dict=True

    # 新建、插入操作
    cursor.execute("""
    IF OBJECT_ID('persons', 'U') IS NOT NULL
        DROP TABLE persons
    CREATE TABLE persons (
        id INT NOT NULL,
        name VARCHAR(100),
        salesrep VARCHAR(100),
        PRIMARY KEY(id)
    )
    """)
    cursor.executemany(
        "INSERT INTO persons VALUES (%d, %s, %s)",
        [(1, 'John Smith', 'John Doe'),
         (2, 'Jane Doe', 'Joe Dog'),
         (3, 'Mike T.', 'Sarah H.')])
    # 如果没有指定autocommit属性为True的话就需要调用commit()方法
    conn.commit()

    # 查询操作1
    # cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
    # row = cursor.fetchone()
    # print(row)
    # while row:
    #     print("ID=%d, Name=%s" % (row[0], row[1]))
    #     row = cursor.fetchone()

    # 查询操作2
    # 也可以使用for循环来迭代查询结果
    # cursor.execute('SELECT * FROM persons')
    # for row in cursor:
    #     print("for循环:ID=%d, Name=%s" % (row[0], row[1]))

    # 查询操作3
    # 也可以使用for循环来迭代查询结果
    cursor.execute('SELECT * FROM persons')
    row_all = cursor.fetchall()
    print(row_all)
    for row in row_all:
        print(row)

    # 关闭连接
    conn.close()


# 使用with语句（上下文管理器）main2
# 可以通过使用with语句来省去显示的调用close方法关闭连接和游标
def main2():
    # host    数据库服务器名称或IP
    # user      用户名
    # password  密码
    # database  数据库名称
    with pymssql.connect(host="Server\SQLEXPRESS", user="sa", password="lmt123", database="HTGasMeterSystemSHLMT",charset="utf8") as conn:
        with conn.cursor(as_dict=True) as cursor:
            cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
            for row in cursor:
                print("ID=%d, Name=%s" % (row['id'], row['name']))


# 使用with语句（上下文管理器）main3
# 可以通过使用with语句来省去显示的调用close方法关闭连接和游标
def main3():
    # host    数据库服务器名称或IP
    # user      用户名
    # password  密码
    # database  数据库名称
    with pymssql.connect(host="Server\SQLEXPRESS", user="sa", password="lmt123", database="HTGasMeterSystemSHLMT",charset="utf8") as conn:
        with conn.cursor(as_dict=True) as cursor:
            cursor.execute('SELECT * FROM persons')
            row_all = cursor.fetchall()
            print(row_all)
            for row in row_all:
                print(row)

# main方法
if __name__ == '__main__':
    # main()
    # main1()
    # main2()
    main3()

# cur = conn.cursor() 输出如下:
# [('0000000001', 0, '合同号', '客户名称', '固定电话', '手机', '证件号码', '0000000000', '详细地址', '楼号', '单元号', '室号', 1, '自定义编号1', '自定义编号2', '自定义编号3', '备注', 1, '', '银行授权码', '银行账号', '银行账户名', 0, '税号', '01', datetime.datetime(2018, 3, 7, 9, 44, 2, 220000), datetime.datetime(2018, 3, 7, 9, 46, 58, 250000), '管理员', '', '', '0000000000'), ('0000000002', 0, '合同号', '客户名称', '固定电话', '手机', '证件号码', '0000000000', '详细地址', '楼号', '单元号', '室号', 0, '1', '2', '3', '备注', 0, '', '银行授权码', '银行账号', '银行账户名', 0, '税号', '01', datetime.datetime(2018, 3, 9, 9, 47, 26, 683000), datetime.datetime(2018, 3, 9, 9, 47, 26, 683000), '管理员', '123', 'CAF1A3DFB505FFED0D024130F58C5CFA', '0000000000')]


# cur = conn.cursor(as_dict=True) 输出如下:
# [{'customerNo': '0000000001', 'customerType': 0, 'contractNo': '合同号', 'customerName': '客户名称', 'telNo': '固定电话', 'mobileNo': '手机', 'certNo': '证件号码', 'estateNo': '0000000000', 'address': '详细地址', 'houseNo': '楼号', 'cellNo': '单元号', 'roomNo': '室号', 'useState': 1, 'defineNo1': '自定义编号1', 'defineNo2': '自定义编号2', 'defineNo3': '自定义编号3', 'remark': '备注', 'payWay': 1, 'bankNo': '', 'bankAuthNo': '银行授权码', 'accountNo': '银行账号', 'accountName': '银行账户名', 'bankCheck': 0, 'taxNo': '税号', 'enterpriseNo': '01', 'buildTime': datetime.datetime(2018, 3, 7, 9, 44, 2, 220000), 'editTime': datetime.datetime(2018, 3, 7, 9, 46, 58, 250000), 'Operator': '管理员', 'loginName': '', 'Password': '', 'BranchNo': '0000000000'}, {'customerNo': '0000000002', 'customerType': 0, 'contractNo': '合同号', 'customerName': '客户名称', 'telNo': '固定电话', 'mobileNo': '手机', 'certNo': '证件号码', 'estateNo': '0000000000', 'address': '详细地址', 'houseNo': '楼号', 'cellNo': '单元号', 'roomNo': '室号', 'useState': 0, 'defineNo1': '1', 'defineNo2': '2', 'defineNo3': '3', 'remark': '备注', 'payWay': 0, 'bankNo': '', 'bankAuthNo': '银行授权码', 'accountNo': '银行账号', 'accountName': '银行账户名', 'bankCheck': 0, 'taxNo': '税号', 'enterpriseNo': '01', 'buildTime': datetime.datetime(2018, 3, 9, 9, 47, 26, 683000), 'editTime': datetime.datetime(2018, 3, 9, 9, 47, 26, 683000), 'Operator': '管理员', 'loginName': '123', 'Password': 'CAF1A3DFB505FFED0D024130F58C5CFA', 'BranchNo': '0000000000'}]


# 游标返回行为字典变量
# 上述例子中游标获取的查询结果的每一行为元组类型，
# 可以通过在创建游标时指定as_dict参数来使游标返回字典变量，
# as_dict（bool）：是否作为字典返回，默认为元组 ------ as_dict=True
# 字典中的键为数据表的列名
