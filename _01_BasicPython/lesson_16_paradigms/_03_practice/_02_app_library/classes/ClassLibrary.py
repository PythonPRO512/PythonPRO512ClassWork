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
        self.title = title

    def get_info(self):
        return f'Материал: {self.title}'


class Book(LibraryItem):
    def get_info(self):
        return f'Книга: {self.title}'


class Journal(LibraryItem):
    def get_info(self):
        return f'Журнал: {self.title}'


class AudioBook(LibraryItem):
    def __init__(self, title, duration):
        super().__init__(title)
        self.duration = duration

    def get_info(self):
        return f'Аудиокнига: {self.title}, длительность: {self.duration} минут.'
