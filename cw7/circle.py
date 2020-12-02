from point import Point
import math


class Circle:

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):
        return "Circle({0}, {1}, {2})".format(self.pt.x, self.pt.y, self.radius)

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return math.pi * math.pow(self.radius, 2)

    def move(self, x, y):
        return Circle(self.pt.x + x, self.pt.y + y, self.radius)

    def cover(self, other):
        d = Point(self.pt.x - other.pt.x, self.pt.y - other.pt.y).length()
        if d == 0 or d <= math.fabs(self.radius - other.radius):
            if self.radius > other.radius:
                return Circle(self.pt.x, self.pt.y, self.radius)
            else:
                return Circle(other.pt.x, other.pt.y, other.radius)
        else:
            p = d + self.radius + other.radius
            if self.pt.x > other.pt.x:
                x = (self.pt.x + self.radius + other.pt.x - other.radius) / 2
            elif self.pt.x < other.pt.x:
                x = (other.pt.x + other.radius + self.pt.x - self.radius) / 2
            else:
                x = self.pt.x
            if self.pt.y > other.pt.y:
                y = (self.pt.y + self.radius + other.pt.y - other.radius) / 2
            elif self.pt.y < other.pt.y:
                y = (other.pt.y + other.radius + self.pt.y - self.radius) / 2
            else:
                y = self.pt.y
            return Circle(x, y, p / 2)
