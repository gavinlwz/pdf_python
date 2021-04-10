import requests
from lxml import etree

url = 'https://guba.eastmoney.com/'

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57",
}
text = requests.get(url, headers=header)  # 头
text.encoding = "utf-8"  # 转gbk
html = etree.HTML(text.text)  # 解析
result = html.xpath('//ul[@class="newlist"]/li')
for i in result:
    comp = i.xpath('./cite/text()')
    readinfo = comp[0].strip()  # 阅读
    commentinfo = comp[1].strip()  # 评论
    titleinfo = i.xpath('./span/a/@title')  # 标题
    Authorinfo = i.xpath('./cite[@class="aut"]/a/font/text()')  # 作者
    # Authorinfo=Authorinfo.xpath('./a/font/text()')
    Update = comp[5].strip()  # 时间

    print('阅读', readinfo, '评论', commentinfo, '标题', titleinfo, '作者', Authorinfo, '时间', Update)
# print(result)
