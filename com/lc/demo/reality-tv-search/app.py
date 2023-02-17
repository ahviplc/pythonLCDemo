import requests
from bs4 import BeautifulSoup

e = requests.get('https://search.bilibili.com/video?keyword=%E7%9C%9F%E4%BA%BA%E7%A7%80')  # 当前网站链接 B站搜索真人秀
html = e.content
soup = BeautifulSoup(html, 'html.parser')  # 解析html
div_people_list = soup.find('ul', attrs={'class': 'video-list'})  # 爬取ul类class为video-list下的数据
# print(div_people_list)
div_people_list_bs = BeautifulSoup(str(div_people_list), "html.parser")
# print(a.contents[0])
items = div_people_list_bs.contents[0]
print("共爬取到视频数量为 => ", len(items.contents))
# 挨个传输到items，然后打印数据
for t in items:
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
    print("===this_info 视频url===> ", 'https:' + this_info.contents[3].get('href'))
    # print('==================')
    # print(more_info_con_bs.contents[1])
    this_info2 = more_info_con_bs.contents[1]
    print("===this_info2 简介===> ", this_info2.text.strip())
    # print(more_info_con_bs.contents[2])
    this_info3 = more_info_con_bs.contents[2]
    print("===this_info3 视频全信息===> ")
    print("===this_info3 视频全信息 观看量===> ", this_info3.contents[0].text.strip())
    print("===this_info3 视频全信息 弹幕数量===> ", this_info3.contents[1].text.strip())
    print("===this_info3 视频全信息 上传时间===> ", this_info3.contents[2].text.strip())
    print("===this_info3 视频全信息 上传up主===> ", this_info3.contents[3].text.strip())
    print('==========================================================================================')
