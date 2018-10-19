import unittest


# Связанный список.
# Состоит из отдельных узлов (данные + связь/ссылка на следующий узел)


class Node:  # класс Node определяет узел:
    def __init__(self, v):
        self.value = v  # данное
        self.next = None  # Next - связь (указатель на следующий узел. Для последнего next будет хранить None


n1 = Node(1)  # создание узла (объект класса Node)
n2 = Node(2)  # создание узла (объект класса Node)
n1.next = n2  # узлу n1 определить указатель на следующий узел n2


class LinkedList:  # Класс LinkedList определяет методы связанного списка
    def __init__(self):
        self.head = None  # указатель на голову (первый узел) списка
        self.tail = None  # указатель на хвост (завершающий узел) списка

    def add_in_tail(self, item):  # метод добавление нового узла в конец списка
        if self.head is None:  # если указатель на первый узел хранит None, т.е. список пуст
            self.head = item  # первым узлом станет новый узел item
        else:  # иначе, т.е. если связанный список уже содержит узлы...
            self.tail.next = item  # указатель на последний узел будет указывать на новый узел item
        self.tail = item  # В любом случае новый узел item будет последним узлом в списке

    def print_all_nodes(self):  # метод вывода всего списка для отладки
        node = self.head  # создание переменной, которая будет хранить указатель на голову списка
        print('[', end='')
        while node is not None:  # пока указатель на узел не равен None...
            print(node.value, end=', ')  # выведи на экран значение указанного узла
            node = node.next  # сохрани в переменной указатель на следующий узел для следующей итерации
        print(']')

    def find(self, val):  # метод поиска узла по значению
        node = self.head  # создание переменной, которая будет хранить указатель на голову списка
        while node is not None:  # пока переменная не хранит None выполняется следующее:
            if node.value == val:  # если значение текущего узла равняется искомому значению...
                return node  # верни текущий узел
            node = node.next  # сохрани в переменной указатель на следующий узел для следующей итерации
        return None  # значение узлов не равно искомому значению верни None

    def del_nod(self, val):  # метод удаления узла с найденным значением
        if self.head is not None:
            node = self.head
            if node.value == val:  # если значение найдено в головном узле
                self.head = node.next  # головой узла станет следующий узел
                node.next = None
                return
            while node.next is not None:
                if node.next.value == val and node.next.next is not None:  # если значение найдено в среднем узле
                    node.next = node.next.next  # перевести указатель предыдущего на следующий узел
                    return
                elif node.next.value == val and node.next.next is None:  # если значение найдено в хвостовом узле
                    self.tail = node  # предыдущий узел станет хвостовым
                    node.next = None
                    return
                node = node.next  # перейти к следующему узлу для новой итерации

    def del_ever_nod(self, val):  # метод удаления всех узлов с найденными значениями
        node = self.head
        while node.next is not None:
            if node.next.value == val and node.next.next is not None:
                node.next = node.next.next
                continue
            elif node.next.value == val and node.next.next is None:
                self.tail = node
                node.next = None
                continue
            elif self.head.value == val:
                self.head = node.next
                continue
            node = node.next

    def clear(self):  # метод очистки всего содержимого списка
        self.__init__()

    def find_all(self, val):  # метод поиска всех узлов по значению
        node = self.head
        find_list = []
        while node is not None:
            if node.value == val:
                find_list.append(node.value)
            node = node.next
        return find_list

    def list_len(self):  # метод определения длинны списка
        node = self.head
        len = 0
        while node is not None:
            len += 1
            node = node.next
        return len

    def insert_node(self, val, num):  # метод добавление нового узла после заданного
        new_node = Node(val)  # создание узла c заданным значением (объект класса Node)
        node = self.head
        ln = 1  # счетчик узлов
        while node is not None:  # перебер узлов списка от головы до хвоста
            if ln == num:  # если номер узла в списке соответствует заданному значению...
                if node.next is not None:  # и если этот узел не последний
                    new_node.next = node.next  # определить указатель нового узла на следующий после найденного
                    node.next = new_node  # определить указатель найденного узла на новый
                else:  # если найденный узел являестя последним в списке...
                    node.next = new_node  # определить указатель найденного узла на новый
                    new_node.next = None  # новый узел станет завершающим в списке
            ln += 1  # увеличить счетчик узлов
            node = node.next  # перейти к следующему узлу для новой итерации цикла


