try:
    # код, который может вызвать ошибку
    user_num = int(input('Введите целое число: '))
    result = 10 / user_num
except ZeroDivisionError:
    print(f'На ноль делить нельзя')
except ValueError:
    print(f'Это не целое число!')
except Exception as e:
    print(type(e).__name__)
else:
    print(f'10 / {user_num} = {result}')
finally:
    print(f'Программа завершена!')
