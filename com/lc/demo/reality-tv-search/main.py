import json
import uuid
import time
import os

import requests
from bs4 import BeautifulSoup
from db.db import add_tvideo_for_mysql, get_dbs, selectTVideo

# 初始化一下db
db = get_dbs()


# 真人秀视频搜索系统 爬虫视频程序

def run(this_url, which_page, tv_category, this_how_many):
    this_url = this_url + '&page=' + str(which_page)
    url = requests.get(this_url)  # 当前网站链接 B站搜索真人秀
    html = url.content
    soup = BeautifulSoup(html, 'html.parser')  # 解析html
    div_people_list = soup.find('ul', attrs={'class': 'video-list'})  # 爬取ul类class为video-list下的数据
    # print(div_people_list)
    div_people_list_bs = BeautifulSoup(str(div_people_list), "html.parser")
    # print(a.contents[0])
    items = div_people_list_bs.contents[0]
    print("共爬取到视频数量为 => ", len(items.contents)," 但你只要总条数为 => ", this_how_many, ' 当前类别为 => ', tv_category)
    # 挨个传输到items，然后打印数据
    this_count = 0
    for t in items:
        this_count = this_count + 1
        if this_count > this_how_many:
            print('========================= ☆ 爬取完毕 | 总共条数', this_how_many)
            break
        else:
            print('========================= ☆ 正在爬取第', this_count, '条数据 | 总共条数', this_how_many)
        print('==========================================================================================')
        # print(t)
        # print(type(t))
        simple_info = t.contents[0]
        # print(simple_info)
        print("此视频简单信息为", simple_info.get('title'), 'https:' + simple_info.get('href'))
        # print('==================')
        more_info = t.contents[1]
        # print(more_info)
        more_info_bs = BeautifulSoup(str(more_info), "html.parser")
        more_info_con_bs = more_info_bs.contents[0]
        # print('==================')
        # print(more_info_con_bs.contents[0])
        this_info = more_info_con_bs.contents[0]
        print("===this_info 视频标题===> ", this_info.text.strip())
        this_real_url = 'https:' + this_info.contents[3].get('href')
        print("===this_info 视频url===> ", this_real_url)
        this_real_url2 = str(this_real_url)[0:-12]
        print("===this_info 视频url去除问号===> ", this_real_url2)
        this_real_url3 = this_real_url2.split("/")
        print("===this_info B站视频AV/BV号===> ", this_real_url3[4])
        # print('==================')
        # print(more_info_con_bs.contents[1])
        this_info2 = more_info_con_bs.contents[1]
        print("===this_info2 简介===> ", this_info2.text.strip())
        # print(more_info_con_bs.contents[2])
        this_info3 = more_info_con_bs.contents[2]
        print("===this_info3 视频全信息===> ")
        print("===this_info3 视频全信息 观看量===> ", this_info3.contents[0].text.strip())
        print("===this_info3 视频全信息 弹幕数量===> ", this_info3.contents[1].text.strip())
        print("===this_info3 视频全信息 上传日期===> ", this_info3.contents[2].text.strip())
        print("===this_info3 视频全信息 上传up主===> ", this_info3.contents[3].text.strip())
        # 获取封面和时长
        this_json_data = get_data_by_av_bv(this_real_url3[4])
        print("===this_info4 视频全信息 视频封面===> ", this_json_data['data']['pic'])
        print("===this_info4 视频全信息 视频时长===> ", this_json_data['data']['duration'])
        print("===this_info4 视频全信息 视频时间日期 时间戳形式===> ", this_json_data['data']['pubdate'])
        # 获取视频播放真正的url
        # 先隐掉
        # print("===this_info4 视频全信息 真实播放地址===> ", get_real_url(this_real_url2))
        # 使用方法2获取视频地址
        # print("===this_info4 视频全信息 真实播放地址2===> ", get_real_url2(this_json_data['data']['cid'], this_json_data['data']['aid'], this_real_url3[4]))
        print("===this_info4 视频全信息 真实播放地址2===> ", this_real_url3[4] + '.mp4' + '#' + this_real_url3[4] + '.mp3')
        # 写入mysql数据库
        count = selectTVideo(this_real_url3[4])
        if count == 0:
            print('此AV/BV 入库成功 => ', this_real_url3[4])
            add_tvideo_for_mysql(str(uuid.uuid4()), this_real_url3[4], this_info.text.strip(), this_real_url2,
                                 this_info2.text.strip(),
                                 this_info3.contents[0].text.strip(), this_info3.contents[1].text.strip(),
                                 this_json_data['data']['pubdate'],
                                 this_info3.contents[3].text.strip(), this_json_data['data']['pic'],
                                 get_real_url2(this_json_data['data']['cid'], this_json_data['data']['aid'], this_real_url3[4]), str(this_json_data['data']['duration']), tv_category)
        else:
            print('此AV/BV已存在 不入库 跳过 => ', this_real_url3[4])
        print('==========================================================================================')


