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
        s_3 = Stack.Stack()
        s_3.push(0)
        self.assertFalse(s_3.is_empty())
        s_3.push(0)
        self.assertEqual(s_3.peek(), 0)
        self.assertEqual(s_3.size(), 2)

    def test_pop(self):
        s_4 = Stack.Stack()
        self.assertIsNone(s_4.pop())
        s_4.push(99)
        s_4.push(1)
        self.assertEqual(s_4.pop(), 1)
        self.assertEqual(s_4.size(), 1)

    def test_peek(self):
        s_5 = Stack.Stack()
        self.assertIsNone(s_5.peek())
        s_5.push(10)
        self.assertEqual(s_5.peek(), 10)
    

    if __name__ == '__main__':
        unittest.main()
