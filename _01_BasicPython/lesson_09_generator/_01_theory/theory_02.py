def my_generator():
    for i in range(1, 11):
        yield i


gen = my_generator()
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))
