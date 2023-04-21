def math_average(a, b, c):
    average = (a + b + c) // 3
    return average


def main():
    choice = None
    a = None
    b = None
    c = None
    average = None
    while choice != "0":
        print("""
                    Меню:
                0 - Выход
                1 - Рассчёт
        """)
        choice = input("Ваш выбор: ")
        if choice == "0":
            print("До свидания!")
        elif choice == "1":
            a = int(input("Введите первое число: "))
            b = int(input("Введите второе число: "))
            c = int(input("Ввеедите третье число: "))
            average = math_average(a, b, c)
            print("\nСреднее арифметическое чисел", a, b, c, "равно", average)
        else:
            print("Извините, в меню нет пункта", choice)


main()
input("\n\nНажмите Enter, чтобы выйти.")
