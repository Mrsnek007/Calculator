class Calculator:
    def __init__(self, choose=1):
        self.choose = choose

    def action(self, operation):
        if self.choose == 1:
            expression = input("Введите выражение: ")
            print(eval(expression))


obj = Calculator(1)
obj.action(1)