# Факториал числа n.

n = int(input("Введите число: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i
print("Факториал Вашего числа равен ", factorial)
