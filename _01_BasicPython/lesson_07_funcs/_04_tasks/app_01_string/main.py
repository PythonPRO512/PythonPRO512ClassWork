from string_utils import reverse_string, count_vowels, is_palindrome

while True:
    command = input(
        """
Доступные операции:
1 - перевернуть строку;
2 - подсчитать гласные;
3 - проверить является ли строка палиндромом;
0 - выход из программы;
Ваш выбор: """)
    if command == '0':
        break
    if command in ['1', '2', '3']:
        text = input('Введите текст: ').strip()

        if command == '1':
            print(f'Перевернутая строка: {reverse_string(text)}')
        elif command == '2':
            print(f'Количество гласный в строке: {count_vowels(text)}')
        elif command == '3':
            if is_palindrome(text):
                print('ДА это палиндром')
            else:
                print('НЕТ это палиндром')
    else:
        print("Неизвестная команда. Попробуйте снова.")
