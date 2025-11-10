try:
    number = int(input("Введите число: "))
except ValueError:
    print("Это не число!")
else:
    print(f"Вы ввели число {number}.")


