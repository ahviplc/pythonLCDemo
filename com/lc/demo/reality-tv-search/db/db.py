import datetime

from pony.orm import *

db_mysql = Database()
db_mysql.bind(provider='mysql', user='root', password='lc2022888', host='43.142.58.153', port=3306,
              database='reality-tv-search')

set_sql_debug(True)


@db_mysql.on_connect(provider='mysql')
def sqlite_case_sensitivity(db, connection):
    print(db, '连接了')


# 暴露db的数据库引擎给外面
def get_dbs():
    init_db(False, True)
    return db_mysql


# 初始化db
# is_show_sql 是否显示sql
# is_mysql_create_tables 其MySQL引擎是否创建表
def init_db(is_show_sql, is_mysql_create_tables):
    sql_debug(is_show_sql)  # 显示debug信息(sql语句)  turn on debug mode
    db_mysql.generate_mapping(create_tables=is_mysql_create_tables, check_tables=True)


# 写model
# id B站视频AV/BV号 视频标题 视频播放url  简介 观看量 弹幕数量 上传时间 上传up主昵称 封面图片 真实播放地址 时长 视频分类
# 以上面的顺序排列了下面的字段
class TVideo(db_mysql.Entity):
    id = PrimaryKey(str, max_len=50, nullable=False, auto=False)
    abv_id = Required(str, nullable=False)  # 先去掉了 unique=True,
    title = Required(str)
    bili_url = Required(str)
    desc = Optional(str, max_len=1000, nullable=True, default=None)

    watch_counts = Optional(str, max_len=50, nullable=True, default=None)
    danmu_counts = Optional(str, max_len=50, nullable=True, default=None)
    up_time = Required(int, nullable=False, column="up_time")
    up_name = Optional(str, max_len=50, nullable=True, default=None)
    tv_pic = Optional(str, max_len=1000, nullable=True, default=None)

    real_url = Optional(str, max_len=1000, nullable=True, default=None)
    tv_duration = Optional(str, max_len=50, nullable=True, default=None)
    tv_category = Optional(str, max_len=50, nullable=True, default=None)


@db_session
def add_tvideo_for_mysql(id, abv_id, title, bili_url, desc, watch_counts, danmu_counts, up_time, up_name, tv_pic,
                         real_url, tv_duration, tv_category):
    try:
        new_TVideo = TVideo(id=id, abv_id=abv_id, title=title, bili_url=bili_url, desc=desc,
                            watch_counts=watch_counts, danmu_counts=danmu_counts, up_time=up_time, up_name=up_name,
                            tv_pic=tv_pic,
                            real_url=real_url, tv_duration=tv_duration, tv_category=tv_category)
    except Exception as ex:
        print(abv_id, ' 已存在 跳过 Exception=> ', ex)
    finally:
        # 将 db_session() 缓存中累积的更改保存到数据库中。您可能永远不需要手动调用此方法，因为它会在离开 db_session() 时自动完成。
        # flush()
        # 使用 flush() 方法保存在当前 db_session() 中所做的所有更改，并将事务提交到数据库。
        commit()  # 提交事务


@db_session
def selectTVideo(this_av_bv_id):
    res = select(item for item in TVideo if item.abv_id == this_av_bv_id)
    res_list = res[:].to_list()
    return len(res_list)


if __name__ == '__main__':
    pass
    # init_db(True, True)
    # add_tvideo_for_mysql(1, "1111", '222', "111", 1676541532)
