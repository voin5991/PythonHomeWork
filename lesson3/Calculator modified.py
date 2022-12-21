import math
from tkinter import Y

x = float(input('First number: '))
y = float(input('Second number: '))
operation = input('Operation: ')

result = None

if operation == '+':
    result = x + y
elif operation == '-':
    result = x - y
elif operation == '*':
    result = x * y
elif operation == '/':
    result = x / y
elif operation == '^':
    result = x ** y
elif operation == 'sin':
    result = math.sin(x), math.sin(y)
elif operation == 'cos':
    result = math.cos(x), math.cos(y)
elif operation == 'tan':
    result = math.tan(x), math.tan(y)
else:
    print('Unsupported operation')

if result is not None:
    print('Result', result)
