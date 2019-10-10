import Calculator


class UpgradeCalculator(Calculator.Calculator):

    def minus(self, val):
        self.value -= val


cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)