# формирование списка:
s_list = LinkedList()  # Создание пустого связанного списка
s_list.add_in_tail(n1)  # добавление узла n1 в хвост списка (пока ещё пустого)
s_list.add_in_tail(Node(1))  # добавление в конец списка новый узел (объект класса Node)
s_list.add_in_tail(n2)  # добавление узла n2 в хвост списка
s_list.add_in_tail(Node(3))  # добавление в конец списка новый узел (объект класса Node)
s_list.add_in_tail(Node(4))  # добавление в конец списка новый узел (объект класса Node)
s_list.add_in_tail(Node(1))  # добавление в конец списка новый узел (объект класса Node)
s_list.add_in_tail(Node(2))  # добавление в конец списка новый узел (объект класса Node)
s_list.add_in_tail(Node(3))  # добавление в конец списка новый узел (объект класса Node)
s_list.add_in_tail(Node(4))  # добавление в конец списка новый узел (объект класса Node)

print('Step_1. Сформированный список:')
s_list.print_all_nodes()  # Вывод на экран всего связанного списка

nf = s_list.find(11)  # создание объекта, который будет хранить результаты метода поиска класса LinkedList
if nf is not None:  # если результаты поиска не хранят None...
    print('Step_2. Результат поиска: ', nf.value)  # выведи данное(значение) узла
else:
    print('Step_2*. Результаты поиска: поиск не дал результатов.')

print('Step_3. Удаление всех узлов с найденным значением:')
s_list.del_ever_nod(1)
s_list.print_all_nodes()

print('Step_4. Удаление первого узла с найденным значением:')
s_list.del_nod(4)
s_list.print_all_nodes()

print('Step_5. Результаты поиска всех узлов по заданному значению:', s_list.find_all(4))

print('Step_6. Список состоит из {} узлов'.format(s_list.list_len()))

print('Step_7. После добавления узла список имеет следующий состав:')
s_list.insert_node(100, 3)
s_list.print_all_nodes()

print('Step_8. Результат очищения списка:')
s_list.clear()  # удаление всех узлов списка
s_list.print_all_nodes()

print('Задание № 1.7')
'''
1.7. Напишите функцию, которая получает на вход два связанных списка, состоящие из целых значений, и если их длины
равны, возвращает список, каждый элемент которого равен сумме соответствующих элементов входных списков.
'''


def comp_list(list_1, list_2):  # функция сравнения и суммирования двух св. списков
    final_list = LinkedList()  # создание пустого связанного списка
    node_1 = list_1.head  # указатель на первый узел первого списка
    node_2 = list_2.head  # указатель на первый узел второго списка
    if list_1.list_len() == list_2.list_len():  # если количество узлов в списках одинаковая...
        while node_1 is not None and node_2 is not None:  # выполни перебор списков от начала до конца
            #  добавь в пустой список сумму данных из узлов двух списков
            final_list.add_in_tail(Node(int(node_1.value + node_2.value)))
            node_1 = node_1.next  # переход к следующему узлу
            node_2 = node_2.next  # переход к следующему узлу
    else:  # иначе, если длины списков отличаются
        return  # верни None
    return final_list  # при положительном сравнении списков верни список сумм


# формирование двух списков для задания №1.7
L_1 = LinkedList()
L_2 = LinkedList()
L_1.add_in_tail(Node(1))
L_1.add_in_tail(Node(3))
L_1.add_in_tail(Node(5))
L_2.add_in_tail(Node(2))
L_2.add_in_tail(Node(4))
L_2.add_in_tail(Node(6))

print('Сформированный список №1:')
L_1.print_all_nodes()
print('Сформированный список №2:')
L_2.print_all_nodes()

print('Итоговый список из сумм двух списков: ')

abc = comp_list(L_1, L_2)
if abs is not None:
    abc.print_all_nodes()
else:
    print('У списков №1 и №2 разная длина.')


