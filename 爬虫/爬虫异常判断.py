from urllib.error import HTTPError  # 导包
from urllib.request import urlopen  # 导包

from bs4 import BeautifulSoup  # 导包


def getTitle(url):
    try:
        html = urlopen(url)  # 检查网页是否正确
    except HTTPError as e:
        return None  # 错误则终止
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title= bs.title  # 要抓取的网页元素
    except BaseException as e:
        return None
    return title


title = getTitle('http://www.dy2018.com')  # 要抓取的网站
if title is None:
    print('Title could not be found')  # 抓取失败返回空值
else:  # 否则返回抓取结果
    print(title)  #
