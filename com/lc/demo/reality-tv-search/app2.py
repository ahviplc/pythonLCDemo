import requests
from bs4 import BeautifulSoup

e = requests.get('https://www.bilibili.com/v/popular/rank/game')  # 当前网站链接
html = e.content
soup = BeautifulSoup(html, 'html.parser')  # 解析html
div_people_list = soup.find('ul', attrs={'class': 'rank-list'})  # 爬取ul类class为rank-list下的数据
ca_s = div_people_list.find_all('a', attrs={'class': 'title'})  # 爬取a类class为title下的数据

# 挨个传输到t，然后打印数据
for t in ca_s:
    url = t['href']
    name = t.get_text()
    print(name + '\t点击链接直接观看链接：' + f'http:{url}')
