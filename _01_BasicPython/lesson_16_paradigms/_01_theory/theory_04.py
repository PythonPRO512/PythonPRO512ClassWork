class Cat:
    def speak(self):
        return 'Мяу'


class Dog:
    def speak(self):
        return 'Гав'


if __name__ == '__main__':
    animals = [Cat(), Dog()]

    for animal in animals:
        print(animal.speak())
