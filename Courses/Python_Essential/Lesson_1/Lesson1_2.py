class MyObject:
    class_attribute = 8

    def __init__(self):
        self.data_attribute = 42

    def instance_method(self):
        print(self.data_attribute)

    @staticmethod # Статический метод не привязан к экземпляру объекта
    def static_method():
        print(MyObject.class_attribute)


if __name__ == "__main__":
    MyObject.static_method()
    obj = MyObject()
    obj.instance_method()
    obj.static_method()
