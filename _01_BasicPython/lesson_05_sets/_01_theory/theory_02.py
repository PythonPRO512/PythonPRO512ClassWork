my_set = {1, 2, 3}
my_set.add(4)
print(my_set)
num = 2
if num in my_set:
    my_set.remove(num)
else:
    print(f'Элемент {num} не найден.')
# my_set.remove(5)
print(my_set)
my_set.discard(5)
print(my_set)
my_set.clear()
print(my_set)

my_set1 = {1, 2, 3}
my_set2 = my_set1.copy()
print(my_set1 is my_set2)
print(len(my_set1))

print(2 in my_set1)
print(5 in my_set1)



