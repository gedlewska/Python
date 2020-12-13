from cw10.randomqueue import *
import unittest


class TestRandomQueue(unittest.TestCase):
    def setUp(self):
        self.randomqueue = RandomQueue()

    def test_is_empty(self):
        self.assertEqual(RandomQueue.is_empty(self.randomqueue), True)

    def test_is_full(self):
        self.assertEqual(RandomQueue.is_full(self.randomqueue), False)
        RandomQueue.insert(self.randomqueue, 11)
        self.assertEqual(RandomQueue.is_full(self.randomqueue), True)

    def test_insert(self):
        RandomQueue.insert(self.randomqueue, 11)
        self.assertEqual(RandomQueue.is_empty(self.randomqueue), False)

    def test_remove(self):
        RandomQueue.insert(self.randomqueue, 11)
        self.assertEqual(RandomQueue.remove(self.randomqueue), 11)
        self.assertEqual(RandomQueue.is_empty(self.randomqueue), True)

    def test_clear(self):
        RandomQueue.insert(self.randomqueue, 11)
        RandomQueue.insert(self.randomqueue, 12)
        RandomQueue.insert(self.randomqueue, 15)
        RandomQueue.clear(self.randomqueue)
        self.assertEqual(RandomQueue.is_empty(self.randomqueue), True)


if __name__ == '__main__':
    unittest.main()
