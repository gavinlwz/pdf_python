# a=2
# b=5
# c=1
# d=b*b-4*a*c
# x1=(-b+math.sqrt(d)/(2*a))
# x2=(-b+math.sqrt(d)/(2*a))
# print('x1=%.6f%x1')
# print('x2=%.6f%x2')
# a,b=eval(input('输入两个整数a，b='))
# x,y=eval(input('输入两个复数x，y='))
# u,v=eval(input('输入两个复数u，v='))
# su=sum(a,b,x,y,u.real,u.imag,v.imag)
# av=su/8
# mi=min(a,b,x,y,u.real,u.imag,v.revl,v.imag)
# ma=max(a,b,x,y,u.real,u.imag,v.revl,v.imag)
# print('和值=',su,'均值=',av,'最小值=',mi,'最大值=',ma,)
# #4.2选择分至
# x=int(input('输入整数'))
# if x%2==0:print(x,'是偶数')

# import math
#
# a, b, c = eval(input('输入实数 a,b,c='))
# d = b * b - 4 * a * c
# if d < 0:
#     print('二次方程无根！')
# elif d == 0:
#     x = -b / (2 * a)
#     print('二次方程单根：')
#     print('x=%.6f' % x)
# else:
#     x1 = (-b + math.sqrt(d)) / (2 * a)
#     x2 = (-b - math.sqrt(d)) / (2 * a)
#     print('二次方程双根：')
#     print('x1=%.6f' % x1)
#     print('x2=%.6f' % x2)


# ------------------------------------
# x=float(input('输入实数x='))
# if x <=-50:
#     y=2*x-7
# elif x<=-25:
#     y=5*x-9
# elif x<=0:
#     y=6*x
# elif x<=25:
#     y=5*x+9
# else:
#     y=2*x+8
#     print('x=%.6f,y=%.6f'%(x,y))
# ------------------------------------
# x=float(input('请输成绩 x='))
# if x>90:
#     y='优秀'
# elif x>=80:
#     y='良好'
# elif x>70:
#     y='中等'
# elif x>=60:
#     y='及格'
# else:
#     y='挂了'
#     print('成绩：%.1f\n等级：'%x,y)
# ------------------------------------
x = float(input('请输月份 x='))
if x == 1:
    print('%d月的名称：' % x, 'January')
elif x == 2:
    print('%d月的名称：' % x, 'Fedruary')
elif x == 3:
    print('%d月的名称：' % x, 'March')
elif x == 4:
    print('%d月的名称：' % x, 'April')
elif x == 5:
    print('%d月的名称：' % x, 'May')
elif x == 6:
    print('%d月的名称：' % x, 'June')
elif x == 7:
    print('%d月的名称：' % x, 'July')
elif x == 8:
    print('%d月的名称：' % x, 'August')
elif x == 9:
    print('%d月的名称：' % x, 'September')
elif x == 10:
    print('%d月的名称：' % x, 'October')
elif x == 11:
    print('%d月的名称：' % x, 'November')
elif x == 12:
    print('%d月的名称：' % x, 'December')
else:
    print('%d:' % x, '无效的月份！')

#--------------------------
#自蜜薯
# for i in range(pow(10,6),pow(10,7)-1):
#     size = len(str(i)) #计算每个数字长度
#     eve = []
#     for j in range(size): # 循环长度次数
#         a = str(i)[j]  # 分解每一位数字
#         eve.insert(j,a) # 将数字保存在list中
#     s = 0
#     for j in range(size):
#         j1 = int(eve[j])
#         s1 = pow(j1,size)
#         s +=s1
#     if i==s:
#         print('{}自幂数：{}'.format(size,i))