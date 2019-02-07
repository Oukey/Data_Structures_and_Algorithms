import unittest

import Stack


class StackTest(unittest.TestCase):
    
    def test_is_empty(self):
        s_1 = Stack.Stack()
        self.assertTrue(s_1.is_empty())
        s_1.push(1)
        self.assertFalse(s_1.is_empty())

    def test_size(self):
        s_2 = Stack.Stack()
        self.assertEqual(s_2.size(), 0)
        s_2.push(1)
        s_2.push(2)
        self.assertEqual(s_2.size(), 2)
        s_2.pop()
        self.assertEqual(s_2.size(), 1)
        s_2.peek()
        self.assertEqual(s_2.size(), 1)

    def test_push(self):
        pass

    def test_pop(self):
        pass

    def test_peek(self):
        pass

    if __name__ == '__main__':
        unittest.main()
