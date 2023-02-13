#                       Программа "Генератор персонажей" для ролевой игры.
# Пользователю должно быть предоставлено 30 пунктов, которые можно распределить между четырьмя характеристиками:
# Сила, Здоровье, Мудрость и Ловкость. Надо стделать так, чтобы пользователь мог не только брать эти пункты из
# общего "пула", но и возвращать их туда из характеристик, которым он решит присвоить другие значения.

char = []
choice = None

while choice != 0:
    choice = int(input("""
    Выберите класс своего персонажа, для подтверждения выбора введите '0'.
    
                0 - Подтвердить выбор
                1 - Воин
                2 - Варвар
                3 - Лучник
                4 - Волшебник
    """))
    if choice == 1:
        char = [["Сила", 5], ["Здоровье", 3], ["Мудрость", 2], ["Ловкость", 2]]
        print("\nВы выбрали Воина")
        print("Его характеристики:")
        print("Сила = ", char[0][1])
        print("Здоровье = ", char[1][1])
        print("Мудрость = ", char[2][1])
        print("Ловкость = ", char[3][1])
    elif choice == 2:
        char = [["Сила", 5], ["Здоровье", 5], ["Мудрость", 1], ["Ловкость", 1]]
        print("Вы выбрали Варвара")
        print("Его характеристики:")
        print("Сила = ", char[0][1])
        print("Здоровье = ", char[1][1])
        print("Мудрость = ", char[2][1])
        print("Ловкость = ", char[3][1])
    elif choice == 3:
        char = [["Сила", 3], ["Здоровье", 2], ["Мудрость", 2], ["Ловкость", 5]]
        print("Вы выбрали Лучника")
        print("Его характеристики:")
        print("Сила = ", char[0][1])
        print("Здоровье = ", char[1][1])
        print("Мудрость = ", char[2][1])
        print("Ловкость = ", char[3][1])
    elif choice == 4:
        char = [["Сила", 1], ["Здоровье", 5], ["Мудрость", 5], ["Ловкость", 1]]
        print("Вы выбрали Волшебника")
        print("Его характеристики:")
        print("Сила = ", char[0][1])
        print("Здоровье = ", char[1][1])
        print("Мудрость = ", char[2][1])
        print("Ловкость = ", char[3][1])

print("Вам дается 30 очков для распределения между 4-мя характеристиками.")
print("Вы можете прибавлять и убавлять количество очков в каждом пункте")

choice1 = None
choice2 = None
score = None
points = 30

while choice1 != 0:
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
        while choice2 != 0:
            print("\nОчков для распределения: ", points)
            print("\n\t\t\tСила = ", char[0][1])
            choice2 = int(input("""
            Добавить или убавить? Для выхода нажмите '0'.
            
                0 - Выход
                1 - Добавить
                2 - Убавить
           """))
            if choice2 == 1 and points != 0:
                score = int(input("Сколько очков вы хотите добавить?: "))
                points -= score
                if points < 0:
                    print("Недостаточно очков для добавления")
                    points += score
                else:
                    char[0][1] += score
            elif choice2 == 2:
                score = int(input("Сколько очков вы хотите убавить?: "))
                char[0][1] -= score
                if char[0][1] < 0:
                    print("Неверное значение")
                    char[0][1] += score
                else:
                    points += score
            elif points <= 0:
                print("Нет очков для распределения")
            elif choice2 == 0:
                continue
            else:
                print("Неверный ввод.")
    elif choice1 == 2:
        while choice2 != 0:
            print("\nОчков для распределения: ", points)
            print("\n\t\t\tЗдоровье = ", char[1][1])
            choice2 = int(input("""
            Добавить или убавить? Для выхода нажмите '0'.

                0 - Выход
                1 - Добавить
                2 - Убавить
           """))
            if choice2 == 1 and points != 0:
                score = int(input("Сколько очков вы хотите добавить?: "))
                points -= score
                if points < 0:
                    print("Недостаточно очков для добавления")
                    points += score
                else:
                    char[1][1] += score
            elif choice2 == 2:
                score = int(input("Сколько очков вы хотите убавить?: "))
                char[1][1] -= score
                if char[1][1] < 0:
                    print("Неверное значение")
                    char[1][1] += score
                else:
                    points += score
            elif choice2 == 0:
                continue
            elif points <= 0:
                print("Нет очков для распределения")
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
            if choice2 == 1 and points != 0:
                score = int(input("Сколько очков вы хотите добавить?: "))
                points -= score
                if points < 0:
                    print("Недостаточно очков для добавления")
                    points += score
                else:
                    char[2][1] += score
            elif choice2 == 2:
                score = int(input("Сколько очков вы хотите убавить?: "))
                char[2][1] -= score
                if char[2][1] < 0:
                    print("Неверное значение")
                    char[2][1] += score
                else:
                    points += score
            elif points <= 0:
                print("Нет очков для распределения")
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
            if choice2 == 1 and points != 0:
                score = int(input("Сколько очков вы хотите добавить?: "))
                points -= score
                if points < 0:
                    print("Недостаточно очков для добавления")
                    points += score
                else:
                    char[3][1] += score
            elif choice2 == 2:
                score = int(input("Сколько очков вы хотите убавить?: "))
                char[3][1] -= score
                if char[3][1] < 0:
                    print("Неверное значение")
                    char[3][1] += score
            elif points <= 0:
                print("Нет очков для распределения")
            elif choice2 == 0:
                continue
            else:
                print("Неверный ввод.")
    elif choice1 == 0:
        print("До свидания.")
    elif points == 0:
        print("Вы распределили все очки")
    elif points < 0:
        print("Не хватает очков для распределения")
    else:
        print("Неверный ввод")
    choice2 = None

input("Нажмите Enter для выхода")
