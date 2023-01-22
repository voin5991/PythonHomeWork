# Игра "Отгадай число", но теперь число загадывает игрок
# А компьютер должен его отгадать.

import random

print("\tДобро пожаловать в игру 'Отгадай число'!")
print("\nЗагадайте натуральное число из диапозона от 1 до 100")
print("Я постараюсь отгадать его за 5 попыток.\n")

guess = random.randint(1,100)
guess_1 = None
the_number = ""
tries = 5

while the_number != "Угадал":
    print("У меня осталось ", tries, " попыток")
    print("Я предполагаю это ", guess)
    the_number = input("Напишите 'Больше, Меньше или Угадал': ")
    if the_number == "Больше":
        guess = random.randint(guess,100)
    elif the_number == "Меньше":
        guess = random.randint(1,guess)
    else:
        print("Проверьте правильность ввода своего ответа. Соблюдайте регистр.")
        continue
    tries -= 1
    if tries == 1:
        print("Достигнут лимит попыток")
        break
if the_number == "Угадал":
    print("Я потратил на угадывание Вашего числа ", tries, "попыток(ки)")
else:
    print("Мне не удалось угадать Ваше число, или Вы меня просто обманываете!")

print(input("Нажмите Enter чтобы завершить программу: "))
