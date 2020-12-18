from urllib.request import Request
from urllib.parse import urlencode
from urllib.request import urlopen


def headpara():#请求头函数
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}#请求头
    return header

def buildUrl(url,para,key):#拼接输入的关键字和链接函数
    wd = {para:key}#把关键字转成字典格式
    wd = urlencode(wd)#把关键字转码
    fullUrl = url + '?' + wd#合并链接和转码后的关键字
    return fullUrl

def dealData(fullUrl,header):#拼接请求链接和请求头
    request = Request(fullUrl, headers=header)#拼凑链接和头
    page=urlopen(request)#请求链接
    return page.read()#解析获得的请求链接
def dealUrl():
    num=int(input("输入要使用的搜索引擎，1搜狗，2百度，3bing："))
    if num==1:
        return "https://www.sogo.com/web","query"
    elif num==2:
        return "https://www.baidu.com/s","wd"
    elif num==3:
        return "https://www.bing.com/search","q"
    else:
        return "https://www.baidu.com/s","wd"


url,para=dealUrl()
# url='https://www.baidu.com/s'#要链接
keyword=input('请输入要搜索的关键字')#输入搜索的关键字
fullUrl=buildUrl(url,para,keyword)#拼接函数拼接后得到完整的链接
print("通过函数拼接后得到完整的链接",fullUrl )
head=headpara()
html=dealData(fullUrl,head)
print(html)

