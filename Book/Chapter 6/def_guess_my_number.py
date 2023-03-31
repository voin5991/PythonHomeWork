# Отгадай число
#
# Компьютер выбирает случайное число в диапозоне от 1 до 100
# Игрок пытается отгадать это число, и компьютер говорит
# предположение больше/меньше, чем загаданное число,
# или попало в точку.

import random
# set the initial values
the_number = random.randint(1, 100)
tries = 0

def intro():
    """
    Показывает вступление
    :return:
    """
    print("\tДобро пожаловать в игру 'Отгадай число'!")
    print("\nЯ загадал натуральное число из диапозона от 1 до 100")
    print("Постарайтесь отгадать его за 5 попыток.\n")

def ask_number(question, low, high):
    """
    Просит ввести число из диапазона.
    :param question:
    :param low:
    :param high:
    :return:
    """
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def guessing_loop():
    """
    Основная часть. Просит угадать число
    :return:
    """
    global the_number, tries
    guess = ask_number("Ваше предположение: ", 1, 100)
    while guess != the_number:
        if guess > the_number:
            print("Меньше...")
        else:
            print("Больше...")
        tries += 1
        if tries == 5:
            print('Достигнут лимит попыток.')
            break
        else:
            print("Вы использовали ", tries, " попытку(ки)")
            guess = ask_number("Ваше предположение: ", 1, 100)
    return guess

def congratulation(answer):
    """
    Выводит на экран результат игры
    :return:
    """
    global the_number, tries
    if answer == the_number:
        print("Вам удалось отгадать число! Это в самом деле ", the_number)
        print("Вы затратили на отгадывание всего лишь ", tries, "попыток(ки)!\n")
    else:
        print("""
        Вы исчерпали свой лимит попыток и не смогли отгадать число!
        Очень жаль... Я до конца не сомневался в Ваших способностях.
        """)

def main():
    intro()
    answer = guessing_loop()
    congratulation(answer)

main()
input("\n\nPress the enter key to exit.")
