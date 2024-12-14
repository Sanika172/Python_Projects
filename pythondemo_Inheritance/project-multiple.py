class calculation1:
    def sum(self, a, b):
        return a + b


class calculation2:
    def mul(self, x, y):
        return x * y


class operation(calculation1, calculation2):
    def divide(self, a, b):
        return a / b


op = operation()
print(op.sum(20, 68))
print(op.mul(56, 3))
print(op.divide(50, 5))
