a = float(input('Введи число:'))
b = float(input('Введи число:'))
operation = input('*,/,+,-')
def calc (a, b, operation):
    if operation == '+':
        return (a+b)
    if operation == '-':
        return (a-b)
    if operation == '*':
        return (a*b)
    if operation == '/':
        return (a/b)
print(calc(a, b, operation))
