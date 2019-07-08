import OrderedList

import unittest


class OrderedListTest(unittest.TestCase):

    def test_norm0(self):
        Od = OrderedList.OrderedList(True)
        Od.delete(123)
        self.assertEqual(Od.len(), 0)
        self.assertIsNone(Od.head)
        Od.add(12)
        self.assertEqual(Od.head.value, 12)
        self.assertEqual(Od.len(), 1)
        Od.add(8)
        Od.add(20)
        Od.add(11)
        Od.add(17)
        self.assertEqual(Od.len(), 5)
        self.assertEqual(Od.head.value, 8)
        self.assertEqual(Od.tail.value, 20)
        self.assertEqual(Od.head.next.next.value, 12)
        self.assertEqual(Od.find(17), Od.tail.prev)
        Od.delete(17)
        self.assertIsNone(Od.find(17))
        Od.delete(8)
        Od.delete(20)
        self.assertNotEqual(Od.head.value, 8)
        self.assertNotEqual(Od.tail.value, 20)
        Od.clean(False)
        self.assertEqual(Od.len(), 0)

    def test_1(self):
        Od = OrderedList.OrderedList(False)
        Od.delete(123)
        Od.add(2)
        Od.add(4)
        Od.add(6)
        Od.add(8)
        self.assertEqual(Od.find(4), Od.tail.prev)
        self.assertEqual(Od.head.value, 8)
        self.assertEqual(Od.tail.value, 2)
        Od.delete(5)
        self.assertEqual(Od.len(), 4)
        Od.delete(2)
        Od.delete(6)
        Od.delete(8)
        self.assertEqual(Od.head.value, 4)
        self.assertIsNone(Od.find(6))

    def test_str(self):
        St = OrderedList.OrderedStringList(True)
        St.delete('00')
        St.add('01')
        self.assertEqual(St.head.value, '01')
        St.add(' 011 ')
        self.assertEqual(St.tail.value, ' 011 ')


if __name__ == "__main__":
    unittest.main()
