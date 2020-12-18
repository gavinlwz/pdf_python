import requests
from bs4 import BeautifulSoup
import time



import pymysql


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
    return  bs

def dataHtml(bs,db):

    image=bs.find('div',{'class':'pic-box clearfix'})
    plik=image.find_all('div',{'class':'qtw-card'})
    for i in plik:
        pilk=i.find('a')['href']

        try:
            nana=i.find('a').find('div',class_='image-box').find('img',class_='lazy')['alt']
        except TypeError:
            pass
        print(pilk,nana)

        para = [pilk,nana]
        print(para)
        db.execute(
            'insert into tb_qiantuwang_haibao (pilk,nana) values(%s,CAST(%s AS CHAR CHARACTER SET utf8))',
            para)
def main(db):
    for i in range(1,278):

        url = "https://www.58pic.com/piccate/10-0-0-p{}.html".format(i)
        bs = dataUrl(url)

        dataHtml(bs,db)
        # time.sleep(1)
        print('抓取的地址',url)


if __name__ == '__main__':
    with DB(host='localhost', user='root', password='root', db='baike')as db:
        main(db)