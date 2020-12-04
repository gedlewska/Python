import math


def heron(a, b, c):
    if c - b >= a >= b + c or c - a >= b >= a + c or b - a >= c >= b + a:
        raise ValueError("Not a triangle")
    d = (a + b + c) / 2
    return math.sqrt(d * (d - a) * (d - b) * (d - c))


try:
    a = int(input("Write a: "))
    b = int(input("Write b: "))
    c = int(input("Write c: "))
except ValueError:
    print("Not a number")
else:
    print("Area of the triangle is:", heron(a, b, c))
