a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
summ = 0

if a < b:
    for i in range(a, b +1):
        summ += i
    print(summ)
else:
    print("\aНеверный ввод")