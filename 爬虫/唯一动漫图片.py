# -*- coding: utf-8 -*-
# @Time    : 2021/3/24 18:27
# @Author  : wamgmingfei
# @Email   : wangmoufei@live.com
# @File    : 唯一动漫图片.py
import pymysql
import requests
from lxml import etree


class DB:
    def __init__(self, host='', port=3306, user='', password='', db='', charset='utf8'):
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, database=db, charset=charset)
        self.cur = self.conn.cursor()

    def __enter__(self):  # 初始化类之后执行的 进入的时候
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cur.close()
        self.conn.close()


def main(db):
    url = 'https://www.mmonly.cc/ktmh/'
    html = dataUrl(url)
    dataHtml(html, db)


def dataUrl(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57",
    }
    text = requests.get(url, headers=header)  # 头
    text.encoding = "gb2312"  # 转gbk
    html = etree.HTML(text.text)  # 解析
    return html


def dataHtml(html, db):
    result = html.xpath('//*[@class="ABox"]')
    for i in result:
        linkinfo = i.xpath('./a/@href')
        nameinfo = i.xpath('./a/img/@alt')
        imageinfo = i.xpath('./a/img/@src')
        print('图片链接', linkinfo, '图片名字', nameinfo, '图片地址', imageinfo)
        para = [linkinfo, nameinfo, imageinfo]
        print(para)
        db.execute(
            'insert into d1tk (linkinfo,nameinfo,imageinfo) values (%s,%s,%s)',
            para)  # 把获取到的数据到如到数据库


if __name__ == '__main__':
    with DB(host='localhost', port=3306, user='root', password='root', db='d1tk') as db:  # 数据库链接
        db.execute('SET NAMES utf8')
        main(db)
