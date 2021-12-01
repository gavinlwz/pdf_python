'''
MySQL +python
mysql数据库,pymysql
sqlserver数据库:massql
'''
import pymysql  # mysql
import time


def main():
    conn = pymysql.connect(host='localhost', port=3306, database='wangfei', user='root', password='root',
                           charset='utf8')
    cur = conn.cursor()

    cur.execute("select 用户id from wyyurl")

    print(cur.fetchall())
    cur.close()
    conn.close()


if __name__ == '__main__':
    main()
