print('Enter the coefficients for the equation')
print('ax^2+bx+c=0: ')

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

discr = b ** 2 - 4 * a * c

x1 = -b + discr ** 0.5 / 2 * a
x2 = -b - discr ** 0.5 / 2 * a

print('x1 = ', x1)
print('x2 = ', x2)
