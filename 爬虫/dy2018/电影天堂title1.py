import pymysql
import requests
from lxml import etree

# # # 根据流程
# # # 1.我们先建立数据库的连接信息
# # host = ****  # 数据库的ip地址
# # user = ***  # 数据库的账号
# # password = ***  # 数据库的密码
# # port = 3306  # mysql数据库通用端口号
#
#
#
# def parse_URL(url):
#     header = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57",
#     }
#     text = requests.get(url, headers=header)  # 头
#     text.encoding = "gb2312"  # 转gbk
#     html = etree.HTML(text.text)  # 解析
#     print(html)
#
# if __name__ == '__main__':
#     db = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='d1tk', charset='utf8')
#     # 2.新建个查询页面
#     cursor = db.cursor()
#     # 3编写sql
#     # sql = 'SELECT * FROM future.member WHERE MobilePhone = 18876153542 '
#     # 4.执行sql
#     # cursor.execute('select links from dytt')
#     cursor.execute('select links from dytt where isdelete=0')
#     # 5.查看结果
#     # url = cursor.fetchone() #用于返回单条数据
#     url = cursor.fetchall()  # 用于返回多条数据/
#     print(url)
#     # parse_URL(url)


import requests
from lxml import etree
import requests_cache
import pymysql

url = 'https://www.dy2018.com/index.html'
requests_cache.install_cache()
res = requests_cache.CachedSession()
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57",
}
text = res.get(url, headers=header)  # 头
text.encoding = "gb2312"  # 转gbk
html = etree.HTML(text.text)  # 解析

result = html.xpath('//div[@id="menu"]/div/ul/li')[:15]
# result = html.xpath('//div[@class="contain"]/ul/li')[:15]
for i in result:
    links = i.xpath('./a/@href')  # 链接
    movieName = i.xpath('./a/text()')  # 分类
    qwert = ""
    links1 = 'https://www.dy2018.com' + qwert.join(links)
    movieName1 = qwert.join(movieName)
    print(links1, movieName1)
    requests_cache.install_cache()
    req = requests_cache.CachedSession()
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57",
    }
    text = req.get(links1, headers=header)  # 头
    text.encoding = "gb2312"  # 转gbk
    html = etree.HTML(text.text)
    for i in html:
        # level2_href = i.xpath('//div[@class="co_content8"]//table//a/@href')#链接
        # level2_title = i.xpath('//div[@class="co_content8"]//table//a/@title')#片名
        level2_director = i.xpath('//div[@class="co_content8"]//table//p/text()')  # 导演
        # level2_type = i.xpath('//div[@class="co_content8"]//table//p[2]/text()')  # 类型
        # level2_actor = i.xpath('//div[@class="co_content8"]//table//p[3]/text()')  # 演员
        print(level2_director)
