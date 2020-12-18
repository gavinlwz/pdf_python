# class  A:
#     def A1(self):
#         print('A1')
# class B (A):
#     def B1(self):
#         print('B1')
# objb =B()
# objb.B1()
# objb.A1()

# class A:
#     def fun(self):
#         print('A1')
#     def fun2(self):
#         print('A2')
#
# class B:
#     def fun2(self):
#         print('B1')
#
# class C (A,B):
#     def fun(self):
#         A.fun(self)
#         A.fun(self)
#         B.fun2(self)
#         print('C')
#         c=C()
#         c.fun()
#
# class A:
#     def fun(self):
#         print('A1')
#
#     def fun(self):
#         print('A2')
#
# class B:
#     def fun(self):
#         print('B1')
# class C(A,B):
#     def fun(self):
#         super().fun()
#         super(C, self).fun()
#         super(A, self).fun()
#         print('C')
# print(C.__mro__)
# c=C()
# c.fun()

'''
多态的
'''

# class Duck(object):
#     def fly(self):
#         print('鸭子嘎嘎嘎，叫')
# class Swank(object):
#     def fly(self):
#         print('天鹅边叫变非')
# class Plane(object):
#     def fly(self):
#         print('飞机呜呜呜呜')
# class Bee(object):
#     def fly(self):
#         print('蜜蜂嗡嗡嗡')
# class Chicken(object):
#     def fly(self):
#         print('公鸡不会飞')
# def fly(obj):
#     obj.fly()
# duck=Duck()
# swan=Swank()
# plane=Plane()
# bee=Bee()
# chicken=Chicken()
#
#
# fly(duck)
# fly(swan)
# fly(plane)
# fly(bee)
# fly(chicken)

'''
抽象
抽象类可以看做是可重用，可移植，可扩张的基类；而根据使用情况的不同，
需要对这个基类进项函数的重新或扩展；抽象类不可实例化，是考虑到并不是所有的情况
都需要这个基类，在不需要的情况下如果还要实例化就会很繁琐；而对基类进项抽象，派生类继承，
在需要使用基类函数的情况下再调用就可以方便使用
'''

import abc
class Animals (metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def talk(self):
        pass

class People(Animals):
    def talk(self):
        print('人说话')

class Cat(Animals):
    def talk(self):
        print('猫说话')

# animal=Animals()#实例化抽象类 会出错
cat1=Cat()
cat1.talk()
peo =People()
peo .talk()



def talk_(obj):
    obj.talk()

talk_(cat1)





