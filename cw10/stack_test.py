from cw10.stack import *
import unittest


class TestSlack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack(2)

    def test_is_empty(self):
        self.assertEqual(Stack.is_empty(self.stack), True)

    def test_is_full(self):
        self.assertEqual(Stack.is_full(self.stack), False)
        Stack.push(self.stack, 11)
        Stack.push(self.stack, 12)
        self.assertEqual(Stack.is_full(self.stack), True)

    def test_push(self):
        Stack.push(self.stack, 11)
        self.assertEqual(Stack.is_empty(self.stack), False)

    def test_pop(self):
        Stack.push(self.stack, 11)
        Stack.pop(self.stack)
        self.assertEqual(Stack.is_empty(self.stack), True)


if __name__ == '__main__':
    unittest.main()
