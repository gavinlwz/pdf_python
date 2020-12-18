'''
MySQL +python
mysql数据库,pymysql
sqlserver数据库:massql
'''
import pymysql  #mysql
import time


def main():
    name = input('输入先查询的手机名：')
    conn = pymysql.connect(host='localhost', port=3306, database='baike', user='root', password='root', charset='utf8')
    cur =conn.cursor()
    paras=['%'+name+'%']
    cur.execute("select * from tb_jingdong where Tradename like %s ",paras)






    print(cur.fetchall())
    cur.close()
    conn.close()
if __name__ == '__main__':
    main()



