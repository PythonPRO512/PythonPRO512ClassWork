# user_input = input("Введите да для продолжения нет для остановки: ")
#
# while user_input != "да" and user_input != "нет":
#     print(f'Ошибка ввода введите 1 или 0')
#     user_input = input("Введите 1 для продолжения 0 для остановки: ")
#
# if user_input == "да":
#     print(f'Делаем что-то')
# elif user_input == "нет":
#     print(f'Не делаем ничего')
#
# print("Программа завершена.")


while True:
    user_input = input("Введите 1 для действия 1, 2 для действия 2, 0 для выхода из программы: ")
    if user_input == '0':
        print(f'Программа завершена ')
        break
    elif user_input == '1':
        print(f'Делаем 1')
    elif user_input == '2':
        print(f'Делаем 2')
    else:
        print(f'Ошибка введите 1, 2 или 0')
