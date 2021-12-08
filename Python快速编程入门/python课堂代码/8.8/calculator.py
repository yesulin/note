class Calculator(object):
    def __init__(self, number):  # 构造函数，记录数值
        self.number = number

    def __add__(self, other):  # 重载运算符+
        self.number = self.number + other
        return self.number

    def __sub__(self, other):  # 重载运算符-
        self.number = self.number - other
        return self.number

    def __mul__(self, other):  # 重载运算符*
        self.number = self.number * other
        return self.number

    def __truediv__(self, other):  # 重载运算符/
        self.number = self.number / other
        return self.number

calculator = Calculator(10)
print(calculator + 5)
print(calculator - 5)
print(calculator * 5)
print(calculator / 5)
