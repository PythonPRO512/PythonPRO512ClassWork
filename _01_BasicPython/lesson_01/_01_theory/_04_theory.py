# name = input("Введите ваше имя: ")
# print("Привет", name)
# print()

without_tax = input("Введите сумму без налога: ")
without_tax_float = float(without_tax)
tax_percent = input("Введите процент налога: ")
tax_percent_float = float(tax_percent)
total_sum = without_tax_float + without_tax_float * tax_percent_float / 100
print(f'Сумма итого: {total_sum}.')
# print('Сумма итого:', total_sum)

# without_tax = float(input("Введите сумму без налога: "))
# tax_percent = float(input("Введите процент налога: "))
# total_sum = without_tax + without_tax * tax_percent / 100
# print(f'Сумма итого: {total_sum:.2f}.')

