import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://comment.bilibili.com/245181867.xml'
html = requests.get(url).content
html_data = str(html, 'utf-8')
bs4 = BeautifulSoup(html_data, 'lxml')
results = bs4.find_all('d')
comments = [comment.text for comment in results]
comments_dict = {'comments': comments}
br = pd.DataFrame(comments_dict)
br.to_csv('文件名.csv', encoding='utf-8')
print(comments_dict)
