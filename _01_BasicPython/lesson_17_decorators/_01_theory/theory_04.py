def decorator1(func):
    def wrapper():
        print(f'Декоратор1 начало')
        func()
        print(f'Декоратор1 конец')

    return wrapper


def decorator2(func):
    def wrapper():
        print(f'Декоратор2 начало')
        func()
        print(f'Декоратор2 конец')

    return wrapper

@decorator1
@decorator2
def say_hello():
    print('Hello World!')


if __name__ == '__main__':
    say_hello()
