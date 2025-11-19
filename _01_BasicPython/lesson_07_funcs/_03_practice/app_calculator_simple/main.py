from math_operations import calculator

if __name__ == '__main__':
    while True:
        print('\nПростой калькулятор:')
        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            operation = input(
                'Введите операцию\n+ >> add\n- >> subtract\n* >> multiply\n/ >> divide\nВаш выбор: ').strip().lower()

            result = calculator(a, b, operation)
            print(f'Результат: {result}')

        except ValueError:
            print(f'Ошибка: введите корректные числа.')
        except ZeroDivisionError as zde:
            print(zde)

        user_continue = input('Хотите продолжить?\n1 - да\n0 - нет\nВаш выбор: ').strip().lower()
        while user_continue not in ['1', '0']:
            print('Ошибка ввода')
            user_continue = input('Хотите продолжить?\n1 - да\n0 - нет\nВаш выбор: ').strip().lower()
        if user_continue == '0':
            break
