# Моя зверушка
# Виртуальный питомец, о котором пользователь может заботиться

class Critter(object):
    """
    Виртуальный питомец
    """

    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "неплохо"
        elif 11 <= unhappiness <= 15:
            m = "не сказать чтобы хорошо"
        else:
            m = "ужасно"
        return m

    def talk(self):
        print("Меня зовут", self.name, ", и сейчас я чувствую себя", self.mood, "\n")
        self.__pass_time()

    def eat(self, food=4):
        print("Мррр... Спасибо!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=4):
        print("Уиии!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    crit_name = input("Как вы назовете свою зверушку? ")
    crit = Critter(crit_name)
    choice = None
    while choice != "0":
        print("""
                    Моя зверушка
                    0 - Выйти
                    1 - Узнать о самочуствии зверушки
                    2 - Покормить зверушку
                    3 - Поиграть со зверушкой
                    """)
        choice = input("Ваш выбор: ")
        print()
        # выход
        if choice == "0":
            print("До свидания")
        # беседа со зверушкой
        elif choice == "1":
            crit.talk()
        # кормление зверушки
        elif choice == "2":
            crit.eat()
        # игра со зверушкой
        elif choice == "3":
            crit.play()
        # непонятный пользовательский ввод
        else:
            print("Извините, в меню нет пункта", choice)


main()
input("\n\nНажмите Enter, чтобы выйти.")

# TODO: Доработать программу так, чтобы пользователь мог сам решить, сколько еды скормить зверюшке и сколько времени
#   потратить на игру с ней (в зависимости от передаваемых величин зверюшка должна неодинаково быстро насыщаться и
#   веселеть).
# TODO: Создать в программе своего рода "черный ход" - способ увидеть точные значения числовых атрибутов объекта.
#   Сделать в меню секретный пункт, который подсказка не будет отражать, и, если пользователь его выберет, выводить
#   объект на экран (для этого в классе Critter должен быть реализован специальный метод __str__()).