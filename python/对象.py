# class ClassA():
#     var1 = 100
#     var2 = 0.01
#     var3 = '两点水'
#
#     def fun1():
#         print('我是 fun1')
#
#     def fun2():
#         print('我是 fun2')
#
#     def fun3():
#         print('我是 fun3')
#
# print(ClassA.var1)
# print(ClassA.var2)
# print(ClassA.var3)
# ClassA.fun1()
# ClassA.fun2()
# ClassA.fun3()

class ClassA(object):
    var1 = '两点谁'

    def fun1(cls):
        print('我是 fun1' + cls.var1)
        # print('年龄'+str(age))


a = ClassA()
a.fun1()
print(a.var1)
# ClassA.fun1(18)
