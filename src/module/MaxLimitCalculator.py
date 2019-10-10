import Calculator


class MaxLimitCalculator(Calculator.Calculator):

    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100


cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)
