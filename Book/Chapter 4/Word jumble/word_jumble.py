# Анаграммы
#
# Компьютер выбирает какое-либо слово и хаотически переставляет его буквы
# Задача игрока - восстановить исходное слово

import random

# Создадим последовательность слов, из которых компьютер будет выбирать
WORDS = ("веник", "букашка", "лента", "вертолет", "борода", "шприц", "пальма", "табло", "зимовка", "посох", "ацетон",
         "купюра", "кирпич", "белка", "башмак", "кнопка", "лак", "конверт", "веер", "сюрприз", "ключ", "пелёнка",
         "пингвин", "корона", "желе", "самолёт", "цыплёнок", "чернила", "хвост", "приемник", "секунда", "поролон",
         "коньки")
# Выбор случайного слова из последовательности
word = random.choice(WORDS)
# создадим переменную, с которой будет затем сопоставлена версия игрока
correct = word
# Создаю переменную для подсказки.
clue = ""

if correct == "веник":
    clue = "Инструмент для наведения порядка"
elif correct == "букашка":
    clue = "Мелкое насекомое"
elif correct == "лента":
    clue = "Тонкая полоска из ткани или другого материала"
elif correct == "вертолет":
    clue = "Летательный аппарат"
elif correct == "борода":
    clue = "Их рубил Петр первый"
elif correct == "шприц":
    clue = "Медицинский инструмент"
elif correct == "пальма":
    clue = "Тропическое дерево"
elif correct == "табло":
    clue = "На нем показывают счет"
elif correct == "зимовка":
    clue = "место, где проводят зиму, а также само существование в зимний сезон"
elif correct == "посох":
    clue = "длинная трость, палка для опоры при ходьбе"
elif correct == "ацетон":
    clue = "органическое вещество, относящееся к классу насыщенных кетонов"
elif correct == "купюра":
    clue = "бумажный денежный знак"
elif correct == "кирпич":
    clue = "строительный материал в виде искусственного камня"
elif correct == "белка":
    clue = "род грызунов семейства беличьих"
elif correct == "башмак":
    clue = "Ботинок или полуботинок"
elif correct == "кнопка":
    clue = "небольшой предмет с остриём, служит для прикрепления листов бумаги к твёрдой поверхности"
elif correct == "лак":
    clue = "Раствор смол в спирте, скипидаре или масле, которым покрывают поверхность предметов для придания блеска"
elif correct == "конверт":
    clue = "оболочка для вкладывания, хранения и пересылки бумаг или плоских предметов"
elif correct == "веер":
    clue = "небольшое, как правило, складное опахало для создания потока воздуха"
elif correct == "сюрприз":
    clue = " нежданный подарок или неожиданное событие"
elif correct == "ключ":
    clue = "приспособление для отпирания замков"
elif correct == "пелёнка":
    clue = "небольшая простынка, в которую завёртывают, пеленают грудных детей"
elif correct == "пингвин":
    clue = "Большая морская птица, обитающая гл. образом в Антарктике"
elif correct == "корона":
    clue = "Головной убор царей"
elif correct == "желе":
    clue = " Сладкое студенистое кушанье"
elif correct == "самолёт":
    clue = "класс воздушных судов тяжелее воздуха"
elif correct == "цыплёнок":
    clue = "птенец курицы и петуха"
elif correct == "чернила":
    clue = "жидкий краситель, пригодный для письма"
elif correct == "хвост":
    clue = "часть тела животных"
elif correct == "приемник":
    clue = "Устройство для приема"
elif correct == "секунда":
    clue = " единица измерения времени"
elif correct == "поролон":
    clue = "лёгкий, эластичный, пористый синтетический материал"
elif correct == "коньки":
    clue = "Полозья для скольжения по льду"

# создадим анаграмму выбранного слова, в которой буквы будут расставленыхаотично
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# начало игры
print(
    """
               Добро пожаловать в игру 'Анаграммы'!
    
       Надо переставить буквы так, чтобы получилось осмысленное слово.
       Вам даётся 100 очков, каждая попытка отгадать стоит 10 очков.
       Подсказка стоит 50 очков. Напишите 'Подсказка', для того, чтобы 
       вызвать подсказку.
    (Для выхода нажмите Enter, не вводя своей версии.)
    """
)
print("Вот анаграмма: ", jumble)

points = 100
guess = input("\nПопробуйте отгадать исходное слово: ")
if guess == "Подсказка":
    points -= 50
    print("\n", clue)
    print("\nУ вас осталось ", points, " очков")
    guess = input("\nПопробуйте отгадать исходное слово: ")

while guess != correct and guess != "" and points > 0:
    print("\nК сожалению, вы не правы.")
    points -= 10
    print("\nУ вас осталось ", points, " очков.")
    guess = input("\nПопробуйте отгадать исходное слово: ")
    if guess == "Подсказка":
        points -= 50
        print("\n", clue)
        print("\nУ вас осталось ", points, " очков")
        guess = input("\nПопробуйте отгадать исходное слово: ")

if guess == correct:
    print("Да, именно так! Вы отгадали!\n")
    print("И заработали ", points, "очков\n")
elif guess == "":
    print("Жаль, что вы так решили. Попробуйте, вам обязательно понравится!\n")
elif points <= 0:
    print("Вы исчерпали все свои попытки.\n Попробуйте снова.\n У ваc обязательно получится!\n")
print("Спасибо за игру.")

input("\n\nНажмите Enter, чтобы выйти.")
