from urllib.request import urlopen

from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'lxml')
# 输出div下p标签的内容
print(soup.div.p)
# 输出img标签中的src属性
print(soup.img['src'])
# 使用enumerate(soup输出tr的所有兄弟节点
print('Next Siblings', list(enumerate(soup.tr.next_siblings)))
