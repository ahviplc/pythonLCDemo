#!/usr/bin/env python
# -*- coding:utf-8 -*-
# test 测试服务类 pony_orm_test_service.py
import datetime
from pony.orm import sql_debug, db_session
# 从models导出类
from models.models import Artist, Artist2, Album

# 现在在db包下进行db初始化操作
pass


@db_session
def add_data_artist_for_mysql():
    new_artist = Artist(name="Newsboys-mysql")
    bands = ["MXPX", "Kutless", "Thousand Foot Krutch"]
    for band in bands:
        artist = Artist(name=band)

    album = Album(artist=new_artist,
                  title="Read All About It",
                  release_date=datetime.date(1988, 12, 1),
                  publisher="Refuge",
                  media_type="CD")

    albums = [{"artist": new_artist,
               "title": "Hell is for Wimps",
               "release_date": datetime.date(1990, 7, 31),
               "publisher": "Sparrow",
               "media_type": "CD"
               },
              {"artist": new_artist,
               "title": "Love Liberty Disco",
               "release_date": datetime.date(1999, 11, 16),
               "publisher": "Sparrow",
               "media_type": "CD"
               },
              {"artist": new_artist,
               "title": "Thrive",
               "release_date": datetime.date(2002, 3, 26),
               "publisher": "Sparrow",
               "media_type": "CD"}
              ]

    for album in albums:
        a = Album(**album)


@db_session
def add_data_artist_for_oracle():
    new_artist_from_oracle = Artist2(name="Newsboys-oralce")

# and so on.
