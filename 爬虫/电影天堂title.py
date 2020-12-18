from urllib.request import urlopen

from bs4 import BeautifulSoup

html = urlopen('http://www.dy2018.com')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.title)
