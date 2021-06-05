import requests
from lxml import etree
import requests_cache
import pymysql


def requisition():  # 请求
    requests_cache.install_cache()
    res = requests_cache.CachedSession()
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57",
    }
    text = res.get(url, headers=header)  # 头
    text.encoding = "gb2312"  # 转gbk
    html = etree.HTML(text.text)  # 解析
    return html


def datainfo(html, conn):
    result = html.xpath('//div[@id="menu"]/div/ul/li')[:15]
    # result = html.xpath('//div[@class="contain"]/ul/li')[:15]
    for i in result:
        links = i.xpath('./a/@href')  # 链接
        movieName = i.xpath('./a/text()')  # 分类
        qwert = ""
        links1 = 'https://dy2018.com' + qwert.join(links)
        movieName1 = qwert.join(movieName)
        print('链接', links1, '分类', movieName1)
        pen = [links1, movieName1]
        sql = "insert into dytt(links,movieName)values(%s,%s) "
        conn.execute(sql, pen)
        db.commit()


if __name__ == '__main__':
    url = 'https://www.dy2018.com/index.html'
    db = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='d1tk', charset='utf8')
    print('成功！')
    conn = db.cursor()
    requisition()
    html = requisition()
    datainfo(html, conn)
