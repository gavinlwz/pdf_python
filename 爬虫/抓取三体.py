import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pickle
import time

all_products = []  ##创建文本


def get_links(url):  ##创建参数
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}  ##伪装头
    pagebody = urllib.request.Request(url, headers=header)  ##把头和身体连接
    page = urlopen(pagebody)
    bs = BeautifulSoup(page, 'html.parser')
    return bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile(
        '^(https://bk.tw.lvfukeji.com/baike-)((?!:).)*$'))  ##返回


links = get_links('https://bk.tw.lvfukeji.com/baike-%E4%B8%89%E4%BD%93_(%E5%B0%8F%E8%AF%B4)')
index = 0  ##记数
for i in links:
    if 'href' in i.attrs:  # 在i中是否有href
        linkinfo = i['href']
        name = urllib.parse.unquote(linkinfo[linkinfo.index('-') + 1:])  ##查找在‘—‘后的数据
        print(name)  ##输出
        links_son = get_links(linkinfo)
        all_products.append(links_son)
    if index == 5:  ##输出5条记录
        print('采集完毕')
        break  ###结束
    index += 1
    time.sleep(0.3)  ##延迟0.3秒
    # all_products.append({
    #     '链接名':name,
    #     '链接':linkinfo
    # })
else:
    print('没有数据了')
print(all_products)


###### 存储文件    每输出一个程序就存储起来

def saveFile(filename, all_producte):
    with open(filename + '.txt', 'wb') as fi:  # 转换成txt文本形式 用只写模式
        pickle.dump(all_products, fi)  # 程序化  把数据转换成字符串


for i in links:
    if 'href' in i.attrs:  # 在i中是否有href
        linkinfo = i['href']
        name = urllib.parse.unquote(linkinfo[linkinfo.index('-') + 1:])
        all_products.append({
            '链接名': name,
            '链接': linkinfo
        })
        saveFile(name, all_products)
