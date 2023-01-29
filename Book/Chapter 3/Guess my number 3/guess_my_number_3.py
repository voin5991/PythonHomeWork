# Полная версия игры "Отгадай число".

import random

print("\tДобро пожаловать в игру 'Отгадай число'!")
print("\nЯ загадал натуральное число из диапозона от 1 до 100")
print("Постарайтесь отгадать его за 5 попыток.\n")

# set the initial values
the_number = random.randint(1, 100)
guess = int(input("Ваше предположение: "))
tries = 1

# guessing loop
while guess != the_number:
    if guess > the_number:
        print("Меньше...")
    else:
        print("Больше...")
    tries += 1
    print("Вы потратили ", tries, " попытку(ки)")
    guess = int(input("Ваше предположение: "))
    if tries == 5:
        print('Достигнут лимит попыток.')
        break

if guess == the_number:
    print("\aВам удалось отгадать число! Это в самом деле ", the_number)
    print("Вы затратили на отгадывание всего лишь ", tries, "попыток(ки)!\n")
else:
    print("""
    \aВы исчерпали свой лимит попыток и не смогли отгадать число!
    Очень жаль... Я до конца не сомневался в Ваших способностях.
    """)

input("\n\nНажмите Enter чтобы продолжить:")


print("\n\n\tТеперь Ваша очередь загадывать!")
print("\nЗагадайте натуральное число из диапозона от 1 до 100")
print("Я постараюсь отгадать его за 5 попыток.\n")

guess = random.randint(1, 100)
the_number = ""
tries = 1

while the_number != "Угадал":
    print("Я потратил ", tries, " попытку(ки)")
    print("Я предполагаю это ", guess)
    the_number = input("Напишите 'Больше, Меньше или Угадал': ")
    if the_number == "Больше" and guess <= 100:
        guess += random.randint(1, 20)
    elif the_number == "Меньше" and guess >= 0:
        guess -= random.randint(1, 20)
    else:
        print("\nПроверьте правильность ввода своего ответа. Соблюдайте регистр.")
        continue
    tries += 1
    if tries == 5:
        print("Достигнут лимит попыток")
        break
if the_number == "Угадал":
    print("\aЯ потратил на угадывание Вашего числа ", tries, "попыток(ки)")
else:
    print("\aМне не удалось угадать Ваше число, или Вы меня просто обманываете!")

print(input("\n\nНажмите Enter чтобы завершить программу: "))
