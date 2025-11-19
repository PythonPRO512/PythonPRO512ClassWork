person = {'name': 'Иван', 'age': 30, 'city': 'Москва'}
# Если мы хотим пройтись только по ключам, используйте цикл for напрямую:
for key in person:
    print(key)
print()

# Также можно использовать метод .keys() для явного получения ключей:
for key in person.keys():
    print(key)
print()

# Для перебора только значений словаря используйте метод .values():
for value in person.values():
    print(value)
print()

# Чтобы перебирать пары «ключ-значение», используйте метод .items():
for key, value in person.items():
    print(f'Ключ: {key}. Значение: {value}')

