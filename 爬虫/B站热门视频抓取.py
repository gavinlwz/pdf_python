import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import pandas as pd
url = 'https://www.bilibili.com/v/popular/rank/all'#抓取的网址
#请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
page = urllib.request.Request(url, headers=headers)#安装请求头
html = urlopen(page)#模拟请求赋值
soup = BeautifulSoup(html, 'lxml')#解析网页
all_products = []
products = soup.select('li.rank-item')
for product in products:
    rank = product.select('div.num')[0].text#要抓取的标签
    name = product.select('div.info > a')[0].text.strip()#要抓取的标签
    play = product.select('span.data-box')[0].text#要抓取的标签
    comment = product.select('span.data-box')[1].text#要抓取的标签
    up = product.select('span.data-box')[2].text#要抓取的标签
    url = product.select('div.info > a')[0].attrs['href']#要抓取的标签

    all_products.append({#创建excel表
        "视频排名":rank,
        "视频名": name,
        "播放量": play,
        "弹幕量": comment,
        "up主": up,
        "视频链接": url
    })


keys = all_products[0].keys()

with open('B站视频热榜TOP100.csv', 'w', newline='', encoding='utf-8-sig') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_products)

#写入数据
pd.DataFrame(all_products,columns=keys).to_csv('B站视频热榜TOP100.csv', encoding='utf-8-sig')
