"""
Задача 1: Создание базы данных для управления пользователями с использованием SQLite3 в Python

Ситуация:
Вы разрабатываете приложение для управления пользователями.
Вам нужно создать базу данных SQLite, которая будет содержать таблицу с данными о пользователях.
Она должна включать информацию о пользователях, их возрасте и адресе email.

Задача:
Создайте таблицу users, которая будет хранить информацию о пользователях.
Затем выполните запросы для добавления данных,
чтения данных и фильтрации записей по возрасту с использованием SQLite3 в Python.
"""
import sqlite3


def display_data():
    try:
        cursor.execute("SELECT * FROM users;")
    except sqlite3.Error as err:
        print(f'{type(err).__name__} >> {err}')
    else:
        users = cursor.fetchall()
        for user in users:
            print(user)
    print()


if __name__ == '__main__':
    conn = sqlite3.connect(r'databases/users.db')
    cursor = conn.cursor()
    # try:
    #     cursor.execute("""
    #     CREATE TABLE IF NOT EXISTS users (
    #         user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         name TEXT NOT NULL,
    #         age INTEGER NOT NULL,
    #         email TEXT UNIQUE NOT NULL
    #         );
    #     """)
    # except sqlite3.Error as err:
    #     print(f'{type(err).__name__} >> {err}')
    # else:
    #     conn.commit()
    #
    # try:
    #     cursor.executemany("""
    #     INSERT INTO users (name, age, email) VALUES (?, ?, ?)
    #     """, [
    #         ('Иван Иванов', 28, 'ivan@example.com'),
    #         ('Мария Смирнова', 34, 'maria@example.com'),
    #         ('Петр Петров', 22, 'peter@example.com'),
    #         ('Алексей Иванов', 25, 'alexey@example.com'),
    #         ('Ольга Сидорова', 29, 'olga@example.com')
    #     ])
    # except sqlite3.Error as err:
    #     print(f'{type(err).__name__} >> {err}')
    # else:
    #     conn.commit()
    #
    # table_name = input("Из какой таблицы извлечь данные: ")
    # try:
    #     cursor.execute(f'SELECT * FROM {table_name};')
    # except sqlite3.Error as err:
    #     print(f'{type(err).__name__} >> {err}')
    # else:
    #     users = cursor.fetchall()
    #     for user in users:
    #         print(user)
    #
    # users_age = int(input('Введите минимальный возраст пользователя: '))
    # try:
    #     cursor.execute(f"SELECT name, age, email FROM users WHERE age > {users_age - 1}")
    # except sqlite3.Error as err:
    #     print(f'{type(err).__name__} >> {err}')
    # else:
    #     filtered_users = cursor.fetchall()
    #     for user in filtered_users:
    #         print(user)
    # print()

    # if conn:
    #     conn.close()

    """
    Задача 2: Работа с таблицей пользователей: обновление и удаление данных
    
    Ситуация:
    Вы продолжаете работать с базой данных пользователей. 
    В этой задаче вам нужно будет обновить информацию о некоторых пользователях и удалить старые данные.
    
    Задача:
    Обновите возраст некоторых пользователей.
    Удалите пользователей с определённым возрастом из базы данных.
    """
    try:
        cursor.execute("""
            UPDATE users
            SET age = age + 2
            WHERE user_id == 1;
            """)

        cursor.execute("""
            UPDATE users
            SET age = age + 3
            WHERE email = 'alexey@example.com'
            """)
    except sqlite3.Error as err:
        print(f'{type(err).__name__} >> {err}')
    else:
        conn.commit()
    display_data()
    print()

    try:
        cursor.execute("""
        DELETE FROM users
        WHERE age < 25
        """)
    except sqlite3.Error as err:
        print(f'{type(err).__name__} >> {err}')
    else:
        conn.commit()
    display_data()
    print()

    if conn:
        conn.close()
