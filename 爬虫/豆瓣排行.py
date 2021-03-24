import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


url = 'https://movie.douban.com/top250?start=0&filter='

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
req = urllib.request.Request(url, headers=headers)
page = urlopen(req)
bs=BeautifulSoup(page,'lxml')
dataInfo=[]#全局函数
li_list=bs.find('ol',class_='grid_view').find_all('li')
for i in li_list:
    #电影名
    dy=i.find(class_='hd').find('span').string
    #电影链接
    lj=i.find(class_='hd').find('a')['href']
    #电影导演
    daoyan=i.find(class_='bd').find(text=re.compile('.*?导演:\s(.*?)\s',re.S)).string.strip()

    dataInfo.append({
        "电影名": dy,
        "电影链接":lj,
        "导演主演": daoyan,

    })

print(dataInfo)
    # print('电影名：  ',dy)
    # print('电影链接：',lj)
    # print(daoyan)