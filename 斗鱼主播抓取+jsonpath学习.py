# -*- coding: utf-8 -*-
# 版权所有 (C) 王菲
# @ 时间: 2021/12/1 11:02
#
# @ 作者     : 王菲
# @ 电子邮件  : 123@qq.com
# @ 文件     : 斗鱼主播抓取+jsonpath学习.py
# @ 软件     : PyCharm
import jsonpath
import requests

url = 'https://www.douyu.com/gapi/rknc/directory/yzRec/1'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
json_data = requests.get(url, headers=headers)  # 安装请求头
json_data = json_data.json()  # 解析获取的的数数据
# 1.格式化输出json包
# import pprint  # 格式化输出包
# pprint.pprint(json_data)  # 格式化输出方法

# 2.进行json数据
# names = jsonpath.jsonpath(json_data, '$..nn')  # ..全网页搜索字段输出全部nn对应的直
# hots = jsonpath.jsonpath(json_data, '$..ol')  # ..全网页搜索字段输出全部nn对应的直
# # print(names, hots)#输出全局获取到的数据
# itme = {}
# for name, hot, in zip(names, hots):  # zip把全局获取到的数据一一对应起来使用for循环输出成
#     # print(name, hot)
#     itme['主播名'] = name
#     itme['主播人气'] = hot
#     # print(itme)  # 字典格式化输出
#     print(itme.items())  # 取出字典输出
# print(json_data)
names = jsonpath.jsonpath(json_data, '$..nn')  # ..全网页搜索字段输出全部nn对应的直
hots = jsonpath.jsonpath(json_data, '$..ol')  # ..全网页搜索字段输出全部ol对应的直
roomIds = jsonpath.jsonpath(json_data, '$..rid')  # ..全网页搜索字段输出全部nn对应的直
roomNames = jsonpath.jsonpath(json_data, '$..rn')  # ..全网页搜索字段输出全部nn对应的直
itme = {}
for name, hot, roomName, roomId in zip(names, hots, roomIds, roomNames):  # zip把全局获取到的数据一一对应起来使用for循环输出成
    # print(name, hot)
    itme['主播名'] = name
    itme['主播人气'] = hot
    itme['房间ID'] = roomId
    itme['房间名字'] = roomName
    # print(itme)  # 字典格式化输出\
    print(itme.items())  # 取出字典输出
