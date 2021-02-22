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

    def test_get_height(self):
        self.avl = AVLTree()
        for x in range(20):
            self.avl.insert(x)
        self.assertEqual(self.avl.get_height(self.avl.root), 5)

    def test_insert_random(self):
        self.avl = AVLTree()
        for x in range(30):
            self.avl.insert(random.randrange(100))
        self.avl.insert(8)
        self.test_is_balanced()

    def test_delete(self):
        self.avl.delete(8)
        self.test_is_balanced()

    def test_get_size(self):
        self.avl = AVLTree()
        for x in range(20):
            self.avl.insert(x)
        self.assertEqual(self.avl.get_size(), 20)


if __name__ == '__main__':
    unittest.main()
