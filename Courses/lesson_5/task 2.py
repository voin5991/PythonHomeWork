def welcome(name):
    if name == "":
        print("Приветствую вас Андрей")
    else:
        print("Приветствую вас", name)


def main():
    name = input("Введите ваше имя: ")
    welcome(name)

main()
input("\n\nPress enter to exit")
