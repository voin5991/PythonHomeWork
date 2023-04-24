def integer_list(a, b):
    """
    Принимает два числа, находит все простые числа в заданном диапозоне
    и вносит их в список. Возвращает полученный список простых чисел.
    :param a:
    :param b:
    :return:
    """
    lst = []
    for i in range(a, b + 1):
        count = 0
        delitel = 2
        while delitel < i:
            if i % delitel == 0:
                count += 1
            delitel += 1
        if count == 0:
            lst.append(i)
    return lst


def main():
    lst = None
    first = None
    second = None
    choice = None
    summ = 0
    multiplication = 1
    while choice != "0":
        print("""
                       Меню:
                   0 - Выход
                   1 - Создать список
                   2 - Вывести список на экран
                   3 - Показать сумму всех чисел списка
                   4 - Показать произведение всех чисел списка
           """)
        choice = input("\nВаш выбор: ")
        if choice == "0":
            print("До свидания!")
        elif choice == "1":
            first = int(input("Введите первое число: "))
            second = int(input("Введите второе число: "))
            lst = integer_list(first, second)
            print("Список создан!")
        elif choice == "2":
            print(lst)
        elif choice == "3":
            for i in lst:
                summ += i
            print("Сумма всех чисел списка равна ", summ)
        elif choice == "4":
            for i in lst:
                multiplication *= i
            print("Произведение всех чисел списка равно ", multiplication)
        else:
            print("В меню нет пункта", choice)


main()
input("\n\nНажмите Enter, чтобы выйти.")
