# common_config 通用配置
common_config = {
    "org_id": "0080",  # org_id 要查询机构号 目前均是 0080
    "run_type": 0,  # run_type 为 0 代表是命令自动执行 无需手动yes确认 【取用 days】 | 为 1 代表 手动执行 针对某一天 需要手动yes确认 【取用 自定义日期 diy_date】|为 2 代表 手动执行 针对某段日期 需要手动yes确认 【取用 自定义日期范围 diy_date】
    "days": -1,  # run_type为0时使用 【days 0代表今天 -1代表昨天 +n代表n天后 -n代表n天前 默认为-1 跑昨天的数据】
    "diy_date": "20210405",  # run_type为1时使用 【20210402 代表就是 抓取 20210402这一天的数据】
    "diy_range_date": "20210405#20210412",  # run_type为2时使用 【20210301#20210331 代表就是 抓取 20210301这一天的最小时间到20210331这一天的最大时间的数据】
    "is_open_log": False,  # 是否开启log日志 | False 不开启 True 开启
    "is_show_sql": False,  # 是否显示pony 执行过程中 SQL语句 | False 不显示 True 显示
    "is_mysql_create_tables": False,  # 默认False即可 不用动 MySQL对象关系映射ORM时是否建表
    "is_oracle_create_tables": False,  # 默认False即可 不用动 Oracle对象关系映射ORM时是否建表
}

# mysql for pony【pony_orm_DBHelper.py】
mysql_db_config = {
    "provider": "mysql",  # 声明数据库种类
    "host": "192.168.0.17",  # 数据库主机地址，也可以是域名
    "port": 3306,  # 端口
    "database": "htiot_qinghaixn_report",  # 数据库名
    "user": "root",  # 用户名
    "password": "Lmtmysql@1",  # 密码
    "charset": "utf8mb4",  # 字符集
}

# oracle for pony【pony_orm_DBHelper.py】
# oracle for cx_Oracle【cx_Oracle_DBHelper.py】
# 真正需要的 是下面四个
# db.bind(provider='oracle', user='', password='', dsn='')
# 一起传过去,为了再次处理,加工
oracle_db_config = {
    "provider": "oracle",  # 声明数据库种类
    "host": "192.168.0.7",  # 数据库主机地址，也可以是域名
    "port": 1521,  # 端口
    "sid": 'LMTPlat',  # sid
    'dsn': '',  # dsn 使用cx_Oracle.makedsn()处理一下
    "user": "SCOTT",  # 用户名
    "password": "Lmt123456",  # 密码
}

# mysql for pymysql【pymysql_DBHelper.py】
# 这个测试使用,无需修改,生产环境用不到
mysql_db_config_for_pymysql = {
    'host': '192.168.0.17',
    'port': 3306,
    'username': 'root',
    'password': 'Lmtmysql@1',
    'database': 'htiot_qinghaixn_report',
    'charset': 'utf8mb4'
}

# mysql for pony【pony_orm_DBHelper.py】 本地数据库 测试使用
mysql_db_config_local = {
    "provider": "mysql",  # 声明数据库种类
    "host": "192.168.0.17",  # 数据库主机地址，也可以是域名
    "port": 3306,  # 端口
    "database": "htiot_qinghaixn_report",  # 数据库名
    "user": "root",  # 用户名
    "password": "Lmt123456",  # 密码
    "charset": "utf8mb4",  # 字符集
}
