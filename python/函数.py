# def Goodstr():
#     print('很哈加油')
#     print('很棒加油')
#     print('~~~~~~')
#
#
# Goodstr()
# Goodstr()
# Goodstr()
#
#
# # 加法计算
# def plusNum(x):
#     sum = x + 2
#     sum = sum * 2
#     sum = sum + 5 * 2
#     return sum
#
#
# num = eval(input('输如一个数'))
# resDef = plusNum(num)
# print(resDef)


# def f33(x, y, z):
#     return x * x * x * +y * y * y * +z * z * z
#
#
# u, v, w = eval(input('输入三个数u，v,w'))
# t = f33(u, v, w)
# print('运算结果是: %16.6f'%t)


# def face():
#     return '(o◆^∨^◆o)'
# def wel():
#     print('Welcome!')
# s=input('输入姓名')
# wel()
# t=face()
# print('%s\n%s'%(s,t))
#
# g = lambda x: x + 1
# print(g(1))
# print(g(2))
#
#
# def g(x):
#     return x + 1
#
#
# print(g(1))
#
#
# def jisuan(x):
#     if x % 3 == 0:
#         return x
#
#
# lis = [2, 18, 9, 22, 17, 24, 8, 12, 27]
# filter_res = filter(lambda x: x % 3 == 0, lis)
# list_res = list(filter_res)
# print(list_res)
#
# map_res = map(lambda x: x * 3 + 5, lis)
# map_lis = list(map_res)
# print(map_lis)


def df(n, x, y, s):
    a = 1
    if n == 0:
        a = 1
    else:
        for i in range(1, n + 1):
            a *= i
    if x > y:
        b = x
        c = y
    else:
        b = y
        c = x
    if n + x > y and n + y > x and x + y > n:
        d = True
    else:
        d = False
    t = s.upper()
    e = ''
    for i in range(len(t)): e = t[i] + e
    return a, b, c, d, e


n = int(input('输入整数n='))
x, y = eval(input('输入两个实数x，y='))
s = input('输入字符串 s=')
v = df(n, x, y, s)
if v[3]:
    import math

    p = (n + x + y) / 2
    w = math.sqrt(p * (p - n) * (p - x) * (p - y))
else:
    w = -1
print('阶乘：%d, 最大值：%6.2f,最小值：%6.2f' % (v[0], v[1], v[2]))
print('面积：%6.2f, 大1写逆序：%s' % (w, v[4]))
