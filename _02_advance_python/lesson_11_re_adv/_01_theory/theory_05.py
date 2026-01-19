import random
import string

print(string.digits)
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.punctuation)
print(string.whitespace)
print(string.printable)

random_pass = random.choices((string.ascii_letters + string.digits), k=10)
print(''.join(random_pass))
