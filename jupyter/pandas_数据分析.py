import pandas as pd
# import pandas as index

# s = pd.Series([29, 30, 1, -29], index=["a", "b", "c", "d"])
# print(s.values)  # 查看元素
# print(s.index)  # 查看标签
# # 索引
# print(s[3])
# print(s["c"])
# # 标签获取数据
# print(s[0:2])
# print(s[["b", "c"]])
# print(s["b":"c"])
#
# # 修改元素
# s[1] = -30
# s["a"] = 50
# print(s)
#
# # 追加
# s = pd.Series([29, 30, 1, -29], index=["a", "b", "c", "d", ])
# n = pd.Series([5], index=["e"])
# s.append(n)
# print(s)
# # 删除drop（）
# print(s.drop("a"))
# print(s.drop(s.index[2]))#索引删除
# print(s["c"!=s.index])
# print(s[-29!=s.values])

# 排序sort_index()
# s = pd.Series([29, 30, 1, -29], index=["b", "c", "d", "a"])
# print("创的数组是",s)
# print("-----------")
# print(s.sort_index(ascending=False))#阿斯克码排序

# reindex()
# fill_value=填充值 或空值
# s = pd.Series([29, 30, 1, -29], index=["b", "c", "d", "a"])
# snew=s.reindex(["a","b","c","d","e"],fill_value=100)
# print(snew)

# import pandas as pd
#
# data = {
#     'color': ['pink', 'black', 'white', 'green', 'yellow'],
#     'object': ['bus', 'boat', 'ship', 'subway', 'paper'],
#     'price': [10000, 666, 999, 9999, 1],
#     'datas': [1,2,3,4,5],
# }
# # df=pd.DataFrame(data)
# # print(df)
# df=pd.DataFrame(data,columns=['object','price'])
# print(df)
import pandas as pd
import numpy as np

# df = pd.DataFrame(np.arange(25).reshape(5, 5),
#                   index=['one', 'two', 'three', 'four', 'five'],
#                   columns=['bus', 'boat', 'ship', 'subway', 'paper'])
# print(df)
# data_nwe=pd.read_table(r'D:\jupyter file\files\books.txt',header='infer',sep='\t',encoding='utf-8')
# print(data_nwe)

# data_nwe = pd.read_csv(r'D:\jupyter file\files\books.csv', header='infer', sep=',')
# print(data_nwe)

# data_nwe = pd.read_excel(r'D:\jupyter file\files\books.xlsx', sheet_name=0,header='infer')
# print(data_nwe)

import pandas as pd
import pymysql
# conn=pymysql.connect(host='localhost',database='d1tk',user='root',password='root')
# data=pd.read_sql("select * from d1tk",con=conn)
# conn.close()
# print(data)
# to_csv(filepath,sep=',', na_rep='', columns=None, header=True, index=True,
#           index_label=None, mode='w', encoding=None)
# 1.filepath 文件路径
# 2.sep=''分隔符 string 默认
# 3.na_rep=''缺失值 默认是‘’
# 4.columns=None 接收list，写入得列名，None
# 5.header boolean 表示是否将列名写出默认是 True
# 6.index boolean 表示是否写出行名 默认是 True
# 7.mode 接收string类型 表示数据写入模式w

import pandas as pd
import numpy as np
#
# data = {
#     'color': ['red', 'green', 'gray', 'blue', 'black'],
#     'object': ['mug', 'paper', 'desk', 'book', 'pen'],
#     'prince': [20, 1.5, 50, 32, 5]
# }
# df = pd.DataFrame(data)
# df.to_csv('files/pandas_csv.csv', sep=',', na_rep='', columns=None, header=True, index=True,
#           index_label=None, mode='w', encoding=None)
# print(df)

# to_sql(name,con,if_exists,'fail',index=True,index_label=None,dtype=None)
# 1. naem 接收string 类型 数据库表名
# 2. con 连接数据库
# 3. if_exists:接收fail‘，’‘replace’；fail表示如果存在 则不执行写入；replace表示如果存在，则将元数据库标删除，在创建，append表示在数据库基础上的再追加数据默认是fail
# 4. dtype写入数据

# import pandas as pd
# from sqlalchemy import create_engine
#
# engine = create_engine("mysql+pymysql://root:root@localhost:3306/d1tk?charset=utf8")
# data = {
#     'color': ['red', 'green', 'gray', 'blue', 'black'],
#     'object': ['mug', 'paper', 'desk', 'book', 'pen'],
#     'prince': [20, 1.5, 50, 32, 5]
# }
# df = pd.DataFrame(data)
# df.to_sql("data", con=engine, if_exists="fail", index=False, index_label="id")
# import httpx
# clie=httpx.Client(http2=True)
# req=clie.get('www.baidu.com')
# print(req.text)

import pandas as pd
import numpy as np

# data_nwe = pd.read_excel(r'files\books2.xlsx', sheet_name=0,header='infer')
# print(data_nwe.drop_duplicates())


df = pd.read_csv(r'files\loan_data.csv', header='infer', sep=',', encoding='gbk')
df
