# -*- coding: utf-8 -*-
# @Time    : 2021/3/24 11:12
# @Author  : wamgmoufei
# @Email   : wangmoufei@live.com
# @File    : 98代理.py
import requests
from lxml import etree
url = 'https://www.89ip.cn/index_1.html'
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57",
}
text = requests.get(url, headers=header)  # 头
html = etree.HTML(text.text)  # 解析
result = etree.tostring(html)  # 转成html文件
result.decode("utf-8")  # 转码
result = html.xpath('//*[@class="layui-table"]/tbody/tr/td/text()').strip()
print(result)

# item.xpath('normalize-space(./div[@class="tags"])')
# item.xpath('./div[@class="tags"]').strip()
