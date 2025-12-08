"""
Ситуация: мы разрабатываем электронную библиотеку.
В библиотеке есть книги, журналы и аудиокниги.
У каждого материала есть общий метод get_info(),
который выводит его тип и название.
Для аудиокниг нужно также показывать время прослушивания.

Задача: создать классы:

LibraryItem (Базовый класс), который содержит:
Поле title (название).
Метод get_info().

Book (Класс-наследник), который:
Переопределяет метод get_info() для вывода «Книга: <название>».

Journal (Класс-наследник), который:
Переопределяет метод get_info() для вывода «Журнал: <название>».

Audiobook (Класс-наследник), который:
Имеет дополнительное поле duration (время прослушивания).
Переопределяет метод get_info() для вывода «Аудиокнига: <название>, длительность: <время> минут».

Программа должна:
Создавать объекты разных типов материалов.
Выводить информацию о каждом материале, используя полиморфизм.
"""


class LibraryItem:
    def __init__(self, title):
        self.__title = title

    @property
    def title(self):
        return self.__title

    def get_info(self):
        return f'Материал: {self.title}'


class Book(LibraryItem):

    def __init__(self, title, author):
        super().__init__(title)
        self.__author = author

    @property
    def author(self):
        return self.__author

    def get_info(self):
        return f'Книга: {self.title}. Автор: {self.author}'


class Journal(LibraryItem):
    def get_info(self):
        return f'Журнал: {self.title}'


class AudioBook(Book):
    def __init__(self, title, author, duration):
        super().__init__(title, author)
        self.__duration = duration

    @property
    def duration(self):
        return self.__duration

    def get_info(self):
        return f'Аудиокнига: {self.title}. Автор: {self.author}. Длительность: {self.duration} минут.'
