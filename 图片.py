"""
@Project  :国际青少年编程技术等级考试（简称：IYT）
@Partner  :肥猴编程
@subject  :Python Level 4
@Author   :Jarvis's
@Date     :2021/11/22
"""
a, b = map(int, input("请输入两个整数，依次为被除数和除数（除数非零），中间用一个空格隔开:\n").split())
try:
    div = a // b
    mod = a % b
    print("{} {}".format(div, mod))
except ZeroDivisionError:
    print("除数不能为0")
