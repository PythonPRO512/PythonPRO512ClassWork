"""
Уровень 1. Базовый
Задача: реализовать программу, в которой два процесса увеличивают общий счётчик.
Счётчик реализуется с помощью объекта Value.
Каждый процесс должен увеличивать значение счётчика 10 раз, синхронизируя доступ к переменной.
"""

import multiprocessing


def increment_counter(shared_counter: multiprocessing.Value, lock):
    for _ in range(10):
        with lock:
            shared_counter.value += 1


def main():
    my_shared_counter = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock()

    processes = [multiprocessing.Process(target=increment_counter, args=(my_shared_counter, lock)) for _ in range(3)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print(f'Итоговое значение счетчика: {my_shared_counter.value}')


if __name__ == '__main__':
    main()
