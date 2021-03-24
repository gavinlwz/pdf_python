import requests
from bs4 import BeautifulSoup
import time
import pymysql

class DB:
    def __init__(self,host='',port=3306,user='',password='',db='',charset='utf8'):
        self.conn = pymysql.connect(host=host,port=port,user=user,password=password,database=db,charset=charset)
        self.cur = self.conn.cursor()

    def __enter__(self):    #初始化类之后执行的 进入的时候
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cur.close()
        self.conn.close()





def dataUrl(url):
    '''

    :param url:
    :return: 获取到的网页源码
    '''
    # url = "https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&stop=1&qrst=1&vt=2&cid3=655&cid2=653&page=17&s=56&click=0"

    header = {
         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
                }
    html = requests.get(url, headers=header)#合成头和身体
    bs = BeautifulSoup(html.text, 'html.parser')#解析获取到的数据
    return bs#扔出输出结果
def dataHtml(bs,db):
    '''

    :param bs: 想要循环抓取的标签
    :param db: 把获取到的数据存入数据库
    :return:
    '''

    DaTa = bs.find_all('div', {'class': 'gl-i-wrap'})#想要循环抓取的标签
    for i in DaTa:
        Tradename=i.find('div',class_='p-name p-name-type-2').find('a',target='_blank').find('em').get_text().strip()#获取到的商品名
        price=i.find('strong').find('i').string#获取到的价格
        link = i.find(class_='p-img').find('a')['href']#获取到的店铺
        # 店铺=i.find(class_='J_im_icon').find('a')['title']
        shop=''
        try:
            shop=i.find(class_='J_im_icon').find('a')['title']#获取的商品链接
        except AttributeError:
           print('无法获取数据')
        print('商品名', Tradename, '价格', price, '店铺', shop,'链接',link)
        para = [Tradename,price,shop,link ]
        print(para)
        db.execute(
            'insert into phone (Commodity,price,shop,link) values (%s,%s,%s,%s)',
            para)#把获取到的数据到如到数据库


def main(db):

    for i in range(1,200,2):#循环1到200每一个数输出一下

        url = "https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&wq=%E6%89%8B%E6%9C%BA&page={}&s=57&click=0".format(i)#循环的书添加到链接形成要抓取的新链接
        bs = dataUrl(url)
        dataHtml(bs, db)
        time.sleep(3)
        print(url)



if __name__ == '__main__':
    with DB(host='localhost',port=3306,user='root',password='root',db='jd') as db:#数据库链接
        db.execute('SET NAMES utf8mb4')
        main(db)


