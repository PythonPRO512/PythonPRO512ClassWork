# Разделение строки
text = "Python is fun"
words_list = text.split()  # ['Python', 'is', 'fun']
print(words_list)
csv_line = "one,two,three"
items = csv_line.split(",")  # ['one', 'two', 'three']
print(items)


# Объединение строки
joined = ' '.join(words_list)
print(joined)
csv_joined = ','.join(items)
print(csv_joined)
