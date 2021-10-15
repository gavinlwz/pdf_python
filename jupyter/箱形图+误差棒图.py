# import numpy as np
# import matplotlib.pyplot as plt
#
# data = np.array([5200, 5254.2, 5283.4, 5107.8, 5443.3, 5550.6, 6400.2, 6404.9, 5483.1, 5330.2, 5543, 6199.9])
# data2 = np.array([4605.2, 4710.3, 5168.9, 4767.2, 4947, 5203, 6047.4, 5945.5, 5219.6, 5038.1, 5196.3, 5698.6])
# sj = ([2017, 2018])
# plt.boxplot([data, data2], meanline=True, widths=0.5, patch_artist=True, vert=False, labels=sj)
#
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

# z = np.arange(3)
# c1 = np.array([2.04, 1.57, 1.63])
# c2 = np.array([1.69, 1.61, 1.64])
# c3 = np.array([4.65, 4.99, 4.94])
# c4 = np.array([3.39, 2.33, 4.10])
# bar_width = 0.2
# plt.rcParams['font.sans-serif'] = ['Simhei']
# plt.bar(z, c1, tick_label=['春', '夏', '秋'], width=bar_width)
# plt.bar(z + bar_width, c2, width=bar_width)
# # plt.bar(z + bar_width, c3, width=bar_width)
#
# plt.show()
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(3)
y1 = np.array([2.04, 1.57, 1.63])
y2 = np.array([1.69, 1.61, 1.64])
y3 = np.array([4.65, 4.99, 4.94])
y4 = np.array([3.93, 2.33, 4.10])
y1s = (0.16, 0.08, 0.10)
y2s = (0.27, 0.14, 0.14)
y3s = (0.34, 0.32, 0.29)
y4s = (0.23, 0.23, 0.39)
bar_width = 0.2
wu = dict(capsize=3, capthick=3)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.bar(x, y1, tick_label=['春季', '夏季', '秋季'], width=bar_width, yerr=y1s, error_kw=wu)
plt.bar(x + bar_width, y2, width=bar_width, yerr=y2s, error_kw=wu)
plt.bar(x + bar_width + bar_width, y3, width=bar_width, yerr=y3s, error_kw=wu)
plt.bar(x + bar_width + bar_width + bar_width, y4, width=bar_width, yerr=y4s, error_kw=wu)
plt.show()
