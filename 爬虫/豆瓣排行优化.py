import urllib

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pandas as pd

dataInfo=[]#全局函数
def  getHtml(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
    req = urllib.request.Request(url, headers=headers)
    page = urlopen(req)
    bs=BeautifulSoup(page,'lxml')
    return bs


def getData(bs):
    li_list = bs.find('ol', class_='grid_view').find_all('li')
    for i in li_list:
        # 电影名
        dy = i.find(class_='hd').find('span').string
        # 电影链接
        lj = i.find(class_='hd').find('a')['href']
        # 电影导演
        daoyan = i.find(class_='bd').find(text=re.compile('.*?导演:\s(.*?)\s', re.S)).string.strip()

        dataInfo.append({
            "电影名": dy,
            "电影链接": lj,
            "导演主演": daoyan,

        })


for i in (0,250,25):
    url_com = 'https://movie.douban.com/top250?start='+str(i)+'&filter='
    bs=getHtml(url_com)
    getData(bs)

keys=dataInfo[0].keys()
pd.DataFrame(dataInfo,columns=keys).to_csv('豆瓣排行榜.csv',encoding='utf-8-sig')




































