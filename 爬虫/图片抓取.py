# -*- coding: utf-8 -*-
# @Time    : 2021/3/24 11:27
# @Author  : wamgmoufei
# @Email   : wangmoufei@live.com
# @File    : 图片抓取.py
import requests
from lxml import etree
url='https://pic.netbian.com/4kmeishi/index_2.html'
header={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57",
}
text=requests.get(url,headers=header)#头
text.encoding="gbk"#转gbk
html=etree.HTML(text.text)#解析
result=html.xpath('//*[@class="clearfix"]/li')
for i in result:
    tp=i.xpath('./a/@href')
    mz=i.xpath('./a/img/@alt')

    print(tp,mz)