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
filePng=open('html代码.txt','rb')#本目录下文件
filePng={'file':filePng}
r=requests.post('https://httpbin.org/post',files=filePng)
print(r.text)

