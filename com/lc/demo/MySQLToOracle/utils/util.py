import datetime
import json
from cx_Oracle import makedsn


# get_now_time
def get_now_time():
    return datetime.datetime.now()


# 处理db_config_oracle
# 使其可用
def make_db_config_oracle_better(db_config_oracle):
    # print(db_config_oracle)
    db_config_oracle_dict = db_config_oracle
    db_config_oracle_dict_new = {}
    db_config_oracle_dict_new['provider'] = db_config_oracle_dict['provider']
    db_config_oracle_dict_new['user'] = db_config_oracle_dict['user']
    db_config_oracle_dict_new['password'] = db_config_oracle_dict['password']
    dsn_tns = makedsn(db_config_oracle_dict['host'], db_config_oracle_dict['port'], db_config_oracle_dict['sid'])
    # 如果是Oracle 12c 数据库需要替换sid 为service_name
    dsn_tns = dsn_tns.replace('SID', 'SERVICE_NAME')
    db_config_oracle_dict_new['dsn'] = dsn_tns
    # print('...美化后...db_config_oracle...',db_config_oracle_dict_new)
    return db_config_oracle_dict_new
