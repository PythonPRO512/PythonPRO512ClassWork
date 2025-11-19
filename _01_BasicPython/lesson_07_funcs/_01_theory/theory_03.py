def greet(name="Гость"):
    print(f'Привет {name}!')


def introduce(name, age=None):
    if age:
        print(f'Меня зовут {name}, мне {age} лет.')
    else:
        print(f'Меня зовут {name}')


if __name__ == '__main__':
    greet()
    greet('User12345')
    print()
    user_name = 'Дмитрий'
    user_age = 37
    introduce(user_name)
    introduce(user_name, user_age)
