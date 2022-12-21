import math

x = float(input('Enter value x: '))

if -math.pi <= x <= math.pi:
    y = math.cos(3 * x)
    print('y = ', y)
elif x < -math.pi or x > math.pi:
    y = x
    print('y = ', y)
