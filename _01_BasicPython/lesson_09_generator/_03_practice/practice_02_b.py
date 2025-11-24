"""
Задача 2: Генератор чётных чисел

Ситуация: мы хотим разработать генератор, который выводит только чётные числа в заданном диапазоне.
Это полезно для экономии времени и ресурсов, когда нужны только определённые данные из большого набора.

Задача: напишите генератор even_numbers(start, end), который принимает два аргумента:

start — начало диапазона.
end — конец диапазона.
Генератор должен возвращать только чётные числа в указанном диапазоне.

"""


def even_numbers_with_lc(start, end):
    return [number for number in range(start, end + 1) if number % 2 == 0]


if __name__ == '__main__':
    user_start = int(input('Введите начало диапазона: '))
    user_end = int(input('Введите конец диапазона: '))

    print(f'Четные числа от {user_start} до {user_end} включительно: ')
    print(even_numbers_with_lc(user_start, user_end))

    for even in even_numbers_with_lc(user_start, user_end):
        print(even)
