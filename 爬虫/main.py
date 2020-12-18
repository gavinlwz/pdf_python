from urllib .request import urlopen#导入urllib .request中的urlopen包
html=urlopen('https://www.mi.com/')#读取网站的url
print(html.read())#输出读取的结果结果