#创建元组
print((),tuple(),type(()),type(tuple()))#
print(('a','b','c','d',),tuple(range(9)),type(tuple(range(9))))
print(tuple(range(1,60,5)))
print((1,2,3,4,5,6,'a','b','b',10.36))
print((1,2)*6,9*(5,))
print(tuple('abcdef123456'))
print(tuple([1,2,3,4,5,6,'a','b','c','d','e','f']))
print(((1,2,3,4,5,6),(6,5,4,3,2,1)))
print(tuple([tuple([2 for x in range(6)]) for y in range(3)]))
#编辑元组
x=(1,2,3,4,5,6)
y=('a','b','c','d')
print(x[:],x[1],x[2:],x[:3],x[1:3],x[1:5:2],y.index('b'))
x=(1,2,3,4,5,6,)
del x
#使用元组
for x in (1,2,3,4,5,6):print(x)
s=tuple(range(10))
print(s[2],s[3:6],s[2:9:3])
s=tuple(range(10));t=('a','b','c')
x=s+t
print(x)
y=x+(True,)
print(y)
s=tuple(range(10))
print(len(s),sum(s),max(s),min(s))
x=('1','2','3');y=('a','b','c')
print(x>y,y+('2',)>=('a','c','D','1'))
print(x is y,x !=y,'2'in x,'c'not in ('a','c','c','D','1'))
print(x is y,x !=y,('2',)in x,('c',)not in('a','c','c','D','1'))
S=(1,2,3,2,3,5,6,5,6,8,9,8,8,6,5)
n=s.count(8)
print(n,s)
#复制元组
a = ('a', 'b', 'c',)
b = a
c = a[:]
import copy

d = copy.copy(a)
print(a, b, c, d)
print(id(a), id(b), id(c), id(d))
a = a + (1,)
print(a, b, c, d)
print(id(a), id(b), id(c), id(d))
b = b + (2,)
print(a, b, c, d)
print(id(a), id(b), id(c), id(d))
c = c + (3,)
print(a, b, c, d)
print(id(a), id(b), id(c), id(d))
d = d + (4,)
print(a, b, c, d)
print(id(a), id(b), id(c), id(d))
