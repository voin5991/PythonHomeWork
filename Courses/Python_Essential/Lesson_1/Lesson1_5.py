class MyObject:
    def __init__(self):
        self.__attribute = 0

    @property
    def attribute(self):
        return self.__attribute

    @attribute.setter
    def attribute(self, value):
        if value < 100:
            self.__attribute = value

