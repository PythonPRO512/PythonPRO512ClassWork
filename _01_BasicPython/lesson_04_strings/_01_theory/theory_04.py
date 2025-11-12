# my_string = "   \n\tHello, world!   "
# stripped_string = my_string.strip()
# print(my_string)
# print(stripped_string)
# rstrip_string = my_string.rstrip()
# print(rstrip_string)
# lstrip_string = my_string.lstrip()
# print(lstrip_string)


# my_string = "Hello, world!"
# char_idx = my_string.find('wor')
# print(char_idx)
#
# my_string1 = "Hello, world! Hello python!"
# print(my_string1.find('Hello'))
# print(my_string1.rfind('Hello'))
#
# replaced_string = my_string1.replace('Hello', 'HELLO')
# print(replaced_string)
# print()
#
# my_string2 = "Hello, ***world! Hello &&&python!"
# replaced_string2 = my_string2.replace('*', '$').replace('&', '*').replace('$', '&')
# print(replaced_string2)


my_string3 = "Hello, world! Hello python!"
print(my_string3.lower())
print(my_string3.upper())
print(my_string3.capitalize())
print(my_string3.title())
print(my_string3.swapcase())


my_string4 = " Apple    "

if my_string4.strip().lower() == 'apple':
    print('Верно!')
