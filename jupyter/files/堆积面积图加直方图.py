import numpy as np
import matplotlib.pyplot as plt

# x = np.arange(12)
# y1 = np.array([198, 215, 245, 222, 200, 236, 201, 253, 236, 200, 266, 290])
# y2 = np.array([203, 236, 200, 236, 269, 216, 298, 333, 301, 349, 360, 358])
# y3 = np.array([185, 205, 226, 199, 238, 200, 250, 209, 246, 219, 253, 288])
# plt.stackplot(x, y1, y2, y3)
# plt.show()
# num = np.random.randint(0, 100, 50)
# num2 = np.random.randint(0, 100, 50)
# num3 = np.random.randint(0, 100, 50)
# # plt.hist(num, bins=8, histtype='stepfilled', rwidth=0.8)
# plt.hist(num2, bins=8, histtype='bar', rwidth=0.8)
# plt.hist(num3, bins=8, histtype='step')
# plt.show()
# random_state = np.random.RandomState(19680801)
# random_x = random_state.random(10000)
# plt.hist(random_x, bins=25)
# plt.show()
# data = np.array([20, 60, 50, 12, 30, 55])
# pie_labels = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
# plt.pie(data, radius=1.5, labels=pie_labels, autopct='%3.1f%%')
# plt.show()
# num = 0.5, 2.0, 4.4, 7.9, 12.3, 17.7, 24.1, 31.5, 39.9, 49.2, 59.5, 70.8, 83.1, 96.4, 110.7, 126.0, 142.2, 159.4, 177.6, 196.8

x = np.array(
    [0.5, 2.0, 4.4, 7.9, 12.3, 17.7, 24.1, 31.5, 39.9, 49.2, 59.5, 70.8, 83.1, 96.4, 110.7, 126.0, 142.2, 159.4,
     177.6, 196.8])
y = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200])
# area = (np.random.rand(num)
plt.scatter(y, x, s=30)
plt.show()
