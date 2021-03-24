a = 1;#创建整数
b = 2;#创建整数
c = 3#创建整数
print('a=', a, 'b=', b, 'c=', c)#输出整数的值
age = 25#创建变量
sex = '男'
sala = 6000
mar = True
du = '教授'
print('年龄：', age, '性别：', sex, '工资：', sala, '婚否：', mar, '职称：', du)
print(a < b and age <= 25 or sala >= 5000 and not mar)
print(age >= 20 and sala <= 9000 and not mar and (a + b) > c)
print(c > b and du == '教授' or mar and not sex == '女')
print((a + b) ^ 2 * c + len('China->' + '浙江' + 'chr(88)' + '杭州') + True + False)
# （2）给出如下语句的运行结果及其功能。
x = 796
print('x=', x)
i = x % 10
j = x // 10 % 10
k = x // 100
print('i=', i, 'j=', j, 'k=', k)
y = 100 * i + 10 * j + k
print('y=', y)
x = 518
print('x=', x)
s = str(x)
t = s[2] + s[1] + s[0]
y = int(t)
print('y=', y)
x = 192837465
print('x=', x, type(x))
s = list(str(x))
print('s=', s)
s.reverse()
print('t=', s)
t = ''.join(s)
print('y=', t, type(t))
y = int(t)
print('y=', y, type(y))
