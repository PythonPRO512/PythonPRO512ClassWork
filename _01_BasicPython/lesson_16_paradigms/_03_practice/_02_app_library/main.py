from classes.ClassLibrary import Book, Journal, AudioBook


if __name__ == '__main__':
    library = [
        Book("Мастер и Маргарита"),
        Journal("National Geographic"),
        AudioBook("Война и мир", 1200)
    ]

    for item in library:
        print(item.get_info())