class LinkedListTest(unittest.TestCase):

    def test_norm(self):
        link_1 = LinkedList()  # создаем пустой св. список, объекст класса LinkedList
        self.assertIsNone(link_1.head)  # тест на пустоту списка

    def setUp(self):
        self.link_1 = LinkedList()
        self.link_1.add_in_tail(Node(12))
        self.link_1.add_in_tail(Node(55))
        self.link_1.add_in_tail(Node(128))

    def tearDown(self):
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

    def test_insert_node(self):
        self.link_1.insert_node(11, 1)
        self.assertEqual(self.link_1.head.next.value, 11)
        self.assertIsNotNone(self.link_1.head.next.next.next)

    def test_insert_node_1(self):
        self.link_1.insert_node(56, 2)
        self.assertEqual(self.link_1.head.next.next.value, 56)
        self.assertIsNotNone(self.link_1.head.next.next.next)

    def test_insert_node_2(self):
        self.link_1.insert_node(-130, 3)
        self.assertEqual(self.link_1.head.next.next.next.value, -130)
        self.assertIsNotNone(self.link_1.head.next.next.next)


class LinkedListTest1(unittest.TestCase):

    def setUp(self):
        self.link_1 = LinkedList()
        self.link_1.add_in_tail(Node(12))
        self.link_1.add_in_tail(Node(55))
        self.link_1.add_in_tail(Node(128))
        self.link_1.add_in_tail(Node(12))
        self.link_1.add_in_tail(Node(55))
        self.link_1.add_in_tail(Node(128))

    def tearDown(self):
        self.link_1.clear()

    def test_ever_nod(self):
        self.link_1.del_ever_nod(12)
        self.assertNotEqual(self.link_1.head.value, 12)
        self.assertNotEqual(self.link_1.head.next.next.next.value, 12)
        self.assertIsNone(self.link_1.head.next.next.next.next)

    def test_ever_nod_1(self):
        self.link_1.del_ever_nod(55)
        self.assertEqual(self.link_1.head.next.value, 128)
        self.assertEqual(self.link_1.head.next.next.next.value, 128)
        self.assertIsNone(self.link_1.head.next.next.next.next)

    def test_ever_nod_2(self):
        self.link_1.del_ever_nod(128)
        self.assertEqual(self.link_1.head.next.next.value, 12)
        self.assertEqual(self.link_1.head.next.next.next.value, 55)
        self.assertIsNone(self.link_1.head.next.next.next.next)

    def test_clear(self):
        self.link_1.clear()
        self.assertIsNone(self.link_1.head)

    def test_find_all(self):
        self.assertEqual(self.link_1.find_all(12), [12, 12])
        self.assertEqual(self.link_1.find_all(11), [])

    def test_list_len(self):
        self.assertEqual(self.link_1.list_len(), 6)

    def test_list_len_1(self):
        self.link_1.add_in_tail(Node(250))
        self.assertEqual(self.link_1.list_len(), 7)

    def test_list_len_2(self):
        self.link_1.clear()
        self.assertEqual(self.link_1.list_len(), 0)


class LinkedListTest3(unittest.TestCase):

    def test_comp_list(self):
        list_1 = LinkedList()
        list_2 = LinkedList()
        abc = comp_list(list_1, list_2)
        self.assertIsNone(abc.head)

    def test_comp_list_1(self):
        list_1 = LinkedList()
        list_1.add_in_tail(Node(3))
        list_1.add_in_tail(Node(5))
        list_1.add_in_tail(Node(7))
        list_2 = LinkedList()
        list_2.add_in_tail(Node(2))
        list_2.add_in_tail(Node(4))
        list_2.add_in_tail(Node(6))
        abc = comp_list(list_1, list_2)
        self.assertEqual(abc.head.value, (list_1.head.value + list_2.head.value))
        self.assertEqual(abc.head.next.value, (list_1.head.next.value + list_2.head.next.value))
        self.assertEqual(abc.head.next.next.value, (list_1.head.next.next.value + list_2.head.next.next.value))
        self.assertIsNone(abc.head.next.next.next)

    def test_comp_2(self):
        list_1 = LinkedList()
        list_1.add_in_tail(Node(3))
        list_2 = LinkedList()
        list_2.add_in_tail(Node(2))
        list_2.add_in_tail(Node(4))
        abc = comp_list(list_1, list_2)
        self.assertIsNone(abc)


if __name__ == '__main__':
    unittest.main()
