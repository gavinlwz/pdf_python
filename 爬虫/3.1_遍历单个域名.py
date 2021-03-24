# -*- coding: utf-8 -*-
# @Time    : 2020/10/28 13:43
# @Author  : Anjianyong
# @Email   : anjianyong@live.com
# @File    : 3.1_遍历单个域名.py

'''


headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}
url='https://bk.tw.lvfukeji.com/baike-%E4%B8%89%E4%BD%93_(%E5%B0%8F%E8%AF%B4)'  #拼接全地址
'''
#
# 1.得有一个链接   https://bk.tw.lvfukeji.com/baike-%E4%B8%AD%E5%9B%BD%E5%A4%A7%E9%99%86
# 2.得有一个伪装头 F12 NETWORK HEADERS
# 3.拼接头和链接
# 4.打开这个链接
# 5.用bs库进行解析
# 6.获取数据

import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pickle
import time

all_products = []
def get_Links(url):
        head = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
        pageBody = urllib.request.Request(url, headers=head)  # 拼接头和身体
        page = urlopen(pageBody)
        bs = BeautifulSoup(page, 'html.parser')  # lxml
        return bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile(
                '^(https://bk.tw.lvfukeji.com/baike-)((?!:).)*$'))

def saveFile(fileName,all_products):
        with open(fileName+'.txt', 'wb') as fi:  # write
                pickle.dump(all_products, fi)  # 序列化

links = get_Links('https://bk.tw.lvfukeji.com/baike-%E4%B8%89%E4%BD%93_(%E5%B0%8F%E8%AF%B4)')
index =0
for i in links:
        if 'href' in i.attrs:
                linkInfo = i['href']
                name =urllib.parse.unquote(linkInfo[linkInfo.index('-')+1:] )    #[6:]   [:6]
                # print(name)
                # links_son = get_Links(linkInfo)
                # all_products.append(links_son)
                all_products.append({
                        '链接名': name,
                        '链接': linkInfo
                })
                saveFile(name,all_products)
        if index==5:
                print('采集完毕')
                break
        index+=1
        time.sleep(0.3)

else:
        print('没有数据了')
print(all_products)

# fi = open('DataOne.txt','wb')  # write
# d = pickle.dump(all_products,fi)  #序列化
# fi.close()
#

#
# with open('DataOne.txt','rb') as fi:  # read
#         info = pickle.load(fi)  #反序列化
#         print(type(info))

# with.... as ....:



