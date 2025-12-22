def greet(name):
    """
    Эта функция принимает строку, которая содержит имя персоны
    и возвращает строку - приветсвие
    :param name:
        str - имя персоны
    :return:
        str - приветствие
    """
    greeting = f'Hello {name}'
    return greeting


def greet1(name):
    """
    Эта функция принимает строку, которая содержит имя персоны
    и возвращает строку - приветсвие
    Parameters:
        name (str): - имя персоны
    Returns:
        str: приветствие
    """
    greeting = f'Hello {name}'
    return greeting


if __name__ == '__main__':
    print(greet("Петр"))
    print(greet1("Иван"))
    print(greet.__doc__)
    print(greet1.__doc__)