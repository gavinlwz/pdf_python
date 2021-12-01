# -*- coding: utf-8 -*-
# 版权所有 (C) 王菲
# @ 时间: 2021/11/9 16:52
#
# @ 作者     : 王菲
# @ 电子邮件  : 123@qq.com
# @ 文件     : 焦作新闻网爬起.py
# @ 软件     : PyCharm
from functools import reduce

import pymysql
import requests
from lxml import etree
import time

for i in range(1, 17):
    url = "http://www.jzrb.com/news/ShowClass.asp?ClassID=3&page={}".format(i)

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38"}
    text = requests.get(url, headers=header)  # 头
    text.encoding = "gb2312"  # 转gbk
    html = etree.HTML(text.text)  # 解析
    result = html.xpath('//div[@class="lmzj"]//tr[position()<29]')
    for i in result:
        house = {}
        href = i.xpath('./td[2]/a/@href')  # 链接
        href1 = ['http://www.jzrb.com' + i for i in href]  # 循环爬取到的链接添加链接头
        theme = i.xpath('./td[2]/a/@title')  # 标题
        Time = i.xpath('./td[3]/text()')  # 时间
        for i in href1:
            # time.sleep(3)
            text = requests.get(i, headers=header)  # 头
            text.encoding = "gb2312"  # 转gbk
            html1 = etree.HTML(text.text)  # 解析
            for i in html1:
                # head_lines = i.xpath('//div[@class="pcbdmap"]//p/text()')  # 内容
                shop = i.xpath('//div[@class="pcbdmap"]//p/text()')
                head_lines = reduce(lambda x, y: str(x) + str(y), shop)
                head_lines = ''.join(head_lines)  # 这个就可以了
                # reporter = i.xpath('//div[@class="pcbdmap"]//p[last()]/text()')  # 记者
                shop1 = i.xpath('//div[@class="pcbdmap"]//p[last()]/text()')
                reporter = reduce(lambda x, y: str(x) + str(y), shop1)
                reporter = ''.join(reporter)  # 这个就可以了
                source = '焦作日报'
                db = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='wangfei',
                                     charset='utf8mb4')
                conn = db.cursor()
                q = [theme, Time, head_lines, reporter, source]
                print(q)
                sql = u"insert into table_name (标题,时间,内容,记者,来源)values(%s,%s,%s,%s,%s)"
                conn.execute(sql, q)
