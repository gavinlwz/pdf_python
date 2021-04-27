import requests
import xlwt
from bs4 import BeautifulSoup
import time
import pymysql

url = 'https://www.qiushibaike.com/text/page/1/'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
html = requests.get(url, headers=header)
bs = BeautifulSoup(html.text, 'html.parser')

divcount = bs.find('div', {'class': 'col1 old-style-col1'})
# print(divcount)
divlist = bs.find_all('div', {'class': "article block untagged mb15 typs_hot"})
all_products = []  # 全局函数爬起的数据存入列表
for i in divlist:
    author = i.find('h2').string
    content = i.find('div', class_='content').find('span').get_text().strip()
    stats = i.find('div', class_='stats')
    vote = stats.find('span', class_='stats-vote').find('i', class_='number').string
    comment = stats.find('span', class_='stats-comments').find('i', class_='number').string
    author_info = i.find('div', class_='articleGender')

    if author_info is not None:
        class_list = author_info['class']
        if 'womenIcon' in class_list:
            gender = '女'
        elif 'manIcon' in class_list:
            gender = '男'
        else:
            gender = ''
        age = author_info.string
    else:
        gender = ''
        age = '0'

    para = [author, content, vote, comment, gender, age]
    all_products.append([  # 创建excel表
        author, content, vote, comment, gender, age
    ])

    book = xlwt.Workbook()  # 创建一个workbook对象
    sh = book.add_sheet("股吧")
    col_name = ["阅读", "评论", "标题", "作者", "时间"]
    for col, name in enumerate(col_name):
        sh.write(0, col, name)

    for i, line in enumerate(all_products):  # 外层循环enumerate函数生成下标存入i中每行数据存入line中
        for j, item in enumerate(line):  # 内层循环enumerate函数生成下标存入j中每个单个数据存入iten中
            sh.write(i + 1, j, item)  # i+1是规避低=第零行 j规避 item数据
            pass
    book.save(r"D:\Desktop\股吧.xls")
