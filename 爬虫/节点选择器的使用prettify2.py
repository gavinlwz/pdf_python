from urllib.request import urlopen

from bs4 import BeautifulSoup

'''
---------------------------------------------------------------------------------
http://192.168.1.126/bsChildren.html
关联选择
1.子节点和子孙节点
'''
html = urlopen('http://192.168.1.126/bsChildren.html')
soup = BeautifulSoup(html, 'lxml')
# 获取子孙节点content：p下一级标签不含《span》
print(soup.p.contents)
#获取子孙接节点children 子孙节点

print(soup.p.children)
for i, child in enumerate(soup.p.children):
    print(i, child)
#获取所有子和子孙节点，子子孙孙节点，单独输出。descendants
print(soup.p.descendants)
for i, child in enumerate(soup.p.descendants):
    print(i,child)
'''
---------------------------------------------------------------------------------
2.父节点和祖父节点
'''
# # 第一个a标签的父节点，输出父节点的所有内容
# print(soup.a.parent)
# # 祖父节点 enumeratr[I'nu：mereit]枚举类型
# # enumerate将一个可循环的对象宠幸合成一个缩影并累出数据和下标
# print(type(soup.a.parents))
# print('-------------------------------------------------------------------------------')
# print(list(enumerate(soup.a.parents)))

print('Next Siling:')
print(type(soup.a.next_sibling))
print(soup.a.next_sibling.string)
print('Parent:')
print(type(soup.a.parents))
print(list(soup.a.parenst)[0])
print(list(soup.a.parenst)[0].attrs['class'])