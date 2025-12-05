"""
Задача 2: Автоматизация работы библиотеки

Ситуация: представьте, что управляете небольшой библиотекой и хотите автоматизировать её работу.
Нам нужно создать программу, которая позволит добавлять книги в библиотеку,
изменять их статусы (например, «выдана» или «в наличии») и просматривать список всех книг.

Задача: создайте программу, которая позволяет:

Добавлять книги в библиотеку.
Изменять статус книги (например, «выдана» или «в наличии»).
Просматривать список всех книг с их статусами.
"""

from classes.ClassBook import Book
from classes.ClassLibrary import Library

if __name__ == '__main__':
    library = Library()
    while True:
        command = input("Введите команду (1 - add book, 2 - change status, 3 - show, 0 - exit): ").strip().lower()
        if command == '1':
            title = input('Введите название книги: ').strip().capitalize()
            author = input('Введите автора книги: ').strip().title()
            book = Book(title, author)
            library.add_book(book)
            print(f"Книга '{title}' добавлена в библиотеку.")
        elif command == '2':
            title = input('Введите название книги: ').strip().capitalize()
            new_status = input("Введите новый статус (например, 'в наличии' или 'выдана'): ").strip()
            print(library.change_status(title, new_status))
        elif command == '3':
            library.show_books()
        elif command == '0':
            print('Программа завершена')
            break
        else:
            print(f'Неизвестная команда, попробуйте снова.')
