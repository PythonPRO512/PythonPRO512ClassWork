greeting = "Hello World! Hello Python!"

first_letter = greeting[0]
print(first_letter)

sub_string = greeting[1:6]
print(sub_string)

slice_from_end = greeting[-1]
print(slice_from_end)

mirror_string = greeting[::-1]
print(mirror_string)

string_length = len(greeting)
print(string_length)
print()

for char in greeting:
    print(char)


list_from_string = list(greeting)
print(list_from_string)

string_from_list = ''.join(list_from_string)
print(string_from_list)
