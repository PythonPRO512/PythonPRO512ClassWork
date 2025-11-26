# линейный поиск

def linear_search(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return f'Элемент {target} найден, его индекс: {index}'
    return f'Элемент {target} не найден'


surnames = ['Иванов', 'Петров', 'Сидоров', "Жуков", "Климов"]
print(linear_search(surnames, 'Жуков'))
print(linear_search(surnames, 'Толбухин'))
