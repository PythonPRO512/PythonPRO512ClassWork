from temperature_converter import celsius_to_fahrenheit, fahrenheit_to_celsius, kelvin_to_celsius

while True:
    print("""
Доступные операции конверсии:
1 - Цельсий в Фаренгейт;
2 - Фаренгейт в Цельсий;
3 - Кельвин в Цельсий;
0 - выход из программы.
""")
    command = input("Введите команду: ")
    if command == '0':
        break

    if command not in ['1', '2', '3']:
        print(f'Неизвестная команда! Попробуйте снова!')
        continue
    try:
        temperature = float(input('Введите температуру: '))
        if command == '1':
            print(f"Температура в Фаренгейтах: {celsius_to_fahrenheit(temperature):.2f}")
        elif command == '2':
            print(f"Температура в Цельсиях: {fahrenheit_to_celsius(temperature):.2f}")
        else:
            result = kelvin_to_celsius(temperature)
            # if type(result) is float:
            if isinstance(result, float):
                print(f"Температура в Цельсиях: {kelvin_to_celsius(temperature):.2f}")
            else:
                print(result)
    except ValueError:
        print(f'Введите числовое значение!')
