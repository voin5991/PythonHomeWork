lst = [1, 4, 3, 7, 12, 67,245, 123]
a = max(lst)
b = min(lst)
summ = 0
for i in lst:
    summ += i
c = len(lst)
average = summ / c
print(lst)
print("Минимальное значение списка: ", b)
print("Максимальное значение списка: ", a)
print("Сумма всех чисел списка: ", summ)
print("Среднее арифметическое чисел в списке: ", average)
