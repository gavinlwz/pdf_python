def goToSchool(name,age,gender):

    print("%s去学校， 今年%d岁，是个%s的"%(name,age,gender))

def ogToZoo(name,age,gender):

    print("%s去动物园， 今年%d岁，是个%s的"%(name,age,gender))

goToSchool('小王',20,'男')

goToSchool('康康',20,'女')


class Foo:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def goToZoo(self):
        print("%s去动物园， 今年%d岁，是个%s的"%(self.name,self.age,self.gender))
    def goToSchool(self):
        print("%s去学校， 今年%d岁，是个%s的"%(self.name,self.age,self.gender))


xiaowang=Foo('小王',20,'男')
xiaowang.goToZoo()
xiaowang.goToSchool()

kangkang=Foo('康康',20,'男')
kangkang.goToZoo()
kangkang.goToSchool()


'''
分装型
'''


# class person:
#     def __init__(self, name, age, gender, height, weight):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.height = height
#         self.weight = weight
#
#     def eaf(self):
#         self.weight += 0.2
#         print('%s吃饭，体重增加到了(%.2f)' % (self.name, self.weight))
#
#     def run(self):
#         self.height += 0.01
#         self.weight += 0.01
#         print('%s跑步，申高增加到了(%.2f),体重减小到了%.2f' % (self.name, self.height, self.weight))
#
#     def __str__(self):
#         return '我是%s，我身高是%.2f，我体重是%d，我性别是%s' % (self.name, self.height, self.weight, self.age, self.gender)
#
#
# kangkang = person('康康', 20, '男', 100, 250)
# kangkang.eaf()
# print()
