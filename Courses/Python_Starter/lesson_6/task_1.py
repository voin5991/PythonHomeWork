def rec_summ(a, b):
    """
    Рассчитывает сумму натуральных чисел в заданном диапазоне.
    :param a:
    :param b:
    :return:
    """
    if b == a:
        return b
    else:
        return b + rec_summ(a, b-1)


first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
print(rec_summ(first, second))
