def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


for number in fibonacci(10):
    print(number)


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()


for line in read_file('students.txt'):
    print(line)
