import sys

# numbers_list = []
# for x in range(1000):
#     numbers_list.append(x ** 2)

numbers_list = [x ** 2 for x in range(1000)]  # Список квадратов чисел
numbers_gen = (x ** 2 for x in range(1000))  # Генератор квадратов чисел

print(f"Размер списка: {sys.getsizeof(numbers_list)} байт")
print(f"Размер генератора: {sys.getsizeof(numbers_gen)} байт")
