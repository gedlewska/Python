from point import Point
import math


class Triangle:

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.apex0 = Point(x1, y1)
        self.apex1 = Point(x2, y2)
        self.apex2 = Point(x3, y3)

    def __str__(self):
        return "[{0}, {1}, {2}]".format(str(self.apex0), str(self.apex1), str(self.apex2))

    def __repr__(self):
        return "Triangle({0}, {1}, {2})".format(str(self.apex0), str(self.apex1), str(self.apex2))

    def __eq__(self, other):
        return self.apex0 == other.apex0 and self.apex1 == other.apex1 and self.apex2 == other.apex2

    def __ne__(self, other):
        return not self == other

    def center(self):
        return Point((self.apex0.x + self.apex1.x + self.apex2.x) / 3, (self.apex0.y + self.apex1.y + self.apex2.y) / 3)

    def area(self):
        a = (self.apex0 - self.apex1).length()
        b = (self.apex1 - self.apex2).length()
        c = (self.apex2 - self.apex0).length()
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

    def move(self, x, y):
        return Triangle(self.apex0.x + x, self.apex0.y + y, self.apex1.x + x, self.apex1.y + y, self.apex2.x + x,
                        self.apex2.y + y)
