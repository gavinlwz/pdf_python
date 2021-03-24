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


class A:
    def fun(self):
        print('A1')

    def fun(self):
        print('A2')

class B:
    def fun(self):
        print('B1')
class C(A,B):
    def fun(self):
        super().fun()
        super(C, self).fun()
        super(A, self).fun()
        print('C')
print(C.__mro__)
c=C()
c.fun()








