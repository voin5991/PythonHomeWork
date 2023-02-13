#                       Программа "Генератор персонажей" для ролевой игры.
# Пользователю должно быть предоставлено 30 пунктов, которые можно распределить между четырьмя характеристиками:
# Сила, Здоровье, Мудрость и Ловкость. Надо стделать так, чтобы пользователь мог не только брать эти пункты из
# общего "пула", но и возвращать их туда из характеристик, которым он решит присвоить другие значения.

points = 30
char = [["Сила", 5],
        ["Здоровье", 4],
        ["Мудрость", 1],
        ["Ловкость", 2]]
choice1 = None
choice2 = None
score = None

print("Вам дается 30 очков для распределения между 4-мя характеристиками.")
print("Вы можете прибавлять и убавлять количество очков в каждом пункте")

while points > 0 and choice1 != 0:
    print("\nВаши характеристики сейчас:")
    print("Сила = ", char[0][1])
    print("Здоровье = ", char[1][1])
    print("Мудрость = ", char[2][1])
    print("Ловкость = ", char[3][1])
    print("\nОчков для распределения: ", points)
    choice1 = int(input("""
    Выберите характеристику, которую хотите изменить. Для выхода введите '0'.
                
            0 - Выход
            1 - Сила
            2 - Здоровье
            3 - Мудрость
            4 - Ловкость
    """))
    if choice1 == 1:
        while choice2 != 0 and points > 0:
            print("\nОчков для распределения: ", points)
            print("\n\t\t\tСила = ", char[0][1])
            choice2 = int(input("""
            Добавить или убавить? Для выхода нажмите '0'.
            
                0 - Выход
                1 - Добавить
                2 - Убавить
           """))
            if choice2 == 1:
                score = int(input("Сколько очков вы хотите добавить?: "))
                char[0][1] += score
                points -= score
            elif choice2 == 2:
                score = int(input("Сколько очков вы хотите убавить?: "))
                char[0][1] -= score
                points += score
            elif choice2 == 0:
                continue
            else:
                print("Неверный ввод.")
    elif choice1 == 2:
        while choice2 != 0 and points > 0:
            print("\nОчков для распределения: ", points)
            print("\n\t\t\tЗдоровье = ", char[1][1])
            choice2 = int(input("""
            Добавить или убавить? Для выхода нажмите '0'.

                0 - Выход
                1 - Добавить
                2 - Убавить
           """))
            if choice2 == 1:
                score = int(input("Сколько очков вы хотите добавить?: "))
                char[1][1] += score
                points -= score
            elif choice2 == 2:
                score = int(input("Сколько очков вы хотите убавить?: "))
                char[1][1] -= score
                points += score
            elif choice2 == 0:
                continue
            else:
                print("Неверный ввод.")
    elif choice1 == 3:
        while choice2 != 0 and points > 0:
            print("\nОчков для распределения: ", points)
            print("\n\t\t\tМудрость = ", char[2][1])
            choice2 = int(input("""
            Добавить или убавить? Для выхода нажмите '0'.

                0 - Выход
                1 - Добавить
                2 - Убавить
           """))
            if choice2 == 1:
                score = int(input("Сколько очков вы хотите добавить?: "))
                char[2][1] += score
                points -= score
            elif choice2 == 2:
                score = int(input("Сколько очков вы хотите убавить?: "))
                char[2][1] -= score
                points += score
            elif choice2 == 0:
                continue
            else:
                print("Неверный ввод.")
    elif choice1 == 4:
        while choice2 != 0 and points > 0:
            print("\nОчков для распределения: ", points)
            print("\n\t\t\tЛовкость = ", char[3][1])
            choice2 = int(input("""
            Добавить или убавить? Для выхода нажмите '0'.

                0 - Выход
                1 - Добавить
                2 - Убавить
           """))
            if choice2 == 1:
                score = int(input("Сколько очков вы хотите добавить?: "))
                char[3][1] += score
                points -= score
            elif choice2 == 2:
                score = int(input("Сколько очков вы хотите убавить?: "))
                char[3][1] -= score
                points += score
            elif choice2 == 0:
                continue
            else:
                print("Неверный ввод.")
    elif choice1 == 0:
        print("До свидания.")
    else:
        print("Неверный ввод")
    choice2 = None

input("Нажмите Enter для выхода")
