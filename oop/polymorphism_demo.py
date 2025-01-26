import math

class Shape:
    def area(self):
        """Base method to be overridden by subclasses"""
        raise NotImplementedError("Subclass must implement abstract method")


class Rectangle(Shape):
    def __init__(self, length, width):
        """Rectangle constructor"""
        self.length = length
        self.width = width

    def area(self):
        """Calculate rectangle area"""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """Circle constructor"""
        self.radius = radius

    def area(self):
        """Calculate circle area"""
        return math.pi * self.radius ** 2
    