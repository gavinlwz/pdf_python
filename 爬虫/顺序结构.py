# x=100
# y=int(input('请输入一整数：'))
# if x==y:
#     print('恭喜你，猜对了')
# else:
#     print('很抱歉，猜错了')
# ------------------------------
x = int(input('请输入一整数：'))
if x % 2 == 0:
    print('x为偶数')
else:
    print('x为奇数')
# --------------------------------
# n = int(input('请输入七位整数n：'))
# s = str(n)
# z = int(s[0])
# x = int(s[1])
# c = int(s[2])
# v = int(s[3])
# b = int(s[4])
# j = int(s[5])
# k = int(s[6])
# if n == pow(z, 7) + pow(x, 7) + pow(c, 7) + pow(v, 7) + pow(b, 7) + pow(j, 7) + pow(k, 7):
#     print('%7d是北斗七星数，自幂数' % n)
# else:
#     print('%7d不是北斗七星数，自幂数' % n)
# ---------------------------------------------------------

# x=str(input('请输入账号:'))
# y=str(input('请输密码:'))
# if x=='username' and y=='123456':
#     print('登录成功')
# else:
#     print('登录失败')

'''
a=float(input('第一条边长：'))
b=float(input('第2条边长：'))
c=float(input('第3条边长：'))
p=(a+b+c)/2
s=(p*(p-a)*(p-b)*(p-c))**0.5
print(s)
'''
#
s = float(input('请输入时间'))
if s < 8:
    print('还可以继续睡')
else:
    x = float(input('请输入星期几'))
    if x == 6 or x == 7:
        print('今天不上课，继续睡')
    else:
        print('起来上课')
