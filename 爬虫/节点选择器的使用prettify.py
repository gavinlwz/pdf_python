from urllib.request import urlopen

from bs4 import BeautifulSoup

html = urlopen('https://www.dy2018.com/')
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())#解释字符串以标准格式输出
print(soup.title.string)#去除标签输出
'''
---------------------------------------------------------------------------------
'''
# soup = BeautifulSoup(html, 'lxml')
# print(soup.title)#输出title的内容
# print(type(soup.title))#输出
# print(soup.title.string)#输出文本内容
# print(soup.head)
# print(soup.p)
'''
----------------------------------------------------------------------------------------
嵌套选择，调节节点元素
'''
# soup=BeautifulSoup(html,'lxml')
# print(soup.head.title)
# print(type(soup.head.title))
# print(soup.head.title.string)
'''
----------------------------------------------------------------------------------------------
提取信息
1.获取名称
2.获取属性
3.获取内荣
'''
# soup=BeautifulSoup(html,'lxml')
# print(soup.title.name)#获取节点名称
# #获取节点属性和属性值
# print(soup.p.attrs)
# print(soup.p.attrs['name'])
# #获取属性值，对于非唯一属性返回列表
# print(soup.p['name'])
# print(soup.p['class'])
# #获取内容string属性获取文本内容
# print(soup.p.string)
'''
--------------------------------------------------------------------------------------------------------------

'''


