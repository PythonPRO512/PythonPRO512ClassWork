name: str = 'Иван'


def multiply(a: int, b: (int, float) = 1) -> int:
    return a * b


if __name__ == '__main__':
    print(multiply(3, 5))
    print(multiply(3, 5.5))
