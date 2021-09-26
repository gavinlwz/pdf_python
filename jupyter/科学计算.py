import numpy as np

# arr = np.arange(10 * 10, dtype=int).reshape(10, 10)
# newArr = arr[2:9:2, 5:].copy()
# print(newArr)
#
#
# np.random.seed(40)
# arr=np.random.randint(1,20,size=(5,5))
# print("创建的随机数组\n",arr)
# arr.sort(axis=0)
# print("--------------------")
# print(arr)
# arr.sort(axis=1)
# print("----------------------")
# print(arr)


# arr=np.array([0,6,3,9,1,7,0])
# arr.argsort()
# print("元数据\n",arr)
# print(arr.argsort())
# a_totle=np.array([1,5,1,4,3,4,4])
# ac =a_totle.copy()
# print("总成绩的排序",ac)
# print("总成绩排序索引",ac.argsort())
# b_math=np.array([9,4,0,4,0,2,1])
# bc=b_math.copy()
# print("排序结果是",np.lexsort((bc,ac)))
#
# a_totle=np.array([1,5,1,4,3,4,4])
# b_math=np.array([9,4,0,4,1,2,7])
# print("排序结果是",np.lexsort((b_math,a_totle)))

# arr= np.arange(5)
# print(arr)
# print(np.tile(arr,4))

# np.random.seed(50)
# arr = np.random.randint(1, 10, size=(3, 3))
# print(arr)
# print("----------")
# print(np.repeat(arr, 2, axis=1))
# print("----------")
# print(np.repeat(arr, 2, axis=0))
# arr =np.arange(20).reshape(4,5)

arr = np.arange(20).reshape(4, 5)
# print("创建的数组",arr)
# print("求和",np.sum(arr))
# print("纵轴求和",np.sum(arr,axis=0))
# print("横轴求和",np.sum(arr,axis=1))

# mean
# print("球均值", np.mean(arr))
# print("球纵轴均值", np.mean(arr, axis=0))
# print("球横轴均值", np.mean(arr, axis=1))
#
# #先输出所有元数据的价格
# #对数据进行直接排序并输出
# #去掉重复数据
# #计算所有价格的总和
# #获取最低价格
# #获取最高价格
#
# txta=np.array([1,2,3,4,5,6])
# # np.savetxt('路径',需要保存的内容,格式)
# np.savetxt('D:\Desktop\price.csv',txta,fmt="%d")#保存
# txtb=np.loadtxt('D:\Desktop\price.csv',delimiter=',',dtype=float)#读取
# print(txtb)


# txtb=np.loadtxt('D:\Desktop\price.csv',delimiter=',',dtype=float)#读取
# print(txtb)
# txtb=np.loadtxt('D:\Desktop\price.csv',delimiter=',',dtype=float)#读取
# txtb.sort()
# print(txtb)
# txtb=np.loadtxt('D:\Desktop\price.csv',delimiter=',',dtype=float)#读取
# print("去重取唯一",np.unique(txtb))

import numpy as np
import matplotlib.pyplot as plt

# data = np.array([1, 2, 3, 4, 5])
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.plot(data)
# plt.show()
# x = np.arange(4, 19)  # 生产日期
# y_max = ([32, 33, 34, 33, 31, 30, 29, 30, 29, 24, 25, 31, 23, 25, 25])
# y_min = ([12, 15, 16, 19, 14, 18, 17, 15, 12, 21, 24, 23, 24, 21, 21])
# plt.plot(x, y_max)  # 画最高温
# plt.plot(x, y_min)  # 画对低温
# plt.show()
# x = np.arange(5)
# y1 = np.array([10, 5, 8, 13, 11])
# y2 = np.array([10, 2, 15, 18, 19])
# # 宽度
# bar_width = 0.3
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体
# error = [2, 1, 5, 2, 1]
# plt.bar(x, y1, tick_label=['小张', '小王', '李雷', '张三', '李四'], width=bar_width)
# plt.bar(x, y2, bottom=y1, width=bar_width, yerr=error)
# plt.show()
# x = [10770, 16780, 24440, 30920, 37670, 48200, 47270]
# x = ['fy2013', 'fy2014', 'fy2015', 'fy2016', 'fy2017', 'fy2018', 'fy2019']
# plt.rcParams['font.sans-serif'] = ['simHei']
# plt.rcParams['axes.unicode_minus'] = False
# plt.title('各种商品的网购代替率 百分比(%)')
# y = np.arange(18)
# x1 = np.array(
#     [95.90, 95.10, 93.50, 92.40, 89.30, 89.20, 86.50, 86.30, 86.00, 85.60, 85.40, 83.50, 82.60, 81.60, 79.80, 76.50,
#      76.30, 67.00])
# plt.barh(y, x1, tick_label=['家政、家教、保姆等生活服务', '飞机票、火车票', '家具', '手机、手机配件', '计算机及其配套产品', '汽车用品', '通信充值、游戏充值',
#                             '个人护理用品', '书报杂志及音像制品', '餐饮、旅游、住宿', '家用电器', '食品、饮料、烟酒、保健品', '家庭日杂用品', '保险、演出票务',
#                             '服装、鞋帽、家用纺织品',
#                             '数码产品',
#                             '其他商品和服务', '工艺品，收藏品',
#                             ], height=0.5)
# plt.show()
