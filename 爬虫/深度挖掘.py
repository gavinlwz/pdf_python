import pickle
import re
import time

from urllib.request import urlopen

from bs4 import BeautifulSoup
import urllib

all_products = []
def get_links(url):

# 创造头
    headers = {
    'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
#拼接头
    page =urllib.request.Request(url, headers=headers)

    html = urlopen(page)
#解析地址
    bs = BeautifulSoup(html, 'lxml')
#获取地址

    return bs.find('div',{'id':'bodyContent'}).find_all('a',href=re.compile('^(https://bk.tw.lvfukeji.com/baike-)((?!:).)*$'))
links= get_links('https://bk.tw.lvfukeji.com/baike-%E4%B8%89%E4%BD%93_(%E5%B0%8F%E8%AF%B4)')
index=0
#循环lists获取地址
for i in links :
    if 'href' in i.attrs:
        #清除空地址
        linkInfo = i['href']
        #解析获取到的地址成中文
        name = urllib.parse.unquote(linkInfo[linkInfo.index('-')+1:])
        all_products.append({
            '链接名': name,
            '链接': linkInfo,
        })
        print(name)
        print(linkInfo)
        # links_son = get_links(linkInfo)
        # all_products.append(links_son)
         ##输出5条记录

          ###结束

    # time.sleep(0.3)



# fi=open('DataOne.txt','wb')
# d=pickle.dump(all_products,fi)
# fi.close()

# with open ('DataOne.txt','wb') as fi:
#     pickle.dump(all_products,fi)
#
# with open('DataOne.txt','rb') as fi:
#     info = pickle.load(fi)
#     print(type(info))
