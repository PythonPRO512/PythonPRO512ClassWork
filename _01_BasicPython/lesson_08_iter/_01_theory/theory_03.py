# with open('students.txt', 'rt', encoding='utf-8') as file:
#     data = file.readlines()
#
# print('Первые 10 строк ')
# print(data[:10])
# print()

# Используем итератор для чтения файла построчно
with open('students.txt', 'rt', encoding='utf-8') as file:
    iterator = iter(file)  # Создаём итератор для файла
    print(iterator)
    for _ in range(10):
        print(next(iterator).strip())
        