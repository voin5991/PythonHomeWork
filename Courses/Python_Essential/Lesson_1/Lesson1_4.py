class MyObject:
    def __init__(self):
        self.__private_attribute = 0

    def get_attribute(self):
        return self.__private_attribute

    def set_attribute(self, value):
        if value < 100:
            self.__private_attribute = value
            