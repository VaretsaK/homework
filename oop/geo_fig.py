from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def __str__(self):
        return f"Name: {self.name} \nColor: {self.color}"


class Rectangle(Shape):
    def __init__(self, name, color, height, width):
        super().__init__(name, color)
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

    def __str__(self):
        return super().__str__() + f"\nHeight: {self.height} " \
                                   f"\nWidth: {self.width} \nArea: {self.area()} \nPerimeter: {self.perimeter()}"


class Circle(Shape):
    def __init__(self, name, color, radius):
        super().__init__(name, color)
        self.radius = radius

    def area(self):
        return round(pi * self.radius ** 2, 2)

    def perimeter(self):
        return round(2 * pi * self.radius, 2)

    def __str__(self):
        return super().__str__() + f"\nRadius: {self.radius} \nArea: {self.area()} \nPerimeter: {self.perimeter()}"


class Square(Shape):
    def __init__(self, name, color, side):
        super().__init__(name, color)
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

    def __str__(self):
        return super().__str__() + f"\nSide: {self.side} \nArea: {self.area()} \nPerimeter: {self.perimeter()}"


if __name__ == "__main__":
    rec_1 = Rectangle("Rectangle", "Green", 10, 2)
    cir_1 = Circle("Circle", "White", 15)
    sqr_1 = Square("Square", "Black", 3)
    print(rec_1)
    print()
    print(cir_1)
    print()
    print(sqr_1)
