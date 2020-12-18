import re
import urllib
from urllib.request import urlopen

from bs4 import BeautifulSoup

url = 'https://baike.tw.lvfukeji.com/wiki/%E4%B8%89%E4%BD%93'  # 地址
# 创造头
headers = {
    'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/5'}

page = urllib.request.Request(url, headers=headers)

html = urlopen(page)
bs = BeautifulSoup(html, 'lxml')
# for a in bs.find_all('a'):
#
#     if'href' in a.attrs:
#         print(urllib.parse.unquote(a['href']))


aInfoIist = bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile(
    '^(https://baike.tw.lvfukeji.com/baike)([^:].)*$'))
for i in aInfoIist:
    if 'href' in i.attrs:
        print(urllib.parse.unquote(i['href']))

# 1.构造伪装头
# 2.Request安装伪装头
# 3.打开链接
# 4.bs解析内容
# 5.查找a标签
# 6.判断是否有href属性
# 7.输出
# time.sleep(2)
