import requests
from bs4 import BeautifulSoup
import time
import pymysql
from urllib.request import urlopen


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


def dataUrl(url):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
    }
    html = requests.get(url, headers=header)
    bs = BeautifulSoup(html.text, 'html.parser')
    return bs


def dataHtml(bs, db):
    image = bs.find('div', {'class': 'pic-box clearfix'})
    plik = image.find_all('div', {'class': 'qtw-card'})
    for i in plik:
        pilk = i.find('a')['href']
        url1 = 'https:' + pilk
        header1 = {

            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",

        }
        html1 = requests.get(url1, headers=header1)
        context = html1.text
        bs1 = BeautifulSoup(context, 'html.parser')
        image1 = bs1.find('div', {'class': 'main-right fr'})
        time.sleep(3)
        Numbering = ''
        Resolution = ''
        Painter = ''
        nana = ''
        try:
            nana = i.find('a').find('div', class_='image-box').find('span', class_='lazy')['alt']
            Numbering = image1.find('div', class_='material-info clearfix').find('p').string  # 编号
            Numbering1 = image1.find('div', class_='material-info clearfix')
            Resolution = Numbering1.contents[1].string  # 分辨率
            Painter = image1.find('div', class_='user-box fl').find('div').find('a').string  # 作者
        except TypeError:
            print('wufa')

        para = [Numbering, Resolution, Painter, pilk, nana]
        print(para)
        db.execute(
            'insert into tb_qiantu (Numbering,Resolution,Painter,pilk,nana) values(%s,CAST(%s AS CHAR CHARACTER SET utf8),%s,%s,%s)',
            para)


def main(db):
    for i in range(5, 278):
        url = "https://www.58pic.com/piccate/2-0-0-p{}.html".format(i)
        bs = dataUrl(url)
        dataHtml(bs, db)

        time.sleep(1)
        print('抓取的地址', url)


if __name__ == '__main__':
    with DB(host='localhost', user='root', password='root', db='baike')as db:
        main(db)
