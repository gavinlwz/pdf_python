# def func(a,b,c):
#     a=99
#     b[0]='hhh'
#     c=['z','x','c']
#     print('函数内部b和c',b,c,id(b),id(c))
#
# num=1
# lis1=[1,2,3,4,5]
# lis2=[9,10,11,12,]
# print('函数外的lis：',lis1,lis2,id(lis1),id(lis2))
# func(1,lis1,lis2)
# print('函数处理后的lis',lis1,lis2,id(lis1),id(lis2))
#
# #例5.9
# def fu(x,y):
#     x=[6,6,6]
#     y={'r':9,'s':9,'t':9}
#     print('调用函数内部：',x,y)
# u=[1,2,3,4,5,6]
# v={'a':1,'b':2,'c':3,'d':5,'e':5}
# print('调用函数内部：',u,v)
# fu(u,v)
# print('调用函数之后',u,v)
#
#
# #例5.10
# def fu(x,y):
#     x=x*x-9
#     y='welcome...'+y+'HappyYou!'
#     z=not x
#     return  x,y,z
# u=eval(input('输入一个数据'))
# v=input('输入一个姓名：')
# w=fu(u,v)
# print('奖金：',w[0])
# print(w[1])
# if w[2]:
#     print('婚否：已婚！')
# else:
#     print('婚否：未婚！')



# 例5.11
def fu(x,y,z='n'):
    x=x*x-9
    y = 'welcome...,' + y + ',HappyYou!'
    if z=='y':
        z=True
    else:
        z=False
    return x,y,z
u=eval(input('输入一个数据'))
v=input('输入一个姓名')
w=input('输入婚否（y/n）？')
e=fu(u,v)
print('奖金：',e[0])
print(e[1])
if e [2]:
    print('婚否：已婚！')
else:
    print('婚否：未婚！')
e=fu(u,v,w)
print('奖金：',e[0])
print(e[1])
if e [2]:
    print('婚否：已婚！')
else:
    print('婚否：未婚！')


# 例5.12
def fu(x,y,z='n'):
    x=x*x-9
    y = 'welcome...,' + y + ',HappyYou!'
    if z=='y':
        z=True
    else:
        z=False
    return x,y,z
u=56
v='Tom'
w='y'
e=fu(y=v,z=w,x=u)
print('奖金：',e[0])
print(e[1])
if e[2]:
    print('婚否：已婚！')
else:
    print('婚否：未婚！')



