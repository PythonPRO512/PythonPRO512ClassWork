"""
Задача 1:
Создайте экземпляр ORM и подключитесь к базе данных.
Затем создайте таблицу «users» со столбцами
«name» (текстовый тип данных) и «age» (целочисленный тип данных).
Добавьте в таблицу несколько строк с указанием имени и возраста пользователей,
а затем выведите на экран все записи из таблицы.


Задача 2: Выполнение запросов к ORM на изменение и удаление значений
Ситуация:
Вы продолжаете работу с ORM из задачи 1.
Выполните несколько запросов к ORM и выведите на экран результат.
Задача:
- Изучив исходный код модели, выполните простой SELECT-запрос с обращением к столбцу «age».
- Затем обновите возраст одного из пользователей.
- Наконец удалите информацию об одном из пользователей, обратившись к столбцу «name».
- Выведите на экран всю информацию о получившейся таблице.
"""

from practice_00_SIMPLE_ORM import SimpleORM

if __name__ == '__main__':
    orm = SimpleORM(r'databases\example.db')
    # TASK2
    # orm.create_table('users', name='Text', age='INTEGER')
    # users = [('Alice', 30), ('Bob', 25)]
    # for user_name, user_age in users:
    #     orm.insert('users', name=user_name, age=user_age)
    # print(orm.select('users'))

    # TASK2
    print(orm.select('users'))
    orm.update('users', {'age': 31}, name='Alice')
    print(orm.select('users'))
    print()
    orm.delete('users', name='Bob')
    print(orm.select('users'))