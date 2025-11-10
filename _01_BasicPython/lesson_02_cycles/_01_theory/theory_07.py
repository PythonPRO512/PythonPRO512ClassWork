try:
    file = open('examole.txt')
    data = file.read()
    file.close()
except FileNotFoundError:
    print(f'Файл не найден!')
finally:
    print('Файл закрыт')
