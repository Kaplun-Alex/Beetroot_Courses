class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'{self.name} {self.country} {self.birthday}'

    def add_book(self, bk):
        self.books.append(bk)
        return self.books

    def get_autor_name(self):
        return self.name

    def get_autor_country(self):
        return self.country

    def get_autor_birthday(self):
        return self.birthday


class Book:
    def __init__(self, name: str, year: int, author):
        self.name = name
        self.year = year
        self.author = author

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'{self.name} {self.year} {self.author}'

    def get_book_year(self):
        return self.year

    def get_book_name(self):
        return self.name

    def get_book_autor(self):
        return self.author.get_autor_name()


class Library:

    def __init__(self, name):
        self.name = name
        self.books = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'{self.books}'

    def __len__(self):
        return len(self.books)

    def add_book(self, book):
        self.books.append(book)
        return self.books

    def group_by_author(self, aut):
        list_of_books = []
        for i in range(len(self.books)):
            if self.books[i].get_book_autor() == aut:
                list_of_books.append(self.books[i].get_book_name())
            else:
                pass
        return list_of_books

    def group_by_year(self, year: int):
        list_of_books = []
        for i in range(len(self.books)):
            if self.books[i].get_book_year() == year:
                list_of_books.append(self.books[i].get_book_name())
            else:
                pass
        return list_of_books


a1 = Author('Хрюндєль', 'Польша', 1855)
a2 = Author('Діч', 'Житомир', 955)
b1 = Book('Как стать ушлепком', 1555, a1)
b2 = Book('Как купить тапки', 1833, a2)


lib1 = Library('Уернадского брат!')
lib1.add_book(b1)
lib1.add_book(b2)
print(lib1.group_by_author('Хрюндєль'))
print(lib1.group_by_year(1833))

print(lib1)
print(repr(lib1))
print(len(lib1))




