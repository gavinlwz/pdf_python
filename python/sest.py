'''
Connection()对象 用来与连接数据库


'''

import pymysql
#打开数据库连接
conn = pymysql.connect(host='localhost',port=3306,database='wangmingfei',user = "root",passwd = "root",charset='utf8')
cur=conn.cursor()
count=cur.execute('select*from studentinfo')
data_all=cur.fetchall()
print(data_all)
cur.close()
conn.close()
'''
gitee：代码管理平台
pk:主键 primary key
NN：非空 not nill
UQ:唯一索引 unique
B:二进制 binary char varchar text binary
UN:unsinged 无符号 非负数
ZF:zero fill 用l零填充 int（10）
ID：int nn ai pk

'''
