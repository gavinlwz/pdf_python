import requests
from lxml import etree
url = 'https://www.dy2018.com/index.html'

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57",
}
text = requests.get(url, headers=header)  # 头
text.encoding = "gb2312"  # 转gbk
html = etree.HTML(text.text)  # 解析
result = html.xpath('//div[@class="co_content222"]')[7]
# reques=html.xpath('//*[@href="/i/103358.html"]/following::*')#获取href="/i/103358.html"之后的所有标签
print(result)
for i in result:
    linkinfo = i.xpath('./li/a/@href')  # 链接
    titleinfo = i.xpath('./li/a/@title')  # 标题
    #
    print("链接", linkinfo, "标题", titleinfo)
