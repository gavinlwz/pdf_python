import requests
from bs4 import BeautifulSoup
import time
import pymysql

class DB:
    def __init__(self,host='',port=3306,user='',password='',db='',charset='utf8'):#初始化
        self.conn = pymysql.connect(host=host,port=port,user=user,password=password,database=db,charset=charset)
        self.cur = self.conn.cursor()#创建游标

    def __enter__(self):    #初始化类之后执行的 进入的时候
        return self.cur#返回游标

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cur.close()#关闭游标
        self.conn.close()#关闭数据库





def dataUrl(url):
    # url = "https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&stop=1&qrst=1&vt=2&cid3=655&cid2=653&page=17&s=56&click=0"

    header = {
         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
                }
    html = requests.get(url, headers=header)
    bs = BeautifulSoup(html.text, 'html.parser')
    return bs
def dataHtml(bs,db):

    手机 = bs.find_all('div', {'class': 'gl-i-wrap'})
    for i in 手机:
        Tradename=i.find('div',class_='p-name p-name-type-2').find('a',target='_blank').find('em').get_text().strip()
        price=i.find('strong').find('i').string
        link = i.find(class_='p-img').find('a')['href']
        # 店铺=i.find(class_='J_im_icon').find('a')['title']
        try:
            shop=i.find(class_='J_im_icon').find('a')['title']
        except AttributeError:#exception
            print('无法获取数据')
        print('商品名', Tradename, '价格', price, '店铺', shop,'链接',link)
        para = [Tradename,price,shop,link ]
        print(para)
        db.execute(
            'insert into phone (Commodity,price,shop,link) values (%s,CAST(%s AS CHAR CHARACTER SET utf8),%s,%s)',
            para)


def main(db):
    for i in range(1,200,2):

        url = "https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&wq=%E6%89%8B%E6%9C%BA&page={}&s=57&click=0".format(i)
        bs = dataUrl(url)
        dataHtml(bs, db)
        time.sleep(1)
        print(url)



if __name__ == '__main__':
    with DB(host='localhost',port=3306,user='root',password='root',db='jd') as db:#12行返回游标db
        db.execute('SET NAMES utf8mb4')
        main(db)


