import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
lines = y1, y2 = np.sin(x), np.cos(x)
plt.plot(x, y1, x, y2)
fontdicts = {
    "family": "SimHei",
    "color": "red",
    "weight": "bold",
    "size": 16}

plt.xlabel('x轴', fontdict=fontdicts)
plt.ylabel('y轴', fontdict=fontdicts)
plt.xlim(x.min() * 1.5, x.max() * 1.5)
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$-\pi/2$', r'$-\pi$'])
plt.title("正弦曲线和余璇曲线", fontdict=fontdicts, loc="left", pad=10)
plt.grid(b=True, axis="both", linewidth=0.5)
plt.show()

# tick_label = ['哪吒魔童降世', '流浪地球', '复仇者联盟4：终局之战', '疯狂的外星人', '飞驰人生', '烈火英雄', '蜘蛛侠：英雄远征', '速度与激情：特别行动', '扫毒2：天地对决',
#               '大黄蜂', '惊奇队长', '比悲伤更悲伤的故事', '哥斯拉2怪兽之王', '阿丽塔：战斗天使', '银河补习班']
# x1 = np.array([48.57, 46.18, 42.05, 21.83, 17.03, 16.70, 14.01, 13.84, 12.85, 11.83, 10.25, 9.46, 9.27, 8.88, 8.64])
# y = range(len(tick_label))
# plt.barh(y, x1, height=0.5, color="orange")
# plt.xlabel("总票房（亿元）")
# plt.ylabel("电影名称")
# plt.yticks(y, tick_label)
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
#
# plt.rcParams['font.sans-serif'] = ['simHei']
# plt.rcParams['axes.unicode_minus'] = False
#
# data = np.array([800, 100, 1000, 200, 300, 200, 200, 200, ])
# pie_labels = np.array(['购物', '人情往来', '餐饮', '通讯', '生活日用', '交通', '休闲', '其他'])
# position = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
# plt.pie(data, radius=1.2, explode=position, labels=pie_labels, autopct='%3.1f%%', startangle=90)
# plt.title("支付宝月账单")
# plt.legend(pie_labels, loc="upper right", bbox_to_anchor=(1.5, 1.3))
# plt.show()
