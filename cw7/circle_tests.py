from circle import *
import unittest
import math


class TestCircle(unittest.TestCase):

    def setUp(self):
        self.circle = Circle(2, 2, 6)

    def test_repr(self):
        self.assertEqual(repr(self.circle), "Circle(2, 2, 6)")

    def test_eq(self):
        self.assertTrue(self.circle == Circle(2, 2, 6))
        self.assertTrue(self.circle != Circle(0, 0, 6))

    def test_area(self):
        self.assertEqual(Circle.area(self.circle), math.pi * 36)

    def test_move(self):
        self.assertEqual(Circle.move(self.circle, 2, 4), Circle(4, 6, 6))
        self.assertEqual(Circle.move(self.circle, -4, 5), Circle(-2, 7, 6))

    def test_cover(self):
        self.assertEqual(Circle.cover(self.circle, Circle(3, 3, 1)), Circle(2, 2, 6))
        self.assertEqual(Circle.cover(self.circle, Circle(2, 10, 2)), Circle(2, 4, 8))
        self.assertEqual(Circle.cover(self.circle, Circle(2, 9, 2)), Circle(2, 3.5, 7.5))

    def tearDown(self):
        del self.circle


if __name__ == '__main__':
    unittest.main()
