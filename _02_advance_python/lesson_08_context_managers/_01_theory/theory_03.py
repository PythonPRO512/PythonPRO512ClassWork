import time
from datetime import datetime

class DBConnection:

    def __enter__(self):
        print('Открываем соединение с базой данных.')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Закрываем соединение с базой данных')
        if exc_type:
            print(f'Произошла ошибка: {exc_val}')


class FileWriter:
    def __enter__(self):
        self.file = open(r'example_files\log.txt', 'a', encoding='utf-8')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_type:
            print(f'Ошибка в файле: {exc_val}')


if __name__ == '__main__':
    with DBConnection() as db, FileWriter() as file:
        file.file.write(f"{datetime.now()} >> Подключение к БД\n")
        print(f"{datetime.now()} >> Подключение к БД\n")
        time.sleep(2)
        print("Продолжаем работать с базой данных")
        time.sleep(2)
        print(f"{datetime.now()} >> Отключение от БД\n")
        file.file.write(f"{datetime.now()} >> Отключение от БД\n")

