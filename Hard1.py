# Hard
#
# Задание 1. Абстрактный класс Shape.
# Создайте абстрактный класс Shape с:
# Абстрактными методами calculate_area() и calculate_perimeter().
# Реализуйте два класса:
# Circle (радиус = 5).
# Rectangle (ширина = 4, высота = 6).
# Проверка:
# Выведите площадь и периметр для каждой фигуры.
# 📝 Пример вывода:
# Площадь круга: 78.5
# Периметр круга: 31.4
# Площадь прямоугольника: 24
# Периметр прямоугольника: 20
from abc import ABC, abstractmethod
import math

class Shape(ABC): # абстрактный класс Shape
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circle(Shape): # Конкретная фигура Circle
    def __init__(self, radius=5):
        self.radius = radius

    def calculate_area(self):
        return round(math.pi * self.radius ** 2, 1)

    def calculate_perimeter(self):
        return round(2 * math.pi * self.radius, 1)

class Rectangle(Shape): # Конкретная фигура
    def __init__(self, width=4, height=6):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=6)

print(f"Площадь круга: {circle.calculate_area()}")
print(f"Периметр круга: {circle.calculate_perimeter()}")

print(f"Площадь прямоугольника: {rectangle.calculate_area()}")
print(f"Периметр прямоугольника: {rectangle.calculate_perimeter()}")
# Вывод:
# Площадь круга: 78.5
# Периметр круга: 31.4
# Площадь прямоугольника: 24
# Периметр прямоугольника: 20


