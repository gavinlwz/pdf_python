from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup

url= 'https://www.dytt8.net/index.htm'
# bs=html
# bs.raise_for_status()  # 判断网站编码，如果没有设置则默认返回 iso-8859-1 编码
# bs.encoding = bs.apparent_encoding
# 哈哈 = BeautifulSoup(bs.read(), 'html.parser')
# print(哈哈.title)

headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
}

html = requests.get(url, headers=headers)

html.raise_for_status()  # 判断网站编码，如果没有设置则默认返回 iso-8859-1 编码
html.encoding = html.apparent_encoding  # 而r.apparent_encoding则通过网页内容来判断其编码。令r.encoding=r.apparent_encoding就不会出现乱码问题。
bs = BeautifulSoup(html.text, 'lxml')
print(bs.title)