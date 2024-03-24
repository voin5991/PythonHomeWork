# TODO: Написать программу "Зооферма", в которой будет создано несколько объектов класса Critter, а манипулировать
#   ими всеми можно будет с помощью списка. Теперь пользователь должен заботиться не об одной зверюшке, а обо всех
#   обитателях зоофермы. Вибирая пункт в меню, пользователь выбирает действие, которое хотел бы выполнить со всеми
#   зверюшками: покормить, поиграть или узнать об их самочуствии. Чтобы программа была интереснее, при создании каждой
#   зверюшки следует назначить ей случайно выбранные уровни голода и уныния.

import random
class Critter:
    def __init__(self):
        self.hunger = random.randint(0, 100)
        self.sleepiness = random.randint(0, 100)

    def feed(self):
        self.hunger -= 50
        print(f"{self.name} is now {self.hunger}% full.")

    def play(self):
        self.sleepiness -= 25
        print(f"{self.name} is now {self.sleepiness}% tired.")

    def tell_story(self):
        print(f"{self.name} loves to tell stories about its adventures!")

class Dog(Critter):
    def __init__(self):
        super().__init__()
        self.name = "Fido"

class Cat(Critter):
    def __init__(self):
        super().__init__()
        self.name = "Fluffy"

class Fish(Critter):
    def __init__(self):
        super().__init__()
        self.name = "Nemo"

critters = [Dog(), Cat(), Fish()]

while True:
    user_input = input("What would you like to do? (1) Feed, (2) Play, (3) Tell a Story, (4) Quit: ")
    if user_input == "1":
        for critter in critters:
            critter.feed()
    elif user_input == "2":
        for critter in critters:
            critter.play()
    elif user_input == "3":
        for critter in critters:
            critter.tell_story()
    elif user_input == "4":
        break
    else:
        print("Invalid input. Please try again.")
