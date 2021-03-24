# （1）列表。给出如下运行结果。
import sys  # 注意操作系统的字长（32 or 64)

print([], type([]), sys.getsizeof([]))
x = 12;
l1 = [x]
print(x, type(x), sys.getsizeof(x), sys.getsizeof(l1))
y = 1.1;
l2 = [y]
print(y, type(y), sys.getsizeof(y), sys.getsizeof(l2))
z = '2';
l3 = [z]
print(z, type(z), sys.getsizeof(z), sys.getsizeof(l3))
w = True;
l4 = [w]
print(w, type(w), sys.getsizeof(w), sys.getsizeof(l4))
s = [1, 2, 3]
for i in s:
    print('i=', i)
    print('s=', s)
    s.remove(i)
print('为什么! for的计数器!')
s = [1, 2, 3]
for i in list(s):
    print('i=', i)
    print('s=', s)
    s.remove(i)
l1 = ['1', '2', 1, 2];
l2 = l1;
l3 = list(l1)
print('l1=', l1, 'l2=', l2, 'l3=', l3)
print('id(l1)=', id(l1), 'id(l2)=', id(l2), 'id(l3)=', id(l3))
l1.remove(l1[0])
print('l1=', l1, 'l2=', l2, 'l3=', l3)
print('id(l1)=', id(l1), 'id(l2)=', id(l2), 'id(l3)=', id(l3))
sinfo = [['学号', '姓名', '性别', '年龄', '婚否'],
         ['1801', '张三', '男', 19, True],
         ['1802', '李四', '女', 16, False],
         ['1803', '王五', '男', 18, True]]
for i in range(4): print(sinfo[i])
print(sinfo[3][1])
print(sinfo[1][0:3])
print(sinfo[1])
print(sinfo[1][:])
for x in range(4): print(sinfo[x][1])
# （2）元组。运行如下程序，然后给出运行结果，进而描述其功能。
a = ((1, 2, 3, 6), (4, 5, 6, 8), (7, 8, 9, 6), (5, 2, 8, 7))
for i in range(4): print(a[i])
print(len(a))
for i in range(4): print('max=', max(a[i]))
print('min=', min((a[0][2], a[1][2], a[2][2], a[3][2])))
print('sum=', sum((a[0][0], a[1][1], a[2][2], a[3][3])))
print('ave=', sum((a[0][3], a[1][2], a[2][1], a[3][0])) / 4.0)
# （3）集合。运行如下程序，然后给出运行结果，进而描述其功能。
u = {1, 2, 3, 4, 5, 6};
v = {5, 6, 7, 8, 9};
w = {'a', 'b', 'c', 5, 6, 7, True}
print(u | v | w, u & v & w)
print(u.union(v, w), u.intersection(v, w))
print(u - v - w, u ^ v ^ w)
print(u.difference(v, w), u.symmetric_difference(v))
print(len(w), sum(u | v), max(u), min(v))
print(u >= v, u < w)
# （4）字典。运行如下程序，然后给出运行结果，进而描述其功能。
s = {'学号': ['姓名', '性别', '年龄', '婚否', ('高数', '英语', '体育', '软件')],
     '1901': ['张三', '男', 19, True, (90, 92, 98, 96)],
     '1902': ['李四', '女', 16, False, (95, 96, 99, 97)],
     '1903': ['王五', '男', 18, True, (97, 91, 95, 98)]}
print(s)
for x in s.keys(): print(x, s[x])
s['1904'] = ['孙六', '女', 20, False, None]
s['1905'] = ['赵七', '女', 22, True]
for x in s.keys(): print(x, s[x])
s['1904'] = ['孙六', '女', 20, False, (99, 99, 99, 99)]
for x in s.keys(): print(x, s[x])
s.pop('1905')
for x in s.keys(): print(x, s[x])
if '1904' in s.keys(): print('1904', s['1904'])
if '1905' not in s.keys(): print('查无此人!')
print('学生人数：', len(s) - 1)
s.clear()
print(s)
