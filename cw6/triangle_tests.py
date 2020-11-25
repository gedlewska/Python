from triangle import *
import unittest


class TestTriangle(unittest.TestCase):

    def setUp(self):
        self.triangle = Triangle(0, 0, 0, 3, 4, 0)

    def test_str(self):
        self.assertEqual(str(self.triangle), "[(0, 0), (0, 3), (4, 0)]")

    def test_repr(self):
        self.assertEqual(repr(self.triangle), "Triangle((0, 0), (0, 3), (4, 0))")

    def test_eq(self):
        self.assertTrue(self.triangle == Triangle(0, 0, 0, 3, 4, 0))
        self.assertTrue(self.triangle != Triangle(0, 0, 4, 5, 15, 15))

    def test_center(self):
        self.assertEqual(Triangle.center(self.triangle), Point(4 / 3, 1))

    def test_area(self):
        self.assertEqual(Triangle.area(self.triangle), 6)

    def test_move(self):
        self.assertEqual(Triangle.move(self.triangle, 2, 4), Triangle(2, 4, 2, 7, 6, 4))
        self.assertEqual(Triangle.move(self.triangle, -4, 5), Triangle(-4, 5, -4, 8, 0, 5))

    def tearDown(self):
        del self.triangle


if __name__ == '__main__':
    unittest.main()
