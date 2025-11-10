count = 1

while count <= 10:
    print(count)
    count += 1
print()

count = 1
while True:
    if count == 15:
        break
    print(count)
    count += 1
print()


count = 1
while count <= 10:
    if count == 5:
        count += 1
        continue
    print(count)
    count += 1
print()
