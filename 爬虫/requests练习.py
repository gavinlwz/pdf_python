# -*- coding: utf-8 -*-
# @Time    : 2021/3/20 8:17
# @Author  : wamgmoufei
# @Email   : wangmoufei@live.com
# @File    : requests练习.py
import requests

#
#
# header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}
# url="http://www.baidu.com/"
# req=requests.get(url,headers=header)
# print(req.text)
'''
6.提交数据
'''
# data={
#     'name':'张三',
#     'age':16,
# }
# # r=requests.post('http://httpbin.org/post',data)
# # print(r.text)
# print(requests.post('http://httpbin.org/post',data).text)
'''
7.响应
'''
# r = requests.get('http://www.jd.com/')
# if r.status_code == requests.codes.ok:
#     print('请求正常')
#     print('抓取数据')
# else:
#     print('Q请求失败')
#     print('跳过抓取contiune')

'''
8.文件上传
'''
# filePng=open('html代码.txt','rb')#本目录下文件
# filePng={'file':filePng}
# r=requests.post('https://httpbin.org/post',files=filePng)
# print(r.text)

'''
9.读取cookies
'''
# r=requests.get('https://www.baidu.com')
# print(r.cookies)
# for key,value in r.cookies.items():
#     print(key+"="+value)


'''
10.cookies的会话维持
'''
# header={
#     "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57",
#     "Cookie":'oschina_new_user=false; remote_way=http; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%228340853%22%2C%22first_id%22%3A%2217810cbad744d3-0e99f7468d6289-1a1c434f-2073600-17810cbad7547f%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcn.bing.com%2F%22%7D%2C%22%24device_id%22%3A%2217810cbad744d3-0e99f7468d6289-1a1c434f-2073600-17810cbad7547f%22%7D; yp_riddler_id=b5df48c7-d47b-41c4-9056-d3330cbe81a5; user_locale=zh-CN; tz=Asia%2FShanghai; Hm_lvt_24f17767262929947cc3631f99bfd274=1615336277,1615336280,1616199243,1616199997; gitee_user=true; gitee-session-n=N2lPUXFMUGF1ZFoxQWI3Ni9uaGZEVTJLNFJpWkd1WWpqWWtuYm0xUks4VkMyQUlPbS96b1FSVW50cXhoZjRxeWRVeWlqRXliV2NSdko0R1RhekU4eHNnYnFQcFVNSm1RVTNZVm5ySjhacEFRdWRzNjhwMnlXRjFRdXh0YU9FN2lFMVpsQ0cyczlKaUhnVVE1RVFlZEx5QlROb1BkUGtwdlB6ZThZMlF1MnRmOVU0Uzg0QkFyNHFmWGk5dXc4elo1azRGdHZvL1ltSW1QT3JwL3J4QkR4ZnBZZU5ncGc1YzZoQmlvS01QMk1MamFNcTRGSW1tVGNRYTVIRkFjR3pzbW81czlRKzBhN2VMdFI4TFozaE9YMlhQb2V4NDBnZGU0Rk84YkdWNHNaZkJPYnFQazlnL2trWmZoSW9ac2JUaFdhWms0enlYVFNDdmpYUGF0OTBabUowSWllNjNRT2VRTEUvQSsyNXlMOWtFPS0tVTlldWpzQXdpam1lSWV2eHBOVm56UT09--dbba020843c83b47e7847dc3c1317397375615bf; Hm_lpvt_24f17767262929947cc3631f99bfd274=1616207100'
# }
# r=requests.get('https://gitee.com/',headers=header)
# # r.encoding='UTF-8'#转码
# print(r.text)
'''
11.ip代理
'''
# proxies={
#     "http":"112.245.17.202:8080"
# }
# header={
#     "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57",
# }
# r=requests.get('http://www.baidu.com',proxies=proxies,headers=header)
# print(r.text)

from bs4 import BeautifulSoup
proxies={
    "http":"8.129.180.208:80"
}
url='http://www.xiladaili.com/gaoni/'
header={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57",
}
r=requests.get(url,proxies=proxies,headers=header)
soup=BeautifulSoup(r.text,'lxml')
name=soup.find_all('table')
print(name)
# for i in name:
#     IP=i.find('tr').find_all('td')
#     print(IP)

