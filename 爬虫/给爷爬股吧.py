import csv

import pandas as pd
import requests
from lxml import etree
import pandas as pd
from openpyxl import Workbook
import xlwt
import xlrd

url = 'https://guba.eastmoney.com/'

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57",
}
text = requests.get(url, headers=header)  # 头
text.encoding = "utf-8"  # 转gbk
html = etree.HTML(text.text)  # 解析
result = html.xpath('//ul[@class="newlist"]/li')
all_products = []  # 全局函数爬起的数据存入列表
for i in result:
    comp = i.xpath('./cite/text()')
    readinfo = comp[0].strip()  # 阅读
    commentinfo = comp[1].strip()  # 评论
    titleinfo = i.xpath('./span/a/@title')  # 标题
    Authorinfo = i.xpath('./cite[@class="aut"]/a/font/text()')  # 作者
    # Authorinfo=Authorinfo.xpath('./a/font/text()')
    Update = comp[5].strip()  # 时间
    all_products.append([  # 创建excel表
        readinfo,
        commentinfo,
        titleinfo,
        Authorinfo,
        Update,
    ])
    # print(all_products)

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
