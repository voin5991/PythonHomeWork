# Программа "Считалка".

num_1 = int(input("Введите начальное число: "))
num_2 = int(input("Введите конечное число: "))
result = None

while num_1 > num_2:
    print("Ошибочный ввод, начальное число не может быть больше конечного!")
    num_1 = int(input("Введите начальное число: "))
    num_2 = int(input("Введите конечное число: "))
for result in range(num_1, num_2 + 1):
    print(result)