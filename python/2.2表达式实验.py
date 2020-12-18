# （1）
import math


x = 10
y = 20
z = (7 + 9j + 2 * x * math.cos(math.radians(66))) / (x + (x - y) / (x + y) + 6)
print(z)
(0.9660467783946386 + 0.574468085106383j)
z = (7 + 9j + 2 * x * math.cos(66 * math.pi / 180)) / (x + (x - y) / (x + y) + 6)
print(z)
# （2）
import math

a = 10;
b = 20;
c = 2
x = math.exp(math.pow(b, math.sqrt(math.pi / 2))) + \
    (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a) + \
    (math.log10(abs(a + b)) + a / b) / math.log(math.pow(a, b) + 100, math.e)
print(x)
3.562009699414695e+18
# （3）
print(250 * 2 + 38 - 17.8686)

520.1314  # （我爱你一生一世）
# （4）
x = 'J bn b Cpz'
y = 'H lhrr xnt'
a = ''
b = ''
for i in range(len(x)):
    if x[i]==' ':
        a+=' '
    else:
        a += chr(ord(x[i]) - 1)
for i in range(len(x)):
    if y[i] == ' ':
        b += ' '
    else:
        b += chr(ord(y[i]) + 1)
print(a, b)
#I am a Boy I miss you




