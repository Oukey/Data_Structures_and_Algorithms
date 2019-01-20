import unittest

import New_LL


class LinkedListTest(unittest.TestCase):
    def test_norm(self):
        link_1 = New_LL.LinkedList()
        self.assertIsNone(link_1.head)

    def test_find_all_1(self):  # тест метода поиска всех объектов
        link_2 = New_LL.LinkedList()
        link_2.add_in_tail(New_LL.Node(12))
        link_2.add_in_tail(New_LL.Node(55))
        link_2.add_in_tail(New_LL.Node(128))
        link_2.add_in_tail(New_LL.Node(55))
        self.assertEqual(link_2.find_all(12), [link_2.head])
        self.assertEqual(link_2.find_all(55), [link_2.head.next, link_2.head.next.next.next])
        self.assertEqual(link_2.find_all(11), [])

    def test_delete(self):  # тест метода удаления
        link_3 = New_LL.LinkedList()
        link_3.add_in_tail(New_LL.Node(12))
        link_3.add_in_tail(New_LL.Node(55))
        link_3.add_in_tail(New_LL.Node(128))
        link_3.add_in_tail(New_LL.Node(12))
        link_3.add_in_tail(New_LL.Node(55))
        link_3.delete(12, all=False)
        self.assertNotEqual(link_3.head.value, 12)
        self.assertEqual(link_3.head.next.next.value, 12)
        link_3.delete(55, all=True)
        self.assertNotEqual(link_3.head.value, 55)
        self.assertNotEqual(link_3.tail.value, 55)
        self.assertIsNone(link_3.head.next.next)

    def test_clean(self):  # тест метода очищения списка
        link_4 = New_LL.LinkedList()
        link_4.add_in_tail(New_LL.Node(12))
        link_4.add_in_tail(New_LL.Node(55))
        self.assertIsNotNone(link_4.head)
        link_4.clean()
        self.assertIsNone(link_4.head)

    def test_len(self):  # тест метода определения длины списка
        link_5 = New_LL.LinkedList()
        self.assertEqual(link_5.len(), 0)
        link_5.add_in_tail(New_LL.Node(12))
        self.assertEqual(link_5.len(), 1)
        link_5.add_in_tail(New_LL.Node(24))
        self.assertEqual(link_5.len(), 2)

    def test_insert(self):  # тест метода вставки после заданного узла
        link_6 = New_LL.LinkedList()
        link_6.insert(0, 1)
        self.assertIsNone(link_6.head)
        link_6.insert(None, 1)
        self.assertEqual(link_6.head.value, 1)
        link_6.insert(0, 3)
        self.assertEqual(link_6.head.next.value, 3)
        link_6.insert(0, 2)
        self.assertEqual(link_6.head.next.value, 2)
