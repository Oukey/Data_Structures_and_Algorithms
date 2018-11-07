import unittest

import Linked_List2


class LinkedList2Test(unittest.TestCase):

    def test_norm2(self):  # тесты на создание и заполнение списка
        link_2 = Linked_List2.LinkedList2()  # создание пустого списка
        self.assertIsNone(link_2.head)  # проверка на содержание None в пустом списке
        link_2.add_in_tail(Linked_List2.Node2(0))  # добавление узла в конец списка
        self.assertEqual(link_2.head.value, 0)  # проверка на равенство значения головного узла
        self.assertEqual(link_2.tail.value, 0)  # проверка на равенство значения хвостового узла

    def test_find_first(self):  # тест метода поиска узла по значению
        link_2 = Linked_List2.LinkedList2()  # создание пустого списка
        self.assertIsNone(link_2.find_first(0))  # проверка поиска в пустом списке
        link_2.add_in_tail(Linked_List2.Node2(1))  # заполнение списка
        link_2.add_in_tail(Linked_List2.Node2(2))  # заполнение списка
        link_2.add_in_tail(Linked_List2.Node2(-3))  # заполнение списка
        self.assertEqual(link_2.find_first(2).value, 2)  # проверка поиска по значению в пустом списке
        self.assertEqual(link_2.find_first(-3).value, -3)  # проверка поиска отрицательного значения
        self.assertIsNone(link_2.find_first(0))  # проверка поиска, если в списке нет искомого значения

    def test_del_first_0(self):  # тест удаления узла по значению №1
        link_2 = Linked_List2.LinkedList2()  # создание пустого списка
        self.assertIsNone(link_2.del_first(1))  # проверка удаления узла в пустом списке
        link_2.add_in_tail(Linked_List2.Node2(1))  # заполнение списка
        link_2.add_in_tail(Linked_List2.Node2(-2))  # заполнение списка
        link_2.add_in_tail(Linked_List2.Node2(3))  # заполнение списка
        link_2.del_first(1)  # Удаление первого узла
        self.assertEqual(link_2.head.value, (-2))  # тест соответствия значения первого узла

    def test_del_first_1(self):  # тест удаления узла по значению №2
        link_2 = Linked_List2.LinkedList2()  # создание пустого списка
        link_2.add_in_tail(Linked_List2.Node2(1))  # заполнение списка
        link_2.add_in_tail(Linked_List2.Node2(-2))  # заполнение списка
        link_2.add_in_tail(Linked_List2.Node2(3))  # заполнение списка
        link_2.del_first(-2)  # удаление среднего узла
        self.assertEqual(link_2.head.next.value, 3)  # тест соответствия значения среднего узла

    def test_del_first_2(self):  # тест удаления узла по значению №3
        link_2 = Linked_List2.LinkedList2()  # создание пустого списка
        link_2.add_in_tail(Linked_List2.Node2(1))  # заполнение списка
        link_2.add_in_tail(Linked_List2.Node2(-2))  # заполнение списка
        link_2.add_in_tail(Linked_List2.Node2(3))  # заполнение списка
        link_2.del_first(3)  # удаление хвостового узда
        self.assertEqual(link_2.tail.value, (-2))  # проверка равенства значения хвостового узла

    def test_insert_next_0(self):  # тест вставки нового узла после заданного
        link_2 = Linked_List2.LinkedList2()  # создание пустого списка
        n_n = Linked_List2.Node2(111)  # создание узла
        link_2.insert_next(None, n_n)  # добавление нового узла после заданного
        self.assertEqual(link_2.head.value, 111)  # проверка добавления нового узла после заданного в пустом списке

    def test_insert_next_1(self):  # тест вставки нового узла после заданного
        link_2 = Linked_List2.LinkedList2()  # создание пустого списка
        n1 = Linked_List2.Node2(1)  # создание узла
        n2 = Linked_List2.Node2(2)  # создание узла
        n3 = Linked_List2.Node2(3)  # создание узла
        n_n = Linked_List2.Node2(111)  # создание узла
        link_2.add_in_tail(n1)  # заполнение списка
        link_2.add_in_tail(n2)  # заполнение списка
        link_2.add_in_tail(n3)  # заполнение списка
        link_2.insert_next(n2, n_n)  # добавление нового узла после заданного
        self.assertEqual(link_2.head.next.next.value, 111)  # проверка значения узла, после добавления нового
        self.assertEqual(link_2.head.next.next.next.value, 3)  # проверка значения узла, после добавления нового

    def test_insert_next_2(self):  # тест вставки нового узла после последнего узла
        link_2 = Linked_List2.LinkedList2()  # создание пустого списка
        n1 = Linked_List2.Node2(1)  # создание узла
        n2 = Linked_List2.Node2(2)  # создание узла
        n_n = Linked_List2.Node2(111)  # создание узла
        link_2.add_in_tail(n1)  # заполнение списка
        link_2.add_in_tail(n2)  # заполнение списка
        link_2.insert_next(n2, n_n)  # добавление нового узла после заданного
        self.assertEqual(link_2.head.next.next.value, 111)  # проверка значения узла, после добавления нового
        self.assertEqual(link_2.tail.value, 111)  # проверка значения хвостового узла

    def test_insert_first(self):
        link_2 = Linked_List2.LinkedList2()  # создание пустого списка
        link_2.insert_first(11)  # добавление в узла в начало пустого списка
        self.assertEqual(link_2.head.value, 11)  # проверка соответствия значения головного узла
        link_2.add_in_tail(Linked_List2.Node2(100))  # добавление узла в конец списка
        link_2.insert_first(0)  # добавление узла в начало списка
        self.assertEqual(link_2.head.value, 0)  # проверка соответствия значения головного узла
        self.assertEqual(link_2.tail.value, 100)  # проверка соответствия значения хвостового узла

    if __name__ == "__main__":
        unittest.main()
