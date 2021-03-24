from urllib.request import urlopen

from bs4 import BeautifulSoup

# html = urlopen('http://www.pythonscraping.com/pages/page1.html')
# soup = BeautifulSoup(html, 'lxml')
# nameList = soup.find_all('span',{'class':'green'})
# for name in nameList:
#     print(name.get_text())

'''
调用find——all方法，传入name参数，值为ul
意思是查询所有ul节点，返回的是列表类型
每个元素是bs4.element.Tag类型
'''
html = urlopen('http://comment.bilibili.com/245181867.xml')
soup = BeautifulSoup(html, 'lxml')
alink = soup.find_all("li", {"class":{'danmaku-info-row'}})
print(alink)

# print(soup.find_all(name='ul'))
# print(type(soup.find_all(name='ul')[0]))

'''
    bs4.element.Tag类型可以进行嵌套查询
    在查询ul内部的il节点
'''
# for ul in soup.find_all(name='ul'):
#     print(ul.find_all(name='li'))
'''
    遍历输出每个il(还是bs4.element.Tag)
    获取它的本内容.string
'''
# for ul in soup.find_all(name='ul'):
#     print(ul.find_all(name='li'))
#     for li in ul.find_all(name='li'):
#         print(li.string)

# alink = soup.find_all("div", {"class":{'co_content222'}})
# print(alink)