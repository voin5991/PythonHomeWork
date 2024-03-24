# TODO: Создать программу, имитирующую телевизор как объект. У пользователя должна быть возможность вводить
#   номер канала, а также увеличивать и уменьшать громкость. Программа должна следить за тем, чтобы номер канала
#   и уровень громкости оставались в допустимых пределах.

class TV:
    def __init__(self):
        self.channel = 0
        self.volume = 50

    def up_channel(self):
        if self.channel < 100:
            self.channel += 1

    def down_channel(self):
        if self.channel > 0:
            self.channel -= 1

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 0
