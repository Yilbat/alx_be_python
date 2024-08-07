# polymorphism_demo.py

import math

class Shape:
    def area(self) -> float:
        raise NotImplementedError("Subclasses should implement this method")

class Rectangle(Shape):
    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)
