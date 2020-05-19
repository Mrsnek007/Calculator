import re


class Calculator:

    def action(self):
        expression = input("Введите выражение: ")
        if self.check_exp(expression):
            print(f"Атвед: {eval(expression)}")
        else:
            print("что за хуйню ты мне написал, педик")
            self.action()

    def check_exp(self, exp):
        res = re.search(r"[^ %-./*+0-9]", exp)
        if not res:
            return True
        return False


obj = Calculator()
obj.action()
