import requests
from bs4 import BeautifulSoup
import bs4
import csv


def parse_page_pre(goods_info, i):
    '''
    处理前30个商品的请求，并使用soup处理数据
    :param goods_info: 商品信息列表
    :param i: 京东商品搜索的第i页
    '''
    url_pre = 'https://search.jd.com/Search?keyword=%E4%B9%A6%E5%8C%85&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page=' + str(
        2 * i - 1)  # 前30个商品的url
    head = {
        'referer': 'https://search.jd.com/Search?keyword=%E4%B9%A6%E5%8C%85&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E4%B9%A6%E5%8C%85&page=1&s=26&click=0',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
    # head里面的referer很重要
    r = requests.get(url_pre, headers=head, timeout=30)
    r.encoding = 'utf-8'
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    try:
        titles_lt = soup.find_all('div', class_='p-name p-name-type-2')  # 所有标签为'div'，属性class为'p-name...'的标签集合列表
        prices_lt = soup.find_all('div', class_='p-price')

        for i in range(len(titles_lt)):
            title = titles_lt[i].a.em.text  # 从集合列表中找到title
            price = prices_lt[i].strong.i.text
            goods_info.append([title, price])
    except:
        print("商品信息获取产生异常")


def parse_page_last(goods_info, i):
    '''
    处理后30个商品的请求，并使用soup处理数据
    :param goods_info: 商品信息列表
    :param i: 京东商品搜索的第i页
    '''
    url_last = 'https://search.jd.com/s_new.php?keyword=%E4%B9%A6%E5%8C%85&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E4%B9%A6%E5%8C%85&page=' + str(
        2 * i) + '&s=' + str(48 * i - 20)
    head = {
        'referer': 'https://search.jd.com/Search?keyword=%E4%B9%A6%E5%8C%85&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E4%B9%A6%E5%8C%85&page=1&s=26&click=0',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
    r = requests.get(url_last, headers=head, timeout=30)
    r.encoding = 'utf-8'
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    try:
        titles_lt = soup.find_all('div', class_='p-name p-name-type-2')
        prices_lt = soup.find_all('div', class_='p-price')

        for i in range(len(titles_lt)):
            title = titles_lt[i].a.em.text
            price = prices_lt[i].strong.i.text
            goods_info.append([title, price])
    except:
        print("商品信息获取产生异常")


def write_in_csv(goods_info):
    '''
    写入csv文件中
    :param goods_info: 商品信息列表
    '''
    with open('./goods.csv', 'w', encoding='gb18030', newline='') as f:
        writer = csv.writer(f)
        for line in goods_info:
            writer.writerow(line)


if __name__ == '__main__':
    depth = 3
    goods_info = []

    for i in range(1, depth + 1):  # 爬取到第depth页
        parse_page_pre(goods_info, i)
        parse_page_last(goods_info, i)

    write_in_csv(goods_info)
