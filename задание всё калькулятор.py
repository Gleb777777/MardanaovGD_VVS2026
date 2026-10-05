'''
class calculator:
    def __init__ (self,a,b):
        self.a = a
        self.b = b
    def calculate (self, operation):
        if operation == '+':
            return (self.a + self.b)
        if operation == '-':
            return (self.a - self.b)
        if operation == '*':
            return (self.a * self.b)
        if operation == '/':
            return (self.a / self.b)
a = float(input('Введите число:'))
b = float(input('Введите число:'))
c = float(input('Введите число:'))
d = float(input('Введите число:'))
operation = input("Введите операцию:")
calc = calculator(a,b)
calc2 = calculator (c,d)
print(calc.calculate(operation))
print(calc2.calculate(operation))
'''
'''
a = float(input("Введите число:"))
b = float(input("Введите число:"))
operation = input("Введите операцию")
if operation == '+'
    print (a+b)
if operation == '-':
    print (a-b)
if operation == '*':
    print (a*b)
if operation == '/':
    print (a/b)
'''
'''
a = float(input("Введите число:"))
b = float(input("Введите число:"))
operation = input("Введите операцию")
def calc(a,b,operation):
    if operation == "+":
        return a+b
    if operation == "-":
        return a-b
    if operation == "*":
        return a*b
    if operation == "/":
        return a/b
print (calc(a,b,operation))
'''
'''
def calc(a,b,operation):
    if operation == "+":
        return a+b
    if operation == "-":
        return a-b
    if operation == "*":
        return a*b
    if operation == "/":
        return a/b
while (True):
    a = float(input("Введите число:"))
    b = float(input("Введите число:"))
    operation = input("Введите операцию")
    print (calc(a,b,operation))
'''
    
















    