# 通过AV/BV号获取视频信息 json格式
def get_data_by_av_bv(this_id):
    # 获取封面和时长
    url = requests.get('https://api.bilibili.com/x/web-interface/view?bvid=' + this_id)
    # print(url.content)
    this_json_data = json.loads(str(url.content, encoding="utf-8"))
    return this_json_data


# 获取真实的播放地址
def get_real_url(av_bv_url):
    # 模仿浏览器UA头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        "upgrade-insecure-requests": "1"
    }
    # 参数
    params = {}
    # 延时一下 防止过快
    time.sleep(0.6)
    url = requests.get(
        'https://www.fodownloader.com/csgeturl?lang=zh-cn&urlInfo=' + av_bv_url, params=params, headers=headers)
    # print(url.content)
    this_html = str(url.content, encoding="utf-8")
    # print(this_html)
    this_html_bs = BeautifulSoup(this_html, "html.parser")
    this_html_bs_ok = this_html_bs.find_all('video')  # 查询 video元素
    this_html_bs_ok = BeautifulSoup(str(this_html_bs_ok[0]), "html.parser")
    return this_html_bs_ok.contents[0]['src']


# 获取真实的播放地址 使用b官方接口
# 自己在前端拼接播放路径吧
def get_real_url2(this_cid, this_aid,this_bvid):
    # 模仿浏览器UA头
    headers = {
        'Referer': 'https://www.bilibili.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    # 参数
    params = {}
    # 延时一下 防止过快
    time.sleep(0.6)
    url = requests.get(
        'https://api.bilibili.com/x/player/playurl?fnval=80&avid=' + str(this_aid) + '&cid=' + str(this_cid), params=params,
        headers=headers)
    # print(url.content)
    this_html = str(url.content, encoding="utf-8")
    this_json_data = json.loads(this_html)
    # 获取视频流地址 m4s格式
    this_video_url =this_json_data['data']['dash']['video'][0]['base_url']
    # this_video_url 再次请求获取二进制流数据 .mp4
    time.sleep(0.3)
    video_response = requests.get(this_video_url, headers=headers).content
    # print(video_response_str)

    # 获取音频流地址 m4s格式
    this_audio_url =this_json_data['data']['dash']['audio'][0]['base_url']
    # this_audio_url 再次请求获取二进制流数据 .mp3
    time.sleep(0.3)
    audioResponse = requests.get(this_audio_url, headers=headers).content

    # 保存到本地
    if os.path.exists("./public/" + this_bvid + ".mp4"):
        print('视频文件 已存在 不存入了 跳过 => ', "./public/" + this_bvid + ".mp4")
    else:
        save_file(video_response, this_bvid + ".mp4")
        print('视频文件 已存入了 目录为 => ', "./public/" + this_bvid + ".mp4")

    if os.path.exists("./public/" + this_bvid + ".mp3"):
        print('音频文件 已存在 不存入了 跳过 => ', "./public/" + this_bvid + ".mp3")
    else:
        save_file(audioResponse, this_bvid + ".mp3")
        print('音频文件 已存入了 目录为 => ', "./public/" + this_bvid + ".mp3")
    pass
    return this_bvid + '.mp4' + '#' + this_bvid + '.mp3'


# 保存音视频文件到本地
# 保存到public文件夹
def save_file(data, name):
    with open("./public/" + name, mode="wb") as f:
        f.write(data)


# this_url 不用改变 url
# which_page 可以改变 选择爬取页面
# tv_category 不用改变 类别
# this_how_many 可以改变 默认每页爬取多少条 使用this_how_many控制 最大是20
if __name__ == '__main__':
    # 综合排序
    # run('https://search.bilibili.com/video?keyword=%E7%9C%9F%E4%BA%BA%E7%A7%80', 1,'all', 2)
    # 最多点击
    # run('https://search.bilibili.com/video?keyword=%E7%9C%9F%E4%BA%BA%E7%A7%80&order=click', 1,'click', 2)
    # 最新发布
    run('https://search.bilibili.com/video?keyword=%E7%9C%9F%E4%BA%BA%E7%A7%80&order=pubdate', 12, 'pubdate', 1)
    # 最多弹幕
    # run('https://search.bilibili.com/video?keyword=%E7%9C%9F%E4%BA%BA%E7%A7%80&order=dm', 1,'dm', 2)
    # 最多收藏
    # run('https://search.bilibili.com/video?keyword=%E7%9C%9F%E4%BA%BA%E7%A7%80&order=stow', 1,'stow', 2)