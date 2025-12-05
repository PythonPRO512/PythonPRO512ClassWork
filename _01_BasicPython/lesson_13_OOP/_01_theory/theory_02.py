class Car:
    wheels = 4  # Атрибут класса

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color


if __name__ == '__main__':
    my_car = Car('Toyota', 'red')
    friend_car = Car('Ford', 'blue')

    print(Car.wheels)
    print(my_car.brand)
    print(my_car.color)
    print(my_car.wheels)
    my_car.wheels = 3
    print(my_car.wheels)
    print()
    print(friend_car.brand)
    print(friend_car.color)
    print(friend_car.wheels)
    print()
    Car.wheels = 6
    print(friend_car.wheels)
    print(my_car.wheels)
