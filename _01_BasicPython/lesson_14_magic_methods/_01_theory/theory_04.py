class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        """
        __eq__ — сравнение объектов
        Этот метод позволяет настраивать, как объекты будут сравниваться с помощью оператора ==.
        """
        if not isinstance(other, Student):
            raise TypeError(
                f"{type(other).__name__} != {type(self).__name__} >> Оба объекта должны принадлежать к классу: {type(self).__name__}")
        return self.name == other.name and self.age == other.age


if __name__ == '__main__':
    s1 = Student('Иван', 16)
    s2 = Student('Иван', 16)
    s3 = Student('Мария', 15)
    print(s1 == s2)
    print(s1 == s3)
    print()
    print(s1 is s2)

    # s4 = s1  # плохо, так как при изменении s4 меняется и s1
    # print(s1 == s4)
    # print(s1 == 'студент')
