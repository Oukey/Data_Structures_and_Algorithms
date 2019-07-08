import unittest

import New_LL2


class LinkedList2Test(unittest.TestCase):

    def test_norm(self):
        LL = New_LL2.LinkedList2()
        self.assertIsNone(LL.head)
        LL.add_in_tail(New_LL2.Node(10))
        self.assertEqual(LL.head.value, 10)
        self.assertEqual(LL.tail.value, 10)

    def test_find(self):
        LL_1 = New_LL2.LinkedList2()
        n1 = New_LL2.Node(1)
        n2 = New_LL2.Node(2)
        n3 = New_LL2.Node(3)
        LL_1.add_in_tail(n1)
        LL_1.add_in_tail(n2)
        LL_1.add_in_tail(n3)
        self.assertEqual(LL_1.find(1), n1)
        self.assertEqual(LL_1.find(2), n2)
        self.assertEqual(LL_1.find(3), n3)

    def test_find_all(self):
        LL_2 = New_LL2.LinkedList2()
        n1 = New_LL2.Node(1)
        n2 = New_LL2.Node(2)
        n3 = New_LL2.Node(3)
        n_1 = New_LL2.Node(1)
        n_2 = New_LL2.Node(2)
        LL_2.add_in_tail(n1)
        LL_2.add_in_tail(n2)
        LL_2.add_in_tail(n3)
        LL_2.add_in_tail(n_2)
        LL_2.add_in_tail(n_1)
        self.assertEqual(LL_2.find_all(1), [n1, n_1])
        self.assertEqual(LL_2.find_all(2), [n2, n_2])
        self.assertEqual(LL_2.find_all(3), [n3])

    def test_delete(self):
        LL_3 = New_LL2.LinkedList2()
        LL_3.add_in_tail(New_LL2.Node(1))
        LL_3.delete(1, all=False)
        self.assertIsNone(LL_3.head)
        LL_3.add_in_tail(New_LL2.Node(1))
        LL_3.add_in_tail(New_LL2.Node(2))
        LL_3.add_in_tail(New_LL2.Node(3))
        LL_3.add_in_tail(New_LL2.Node(2))
        LL_3.add_in_tail(New_LL2.Node(1))
        LL_3.delete(1, all=False)
        self.assertNotEqual(LL_3.head.value, 1)
        self.assertEqual(LL_3.tail.value, 1)
        LL_3.delete(2, all=True)
        self.assertEqual(LL_3.find_all(2), [])

    def test_clean(self):
        LL_4 = New_LL2.LinkedList2()
        for i in range(1, 5):
            LL_4.add_in_tail(New_LL2.Node(i))
        self.assertIsNotNone(LL_4.head.next.next.next)
        LL_4.clean()
        self.assertIsNone(LL_4.head)

    def test_len(self):
        LL_5 = New_LL2.LinkedList2()
        for i in range(1, 6):
            LL_5.add_in_tail(New_LL2.Node(i))
        self.assertEqual(LL_5.len(), 5)

    def test_insert(self):
        LL_6 = New_LL2.LinkedList2()
        n1 = New_LL2.Node(1)
        n2 = New_LL2.Node(2)
        n3 = New_LL2.Node(3)
        n0 = None
        self.assertIsNone(LL_6.head)
        LL_6.insert(n0, n1)
        self.assertEqual(LL_6.head.value, 1)
        LL_6.insert(n0, n2)
        self.assertEqual(LL_6.tail.value, 2)
        LL_6.insert(n1, n3)
        self.assertEqual(LL_6.head.value, 1)
        self.assertEqual(LL_6.tail.value, 2)
        self.assertEqual(LL_6.head.next, n3)

    def test_add_in_head(self):
        LL_7 = New_LL2.LinkedList2()
        LL_7.add_in_head(New_LL2.Node(11))
        self.assertEqual(LL_7.head.value, 11)
        LL_7.add_in_head(New_LL2.Node(1))
        self.assertEqual(LL_7.head.value, 1)
        self.assertEqual(LL_7.tail.value, 11)

    if __name__ == "__main__":
        unittest.main()
