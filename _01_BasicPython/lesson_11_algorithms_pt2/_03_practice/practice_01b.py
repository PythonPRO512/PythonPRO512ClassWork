"""
Практикум
Задача 1: Работа с очередью в магазине

Ситуация: мы управляем очередью в магазине самообслуживания.
Каждому покупателю присваивается номер, по которому он проходит через кассу.
Нужно создать программу, которая помогает управлять очередью:
- добавлять новых покупателей;
- обслуживать их по порядку;
- выводить текущую очередь.

Задача: напишите программу, которая:

Добавляет нового покупателя в конец очереди.
Обслуживает покупателя в начале очереди (удаляет его).
Показывает текущую очередь.
"""

from collections import deque


def enqueue(queue, customer):
    queue.append(customer)


def dequeue(queue):
    if queue:
        served = queue.popleft()
        return served
    return None


def show(queue):
    if queue:
        return list(queue)
    return None


if __name__ == '__main__':
    my_queue = deque()

    while True:
        command = input("Введите команду: 1 - add, 2 - serve, 3 - show, 4 - exit: ").strip()
        if command == "1":
            new_customer = input("Введите имя покупателя: ")
            enqueue(my_queue, new_customer)
            print(f'Покупатель {new_customer} добавлен в очередь.')

        elif command == '2':
            served_customer = dequeue(my_queue)
            if served_customer:
                print(f'Покупатель {served_customer} обслужен.')
            else:
                print(f'Очередь пуста.')

        elif command == '3':
            customers_queue = show(my_queue)
            if customers_queue:
                print(f'Текущей: {', '.join(customers_queue)}')
            else:
                print(f'Очередь пуста.')

        elif command == '4':
            print(f'Работа завершена')
            break

        else:
            print("Ошибка ввода.")
