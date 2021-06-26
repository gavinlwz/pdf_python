import requests
from bs4 import BeautifulSoup
import pandas as pd
from lxml import etree

from Common import RequestsCommon

url = 'https://comment.bilibili.com/160407915.xml'
html = requests.get(url).content
html_data = str(html, 'utf-8')
bs4 = BeautifulSoup(html_data, 'lxml')
results = bs4.find_all('d')
comments = [comment.text for comment in results]
comments_dict = {'comments': comments}
br = pd.DataFrame(comments_dict)
br.to_csv('文件名.csv', encoding='utf-8')
print(comments_dict)
# url = 'https://qinggongju.com/zlcx/hero.php?name='+input('请输入查询的英雄名')
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57",
# }
# text = requests.get(url, headers=header)  # 头
# text.encoding = "utf-8"  # 转gbk
# text = etree.HTML(text.text)  # 解析
# hero_info = text.xpath('//div[@class="layui-row layui-col-space15"]//div[@class="layui-card-body"]//a//cite/text()')#英雄明
# qqPower = text.xpath('//div[@class="layui-tab-content"]//tr/td/text()')#qqzhanl战力
# # wxPower = text.xpath('//div[@class="layui-tab-content"]')#微信战力
# print(hero_info,qqPower)
