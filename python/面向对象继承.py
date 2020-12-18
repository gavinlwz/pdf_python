class fu:
    def chi(self):
        print('吃')

    def he(self):
        print('喝')

class zi:
    def fun(self):
        print('拉')

class dongwu(fu,zi):
    def chi(self):
        super().chi()
        super().he()

# print(dongwu.__mro__)
dongwu=dongwu()
dongwu.chi()