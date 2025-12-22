"""
Задача: написать класс Rectangle, который принимает ширину и высоту (оба параметра типа float) при инициализации.
Реализовать строгую типизацию этих параметров. Реализовать метод area, который возвращает площадь прямоугольника.
Также добавить метод perimeter, который возвращает периметр прямоугольника.
Использовать аннотацию типов и добавить docstrings к классу и методам.
"""


class Rectangle:
    """
    Represents a rectangle with width and height.

    Attributes:
        width (float, int): The width of the rectangle.
        height (float, int): The height of the rectangle.

    Methods:
        area() -> (float, int):
            Calculates and returns the area of the rectangle.

        perimeter() -> (float, int):
            Calculates and returns the perimeter of the rectangle.
    """

    def __init__(self, width: (float, int), height: (float, int)):
        """
         Initializes the rectangle with the given width and height.

         Args:
             width (float, int): The width of the rectangle.
             height (float, int): The height of the rectangle.
         """
        if not (isinstance(width, (float, int)) and isinstance(height, (float, int))):
            raise TypeError(f"""Ожидаемый тип данных: float. 
Получено: width > {type(width).__name__}, height > {type(height).__name__}""")
        self.width = width
        self.height = height

    def calculate_area(self) -> (float, int):
        """
        Calculates the area of the rectangle.

        Returns:
            (float, int): The area of the rectangle (width * height).
        """
        return self.width * self.height

    def calculate_perimeter(self) -> (float, int):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            (float, int): The perimeter of the rectangle (2 * (width + height)).
        """
        return 2 * (self.width + self.height)


if __name__ == '__main__':
    rectangle = Rectangle(6.0, 6.0)
    print(rectangle.calculate_area())
    print(rectangle.calculate_perimeter())
    print(Rectangle.__doc__)
    print(rectangle.calculate_perimeter.__doc__)
    print(rectangle.calculate_perimeter.__doc__)
