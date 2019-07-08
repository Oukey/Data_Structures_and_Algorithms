import unittest

import Deque


class DequeTest(unittest.TestCase):

    def test_norm(self):
        de = Deque.Deque()
        self.assertEqual(de.size(), 0)
        de.addFront(1)
        self.assertEqual(de.size(), 1)

    def test_add_1(self):
        de_1 = Deque.Deque()
        de_1.addFront(10)
        de_1.addTail(20)
        de_1.addFront(30)
        self.assertEqual(de_1.size(), 3)
        self.assertEqual(de_1.removeTail(), 20)
        self.assertEqual(de_1.removeFront(), 30)
        self.assertEqual(de_1.size(), 1)
        de_1.removeFront()
        self.assertIsNone(de_1.removeFront())

    if __name__ == 'main':
        unittest.main()
