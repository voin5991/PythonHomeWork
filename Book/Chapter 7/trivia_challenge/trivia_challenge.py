# Викторина
# Игра на выбор правильного варианта ответа.
# вопросы которой читаются из текстового файла
import sys

def open_file(file_name, mode):
    """
    Открывает файл.
    :param file_name:
    :param mode:
    :return:
    """
    try:
        the_file = open(file_name, mode, encoding='utf-8')
    except IOError as e:
        print("Невозможно открыть файл", file_name, ". Работа программы будет завершена.\n", e)
        input("\n\nНажмите Enter, чтобы выйти.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """
    Возвращает в отформатированном виде очередную строку игрового файла.
    :param the_file:
    :return:
    """
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """
    Возвращает очередной блок данных из игрового файла.
    :param the_file:
    :return:
    """
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    explanation = next_line(the_file)
    return category, question, answers, correct, explanation

def welcome(title):
    """
    Приветствует игрока и сообщает тему игры.
    :param title:
    :return:
    """
    print("\t\tДобро пожаловать в игру 'Викторина'!\n")
    print("\t\t", title, "\n")

def main():
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0
    # извлечение первого блока
    category, question, answers, correct, explanation = next_block(trivia_file)
    while category:
        # вывод вопроса на экран
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])
        # получение ответа
        answer = input("Ваш ответ: ")
        # проверка ответа
        if answer == correct:
            print("\nДа!", end=" ")
            score += 1
        else:
            print("\nНет.", end=" ")
        print(explanation)
        print("Счет: ", score, "\n\n")
        # переход к следующему вопросу
        category, question, answers, correct, explanation = next_block(trivia_file)
    trivia_file.close()
    print("Это был последний вопрос!")
    print("На вашем счету", score)

main()
input("\n\nНажмите Enter, чтобы выйти.")
