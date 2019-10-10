class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second




calA = FourCal(2,4)
calB = FourCal(1,5)

print(calA.add())
print(calA.sub())
print(calA.mul())
print(calA.div())
print('-'*10)

print(calB.add())
print(calB.sub())
print(calB.mul())
print(calB.div())
print('-'*10)


class MoreCal(FourCal):
    def pow(self):
        return self.first ** self.second
    def div(self):
        if self.second == 0:
            print('division by zero!!')
            return 0
        else:
            return self.first / self.second


calC = MoreCal(4,5)
print(calC.add())
print(calC.sub())
print(calC.mul())
print(calC.div())
print(calC.pow())
print('-'*10)
