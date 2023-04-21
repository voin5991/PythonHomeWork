def addition(a, b):
    result = a + b
    return result


def subtraction(a, b):
    result = a - b
    return result


def multiplication(a, b):
    result = a * b
    return result


def division(a, b):
    if a != 0 and b != 0:
        result = a / b
        return result
    else:
        print("На 0 делить нельзя!")


def main():
    choice = None
    a = None
    b = None
    while choice != "0":
        print("""
                        Меню:
                    0 - Выход
                    1 - Сложение
                    2 - Вычитание
                    3 - Умножение
                    4 - Деление
            """)
        choice = input("Ваш выбор: ")
        if choice == "0":
            print("До свидания!")
        elif choice == "1":
            a = int(input("Введите первое число: "))
            b = int(input("Введите второе число: "))
            result = addition(a, b)
            print(a, "+", b, "=", result)
        elif choice == "2":
            a = int(input("Введите первое число: "))
            b = int(input("Введите второе число: "))
            result = subtraction(a, b)
            print(a, "-", b, "=", result)
        elif choice == "3":
            a = int(input("Введите первое число: "))
            b = int(input("Введите второе число: "))
            result = multiplication(a, b)
            print(a, "*", b, "=", result)
        elif choice == "4":
            a = int(input("Введите первое число: "))
            b = int(input("Введите второе число: "))
            result = division(a, b)
            print(a, "/", b, "=", result)
        else:
            print("Извините, в меню нет пункта", choice)

main()
input("\n\nНажмите Enter, чтобы выйти.")
