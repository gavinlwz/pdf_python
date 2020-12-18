from urllib.request import Request
from urllib.parse import urlencode
from urllib.request import urlopen
# from bs4 import BeautifulSoup
url='https://www.baidu.com/s'#要搜索的链接
header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}#请求头
keyword=input('请输入要搜索的关键字')#要搜索的关键字
wd={"wd":keyword}#把关键字转成字典格式
print(wd)
wd=urlencode(wd)#把关键字转码
print(wd)
fullUrl=url+'?'+wd#合并链接和转码后的关键字
print(fullUrl)
page=Request(fullUrl,headers=header)#拼凑链接和头
html=urlopen(page)#请求链接
print(html)#输出请求
print(html.read())#输出解析后的请求
# soup=BeautifulSoup(html,'lxml')
# print(soup)

