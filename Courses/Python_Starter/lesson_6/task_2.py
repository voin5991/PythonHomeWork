def palindrome(word):
    """
    Определяет, является ли фраза палиндромом
    :param word:
    :return:
    """
    rev = ''.join(reversed(word))
    if rev == word:
        print("Это палиндром!")
    else:
        print("Это не палиндром!")


string = input("Введите фразу для проверки: ")
print(palindrome(string))