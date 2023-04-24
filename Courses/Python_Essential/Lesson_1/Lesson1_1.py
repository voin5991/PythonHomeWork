class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name, "is", self.age)


john = Person("John", 22)

lucy = Person("Lucy", 21)

Person.print_info(john)
Person.print_info(lucy)

