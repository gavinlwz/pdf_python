import pymysql
import requests
from lxml import etree

db = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='weiyituku', charset='utf8')
print('成功！')
conn = db.cursor()

url = "https://www.mmonly.cc/tag/xy/"
head = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) MZzAppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}
response = requests.get(url, headers=head)
response.encoding = "gb2312"
html = etree.HTML(response.text)
trs = html.xpath('//div[@class="ABox"]')
for i in trs:
    linkinfo = i.xpath('./a[@target="_blank"]/@href')
    pictureinfo = i.xpath('./a/img/@src')
    titleinfo = i.xpath('./a/img/@alt')
    print(linkinfo, pictureinfo, titleinfo)
    q = [linkinfo, pictureinfo, titleinfo]
    sql = u"insert into xiaoyuan(linkinfo,pictureinfo,titleinfo)values(%s,%s,%s)"
    conn.execute(sql, q)
    db.commit()
    print('成功')
