import os


def check_file(filename):
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8'):
            print('Файл успешно создан')
    else:
        print('Файл уже существует')


def add_participants(filename, participant_name):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(participant_name + '\n')


def show_participants(filename):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            participants = file.readlines()
            if participants:
                for participant in participants:
                    print(participant.rstrip())
            else:
                print(f'Список участников пуст.')
    else:
        print(f'Файл с участниками не найден.')
