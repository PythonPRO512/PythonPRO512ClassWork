"""
Уровень 3: Продвинутый

Задача: напишите функцию-генератор filter_and_square(numbers, threshold),
которая принимает список чисел и пороговое значение threshold.
Генератор должен возвращать квадраты только тех чисел, которые больше threshold.
В основной программе запросите у пользователя список чисел и порог, а затем выведите результаты.

"""


def filter_and_square(numbers, threshold):
    for num in numbers:
        if num > threshold:
            yield num ** 2


if __name__ == '__main__':
    user_numbers = list(map(int, input('Введите числа через пробел: ').split()))
    user_threshold = int(input("Введите пороговое значение: "))

    print(f'Квадраты чисел, превышающих порог {user_threshold}:')
    for square in filter_and_square(user_numbers, user_threshold):
        print(square)
