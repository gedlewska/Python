from projekt.avl import *
import unittest
import random


class TestAvl(unittest.TestCase):
    def setUp(self):
        self.avl = AVLTree()

    def test_is_balanced(self):
        self.assertTrue(self.avl.is_balanced())

    def test_insert(self):
        for x in range(20):
            self.avl.insert(x)
        self.test_is_balanced()

    def test_pre_order(self):
        self.assertEqual(self.avl.pre_order(), "7 3 15 2 5 11 17 1 3 4 6 9 13 16 19 8 10 12 14 18 20")

    def test_get_height(self):
        self.assertEqual(self.avl.get_height(self.avl.root), 5)

    def test_insert_random(self):
        for x in range(20):
            self.avl.delete(x)
        for x in range(30):
            self.avl.insert(random.randrange(100))
        self.avl.insert(8)
        self.test_is_balanced()

    def test_delete(self):
        self.avl.delete(8)
        self.test_is_balanced()

    def test_get_size(self):
        self.assertEqual(self.avl.get_size(), 30)


if __name__ == '__main__':
    unittest.main()
