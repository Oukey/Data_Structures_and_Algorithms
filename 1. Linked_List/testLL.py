import unittest

import Linked_list


class LinkedListTest(unittest.TestCase):

    def test_norm(self):
        link_1 = Linked_list.LinkedList()  # создаем пустой св. список, объекст класса LinkedList
        self.assertIsNone(link_1.head)  # тест на пустоту списка

    def setUp(self):  # метод подготовки к тестам
        self.link_1 = Linked_list.LinkedList()
        self.link_1.add_in_tail(Linked_list.Node(12))
        self.link_1.add_in_tail(Linked_list.Node(55))
        self.link_1.add_in_tail(Linked_list.Node(128))

    def tearDown(self):  # возвращение на исходную после теста
        self.link_1.clear()

    def test_add_in_tail(self):
        self.assertEqual(self.link_1.head.value, 12)
        self.assertEqual(self.link_1.head.next.value, 55)
        self.assertEqual(self.link_1.head.next.next.value, 128)
        self.assertIsNone(self.link_1.head.next.next.next)

    def test_del_nod_1(self):  # тест на удаление первого узла)
        self.link_1.del_nod(12)
        self.assertNotEqual(self.link_1.head.value, 12)

    def test_del_nod_2(self):  # тест на удаление среднего узла
        self.link_1.del_nod(55)
        self.assertNotEqual(self.link_1.head.next.value, 55)

    def test_del_nod_3(self):  # тест на удаление хвостового узла
        self.link_1.del_nod(128)
        self.assertIsNone(self.link_1.head.next.next)

    def test_insert_node(self):  # тест на добавление нового узла после первого в св. списке
        self.link_1.insert_node(11, 0)
        self.assertEqual(self.link_1.head.next.value, 11)
        self.assertIsNotNone(self.link_1.head.next.next.next)

    def test_insert_node_1(self):  # тест добавление нового узла в середину св. списка
        self.link_1.insert_node(56, 1)
        self.assertEqual(self.link_1.head.next.next.value, 56)
        self.assertIsNotNone(self.link_1.head.next.next.next)

    def test_insert_node_2(self):  # тест добавления нового узла после последнего узла св. списка
        self.link_1.insert_node(-130, 2)
        self.assertEqual(self.link_1.head.next.next.next.value, -130)
        self.assertIsNotNone(self.link_1.head.next.next.next)
        self.assertIs(self.link_1.head.next.next, self.link_1.tail)


class LinkedListTest1(unittest.TestCase):

    def setUp(self):  # метод подготовки к тестам
        self.link_1 = Linked_list.LinkedList()
        self.link_1.add_in_tail(Linked_list.Node(12))
        self.link_1.add_in_tail(Linked_list.Node(55))
        self.link_1.add_in_tail(Linked_list.Node(128))
        self.link_1.add_in_tail(Linked_list.Node(12))
        self.link_1.add_in_tail(Linked_list.Node(55))
        self.link_1.add_in_tail(Linked_list.Node(128))

    def tearDown(self):  # возвращение на исходную после теста
        self.link_1.clear()

    def test_ever_nod(self):  # тест удаления всех узлов с заданным значением при удалении головного узела
        self.link_1.del_ever_nod(12)
        self.assertNotEqual(self.link_1.head.value, 12)
        self.assertNotEqual(self.link_1.head.next.next.next.value, 12)
        self.assertIsNone(self.link_1.head.next.next.next.next)

    def test_ever_nod_1(self):
        self.link_1.del_ever_nod(55)  # тест удаления всех узлов с заданным значение при удалении среднего узла
        self.assertEqual(self.link_1.head.next.value, 128)
        self.assertEqual(self.link_1.head.next.next.next.value, 128)
        self.assertIsNone(self.link_1.head.next.next.next.next)

    def test_ever_nod_2(self):
        self.link_1.del_ever_nod(128)  # тест удаления всех узлов с заданным значение при удалении хвостового узла
        self.assertEqual(self.link_1.head.next.next.value, 12)
        self.assertEqual(self.link_1.head.next.next.next.value, 55)
        self.assertIsNone(self.link_1.head.next.next.next.next)

    def test_clear(self):  # тест очистки списка
        self.link_1.clear()
        self.assertIsNone(self.link_1.head)

    def test_find_all(self):  # тест поиска всех узлов по значениям
        self.assertEqual(self.link_1.find_all(12), [12, 12])
        self.assertEqual(self.link_1.find_all(11), [])

    def test_list_len(self):  # тест определения длины списка
        self.assertEqual(self.link_1.list_len(), 6)

    def test_list_len_1(self):  # тест определения длины списка после добавления нового узла
        self.link_1.add_in_tail(Linked_list.Node(250))
        self.assertEqual(self.link_1.list_len(), 7)

    def test_list_len_2(self):  # тест определения длины списка после его очистки
        self.link_1.clear()
        self.assertEqual(self.link_1.list_len(), 0)


class LinkedListTest3(unittest.TestCase):

    def test_comp_list(self):
        list_1 = Linked_list.LinkedList()
        list_2 = Linked_list.LinkedList()
        abc = Linked_list.comp_list(list_1, list_2)
        self.assertIsNone(abc.head)

    def test_comp_list_1(self):
        list_1 = Linked_list.LinkedList()
        list_1.add_in_tail(Linked_list.Node(3))
        list_1.add_in_tail(Linked_list.Node(5))
        list_1.add_in_tail(Linked_list.Node(7))
        list_2 = Linked_list.LinkedList()
        list_2.add_in_tail(Linked_list.Node(2))
        list_2.add_in_tail(Linked_list.Node(4))
        list_2.add_in_tail(Linked_list.Node(6))
        abc = Linked_list.comp_list(list_1, list_2)
        self.assertEqual(abc.head.value, (list_1.head.value + list_2.head.value))
        self.assertEqual(abc.head.next.value, (list_1.head.next.value + list_2.head.next.value))
        self.assertEqual(abc.head.next.next.value, (list_1.head.next.next.value + list_2.head.next.next.value))
        self.assertIsNone(abc.head.next.next.next)

    def test_comp_2(self):
        list_1 = Linked_list.LinkedList()
        list_1.add_in_tail(Linked_list.Node(3))
        list_2 = Linked_list.LinkedList()
        list_2.add_in_tail(Linked_list.Node(2))
        list_2.add_in_tail(Linked_list.Node(4))
        abc = Linked_list.comp_list(list_1, list_2)
        self.assertIsNone(abc)


if __name__ == '__main__':
    unittest.main()
