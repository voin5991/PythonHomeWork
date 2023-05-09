# TODO: Создайте класс, описывающий автомобиль. Создайте класс автосалона, содержащий в себе список автомобилей,
#  доступных для продажи, и функцию продажи заданного автомобиля.

class Car(object):
    def __init__(self, brand, model, body_type, production_year, price):
        self.brand = brand
        self.body_type = body_type
        self.production_year = production_year
        self.price = price
        self.model = model

    def __str__(self):
        return """\t\tМарка: {},
            Модель: {},
            Тип кузова: {},
            Год выпуска: {},
            Цена: {!r}
            """.format(self.brand, self.model, self.body_type, self.production_year, self.price)


car_1 = Car("Toyota", "Land Cruiser", "SUV", "2016", 6000000)
car_2 = Car("Ford", "Focus", "Sedan", "2006", 475000)
car_3 = Car("LADA", "Priora", "High back", "2011", 210000)
car_4 = Car("Honda", "Accord", "Sedan", "2011", 1265000)


class Car_showroom:
    def __init__(self, cars, choice):
        cars = [car_1, car_2, car_3, car_4]
        self.cars = cars
        self.choice = choice

    def sell(self, choice, cars):
        """
        Функция продажи автомобиля
        :return:
        """
        if choice in cars:
            del cars[choice]
        else:
            print("Wrong choice!")
