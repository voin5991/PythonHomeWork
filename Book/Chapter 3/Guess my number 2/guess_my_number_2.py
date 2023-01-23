# Игра "Отгадай число", но теперь число загадывает игрок
# А компьютер должен его отгадать.

import random

print("\tДобро пожаловать в игру 'Отгадай число'!")
print("\nЗагадайте натуральное число из диапозона от 1 до 100")
print("Я постараюсь отгадать его за 5 попыток.\n")

guess = random.randint(1,100)
the_number = ""
tries = 1

while the_number != "Угадал":
    print("Я потратил ", tries, " попытку(ки)")
    print("Я предполагаю это ", guess)
    the_number = input("Напишите 'Больше, Меньше или Угадал': ")
    if the_number == "Больше" and guess <= 100:
        guess += random.randint(1,20)
    elif the_number == "Меньше" and guess >= 0:
        guess -= random.randint(1,20)
    else:
        print("Проверьте правильность ввода своего ответа. Соблюдайте регистр.")
        continue
    tries += 1
    if tries == 5:
        print("Достигнут лимит попыток")
        break
if the_number == "Угадал":
    print("Я потратил на угадывание Вашего числа ", tries, "попыток(ки)")
else:
    print("Мне не удалось угадать Ваше число, или Вы меня просто обманываете!")

print(input("\n\nНажмите Enter чтобы завершить программу: "))
