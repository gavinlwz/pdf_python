class Animal:

    def eat(self):
        print("%s 吃 " % self.name)

    def drink(self):
        print("%s 喝 " % self.name)

    def shit(self):
        print("%s 拉 " % self.name)

    def pee(self):
        print("%s 撒 " % self.name)


class Cat(Animal):

    def __init__(self, name):
        self.name = '猫在'

class Dog(Animal):

    def __init__(self, name):
        self.name = '狗在'

class Animals(Cat, Dog):
    def fun(self):
        super(Animals, self).fun()
        super(Cat, self).fun()
        print('dongwu')

print(Animals.__mro__)
cat=Cat('Cat')
cat.pee()



# c1 = Cat(Cat)
# c1.eat()
# c1.drink()
# c1.pee()
# c1.shit()
#
#
#
# d1 = Dog(Dog)
# d1.eat()
# d1.drink()
# d1.pee()
# d1.shit()