# Инструкция
# Демонстрирует, как создавать собственные функции

def instructions():
    """
    Выводит на экран инструкцию для игрока.
    """
    print(
        """
        Добро пожаловать на ринг грандиознейших интеллектуальных состязаний всех времен.
        Твой мозг и мой процессор сойдутся в схватке за доской игры "Крестики-нолики".
        Чтобы сделать ход, введи число от 0 до 8. Числа однозначно соответствуют полям
        доски - так, как показано ниже:
        0 | 1 | 2
        ---------
        3 | 4 | 5
        ---------
        6 | 7 | 8
        Приготовься к бою, жалкий белковый человечишка. Вот-вот начнется решающее сра-
        жение.\n        
        """
    )
# основная часть
print("Это инструкция для игры в 'Крестики-нолики': ")
instructions()
print("Это опять та же самая инструкция: ")
instructions()
input("\n\nНажмите Enter, чтобы выйти.")