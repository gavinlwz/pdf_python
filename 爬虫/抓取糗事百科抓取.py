import requests
from bs4 import BeautifulSoup
import time
import pymysql


# url=('https://www.qiushibaike.com/text/')#目标网址
class DB:
    def __init__(self, host='', port=3306, user='', password='', db='', charset='utf8'):
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, database=db, charset=charset)
        self.cur = self.conn.cursor()

    def __enter__(self):
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cur.close()
        self.conn.close()


def dealUrl(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    html = requests.get(url, headers=header)
    bs = BeautifulSoup(html.text, 'html.parser')
    return bs


def dealData(bs, db):
    divcount = bs.find('div', {'class': 'col1 old-style-col1'})
    # print(divcount)
    divlist = bs.find_all('div', {'class': "article block untagged mb15 typs_hot"})
    for i in divlist:
        author = i.find('h2').string
        content = i.find('div', class_='content').find('span').get_text().strip()
        stats = i.find('div', class_='stats')
        vote = stats.find('span', class_='stats-vote').find('i', class_='number').string
        comment = stats.find('span', class_='stats-comments').find('i', class_='number').string
        author_info = i.find('div', class_='articleGender')

        if author_info is not None:
            class_list = author_info['class']
            if 'womenIcon' in class_list:
                gender = '女'
            elif 'manIcon' in class_list:
                gender = '男'
            else:
                gender = ''
            age = author_info.string
        else:
            gender = ''
            age = '0'

        para = [author, content, vote, comment, gender, age]
        print(para)
        db.execute(
            'insert into tb_qiubai(author,content,vote,comment,gender,age) values(%s,CAST(%s AS CHAR CHARACTER SET utf8),%s,%s,%s,%s)',
            para)


def main(db):
    for i in range(1, 14):
        url = 'https://www.qiushibaike.com/text/page/{}/'.format(i)
        bs = dealUrl(url)
        dealData(bs, db)
        time.sleep(1)

    # print(content)


if __name__ == '__main__':
    with DB(host='localhost', user='root', password='root', db='baike')as db:
        main(db)
