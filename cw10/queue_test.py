from cw10.queue import *
import unittest


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue(2)

    def test_is_empty(self):
        self.assertEqual(Queue.is_empty(self.queue), True)

    def test_is_full(self):
        self.assertEqual(Queue.is_full(self.queue), False)
        Queue.put(self.queue, 11)
        Queue.put(self.queue, 12)
        self.assertEqual(Queue.is_full(self.queue), True)

    def test_put(self):
        Queue.put(self.queue, 11)
        self.assertEqual(Queue.is_empty(self.queue), False)

    def test_get(self):
        Queue.put(self.queue, 11)
        self.assertEqual(Queue.get(self.queue), 11)


if __name__ == '__main__':
    unittest.main()
