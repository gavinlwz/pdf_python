class ClassA():
    var1='两点水'

    @classmethod
    def fun1(cls):
        print('var1值为：'+cls.var1)


ClassA.fun1()
ClassA.var1=input('请输入修改的var1的值：')
ClassA.fun1()
ClassA.var2=input('请输入新增类属性var2的值：')
print(ClassA.var2)