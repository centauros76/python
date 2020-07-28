class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result


cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(5))
print(cal2.add(1))


class FourCal:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def setdata(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return 0


class NewFourCal(FourCal):
    def pow(self):
        return self.a ** self.b


fcal = FourCal(6, 3)
print("{} + {} = {}".format(fcal.a, fcal.b, fcal.add()))
print("{} - {} = {}".format(fcal.a, fcal.b, fcal.sub()))
print("{} * {} = {}".format(fcal.a, fcal.b, fcal.mul()))
print("{} / {} = {}".format(fcal.a, fcal.b, fcal.div()))



nfcal = NewFourCal(9, 3)
print("{} + {} = {}".format(nfcal.a, nfcal.b, nfcal.add()))
print("{} - {} = {}".format(nfcal.a, nfcal.b, nfcal.sub()))
print("{} * {} = {}".format(nfcal.a, nfcal.b, nfcal.mul()))
print("{} / {} = {}".format(nfcal.a, nfcal.b, nfcal.div()))
print("{} ** {} = {}".format(nfcal.a, nfcal.b, nfcal.pow()))