class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result

    def mul(self, num):
        self.result *= num
        return self.result

    def div(self, num):
        if(num == 0):
            print('not divisible by zero')
            return self.result
        self.result /= num
        return self.result


cal1 = Calculator()
cal2 = Calculator()
cal4 = Calculator()

cal1.add(2)
cal = cal1.add(2)
print(cal)

cal2.add(4)
cal = cal2.sub(2)
print(cal)

cal4.add(4)
cal = cal4.div(0)
print(cal)
cal = cal4.div(2)
print(cal)