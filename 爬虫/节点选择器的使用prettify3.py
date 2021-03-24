from urllib.request import urlopen

from bs4 import BeautifulSoup
'''
---------------------------------------------------------------------------------
http://192.168.1.126/bsBrother.html

'''
html = urlopen('http://www.dy2018.com')
soup = BeautifulSoup(html, 'lxml')
print('Next Siling:')
print(type(soup.a.next_sibling))
print(soup.a.next_sibling)
print(soup.a.next_sibling.string)
print('Parent:')
print(type(soup.a.parents))
print(list(soup.a.parents)[0])
print(list(soup.a.parents)[0].attrs['class'])
'''
---------------------------------------------------------------------------------
3.兄弟节点

'''
# #获取节点的下一个元素
# print('Nexr Sibling',soup.a.next_sibling)
# #获取节点的上一个元素
# print('Prev Sibling',soup.a.paevious_sibling)
#获取节点后面的兄弟节点
# print('Prev Sibling',list(enumerate(soup.a.next_sibling)))
# #获取及地点前面的兄弟节点
# print('Prev Siblngs',list (enumerate( soup.a.previous_siblings)))