class Book:
    def __init__(self, author, book_name, year, genre):
        self.author = author
        self.book_name = book_name
        self.year = year
        self.genre = genre

    def __eq__(self, other):
        return self.author == other.author and self.book_name == other.book_name and self.year == other.year and \
            self.genre == other.genre

    def __repr__(self):
        return """\t\tАвтор: {}, 
        Название: {},
        Год выпуска: {!r},
        Жанр: {}
        """.format(self.author, self.book_name, self.year, self.genre)

    def __str__(self):
        return """\t\tАвтор: {}, 
        Название: {},
        Год выпуска: {!r},
        Жанр: {}
        """.format(self.author, self.book_name, self.year, self.genre)


book_1 = Book("Жюль Верн", "Таинственный остров", 1873, "Робинзонада")
book_2 = Book("Александр Дюма", "Граф Монте-Кристо", 1846, "Исторический роман")
book_3 = Book("Майкл Доусон", "Программируем на Python", 2022, "Учебное пособие")

print(book_1)
print(book_2)
print(book_3)