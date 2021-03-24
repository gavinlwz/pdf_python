# n = 0
# while n < 100:  # 死循环
#     print('第{}次'.format(n))
#     n = n + 1
#     print('n=', n)
# ------------------------------------
# import math
#
# i, s = 0, 0
# while i < math.pow(10, 6):
#     s = s + i
#     i = i + 1
# else:
#     print('循环结束')
# print('Sum=', s)
# # ------------------------------------
# i = 1
# while i <= 26:
#     print('%c-%c' % (chr(96 + i), chr(64 + i)))
#     i += 1
# else:
#     print('循环结束')
# ------------------------------------
# import math
# i,s=0,0
# while i < math.pow(10,6):
#     if i %7==0:
#         i=i+1
#         continue
#     s+=i
#     i+=1
# print('Sun=',s)
#---------------------------------------
# import math
# ma=mi=su=av=nu=0
# mi=math.inf
# while 1 :
#     n=int(input('请输入整数 n='))
#     if n==0:
#         if mi ==math.inf:
#                 mi=0
#             nu+=1
#             break
#         nu+=1
#         su+=n
#         if n>ma:
#                 ma=n
#
#         if n< mi:
#                 mi=n
#     else:
#         print('循环结束')
#     if nu==1:
#         pass
#     else:
#         av=su/nu
#     print('和值=',su,'均值=',av,'最小值=',mi,'最大值=',ma,'个数=',nu)

