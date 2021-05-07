# -*- coding: utf-8 -*-
# @Time    : 2021/3/24 8:13
# @Author  : wamgmoufei
# @Email   : wangmoufei@live.com
# @File    : xpath练习.py

import requests
from lxml import etree
# text="""
# <div>
#  <ul>
#   <li class="item-0"><a href="link1.html">first item</a></li>
#   <li class="item-1"><a href="link2.html">second item</a></li>
#   <li class="item-inactive"><a href="link3.html">third item</a></li>
#   <li class="item-1"><a href="link4.html">fourth item</a></li>
#   <li class="item-0"><a href="link5.html">fifth item</a>
#   </ul>
#   </div>
#   """
# req=requests.get('http://www.baidu.com')
# html=etree.HTML(req.text)
# result=etree.tostring(html)
# print(result.decode("utf-8"))

# req=requests.get('http://www.baidu.com')
# html=etree.parse('C:/Users/Administrator/新建文件夹/html1.txt',etree.HTMLParser())
# result=etree.tostring(html)
# print(result.decode("utf-8"))





'''
nodename:获取此节点下的所有自节点
/：从当前节点选取直接子节点
//：从当前节点选取子孙节点
.：选取当前节点
..：选取当前节点的父节点
@选取属性
@在中括号中是检索条件 在/后面是获取属性
'''

# html=etree.HTML(text)#自动补全 解析
# result=html.xpath('//*')#获取所有节点
# print(result)


# html=etree.HTML(text)#自动补全 解析
# result=html.xpath('//li')#获取当前节点的子孙节点 查新所有li
# print(result)

# html=etree.HTML(text)#自动补全 解析
# result=html.xpath('//li/a')#获取所有 子节点
# print(result)


# html=etree.HTML(text)#自动补全 解析
# result=html.xpath('//ul//a')#获取 ul的子孙节点a标签
# print(result)
''''
父节点
'''

# html=etree.HTML(text)#自动补全 解析
# result=html.xpath('//a[@href="link1.html"]/../@class')#寻找a标签link3的条件a[@href="link1.html"]  /../@class输出其class属性
# print(result)

'''
属性匹配
'''
# html=etree.HTML(text)#自动补全 解析
# result=html.xpath('//li[@class="item-inactive"]/@class')#寻找a标签link3的条件a[@href="link1.html"]  /../@class输出其class属性
# print(result)


# html=etree.HTML(text)#自动补全 解析
# result=html.xpath('//a[@href="link5.html"]/@href')#
# print(result)


# html=etree.HTML(text)#自动补全 解析
# result=html.xpath('//li[@class="item-1"]/@class')[1]#寻找a标签link3的条件a[@href="link1.html"]  /../@class输出其class属性
# print(result)




'''
文字获取
'''

# html=etree.HTML(text)#自动补全 解析
# result=html.xpath('//a[@href="link5.html"]/text()')#
# print(result)


# html=etree.HTML(text)#自动补全 解析
# result=html.xpath('//li[@class="item-0"]/a/text()')#会出现/n的原因是xpath解析是自动补全了一个代码/n是换行符的意思
# print(result)


#
#
from bs4 import BeautifulSoup

url = 'https://ip.jiangxianli.com/'
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57",
}
text = requests.get(url, headers=header)  # 头
html = etree.HTML(text.text)  # 解析
result = etree.tostring(html)  # 转成html文件
result = result.decode("utf-8")  # 转码
result = html.xpath('//*[@class="layui-table"]/tbody/tr')
for tr in result:
    tds = tr.xpath('./td/text()')
    ipinfo = tds[0].strip()
    portinfo = tds[1].strip()

    print(ipinfo, portinfo, tds)

'''
多属性匹配
contains()
'''
# text="""
# <div>
#  <ul>
#   <li class="li" name="sp"><a href="link1.html">first item</a></li>
#   <li class="item-1"><a href="link2.html">second item</a></li>
#   <li class="item-inactive"><a href="link3.html">third item</a></li>
#   <li class="item-1 aaa"><a href="link5.html">fourth item</a></li>
#   <li class="item-0" name="sp"><a href="link5.html">fifth item</a>
#   <li class="li" name="sp"><a href="link5.html">sp内容</a></li>
#
#   </ul>
#   </div>
#   """
#
# # html=etree.HTML(text)#自动补全 解析
# # result=html.xpath('//li[contains(@class,"item-0")]/@class')#contains() 多属性匹配
# # print(result)
#
#
# html=etree.HTML(text)#自动补全 解析
# result=html.xpath('//li[contains(@class,"li")and @name="sp"]/a/text()')#同时满足才会输出
# print(result)

'''
按序选择
'''
text = """
<div>
 <ul>
  <li class="li" name="sp"><a href="link1.html">first item</a></li>
  <li class="item-1"><a href="link2.html">second item</a></li>
  <li class="item-inactive"><a href="link3.html">third item</a></li>
  <li class="item-1 aaa"><a href="link5.html">fourth item</a></li>
  <li class="item-0" name="sp"><a href="link5.html">fifth item</a>
  <li class="li" name="sp"><a href="link5.html">sp内容</a></li>

  </ul>
  </div>
  """
# html=etree.HTML(text)#自动补全 解析
# # result=html.xpath('//li/a/text()')[1]#按序选着引号内是按序号选着引号外是按下标选择
# result=html.xpath('//li[last]/a/text()')#[last]选择最后一个元素
# result=html.xpath('//li[last()-1]/a/text()')#[last()-1]选择倒数第1个元素
# # result=html.xpath('//li[position()<=3]/a/text()')#[position()<=3]选择前三个元素
# result=html.xpath('//li[position()>=3]/a/text()')#[position()>=3]选择后三个元素
# print(result)


'''
节点树
子节点
子孙节点
父节点
兄弟节点
祖父节点
'''
text = """
<div>
 <ul>
  <li class="li" name="sp"><a href="link1.html">first item</a><span>sp<span></li>
  <li class="item-1"><a href="link2.html">second item</a></li>
  <li class="item-inactive"><a href="link3.html">third item</a></li>
  <li class="item-1 aaa"><a href="link5.html">fourth item</a></li>
  <li class="item-0" name="sp"><a href="link5.html">fifth item</a>
  <li class="li" name="sp"><a href="link5.html">sp内容</a></li>

  </ul>
  </div>
  """
# html=etree.HTML(text)#自动补全 解析
# # result=html.xpath('//li[1]/child::*')#获取第一个li的所有子标签
# # result=html.xpath('//li[1]/child::a')#只输出第一个li标签的所有子节点a标签的
# # result=html.xpath('//li[1]/child::a[@href="link1.html"]/text()')#指定输出第一个li下子节点a标签href="link1.html"的内容
# result=html.xpath('//li[1]/following::*')#获取第一个li之后所有的标签
# result=html.xpath('//li[1]/following::*[3]')#获取第一个li之后的第三个标签
# result=html.xpath('//li[1]/following-sibling::*')#获取li的同级标签
# print(result)